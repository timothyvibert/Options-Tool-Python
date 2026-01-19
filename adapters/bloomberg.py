from __future__ import annotations

from contextlib import contextmanager
from datetime import date, datetime
from typing import Dict, Iterable, Mapping, Optional, Sequence

import pandas as pd

from core.pricing import select_price


OPTION_SNAPSHOT_FIELDS = [
    "BID",
    "ASK",
    "PX_MID",
    "MID",
    "PX_LAST",
    "IVOL_MID",
    "IVOL",
    "DAYS_TO_EXPIRATION",
    "DAYS_EXPIRE",
    "OPT_STRIKE_PX",
    "OPT_PUT_CALL",
    "DELTA_MID_RT",
    "THETA",
    "THETA_MID",
    "GAMMA",
    "VEGA",
]
MARKET_SECTOR_KEYWORDS = {"EQUITY", "INDEX", "CURNCY", "COMDTY"}
DEFAULT_STRIKE_OFFSETS = [-0.5, 0.5, -1.0, 1.0, -2.5, 2.5, -5.0, 5.0]
UNDERLYING_FIELDS = [
    "PX_LAST",
    "NAME",
    "GICS_SECTOR_NAME",
    "INDUSTRY_SECTOR",
    "52WK_HIGH",
    "52WK_LOW",
    "HIGH_52WEEK",
    "LOW_52WEEK",
    "HIGH_DT_52WEEK",
    "LOW_DT_52WEEK",
    "CHG_PCT_1YR",
    "EQY_TRR_PCT_1YR",
    "CHG_PCT_5D",
    "CHG_PCT_3M",
    "CHG_PCT_YTD",
    "VOL_PERCENTILE",
    "3MTH_IMPVOL_100.0%MNY_DF",
    "EARNINGS_RELATED_IMPLIED_MOVE",
    "DVD_YLD",
    "EQY_DVD_YLD_IND",
    "DVD_EX_DT",
    "EQY_DVD_EX_DT",
    "DVD_EX_DATE",
    "EQY_DVD_EX_DATE",
    "EXPECTED_REPORT_DT",
    "EARNINGS_ANNOUNCEMENT_DATE",
]
DIVIDEND_FIELDS = [
    "DVD_EX_DT",
    "EQY_DVD_EX_DT",
    "DVD_EX_DATE",
    "EQY_DVD_EX_DATE",
]


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


def fetch_underlying_snapshot(ticker: str) -> pd.Series:
    if not ticker:
        return pd.Series(dtype=object)
    with with_session() as query:
        raw = query.bdp([ticker], UNDERLYING_FIELDS)
    df = _ensure_security_column(_to_pandas(raw))
    df = _ensure_columns(df, UNDERLYING_FIELDS)
    if df.empty:
        return pd.Series(dtype=object)
    row = df.loc[df["security"] == ticker]
    if row.empty:
        row = df.iloc[[0]]
    record = row.iloc[0].copy()
    def _clean_value(value: object) -> object:
        try:
            if pd.isna(value):
                return None
        except Exception:
            pass
        return value

    high_52week = record.get("HIGH_52WEEK")
    if pd.isna(high_52week):
        high_52week = record.get("52WK_HIGH")
    low_52week = record.get("LOW_52WEEK")
    if pd.isna(low_52week):
        low_52week = record.get("52WK_LOW")
    record["high_52week"] = _clean_value(high_52week)
    record["low_52week"] = _clean_value(low_52week)
    record["week_52_high"] = record.get("high_52week")
    record["week_52_low"] = record.get("low_52week")
    record["high_dt_52week"] = _clean_value(record.get("HIGH_DT_52WEEK"))
    record["low_dt_52week"] = _clean_value(record.get("LOW_DT_52WEEK"))
    record["chg_pct_1yr"] = _clean_value(record.get("CHG_PCT_1YR"))
    record["eqy_trr_pct_1yr"] = _clean_value(record.get("EQY_TRR_PCT_1YR"))
    record["chg_pct_5d"] = _clean_value(record.get("CHG_PCT_5D"))
    record["chg_pct_3m"] = _clean_value(record.get("CHG_PCT_3M"))
    record["chg_pct_ytd"] = _clean_value(record.get("CHG_PCT_YTD"))
    record["vol_percentile"] = _clean_value(record.get("VOL_PERCENTILE"))
    record["impvol_3m_atm"] = _clean_value(record.get("3MTH_IMPVOL_100.0%MNY_DF"))
    record["earnings_related_implied_move"] = _clean_value(
        record.get("EARNINGS_RELATED_IMPLIED_MOVE")
    )
    bds_dividend = fetch_projected_dividend(ticker)
    bdp_ex_div_date = get_next_dividend_date(ticker, snapshot=record.to_dict())
    ex_div_date = bds_dividend.get("ex_div_date") or bdp_ex_div_date
    record["ex_div_date"] = ex_div_date
    record["projected_dividend"] = bds_dividend.get("projected_dividend")
    record["dividend_status"] = bds_dividend.get("dividend_status")
    record["dividend_debug"] = bds_dividend.get("debug") or {}
    return record


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
                "IVOL",
                "DAYS_TO_EXPIRATION",
                "DAYS_EXPIRE",
                "OPT_STRIKE_PX",
                "OPT_PUT_CALL",
                "DELTA_MID_RT",
                "THETA",
                "THETA_MID",
                "GAMMA",
                "VEGA",
                "dte",
                "delta_mid",
                "theta",
                "gamma",
                "vega",
                "iv_mid",
            ]
        )

    with with_session() as query:
        raw = query.bdp(option_tickers, OPTION_SNAPSHOT_FIELDS)
    df = _ensure_security_column(_to_pandas(raw))
    df = _ensure_columns(df, OPTION_SNAPSHOT_FIELDS)
    if "MID" in df.columns:
        df["PX_MID"] = pd.to_numeric(df["PX_MID"], errors="coerce")
        mid_values = pd.to_numeric(df["MID"], errors="coerce")
        df["PX_MID"] = df["PX_MID"].fillna(mid_values)
    if "MID" in df.columns:
        df = df.drop(columns=["MID"])

    numeric_fields = [
        "BID",
        "ASK",
        "PX_MID",
        "PX_LAST",
        "IVOL_MID",
        "IVOL",
        "DAYS_TO_EXPIRATION",
        "DAYS_EXPIRE",
        "OPT_STRIKE_PX",
        "DELTA_MID_RT",
        "THETA",
        "THETA_MID",
        "GAMMA",
        "VEGA",
    ]
    for field in numeric_fields:
        if field in df.columns:
            df[field] = pd.to_numeric(df[field], errors="coerce")

    dte = pd.to_numeric(df.get("DAYS_TO_EXPIRATION"), errors="coerce")
    if "DAYS_EXPIRE" in df.columns:
        dte_alt = pd.to_numeric(df.get("DAYS_EXPIRE"), errors="coerce")
        dte = dte.fillna(dte_alt)
    df["dte"] = dte

    df["delta_mid"] = pd.to_numeric(df.get("DELTA_MID_RT"), errors="coerce")
    theta = pd.to_numeric(df.get("THETA"), errors="coerce")
    if "THETA_MID" in df.columns:
        theta = theta.fillna(pd.to_numeric(df.get("THETA_MID"), errors="coerce"))
    df["theta"] = theta
    df["gamma"] = pd.to_numeric(df.get("GAMMA"), errors="coerce")
    df["vega"] = pd.to_numeric(df.get("VEGA"), errors="coerce")
    iv_mid = pd.to_numeric(df.get("IVOL_MID"), errors="coerce")
    if "IVOL" in df.columns:
        iv_mid = iv_mid.fillna(pd.to_numeric(df.get("IVOL"), errors="coerce"))
    df["iv_mid"] = iv_mid
    return df[
        [
            "security",
            "BID",
            "ASK",
            "PX_MID",
            "PX_LAST",
            "IVOL_MID",
            "IVOL",
            "DAYS_TO_EXPIRATION",
            "DAYS_EXPIRE",
            "OPT_STRIKE_PX",
            "OPT_PUT_CALL",
            "DELTA_MID_RT",
            "THETA",
            "THETA_MID",
            "GAMMA",
            "VEGA",
            "dte",
            "delta_mid",
            "theta",
            "gamma",
            "vega",
            "iv_mid",
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


def _normalize_dividend_date(value: object) -> Optional[date]:
    if value is None:
        return None
    try:
        if pd.isna(value):
            return None
    except TypeError:
        pass
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, pd.Timestamp):
        return value.date()
    parsed = pd.to_datetime(value, errors="coerce")
    if pd.isna(parsed):
        return None
    return parsed.date()


def get_next_dividend_date(
    ticker: str, snapshot: Optional[Dict[str, object]] = None
) -> Optional[date]:
    if snapshot:
        for field in DIVIDEND_FIELDS:
            value = snapshot.get(field)
            parsed = _normalize_dividend_date(value)
            if parsed is not None:
                return parsed

    if not ticker:
        return None

    with with_session() as query:
        raw = query.bdp([ticker], DIVIDEND_FIELDS)
    df = _ensure_security_column(_to_pandas(raw))
    df = _ensure_columns(df, DIVIDEND_FIELDS)
    if df.empty:
        return None
    row = df.loc[df["security"] == ticker]
    if row.empty:
        row = df.iloc[[0]]
    record = row.iloc[0]
    for field in DIVIDEND_FIELDS:
        parsed = _normalize_dividend_date(record.get(field))
        if parsed is not None:
            return parsed
    return None


def _fetch_bds_rows(security: str, field: str) -> tuple[list[dict], Optional[str]]:
    error = None
    try:
        with with_session() as query:
            bds_fn = getattr(query, "bds", None)
            if callable(bds_fn):
                raw = bds_fn([security], field)
                df = _to_pandas(raw)
                if isinstance(df, pd.DataFrame):
                    return df.to_dict(orient="records"), None
                return [], None
    except Exception as exc:
        error = str(exc)

    try:
        import blpapi
    except Exception as exc:
        return [], error or str(exc)

    session = blpapi.Session()
    if not session.start():
        return [], error or "Failed to start Bloomberg session."
    try:
        if not session.openService("//blp/refdata"):
            return [], error or "Failed to open //blp/refdata."
        service = session.getService("//blp/refdata")
        request = service.createRequest("ReferenceDataRequest")
        request.getElement("securities").appendValue(security)
        request.getElement("fields").appendValue(field)
        session.sendRequest(request)
        rows: list[dict] = []
        request_error = error
        while True:
            event = session.nextEvent()
            for message in event:
                if message.hasElement("responseError"):
                    request_error = str(message.getElement("responseError"))
                if not message.hasElement("securityData"):
                    continue
                sec_data_array = message.getElement("securityData")
                for i in range(sec_data_array.numValues()):
                    sec_data = sec_data_array.getValueAsElement(i)
                    if sec_data.hasElement("securityError"):
                        request_error = str(sec_data.getElement("securityError"))
                        continue
                    if not sec_data.hasElement("fieldData"):
                        continue
                    field_data = sec_data.getElement("fieldData")
                    if not field_data.hasElement(field):
                        continue
                    bulk = field_data.getElement(field)
                    for j in range(bulk.numValues()):
                        row_elem = bulk.getValueAsElement(j)
                        row: dict[str, object] = {}
                        for k in range(row_elem.numElements()):
                            elem = row_elem.getElement(k)
                            name = str(elem.name())
                            if elem.isNull():
                                value = None
                            else:
                                try:
                                    value = elem.getValue()
                                except Exception:
                                    value = str(elem)
                            row[name] = value
                        rows.append(row)
            if event.eventType() == blpapi.Event.RESPONSE:
                break
        return rows, request_error
    finally:
        session.stop()


def fetch_projected_dividend(
    ticker: str, as_of_date: Optional[date] = None
) -> Dict[str, object]:
    debug = {
        "dataset": "BDVD_PR_EX_DTS_DVD_AMTS_W_ANN",
        "rows": None,
        "first_row": None,
        "selected_row": None,
        "parsed": {
            "ex_div_date": None,
            "projected_dividend": None,
            "dividend_status": None,
        },
        "error": None,
    }
    if not ticker:
        return {
            "ex_div_date": None,
            "projected_dividend": None,
            "dividend_status": None,
            "debug": debug,
        }
    rows, error = _fetch_bds_rows(
        ticker, "BDVD_PR_EX_DTS_DVD_AMTS_W_ANN"
    )
    debug["error"] = error
    debug["rows"] = len(rows)
    if not rows:
        return {
            "ex_div_date": None,
            "projected_dividend": None,
            "dividend_status": None,
            "debug": debug,
        }

    date_keys = [
        "EX DATE",
        "EX_DATE",
        "DVD_EX_DT",
        "EX_DIV_DATE",
        "EX-DATE",
        "EX DATE (PROJECTED)",
    ]
    amount_keys = [
        "AMOUNT",
        "DVD_AMT",
        "DIVIDEND AMOUNT",
        "PROJECTED DIVIDEND",
        "DIVIDEND",
    ]
    type_keys = [
        "TYPE",
        "DIVIDEND TYPE",
        "STATUS",
        "DIVIDEND STATUS",
        "DVD_TYPE",
    ]

    def _pick_value(row: Mapping[str, object], keys: Iterable[str]) -> object:
        for key in keys:
            if key in row:
                return row.get(key)
        return None

    def _first_date_like(values: Iterable[object]) -> Optional[date]:
        for value in values:
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                continue
            parsed = _normalize_dividend_date(value)
            if parsed is not None:
                return parsed
        return None

    def _first_numeric_like(values: Iterable[object]) -> Optional[float]:
        for value in values:
            if isinstance(value, (datetime, date, pd.Timestamp)):
                continue
            if _normalize_dividend_date(value) is not None and not isinstance(
                value, (int, float, str)
            ):
                continue
            numeric = pd.to_numeric(value, errors="coerce")
            if pd.isna(numeric):
                continue
            return float(numeric)
        return None

    def _coerce_status(value: object) -> Optional[str]:
        if value is None:
            return None
        try:
            if pd.isna(value):
                return None
        except TypeError:
            pass
        text = str(value).strip()
        return text if text else None

    parsed_rows = []
    for idx, row in enumerate(rows):
        row_map = {str(key).strip(): value for key, value in row.items()}
        upper_map = {key.upper(): value for key, value in row_map.items()}
        ex_div_raw = _pick_value(upper_map, date_keys)
        if ex_div_raw is None:
            ex_div_date = _first_date_like(row_map.values())
        else:
            ex_div_date = _normalize_dividend_date(ex_div_raw)

        projected_raw = _pick_value(upper_map, amount_keys)
        if projected_raw is None:
            projected_value = _first_numeric_like(row_map.values())
        else:
            projected_value = pd.to_numeric(projected_raw, errors="coerce")
            if pd.isna(projected_value):
                projected_value = None
            else:
                projected_value = float(projected_value)

        status_raw = _pick_value(upper_map, type_keys)
        status_value = _coerce_status(status_raw)

        parsed_rows.append(
            {
                "index": idx,
                "ex_div_date": ex_div_date,
                "projected_dividend": projected_value,
                "dividend_status": status_value,
                "raw": row_map,
            }
        )

    if parsed_rows:
        debug_first = {}
        for key, value in parsed_rows[0]["raw"].items():
            text = str(value)
            if len(text) > 120:
                text = text[:117] + "..."
            debug_first[key] = text
        debug["first_row"] = debug_first

    as_of_date = as_of_date or datetime.now().date()
    candidates = [
        row for row in parsed_rows
        if row["ex_div_date"] is not None and row["ex_div_date"] >= as_of_date
    ]

    def _is_projection(status: Optional[str]) -> bool:
        if not status:
            return False
        upper = status.upper()
        return "BDVD" in upper or "PROJ" in upper

    selected = None
    preferred = [row for row in candidates if _is_projection(row["dividend_status"])]
    if preferred:
        selected = sorted(preferred, key=lambda row: row["index"])[0]
    elif candidates:
        selected = sorted(
            candidates, key=lambda row: (row["ex_div_date"], row["index"])
        )[0]

    if selected is None:
        return {
            "ex_div_date": None,
            "projected_dividend": None,
            "dividend_status": None,
            "debug": debug,
        }

    parsed_ex_div = selected["ex_div_date"]
    projected_value = selected["projected_dividend"]
    status_value = selected["dividend_status"]
    debug["selected_row"] = {
        "ex_div_date": parsed_ex_div,
        "projected_dividend": projected_value,
        "dividend_status": status_value,
    }
    debug["parsed"] = {
        "ex_div_date": parsed_ex_div,
        "projected_dividend": projected_value,
        "dividend_status": status_value,
    }
    return {
        "ex_div_date": parsed_ex_div,
        "projected_dividend": projected_value,
        "dividend_status": status_value,
        "debug": debug,
    }


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
