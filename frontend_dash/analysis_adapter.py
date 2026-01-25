from __future__ import annotations

import math
from dataclasses import asdict, is_dataclass
from datetime import date, datetime, timezone
from decimal import Decimal
from typing import Mapping

try:
    import numpy as np
except Exception:  # pragma: no cover - optional dependency
    np = None

try:
    import pandas as pd
except Exception:  # pragma: no cover - optional dependency
    pd = None


def to_jsonable(obj):
    if obj is None or isinstance(obj, (bool, int, str)):
        return obj
    if isinstance(obj, float):
        if not math.isfinite(obj):
            return None
        return obj
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        return float(obj)
    if np is not None and isinstance(obj, np.ndarray):
        return [to_jsonable(item) for item in obj.tolist()]
    if np is not None and isinstance(obj, np.generic):
        return to_jsonable(obj.item())
    if pd is not None and isinstance(obj, pd.DataFrame):
        records_raw = obj.to_dict("records")
        records_clean = [to_jsonable(record) for record in records_raw]
        return {
            "__type__": "DataFrame",
            "columns": [str(col) for col in obj.columns],
            "records": records_clean,
        }
    if pd is not None and isinstance(obj, pd.Series):
        data_raw = obj.to_dict()
        return {"__type__": "Series", "data": to_jsonable(data_raw)}
    if isinstance(obj, Mapping):
        return {str(key): to_jsonable(value) for key, value in obj.items()}
    if isinstance(obj, (list, tuple, set)):
        return [to_jsonable(item) for item in obj]
    if is_dataclass(obj):
        return to_jsonable(asdict(obj))
    return str(obj)


def analysis_pack_to_store(pack: dict) -> dict:
    if not isinstance(pack, dict):
        return {"error": "invalid pack"}
    return to_jsonable(pack)


def utc_now_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def find_bbg_helpers() -> dict[str, callable]:
    try:
        from adapters import bloomberg as bbg
    except Exception:
        return {}
    helpers: dict[str, callable] = {}
    for name in (
        "resolve_security",
        "fetch_spot",
        "fetch_underlying_snapshot",
        "fetch_option_snapshot",
        "resolve_option_ticker_from_strike",
    ):
        func = getattr(bbg, name, None)
        if callable(func):
            helpers[name] = func
    return helpers


def fetch_bloomberg_snapshot(
    raw_ticker: str,
    expiry: str | None,
    legs: list[dict],
) -> dict:
    timestamp = utc_now_str()
    snapshot = {
        "refreshed_at": timestamp,
        "resolved_underlying": (raw_ticker or "").strip() or None,
        "market_spot": None,
        "underlying_profile": None,
        "leg_quotes": [],
        "per_leg_iv": [],
        "errors": [],
    }
    errors: list[str] = []
    helpers = find_bbg_helpers()
    resolve_security = helpers.get("resolve_security")
    fetch_spot = helpers.get("fetch_spot")
    fetch_underlying_snapshot = helpers.get("fetch_underlying_snapshot")
    fetch_option_snapshot = helpers.get("fetch_option_snapshot")
    resolve_option_ticker_from_strike = helpers.get("resolve_option_ticker_from_strike")
    if not all(
        [
            resolve_security,
            fetch_spot,
            fetch_underlying_snapshot,
            fetch_option_snapshot,
            resolve_option_ticker_from_strike,
        ]
    ):
        errors.append("Bloomberg fetch functions not found in repo.")
        snapshot["errors"] = errors
        return snapshot

    raw = (raw_ticker or "").strip()
    resolved = ""
    if raw:
        try:
            resolved = resolve_security(raw)
        except Exception as exc:
            errors.append(f"Resolve security failed: {exc}")
    if not resolved:
        errors.append("No ticker provided for Bloomberg snapshot.")
        snapshot["errors"] = errors
        return snapshot

    snapshot["resolved_underlying"] = resolved

    try:
        spot_result = fetch_spot(resolved)
        if isinstance(spot_result, dict):
            spot_value = spot_result.get("spot")
            if spot_value is None:
                spot_value = spot_result.get("px_last")
            if spot_value is None:
                spot_value = spot_result.get("PX_LAST")
        else:
            spot_value = spot_result
        snapshot["market_spot"] = to_jsonable(spot_value)
    except Exception as exc:
        errors.append(f"Spot fetch failed: {exc}")

    try:
        underlying = fetch_underlying_snapshot(resolved)
        if hasattr(underlying, "to_dict"):
            underlying = underlying.to_dict()
        snapshot["underlying_profile"] = to_jsonable(underlying) if underlying else {}
    except Exception as exc:
        errors.append(f"Underlying snapshot failed: {exc}")
        snapshot["underlying_profile"] = {}

    option_tickers: list[str] = []
    leg_tickers: list[str | None] = []
    for idx, leg in enumerate(legs or []):
        if not isinstance(leg, dict):
            leg_tickers.append(None)
            errors.append(f"Leg {idx + 1}: invalid leg data")
            continue
        kind = str(leg.get("kind", "")).strip().lower()
        strike = leg.get("strike")
        if kind not in {"call", "put"} or strike is None:
            leg_tickers.append(None)
            errors.append(f"Leg {idx + 1}: missing kind/strike")
            continue
        if not expiry:
            leg_tickers.append(None)
            errors.append(f"Leg {idx + 1}: missing expiry")
            continue
        put_call = "CALL" if kind == "call" else "PUT"
        try:
            ticker = resolve_option_ticker_from_strike(
                resolved, expiry, put_call, float(strike)
            )
        except Exception as exc:
            ticker = None
            errors.append(f"Leg {idx + 1}: ticker resolve failed ({exc})")
        leg_tickers.append(ticker)
        if ticker:
            option_tickers.append(ticker)
        else:
            errors.append(f"Leg {idx + 1}: no valid option ticker")

    quotes: list[dict] = [{} for _ in leg_tickers]
    per_leg_iv: list[float | None] = [None for _ in leg_tickers]
    if option_tickers:
        try:
            df = fetch_option_snapshot(option_tickers)
            if pd is not None and df is not None and not df.empty:
                if "security" in df.columns:
                    df_key = df.set_index("security")
                else:
                    df_key = df
                for idx, ticker in enumerate(leg_tickers):
                    if not ticker or ticker not in df_key.index:
                        continue
                    row = df_key.loc[ticker]
                    if hasattr(row, "to_dict"):
                        row = row.to_dict()
                    bid = row.get("BID")
                    ask = row.get("ASK")
                    mid = row.get("PX_MID") or row.get("MID")
                    last = row.get("PX_LAST")
                    iv = row.get("IVOL_MID") or row.get("iv_mid")
                    quote = {
                        "bid": to_jsonable(bid),
                        "ask": to_jsonable(ask),
                        "mid": to_jsonable(mid),
                        "last": to_jsonable(last),
                        "iv": to_jsonable(iv),
                    }
                    quotes[idx] = quote
                    per_leg_iv[idx] = to_jsonable(iv)
        except Exception as exc:
            errors.append(f"Option snapshot failed: {exc}")

    snapshot["leg_quotes"] = quotes
    snapshot["per_leg_iv"] = per_leg_iv
    snapshot["errors"] = errors
    return snapshot


def refresh_leg_premiums(
    raw_underlying: str,
    resolved_underlying: str | None,
    expiry: str,
    legs_rows: list[dict],
    pricing_mode: str,
) -> tuple[list[dict], dict, str]:
    timestamp = utc_now_str()
    market_snapshot = {
        "refreshed_at": timestamp,
        "resolved_underlying": None,
        "leg_quotes": [],
        "per_leg_iv": [],
        "errors": [],
    }
    errors: list[str] = []
    try:
        from adapters.bloomberg import (
            fetch_option_snapshot,
            resolve_option_ticker_from_strike,
            resolve_security,
        )
    except Exception as exc:
        errors.append(f"Bloomberg helpers unavailable: {exc}")
        market_snapshot["errors"] = errors
        return legs_rows, market_snapshot, "Refresh failed: Bloomberg unavailable"

    base = (resolved_underlying or "").strip()
    if not base:
        raw = (raw_underlying or "").strip()
        if raw:
            try:
                base = resolve_security(raw)
            except Exception as exc:
                errors.append(f"Resolve security failed: {exc}")
        if not base:
            base = raw
    market_snapshot["resolved_underlying"] = base or None

    option_tickers: list[str] = []
    row_tickers: list[str | None] = []
    updated_rows: list[dict] = []
    for idx, row in enumerate(legs_rows or []):
        if not isinstance(row, dict):
            row_tickers.append(None)
            updated_rows.append(row)
            errors.append(f"Leg {idx + 1}: invalid row")
            continue
        kind = str(row.get("kind", "")).strip().lower()
        strike = row.get("strike")
        if kind not in {"call", "put"} or strike is None:
            row_tickers.append(None)
            updated_rows.append(dict(row))
            errors.append(f"Leg {idx + 1}: missing kind/strike")
            continue
        put_call = "CALL" if kind == "call" else "PUT"
        try:
            ticker = resolve_option_ticker_from_strike(
                base, expiry, put_call, float(strike)
            )
        except Exception as exc:
            ticker = None
            errors.append(f"Leg {idx + 1}: ticker resolve failed ({exc})")
        row_tickers.append(ticker)
        updated_row = dict(row)
        if ticker and "bbg_ticker" in row:
            updated_row["bbg_ticker"] = ticker
        updated_rows.append(updated_row)
        if ticker:
            option_tickers.append(ticker)
        else:
            errors.append(f"Leg {idx + 1}: no valid ticker")

    unique_tickers = list(dict.fromkeys(option_tickers))
    quotes_by_ticker: dict[str, dict] = {}
    if unique_tickers:
        try:
            raw_quotes = fetch_option_snapshot(unique_tickers)
            if pd is not None and isinstance(raw_quotes, pd.DataFrame):
                df = raw_quotes
                if "security" in df.columns:
                    df = df.set_index("security")
                for ticker in unique_tickers:
                    if ticker in df.index:
                        row = df.loc[ticker]
                        if hasattr(row, "to_dict"):
                            quotes_by_ticker[ticker] = row.to_dict()
            elif isinstance(raw_quotes, dict):
                quotes_by_ticker = raw_quotes
        except Exception as exc:
            errors.append(f"Option snapshot failed: {exc}")

    def _get_field(quote: dict, keys: list[str]) -> float | None:
        for key in keys:
            if key in quote and quote[key] is not None:
                try:
                    return float(quote[key])
                except (TypeError, ValueError):
                    continue
        return None

    def _select_premium(quote: dict, position: float, mode: str) -> float:
        bid = _get_field(quote, ["BID", "PX_BID", "bid"])
        ask = _get_field(quote, ["ASK", "PX_ASK", "ask"])
        mid = _get_field(quote, ["PX_MID", "MID", "mid"])
        last = _get_field(quote, ["PX_LAST", "last"])
        avg = None
        if bid is not None and ask is not None:
            avg = (bid + ask) / 2.0
        mode_key = (mode or "").strip().lower()
        if mode_key == "mid":
            for value in (mid, avg, bid, ask, last):
                if value is not None:
                    return float(value)
            return 0.0
        if position > 0:
            for value in (ask, mid, avg, bid, last):
                if value is not None:
                    return float(value)
            return 0.0
        if position < 0:
            for value in (bid, mid, avg, ask, last):
                if value is not None:
                    return float(value)
            return 0.0
        for value in (mid, avg, bid, ask, last):
            if value is not None:
                return float(value)
        return 0.0

    updated_with_premiums: list[dict] = []
    leg_quotes: list[dict] = []
    per_leg_iv: list[float | None] = []
    for idx, row in enumerate(updated_rows):
        if not isinstance(row, dict):
            updated_with_premiums.append(row)
            leg_quotes.append({})
            per_leg_iv.append(None)
            continue
        ticker = row_tickers[idx] if idx < len(row_tickers) else None
        quote = quotes_by_ticker.get(ticker, {}) if ticker else {}
        position = row.get("position")
        try:
            position_val = float(position)
        except (TypeError, ValueError):
            position_val = 0.0
        premium = _select_premium(quote, position_val, pricing_mode)
        updated_row = dict(row)
        updated_row["premium"] = abs(float(premium))
        updated_with_premiums.append(updated_row)
        leg_quotes.append(
            {
                "bid": _get_field(quote, ["BID", "PX_BID", "bid"]),
                "ask": _get_field(quote, ["ASK", "PX_ASK", "ask"]),
                "mid": _get_field(quote, ["PX_MID", "MID", "mid"]),
                "last": _get_field(quote, ["PX_LAST", "last"]),
                "iv": _get_field(quote, ["IVOL_MID", "IV_MID", "iv_mid", "iv"]),
            }
        )
        per_leg_iv.append(leg_quotes[-1]["iv"])

    status = f"Market refreshed at {timestamp}"
    if errors:
        status = f"{status} (errors: {len(errors)})"
    market_snapshot["leg_quotes"] = leg_quotes
    market_snapshot["per_leg_iv"] = per_leg_iv
    market_snapshot["errors"] = errors
    return updated_with_premiums, market_snapshot, status
