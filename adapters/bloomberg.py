from __future__ import annotations

from contextlib import contextmanager
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
