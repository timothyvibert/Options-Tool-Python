from __future__ import annotations

from contextlib import contextmanager
from datetime import date, datetime
from typing import Dict, Iterable, Optional, Sequence

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
DEFAULT_STRIKE_OFFSETS = [-0.5, 0.5, -1.0, 1.0, -2.5, 2.5, -5.0, 5.0]


@contextmanager
def with_session():
    from polars_bloomberg import BQuery

    with BQuery() as query:
        yield query


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


def normalize_iso_date(value: object) -> Optional[str]:
    if value is None:
        return None
    try:
        if pd.isna(value):
            return None
    except TypeError:
        pass
    if isinstance(value, pd.Timestamp):
        return value.date().isoformat()
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    text = str(value).strip()
    if text == "":
        return None
    if len(text) == 10 and text[4] == "-" and text[7] == "-":
        return text
    parsed = pd.to_datetime(text, errors="coerce")
    if pd.isna(parsed):
        return None
    return parsed.date().isoformat()


def format_bbg_expiry(expiry: object) -> str:
    if isinstance(expiry, (date, datetime, pd.Timestamp)):
        expiry_date = expiry.date() if isinstance(expiry, datetime) else expiry
    else:
        parsed = pd.to_datetime(expiry, errors="coerce")
        if pd.isna(parsed):
            raise ValueError("Invalid expiry provided for Bloomberg ticker.")
        expiry_date = parsed.date()
    month = expiry_date.month
    day = expiry_date.day
    year = expiry_date.year % 100
    return f"{month}/{day}/{year:02d}"


def _strip_sector_suffix(underlying: str) -> str:
    parts = underlying.strip().split()
    if not parts:
        return ""
    if parts[-1].upper() in MARKET_SECTOR_KEYWORDS:
        parts = parts[:-1]
    return " ".join(parts).strip()


def _infer_sector_suffix(underlying: str, sector_hint: Optional[str]) -> str:
    hint = (sector_hint or "").strip()
    if hint:
        hint_key = hint.upper()
        if hint_key in MARKET_SECTOR_KEYWORDS:
            return hint_key.title()
        return hint
    if "INDEX" in underlying.upper():
        return "Index"
    return "Equity"


def _format_strike_for_ticker(strike: float) -> str:
    try:
        value = float(strike)
    except (TypeError, ValueError):
        raise ValueError("Strike must be numeric for ticker construction.")
    if abs(value - round(value)) < 1e-6:
        return str(int(round(value)))
    text = f"{value:.6f}".rstrip("0").rstrip(".")
    return text


def construct_option_ticker(
    underlying: str,
    expiry: str,
    put_call: str,
    strike: float,
    sector_hint: Optional[str] = None,
) -> str:
    base = _strip_sector_suffix(underlying)
    if not base:
        raise ValueError("Underlying is required for ticker construction.")
    side = _normalize_put_call(put_call)
    if side is None:
        raise ValueError("put_call must be CALL or PUT.")
    prefix = "C" if side == "CALL" else "P"
    expiry_text = format_bbg_expiry(expiry)
    strike_text = _format_strike_for_ticker(strike)
    sector = _infer_sector_suffix(underlying, sector_hint)
    return f"{base} {expiry_text} {prefix}{strike_text} {sector}".strip()


def validate_tickers(tickers: list[str]) -> pd.DataFrame:
    if not tickers:
        return pd.DataFrame(columns=["security"])
    fields = [
        "PX_LAST",
        "BID",
        "ASK",
        "PX_MID",
        "MID",
        "OPT_EXPIRATION_DATE",
        "OPT_STRIKE_PX",
        "OPT_PUT_CALL",
    ]
    with with_session() as query:
        raw = query.bdp(tickers, fields)
    df = _ensure_security_column(_to_pandas(raw))
    df = _ensure_columns(df, fields)
    if "PX_MID" not in df.columns and "MID" in df.columns:
        df["PX_MID"] = df["MID"]
    key_fields = [
        "PX_LAST",
        "BID",
        "ASK",
        "PX_MID",
        "MID",
        "OPT_EXPIRATION_DATE",
        "OPT_STRIKE_PX",
        "OPT_PUT_CALL",
    ]
    mask = pd.Series(False, index=df.index)
    for field in key_fields:
        if field in df.columns:
            mask = mask | df[field].notna()
    return df[mask].copy()


def resolve_option_ticker_from_strike(
    underlying: str,
    expiry: str,
    put_call: str,
    strike: float,
    sector_hint: Optional[str] = None,
    offsets: Optional[Sequence[float]] = None,
) -> Optional[str]:
    exact = construct_option_ticker(
        underlying, expiry, put_call, strike, sector_hint
    )
    exact_df = validate_tickers([exact])
    if not exact_df.empty:
        return exact

    offset_list = list(offsets) if offsets is not None else DEFAULT_STRIKE_OFFSETS
    candidates: list[str] = []
    seen: set[str] = set()
    for offset in offset_list:
        if offset == 0:
            continue
        candidate_strike = float(strike) + float(offset)
        if candidate_strike <= 0:
            continue
        ticker = construct_option_ticker(
            underlying, expiry, put_call, candidate_strike, sector_hint
        )
        key = ticker.upper()
        if key in seen:
            continue
        seen.add(key)
        candidates.append(ticker)

    if not candidates:
        return None
    validated = validate_tickers(candidates)
    if validated.empty:
        return None
    valid_set = {
        str(value).strip().upper()
        for value in validated["security"].dropna().tolist()
    }
    for ticker in candidates:
        if ticker.upper() in valid_set:
            return ticker
    return None


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
