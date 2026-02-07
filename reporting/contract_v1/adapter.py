from __future__ import annotations

import re
from datetime import date, datetime
from typing import Any, Dict, Iterable, List, Mapping, Optional

FieldStatus = str

MISSING_TEXT = {"", "--", "—", "â€”", "N/A", "n/a", "NA", "na"}


def _is_missing(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip() in MISSING_TEXT
    return False


def _field(value: object, status: Optional[FieldStatus] = None) -> Dict[str, object]:
    if status is None:
        if _is_missing(value):
            return {"value": None, "status": "not_computed"}
        return {"value": value, "status": "computed"}
    if _is_missing(value):
        value = None
    return {"value": value, "status": status}


def _pick(mapping: Mapping[str, object], keys: Iterable[str]) -> object:
    for key in keys:
        if key in mapping and not _is_missing(mapping.get(key)):
            return mapping.get(key)
    return None


def _as_mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _as_list(value: object) -> List[Mapping[str, object]]:
    if isinstance(value, list):
        return [item for item in value if isinstance(item, Mapping)]
    return []


def _parse_number(value: object) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        if isinstance(value, float) and value != value:
            return None
        return float(value)
    if isinstance(value, str):
        text = value.strip()
        if text in MISSING_TEXT:
            return None
        negative = text.startswith("(") and text.endswith(")")
        if negative:
            text = text[1:-1]
        lower = text.lower()
        sign = -1.0 if negative else 1.0
        if "debit" in lower and "-" not in text:
            sign = -1.0
        if "credit" in lower and "-" not in text:
            sign = 1.0
        cleaned = re.sub(r"[^0-9.\-]", "", text)
        if cleaned in ("", "-", "."):
            return None
        try:
            return sign * float(cleaned)
        except ValueError:
            return None
    return None


def _parse_shares_value(value: object) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        text = value.strip()
        if text in MISSING_TEXT:
            return None
        match = re.search(r"[-+]?\d*\.?\d+", text.replace(",", ""))
        if not match:
            return None
        try:
            return float(match.group(0))
        except ValueError:
            return None
    return None


def _parse_value(value: object) -> Optional[object]:
    number = _parse_number(value)
    if number is not None:
        return number
    if _is_missing(value):
        return None
    if isinstance(value, str):
        return value.strip()
    return value


def _normalize_iso_datetime(value: object) -> str:
    if _is_missing(value):
        return ""
    if isinstance(value, datetime):
        return value.replace(microsecond=0).isoformat()
    if isinstance(value, date):
        return datetime(value.year, value.month, value.day).isoformat() + "Z"
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return ""
        if re.match(r"^\d{4}-\d{2}-\d{2}$", text):
            return f"{text}T00:00:00Z"
        if re.match(r"^\d{2}/\d{2}/\d{4}$", text):
            try:
                parsed = datetime.strptime(text, "%m/%d/%Y")
                return parsed.isoformat() + "Z"
            except ValueError:
                return text
        return text
    return str(value)


def _normalize_side(raw: object) -> str:
    if _is_missing(raw):
        return ""
    text = str(raw).strip().lower()
    if "short" in text or "sell" in text or text.startswith("s"):
        return "Sell"
    return "Buy"


def _normalize_type(raw: object) -> str:
    if _is_missing(raw):
        return ""
    text = str(raw).strip().lower()
    if "put" in text or text == "p":
        return "PUT"
    if "call" in text or text == "c":
        return "CALL"
    return str(raw).strip().upper()


def _scenario_rows_from_legacy(legacy: Mapping[str, object]) -> List[Mapping[str, object]]:
    for key in [
        "key_levels_display_rows_by_price",
        "key_levels_display_rows",
        "key_levels_rows_by_price",
        "key_levels_rows",
        "key_levels",
    ]:
        rows = legacy.get(key)
        if isinstance(rows, list) and rows:
            return [row for row in rows if isinstance(row, Mapping)]
    return []


def _extract_strategy_description(legacy: Mapping[str, object]) -> Optional[str]:
    direct = legacy.get("strategy_description")
    if isinstance(direct, str) and direct.strip():
        return direct.strip()
    return None


def _join_disclosures(value: object) -> Optional[str]:
    if isinstance(value, list):
        parts = [str(item).strip() for item in value if str(item).strip()]
        parts = [part for part in parts if part not in MISSING_TEXT]
        return " ".join(parts) if parts else None
    if isinstance(value, str):
        text = value.strip()
        return text if text and text not in MISSING_TEXT else None
    return None


def build_report_contract_v1(legacy_report_model: Dict[str, object]) -> Dict[str, object]:
    legacy = legacy_report_model if isinstance(legacy_report_model, Mapping) else {}
    header = _as_mapping(legacy.get("header"))
    structure = _as_mapping(legacy.get("structure"))
    metrics_block = _as_mapping(legacy.get("metrics"))
    metrics_rows = _as_list(metrics_block.get("rows"))
    stock_banner = _as_mapping(legacy.get("stock_banner"))

    as_of = _normalize_iso_datetime(header.get("report_time"))
    has_scenario_data = False
    scenario_table = _as_mapping(legacy.get("scenario_table"))
    scenario_full = scenario_table.get("full")
    if isinstance(scenario_full, list) and scenario_full:
        has_scenario_data = True
    if _scenario_rows_from_legacy(legacy):
        has_scenario_data = True

    move_pct_value = _parse_value(
        _pick(stock_banner, ["chg_pct_ytd"]) or _pick(header, ["chg_pct_ytd"])
    )

    ticker = _field(_pick(header, ["ticker"]))
    name = _field(_pick(header, ["name"]))
    sector = _field(_pick(header, ["sector"]))
    spot_value = _parse_value(_pick(header, ["last_price"]))
    spot = _field(spot_value)
    dividend_yield = _field(
        _parse_value(_pick(header, ["dividend_yield"]) or _pick(stock_banner, ["dividend_yield"]))
    )
    high_52w = _field(
        _parse_value(_pick(header, ["high_52w"]) or _pick(stock_banner, ["high_52w"]))
    )
    low_52w = _field(
        _parse_value(_pick(header, ["low_52w"]) or _pick(stock_banner, ["low_52w"]))
    )
    earnings_date = _field(
        _pick(header, ["earnings_date"]) or _pick(stock_banner, ["earnings_date"])
    )

    analyst_rating = _field(_pick(header, ["ubs_rating", "ubs_grp_rating", "ubs_grp_rating"]))
    analyst_target = _field(
        _parse_value(_pick(header, ["ubs_grp_target", "target", "ubs_target"]))
    )
    # CIO Rating: user-input field, not from Bloomberg. Dashboard input TBD.
    analyst_cio = _field(_pick(header, ["cio_rating", "ubs_cio_rating"]))

    shares_value = _parse_shares_value(
        _pick(header, ["shares"]) or _pick(stock_banner, ["shares"])
    )
    avg_cost_value = _parse_number(
        _pick(header, ["avg_cost"]) or _pick(stock_banner, ["avg_cost"])
    )
    spot_number = _parse_number(spot_value)

    has_client_position = bool(
        shares_value is not None and abs(shares_value) > 0
    )
    market_value = None
    pnl_dollar = None
    pnl_percent = None
    if has_client_position and avg_cost_value is not None and spot_number is not None:
        market_value = shares_value * spot_number
        cost_value = shares_value * avg_cost_value
        pnl_dollar = market_value - cost_value
        if cost_value:
            pnl_percent = (pnl_dollar / cost_value) * 100.0

    if has_client_position:
        client_position = {
            "shares": _field(shares_value),
            "avg_cost": _field(avg_cost_value),
            "market_value": _field(market_value),
            "pnl_dollar": _field(pnl_dollar),
            "pnl_percent": _field(pnl_percent),
        }
    else:
        client_position = {
            "shares": _field(None, status="not_applicable"),
            "avg_cost": _field(None, status="not_applicable"),
            "market_value": _field(None, status="not_applicable"),
            "pnl_dollar": _field(None, status="not_applicable"),
            "pnl_percent": _field(None, status="not_applicable"),
        }

    strategy_name = _field(_pick(header, ["strategy_name"]))
    strategy_description = _field(_extract_strategy_description(legacy))

    legs: List[Dict[str, object]] = []
    for leg in _as_list(structure.get("legs")):
        side_text = leg.get("side")
        action = _normalize_side(side_text)
        leg_type = _normalize_type(leg.get("type") or leg.get("kind") or side_text)
        quantity_value = _parse_number(leg.get("qty") or leg.get("quantity")) or 1.0
        strike_value = _parse_value(leg.get("strike"))
        premium_value = _parse_number(leg.get("premium"))
        price_value = abs(premium_value) if premium_value is not None else None
        legs.append(
            {
                "action": _field(action),
                "type": _field(leg_type),
                "quantity": _field(quantity_value),
                "expiry": _field(leg.get("Expiry") or leg.get("expiry")),
                "strike": _field(_parse_value(strike_value)),
                "price": _field(price_value),
                "delta": _field(_parse_value(leg.get("delta"))),
                "otm_percent": _field(_parse_value(leg.get("otm_percent") or leg.get("otm_pct"))),
                "premium": _field(_parse_value(leg.get("premium"))),
            }
        )

    metrics: Dict[str, Dict[str, object]] = {
        "max_profit": _field(None),
        "max_loss": _field(None),
        "reward_risk": _field(None),
        "max_roi": _field(None),
        "min_roi": _field(None),
        "capital_basis": _field(None),
        "net_cost": _field(None),
        "net_premium_total": _field(_parse_value(structure.get("net_premium_total"))),
        "net_premium_per_share": _field(_parse_value(structure.get("net_premium_per_share"))),
        "yield_percent": _field(None),
        "max_profit_options": _field(None),
        "max_loss_options": _field(None),
        "reward_risk_options": _field(None),
        "max_roi_options": _field(None),
        "min_roi_options": _field(None),
        "capital_basis_options": _field(None),
        "net_cost_options": _field(None),
    }

    label_map = {
        "maxprofit": "max_profit",
        "maxloss": "max_loss",
        "rewardrisk": "reward_risk",
        "maxroi": "max_roi",
        "minroi": "min_roi",
        "capitalbasis": "capital_basis",
        "costcredit": "net_cost",
        "netpremshare": "net_premium_per_share",
        "netprem%spot": "yield_percent",
        "netpremspot": "yield_percent",
        "netprempercentspot": "yield_percent",
        "netprempercent": "yield_percent",
    }

    options_keys = {
        "max_profit", "max_loss", "reward_risk", "max_roi", "min_roi",
        "capital_basis", "net_cost",
    }

    for row in metrics_rows:
        label = row.get("metric")
        if not isinstance(label, str):
            continue
        normalized = re.sub(r"[^a-z0-9]", "", label.lower())
        target_key = label_map.get(normalized)
        if not target_key:
            continue
        raw_value = row.get("combined")
        if _is_missing(raw_value):
            raw_value = row.get("options")
        parsed = _parse_value(raw_value)
        metrics[target_key] = _field(parsed)
        if target_key in options_keys:
            options_raw = row.get("options")
            metrics[f"{target_key}_options"] = _field(_parse_value(options_raw))

    scenarios: List[Dict[str, object]] = []
    for card in _as_list(legacy.get("scenario_analysis_cards")):
        label = card.get("title")
        narrative = card.get("body") or card.get("description")
        scenarios.append(
            {
                "label": _field(label),
                "narrative": _field(narrative),
                "underlying_price": _field(None),
                "move_pct": _field(None),
                "stock_pnl": _field(None),
                "option_pnl": _field(None),
                "option_roi": _field(None),
                "net_pnl": _field(None),
                "net_roi": _field(None),
            }
        )

    key_level_rows: List[Dict[str, object]] = []
    for row in _scenario_rows_from_legacy(legacy):
        label = _pick(row, ["Scenario", "scenario", "label"])
        price = _pick(row, ["Price", "price"])
        move_pct = _pick(row, ["Move %", "move_pct", "movePercent", "move_percent"])
        stock_pnl = _pick(row, ["Stock PnL", "stock_pnl", "stockPnL"])
        option_pnl = _pick(row, ["Option PnL", "option_pnl", "optionPnL"])
        option_roi = _pick(row, ["Option ROI", "option_roi", "optionROI"])
        net_pnl = _pick(row, ["Net PnL", "net_pnl", "netPnL"])
        net_roi = _pick(row, ["Net ROI", "net_roi", "netROI"])
        key_level_rows.append(
            {
                "label": _field(label),
                "underlying_price": _field(_parse_value(price)),
                "move_pct": _field(_parse_value(move_pct)),
                "stock_pnl": _field(_parse_value(stock_pnl)),
                "option_pnl": _field(_parse_value(option_pnl)),
                "option_roi": _field(_parse_value(option_roi)),
                "net_pnl": _field(_parse_value(net_pnl)),
                "net_roi": _field(_parse_value(net_roi)),
            }
        )

    disclosure_text = (
        _join_disclosures(legacy.get("disclosures_text"))
        or _join_disclosures(legacy.get("disclosures"))
        or _join_disclosures(legacy.get("disclaimers"))
    )

    sections = {
        "client_position": {
            "visible": has_client_position,
            "reason": "has_underlying_position" if has_client_position else "no_underlying_position",
        },
        "analyst_view": {"visible": True, "reason": "default"},
        "key_data": {"visible": True, "reason": "default"},
        "scenario_analysis": {
            "visible": bool(has_scenario_data and scenarios),
            "reason": "computed" if has_scenario_data and scenarios else "not_computed",
        },
        "key_levels": {
            "visible": bool(key_level_rows),
            "reason": "computed" if key_level_rows else "not_computed",
        },
        "disclosures": {"visible": True, "reason": "default"},
    }

    layout = {
        "top_banner_mode": "client_and_analyst" if has_client_position else "analyst_only",
        "center_key_data": not has_client_position,
    }

    contract = {
        "meta": {"report_version": "v1"},
        "analysis_status": {
            "computed": bool(has_scenario_data),
            "as_of": as_of,
        },
        "layout": layout,
        "sections": sections,
        "underlying": {
            "ticker": ticker,
            "name": name,
            "sector": sector,
            "spot": spot,
            "move_pct": _field(move_pct_value),
            "dividend_yield": dividend_yield,
            "high_52w": high_52w,
            "low_52w": low_52w,
            "earnings_date": earnings_date,
        },
        "analyst": {
            "ubs_rating": analyst_rating,
            "price_target": analyst_target,
            "cio_view": analyst_cio,
        },
        "client_position": client_position,
        "strategy": {"name": strategy_name, "description": strategy_description},
        "legs": legs,
        "metrics": metrics,
        "scenarios": scenarios,
        "key_levels": {"rows": key_level_rows},
        "disclosures": {"text": _field(disclosure_text)},
    }

    return contract
