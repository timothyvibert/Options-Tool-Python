from __future__ import annotations

from contextlib import contextmanager
from datetime import date
from typing import Dict, Iterable, Optional

import pandas as pd

from core.pricing import select_price


FIELDS = [
    "BID",
    "ASK",
    "PX_MID",
    "MID",
    "PX_LAST",
    "IVOL_MID",
    "DAYS_TO_EXPIRATION",
    "OPT_STRIKE_PX",
    "OPT_PUT_CALL",
]
MARKET_SECTOR_KEYWORDS = {"EQUITY", "INDEX", "CURNCY", "COMDTY"}


@contextmanager
def with_session():
    from polars_bloomberg import BQuery

    query = BQuery()
    try:
        yield query
    finally:
        close = getattr(query, "close", None)
        if callable(close):
            close()


def _to_pandas(data: object) -> pd.DataFrame:
    if isinstance(data, pd.DataFrame):
        return data
    to_pandas = getattr(data, "to_pandas", None)
    if callable(to_pandas):
        return to_pandas()
    return pd.DataFrame(data)


def _ensure_security_column(df: pd.DataFrame) -> pd.DataFrame:
    if "security" in df.columns:
        return df
    for candidate in ["Security", "SECURITY", "ticker", "Ticker"]:
        if candidate in df.columns:
            return df.rename(columns={candidate: "security"})
    if df.index.name:
        return df.reset_index().rename(columns={df.index.name: "security"})
    return df.reset_index().rename(columns={"index": "security"})


def _ensure_columns(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
    for column in columns:
        if column not in df.columns:
            df[column] = pd.NA
    return df


def fetch_spot(ticker: str) -> float:
    with with_session() as query:
        raw = query.bdp([ticker], ["PX_LAST"])
    df = _ensure_security_column(_to_pandas(raw))
    if "PX_LAST" not in df.columns or df.empty:
        return float("nan")
    row = df.loc[df["security"] == ticker]
    if row.empty:
        row = df.iloc[[0]]
    value = row["PX_LAST"].iloc[0]
    if pd.isna(value):
        return float("nan")
    return float(value)


def fetch_option_snapshot(option_tickers: list[str]) -> pd.DataFrame:
    if not option_tickers:
        return pd.DataFrame(
            columns=[
                "security",
                "BID",
                "ASK",
                "PX_MID",
                "PX_LAST",
                "IVOL_MID",
                "DAYS_TO_EXPIRATION",
                "OPT_STRIKE_PX",
                "OPT_PUT_CALL",
            ]
        )

    with with_session() as query:
        raw = query.bdp(option_tickers, FIELDS)
    df = _ensure_security_column(_to_pandas(raw))
    df = _ensure_columns(df, FIELDS)
    if "PX_MID" not in df.columns and "MID" in df.columns:
        df["PX_MID"] = df["MID"]
    if "MID" in df.columns:
        df = df.drop(columns=["MID"])
    return df[
        [
            "security",
            "BID",
            "ASK",
            "PX_MID",
            "PX_LAST",
            "IVOL_MID",
            "DAYS_TO_EXPIRATION",
            "OPT_STRIKE_PX",
            "OPT_PUT_CALL",
        ]
    ]


def _normalize_put_call(value: object) -> Optional[str]:
    if value is None:
        return None
    try:
        if pd.isna(value):
            return None
    except TypeError:
        pass
    text = str(value).strip().upper()
    if text in {"C", "CALL"}:
        return "CALL"
    if text in {"P", "PUT"}:
        return "PUT"
    return None


def _has_market_sector(ticker: str) -> bool:
    parts = ticker.strip().split()
    if not parts:
        return False
    return parts[-1].upper() in MARKET_SECTOR_KEYWORDS


def resolve_security(user_ticker: str) -> str:
    if _has_market_sector(user_ticker):
        return user_ticker

    with with_session() as query:
        raw = query.bsrch(user_ticker)
    df = _ensure_security_column(_to_pandas(raw))
    if df.empty or "security" not in df.columns:
        return user_ticker
    first = df["security"].dropna()
    if first.empty:
        return user_ticker
    return str(first.iloc[0])


def _chain_column_map(df: pd.DataFrame) -> pd.DataFrame:
    mapping = {
        "OPTION_TICKER": "option_ticker",
        "SECURITY": "option_ticker",
        "OPT_STRIKE_PX": "strike",
        "STRIKE": "strike",
        "OPT_PUT_CALL": "put_call",
        "PUT_CALL": "put_call",
        "OPT_EXPIRATION_DATE": "expiry",
        "EXPIRY": "expiry",
        "EXPIRATION": "expiry",
    }
    rename = {}
    for column in df.columns:
        key = column.upper()
        if key in mapping:
            rename[column] = mapping[key]
    df = df.rename(columns=rename)
    if "option_ticker" not in df.columns and "security" in df.columns:
        df = df.rename(columns={"security": "option_ticker"})
    return df


def _normalize_expiry(value: object) -> Optional[str]:
    if value is None:
        return None
    try:
        if pd.isna(value):
            return None
    except TypeError:
        pass
    if isinstance(value, date):
        return value.isoformat()
    text = str(value).strip()
    if text == "":
        return None
    parsed = pd.to_datetime(text, errors="coerce")
    if pd.isna(parsed):
        return None
    return parsed.date().isoformat()


def fetch_option_chain(
    underlying: str, expiry: str, spot: float, pct_window: float
) -> pd.DataFrame:
    lower = spot * (1.0 - pct_window)
    upper = spot * (1.0 + pct_window)
    expiry_key = pd.to_datetime(expiry).date().isoformat()
    bql_query = (
        "get(OPT_CHAIN('{underlying}'),"
        " 'OPTION_TICKER','OPT_STRIKE_PX','OPT_PUT_CALL','OPT_EXPIRATION_DATE') "
        "for(filter(OPT_CHAIN('{underlying}'),"
        " OPT_EXPIRATION_DATE='{expiry}'"
        " and OPT_STRIKE_PX>={lower}"
        " and OPT_STRIKE_PX<={upper}))"
    ).format(
        underlying=underlying,
        expiry=expiry_key,
        lower=lower,
        upper=upper,
    )

    with with_session() as query:
        raw = query.bql(bql_query)
    df = _ensure_security_column(_to_pandas(raw))
    df = _chain_column_map(df)

    required = {"option_ticker", "strike", "put_call", "expiry"}
    missing = required - set(df.columns)
    if missing:
        raise RuntimeError(
            f"Option chain response missing columns: {sorted(missing)}"
        )

    df["expiry"] = df["expiry"].apply(_normalize_expiry)
    df["strike"] = pd.to_numeric(df["strike"], errors="coerce")
    df["put_call"] = df["put_call"].apply(_normalize_put_call)
    df = df.dropna(subset=["option_ticker", "strike", "put_call", "expiry"])
    df = df[df["expiry"] == expiry_key]
    df = df[(df["strike"] >= lower) & (df["strike"] <= upper)]

    if df.empty:
        raise RuntimeError("Option chain query returned no rows.")

    return df[["option_ticker", "strike", "put_call", "expiry"]].copy()


def chain_strikes(chain_df: pd.DataFrame, put_call: str) -> list[float]:
    if chain_df is None or chain_df.empty:
        return []
    side = _normalize_put_call(put_call)
    if side is None:
        return []
    strikes = []
    for value, row_side in zip(chain_df["strike"], chain_df["put_call"]):
        if _normalize_put_call(row_side) != side:
            continue
        strike = _value_or_none(value)
        if strike is None:
            continue
        strikes.append(float(strike))
    return sorted(set(strikes))


def select_chain_ticker(
    chain_df: pd.DataFrame, put_call: str, strike: float
) -> Optional[str]:
    if chain_df is None or chain_df.empty:
        return None
    side = _normalize_put_call(put_call)
    if side is None:
        return None
    target = float(strike)
    candidates = chain_df[
        chain_df["put_call"].apply(_normalize_put_call) == side
    ]
    if candidates.empty:
        return None
    candidates = candidates.copy()
    candidates["strike"] = pd.to_numeric(candidates["strike"], errors="coerce")
    candidates = candidates.dropna(subset=["strike"])
    matches = candidates[
        (candidates["strike"] - target).abs() < 1e-6
    ]
    if matches.empty:
        return None
    return str(matches.iloc[0]["option_ticker"])


def _value_or_none(value: object) -> Optional[float]:
    if value is None:
        return None
    try:
        if pd.isna(value):
            return None
    except TypeError:
        pass
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def build_leg_price_updates(
    legs: list[Dict[str, object]],
    snapshot_df: pd.DataFrame,
    pricing_mode: str,
) -> Dict[int, float]:
    if snapshot_df is None or snapshot_df.empty:
        return {}
    df = _ensure_security_column(snapshot_df.copy())
    df = _ensure_columns(df, ["BID", "ASK", "PX_MID", "MID"])
    ticker_map: Dict[str, pd.Series] = {}
    for _, row in df.iterrows():
        security = str(row.get("security", "")).strip().upper()
        if security:
            ticker_map[security] = row

    updates: Dict[int, float] = {}
    for leg in legs:
        ticker = str(leg.get("ticker", "")).strip()
        if not ticker or leg.get("manual_override"):
            continue
        row = ticker_map.get(ticker.upper())
        if row is None:
            continue
        bid = _value_or_none(row.get("BID"))
        ask = _value_or_none(row.get("ASK"))
        mid = _value_or_none(row.get("PX_MID"))
        if mid is None:
            mid = _value_or_none(row.get("MID"))
        price = select_price(
            float(leg.get("position", 0.0)), bid, mid, ask, pricing_mode
        )
        if price is None:
            continue
        updates[int(leg["index"])] = float(price)
    return updates
