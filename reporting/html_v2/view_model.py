from __future__ import annotations

import base64
import math
from datetime import datetime
from typing import Any, Dict, Iterable, List, Mapping, Optional

MISSING = "—"
DEFAULT_DISCLOSURE = (
    "Options involve risk and are not suitable for all investors. Please ensure that you have read and "
    "understood the current Options Disclosure Document titled \"Characteristics and Risks of Standardized Options\". "
    "This report is for simulation purposes only. Past performance is not a guarantee of future results. "
    "The analysis assumes the options are held to expiration, although they may be closed out earlier. "
    "UBS Financial Services Inc. does not provide tax or legal advice. Please consult with your tax and legal advisors "
    "regarding your personal circumstances."
)


def _to_text(value: object, fallback: str = MISSING) -> str:
    if value is None:
        return fallback
    if isinstance(value, str):
        text = value.strip()
        if text in ("", "--", MISSING):
            return fallback
        return text
    return str(value)


def _to_number(value: object) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        if isinstance(value, float) and not (value == value):
            return None
        return float(value)
    if isinstance(value, str):
        text = value.strip()
        if not text or text in (MISSING, "--"):
            return None
        negative = text.startswith("(") and text.endswith(")")
        cleaned = text.replace("(", "").replace(")", "")
        cleaned = (
            cleaned.replace("$", "")
            .replace(",", "")
            .replace("%", "")
            .replace(" ", "")
        )
        try:
            parsed = float(cleaned)
        except ValueError:
            return None
        return -parsed if negative else parsed
    return None


def _to_number_or_text(value: object) -> object:
    number = _to_number(value)
    if number is None:
        return _to_text(value)
    return number


def _to_percent_ratio(value: object) -> object:
    if isinstance(value, str) and "%" in value:
        parsed = _to_number(value)
        if parsed is not None:
            return parsed / 100.0
    if isinstance(value, (int, float)):
        return value
    return value if value is not None else MISSING


def _format_date(value: object) -> str:
    if value is None:
        return MISSING
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d")
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return MISSING
        return text
    return str(value)


def _format_long_date(value: object) -> str:
    """Format date as 'February 7, 2026'. Falls back to raw string."""
    if value is None:
        return MISSING
    if isinstance(value, datetime):
        return f"{value.strftime('%B')} {value.day}, {value.strftime('%Y')}"
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return MISSING
        # Strip trailing Z, then try ISO formats
        clean = text.replace("Z", "").replace("z", "")
        for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
            try:
                dt = datetime.strptime(clean, fmt)
                return f"{dt.strftime('%B')} {dt.day}, {dt.strftime('%Y')}"
            except ValueError:
                continue
        # Try date-only from first 10 chars
        try:
            dt = datetime.strptime(text[:10], "%Y-%m-%d")
            return f"{dt.strftime('%B')} {dt.day}, {dt.strftime('%Y')}"
        except ValueError:
            pass
        return text
    return str(value)


def _format_currency(value: object, decimals: int = 2) -> str:
    if value is None:
        return MISSING
    if isinstance(value, str):
        text = value.strip()
        if not text or text in (MISSING, "--"):
            return MISSING
        number = _to_number(text)
        if number is None:
            return text
        value = number
    if isinstance(value, (int, float)):
        return f"${value:,.{decimals}f}"
    return str(value)


def _format_number(value: object, decimals: int = 2) -> str:
    number = _to_number(value)
    if number is None:
        return _to_text(value)
    return f"{number:.{decimals}f}"


def _format_percent(value: object, decimals: int = 2) -> str:
    if isinstance(value, str) and "%" in value:
        return value
    number = _to_number(value)
    if number is None:
        return _to_text(value)
    return f"{number:.{decimals}f}%"


def _value_class(value: object) -> str:
    if isinstance(value, (int, float)):
        if value < 0:
            return "value-negative"
        if value > 0:
            return "value-positive"
        return "value-neutral"
    if isinstance(value, str):
        if "-" in value and value not in ("---", MISSING, "--"):
            return "value-negative"
    return "value-neutral"


def _normalize_side(raw: str) -> Dict[str, str]:
    text = raw.lower()
    type_val = "Put" if "put" in text else "Call" if "call" in text else ""
    action = "Sell" if "short" in text or "sell" in text else "Buy"
    return {"action": action, "type": type_val}


def _pick(obj: Mapping[str, object], keys: Iterable[str]) -> object:
    for key in keys:
        if key in obj:
            return obj.get(key)
    return None


def _build_metrics(rows: List[Mapping[str, object]]) -> Dict[str, Dict[str, object]]:
    by_metric: Dict[str, Mapping[str, object]] = {}
    for row in rows:
        label = row.get("metric")
        if isinstance(label, str):
            by_metric[label] = row

    def metric_value(label: str, field: str) -> object:
        row = by_metric.get(label)
        if not row:
            return MISSING
        if "ROI" in label or "Prem %" in label:
            return _to_percent_ratio(row.get(field))
        return _to_number_or_text(row.get(field))

    return {
        "max_profit": {
            "label": "Max Profit",
            "combined": metric_value("Max Profit", "combined"),
            "options": metric_value("Max Profit", "options"),
        },
        "max_loss": {
            "label": "Max Loss",
            "combined": metric_value("Max Loss", "combined"),
            "options": metric_value("Max Loss", "options"),
        },
        "reward_risk": {
            "label": "R/R Ratio",
            "combined": metric_value("Reward/Risk", "combined"),
            "options": metric_value("Reward/Risk", "options"),
        },
        "max_roi": {
            "label": "Max ROI",
            "combined": metric_value("Max ROI", "combined"),
            "options": metric_value("Max ROI", "options"),
        },
        "min_roi": {
            "label": "Min ROI",
            "combined": metric_value("Min ROI", "combined"),
            "options": metric_value("Min ROI", "options"),
        },
        "capital_basis": {
            "label": "Capital Basis",
            "combined": metric_value("Capital Basis", "combined"),
            "options": metric_value("Capital Basis", "options"),
        },
        "cost_credit": {
            "label": "Net Cost",
            "combined": metric_value("Cost/Credit", "combined"),
            "options": metric_value("Cost/Credit", "options"),
        },
        "net_prem_per_share": {
            "label": "Net Prem/Share",
            "combined": metric_value("Net Prem/Share", "combined"),
            "options": metric_value("Net Prem/Share", "options"),
        },
        "net_prem_percent": {
            "label": "Yield %",
            "combined": metric_value("Net Prem % Spot", "combined"),
            "options": metric_value("Net Prem % Spot", "options"),
        },
    }


def _metric_display(value: object, is_percent: bool) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float)):
        if is_percent:
            return f"{value * 100:.2f}%"
        return _format_currency(value, decimals=0)
    return _to_text(value)


def _build_metric_view(metrics: Dict[str, Dict[str, object]]) -> Dict[str, Dict[str, str]]:
    percent_keys = {"max_roi", "min_roi", "net_prem_percent"}
    view: Dict[str, Dict[str, str]] = {}
    for key, metric in metrics.items():
        is_percent = key in percent_keys
        combined = metric.get("combined")
        options = metric.get("options")
        view[key] = {
            "label": metric.get("label", ""),
            "display": _metric_display(combined, is_percent),
            "class": _value_class(combined),
            "sub_display": _metric_display(options, is_percent),
        }
    return view


def _build_key_levels(rows: List[Mapping[str, object]]) -> List[Dict[str, str]]:
    display_rows: List[Dict[str, str]] = []
    for row in rows:
        scenario = _to_text(_pick(row, ["Scenario", "scenario"]))
        price_val = _pick(row, ["Price", "price"])
        move_val = _pick(row, ["Move %", "move_pct", "movePercent"])
        stock_val = _pick(row, ["Stock PnL", "stock_pnl", "stockPnL"])
        option_val = _pick(row, ["Option PnL", "option_pnl", "optionPnL"])
        option_roi_val = _pick(row, ["Option ROI", "option_roi", "optionROI"])
        net_val = _pick(row, ["Net PnL", "net_pnl", "netPnL"])
        net_roi_val = _pick(row, ["Net ROI", "net_roi", "netROI"])

        price = _format_currency(price_val, decimals=2)
        move_percent = _format_percent(move_val, decimals=2)
        stock_pnl = _format_currency(stock_val, decimals=2)
        option_pnl = _format_currency(option_val, decimals=2)
        option_roi = _format_percent(option_roi_val, decimals=2)
        net_pnl = _format_currency(net_val, decimals=2)
        net_roi = _format_percent(net_roi_val, decimals=2)

        display_rows.append(
            {
                "scenario": scenario,
                "price": price,
                "move_percent": move_percent,
                "move_class": _value_class(move_val),
                "stock_pnl": stock_pnl,
                "stock_class": _value_class(stock_val),
                "option_pnl": option_pnl,
                "option_class": _value_class(option_val),
                "option_roi": option_roi,
                "option_roi_class": _value_class(option_roi_val),
                "net_pnl": net_pnl,
                "net_pnl_class": _value_class(net_val),
                "net_roi": net_roi,
                "net_roi_class": _value_class(net_roi_val),
                "row_class": "bg-yellow-50" if scenario == "Current Market Price" else "",
            }
        )
    if not display_rows:
        display_rows.append(
            {
                "scenario": MISSING,
                "price": MISSING,
                "move_percent": MISSING,
                "move_class": "text-gray-900",
                "stock_pnl": MISSING,
                "stock_class": "text-gray-900",
                "option_pnl": MISSING,
                "option_class": "text-gray-900",
                "option_roi": MISSING,
                "option_roi_class": "text-gray-900",
                "net_pnl": MISSING,
                "net_pnl_class": "text-gray-900",
                "net_roi": MISSING,
                "net_roi_class": "text-gray-900",
                "row_class": "",
            }
        )
    return display_rows


def _build_scenarios(cards: List[Mapping[str, object]]) -> List[Dict[str, str]]:
    scenarios: List[Dict[str, str]] = []
    for card in cards:
        title = _to_text(card.get("title"))
        type_text = title.lower()
        if "bear" in type_text:
            dot_class = "dot-red"
        elif "bull" in type_text:
            dot_class = "dot-green"
        else:
            dot_class = "dot-gray"
        scenarios.append(
            {
                "title": title,
                "condition": _to_text(card.get("condition")),
                "description": _to_text(card.get("body") or card.get("description")),
                "dot_class": dot_class,
            }
        )
    labels = [
        ("Bearish", "dot-red"),
        ("Stagnant", "dot-gray"),
        ("Bullish", "dot-green"),
    ]
    while len(scenarios) < 3:
        label, dot_class = labels[len(scenarios)]
        scenarios.append({"title": label, "condition": MISSING, "description": MISSING, "dot_class": dot_class})
    return scenarios[:3]


def _join_disclosures(value: object) -> str:
    if isinstance(value, list):
        cleaned = [str(item).strip() for item in value if str(item).strip()]
        cleaned = [item for item in cleaned if item != MISSING]
        return " ".join(cleaned) if cleaned else DEFAULT_DISCLOSURE
    if isinstance(value, str):
        text = value.strip()
        return text if text else DEFAULT_DISCLOSURE
    text = _to_text(value)
    return text if text != MISSING else DEFAULT_DISCLOSURE


def _strategy_description(contract: Mapping[str, object]) -> str:
    direct = _to_text(contract.get("strategy_description") or "")
    if direct != MISSING:
        return direct
    commentary = contract.get("commentary_blocks")
    if isinstance(commentary, Mapping):
        blocks = commentary.get("blocks")
        if isinstance(blocks, list) and blocks:
            first = blocks[0]
            if isinstance(first, Mapping):
                return _to_text(first.get("text") or "")
    if isinstance(commentary, list) and commentary:
        first = commentary[0]
        if isinstance(first, Mapping):
            return _to_text(first.get("text") or "")
    return MISSING


def _looks_like_template_data(data: Mapping[str, object]) -> bool:
    return "strategyName" in data or "stockDetails" in data


def _from_template_data(data: Mapping[str, object]) -> Dict[str, object]:
    return {
        "header": {
            "title": _to_text(data.get("strategyName")),
            "subtitle": _to_text(data.get("subtitle") or "Wealth Management Option Strategy"),
            "date": _to_text(data.get("date")),
            "disclaimer": DEFAULT_DISCLOSURE,
        },
        "stock_details": {
            "ticker": _to_text(data.get("stockDetails", {}).get("ticker") if isinstance(data.get("stockDetails"), Mapping) else None),
            "name": _to_text(data.get("stockDetails", {}).get("name") if isinstance(data.get("stockDetails"), Mapping) else None),
            "sector": _to_text(data.get("stockDetails", {}).get("sector") if isinstance(data.get("stockDetails"), Mapping) else None),
            "ubs_rating": _to_text(data.get("stockDetails", {}).get("ubsGrpRating") if isinstance(data.get("stockDetails"), Mapping) else None),
            "ubs_target": _to_text(data.get("stockDetails", {}).get("ubsGrpTarget") if isinstance(data.get("stockDetails"), Mapping) else None),
            "cio_rating": _to_text(data.get("stockDetails", {}).get("ubsCioRating") if isinstance(data.get("stockDetails"), Mapping) else None),
            "last_price": _to_text(data.get("stockDetails", {}).get("lastPrice") if isinstance(data.get("stockDetails"), Mapping) else None),
            "ten_day_change": _to_text(data.get("stockDetails", {}).get("tenDayChange") if isinstance(data.get("stockDetails"), Mapping) else None),
            "change_class": "value-neutral",
            "change_symbol": "",
            "fifty_two_week_high": _to_text(data.get("stockDetails", {}).get("fiftyTwoWeekHigh") if isinstance(data.get("stockDetails"), Mapping) else None),
            "fifty_two_week_low": _to_text(data.get("stockDetails", {}).get("fiftyTwoWeekLow") if isinstance(data.get("stockDetails"), Mapping) else None),
            "dividend_yield": _to_text(data.get("stockDetails", {}).get("dividendYield") if isinstance(data.get("stockDetails"), Mapping) else None),
            "earnings_date": _to_text(data.get("stockDetails", {}).get("earningsDate") if isinstance(data.get("stockDetails"), Mapping) else None),
        },
        "client_position": data.get("clientPosition") if isinstance(data.get("clientPosition"), Mapping) else None,
        "strategy_description": _to_text(data.get("strategyDescription") or ""),
        "option_legs_title": _to_text(data.get("optionLegsTitle") or ""),
        "option_legs": data.get("optionLegs") if isinstance(data.get("optionLegs"), list) else [],
        "net_premium": {"display": _to_text(data.get("netPremium")), "class": "text-gray-900"},
        "metrics": {},
        "key_levels": data.get("keyLevels") if isinstance(data.get("keyLevels"), list) else [],
        "scenario_analysis": data.get("scenarioAnalysis") if isinstance(data.get("scenarioAnalysis"), list) else [],
        "disclosures": DEFAULT_DISCLOSURE,
        "page": {"total": 2},
    }


def _field_value(field: object) -> Optional[object]:
    if not isinstance(field, Mapping):
        return None
    if field.get("status") != "computed":
        return None
    return field.get("value")


def _field_text(field: object) -> str:
    return _to_text(_field_value(field))


def build_view_model_from_contract(contract: Mapping[str, object]) -> Dict[str, object]:
    data = contract if isinstance(contract, Mapping) else {}
    analysis_status = data.get("analysis_status") if isinstance(data.get("analysis_status"), Mapping) else {}
    sections = data.get("sections") if isinstance(data.get("sections"), Mapping) else {}
    underlying = data.get("underlying") if isinstance(data.get("underlying"), Mapping) else {}
    analyst = data.get("analyst") if isinstance(data.get("analyst"), Mapping) else {}
    client_position = data.get("client_position") if isinstance(data.get("client_position"), Mapping) else {}
    strategy = data.get("strategy") if isinstance(data.get("strategy"), Mapping) else {}
    metrics = data.get("metrics") if isinstance(data.get("metrics"), Mapping) else {}

    has_stock_component = False
    strategy_stock = strategy.get("has_stock_component")
    if isinstance(strategy_stock, Mapping) and strategy_stock.get("status") == "computed":
        has_stock_component = bool(strategy_stock.get("value"))

    sections_client = sections.get("client_position") if isinstance(sections.get("client_position"), Mapping) else {}
    sections_scenario = sections.get("scenario_analysis") if isinstance(sections.get("scenario_analysis"), Mapping) else {}
    sections_key_levels = sections.get("key_levels") if isinstance(sections.get("key_levels"), Mapping) else {}
    sections_disclosures = sections.get("disclosures") if isinstance(sections.get("disclosures"), Mapping) else {}

    client_visible = bool(sections_client.get("visible", True))
    scenario_visible = bool(sections_scenario.get("visible", True))
    key_levels_visible = bool(sections_key_levels.get("visible", True))
    disclosures_visible = bool(sections_disclosures.get("visible", True))

    move_value = _field_value(underlying.get("move_pct"))
    move_text = _format_percent(move_value, decimals=2)
    negative_move = False
    if isinstance(move_value, (int, float)):
        negative_move = move_value < 0
    elif isinstance(move_text, str) and move_text.startswith("-"):
        negative_move = True
    change_class = "value-neutral"
    change_symbol = ""
    if move_text != MISSING:
        change_class = "change-down" if negative_move else "change-up"
        # Don't add symbol if the text already contains the sign
        if negative_move and move_text.startswith("-"):
            change_symbol = ""
        elif negative_move:
            change_symbol = "-"
        else:
            change_symbol = "+"
        move_text = move_text + " YTD"

    header = {
        "title": _field_text(strategy.get("name")),
        "subtitle": "Wealth Management Option Strategy",
        "date": _format_long_date(analysis_status.get("as_of")),
        "disclaimer": (
            "The illustration is intended for informational and internal use. "
            "Although it can be shared with clients approved for trading Options or "
            "have received a copy of the Option Disclosure Document. For specific stock "
            "ratings relative to UBS INV research, CIO research, and/or SPGMI's Quality "
            "ranking, please refer to the research tab on ConsultWorks. Commissions or fees not included."
        ),
    }

    stock_details = {
        "ticker": _field_text(underlying.get("ticker")),
        "name": _field_text(underlying.get("name")),
        "sector": _field_text(underlying.get("sector")),
        "ubs_rating": _field_text(analyst.get("ubs_rating")),
        "ubs_target": _format_currency(_field_value(analyst.get("price_target")), decimals=2),
        "cio_rating": _field_text(analyst.get("cio_view")),
        "last_price": _format_currency(_field_value(underlying.get("spot")), decimals=2),
        "ten_day_change": move_text,
        "change_class": change_class,
        "change_symbol": change_symbol,
        "fifty_two_week_high": _format_currency(_field_value(underlying.get("high_52w")), decimals=0),
        "fifty_two_week_low": _format_currency(_field_value(underlying.get("low_52w")), decimals=0),
        "dividend_yield": _format_percent(_field_value(underlying.get("dividend_yield")), decimals=2),
        "earnings_date": _field_text(underlying.get("earnings_date")),
    }

    if client_visible:
        pnl_dollar = _field_value(client_position.get("pnl_dollar"))
        pnl_class = "value-positive"
        pnl_badge_class = "value-positive"
        if isinstance(pnl_dollar, (int, float)) and pnl_dollar < 0:
            pnl_class = "value-negative"
            pnl_badge_class = "value-negative"
        client_block = {
            "shares": _format_number(_field_value(client_position.get("shares")), decimals=0),
            "avg_cost": _format_currency(_field_value(client_position.get("avg_cost")), decimals=2),
            "mkt_value": _format_currency(_field_value(client_position.get("market_value")), decimals=2),
            "pnl_dollar": _format_currency(pnl_dollar, decimals=2),
            "pnl_percent": _format_number(_field_value(client_position.get("pnl_percent")), decimals=2),
            "pnl_class": pnl_class,
            "pnl_badge_class": pnl_badge_class,
        }
    else:
        client_block = None

    legs: List[Dict[str, object]] = []
    net_premium_accum = 0.0
    for idx, leg in enumerate(data.get("legs", [])):
        if not isinstance(leg, Mapping):
            continue
        price_num = _to_number(_field_value(leg.get("price"))) or 0
        qty_num = _to_number(_field_value(leg.get("quantity"))) or 1
        # Total premium = quantity × per-contract price × 100 shares per contract
        total_premium = qty_num * price_num * 100
        action_text = _field_text(leg.get("action"))
        # Premium color: Buy = debit (red), Sell = credit (green)
        if action_text == "Buy":
            premium_class = "value-negative"
            net_premium_accum -= total_premium
        elif action_text == "Sell":
            premium_class = "value-positive"
            net_premium_accum += total_premium
        else:
            premium_class = _value_class(total_premium)
        legs.append(
            {
                "leg": idx + 1,
                "action": action_text,
                "quantity": _format_number(_field_value(leg.get("quantity")), decimals=0),
                "expiration": _field_text(leg.get("expiry")),
                "strike": _format_currency(_field_value(leg.get("strike")), decimals=2),
                "type": _field_text(leg.get("type")),
                "price": _format_currency(_field_value(leg.get("price")), decimals=2),
                "delta": _format_number(_field_value(leg.get("delta")), decimals=2),
                "otm_percent": _format_percent(_field_value(leg.get("otm_percent")), decimals=2),
                "premium": total_premium,
                "premium_display": _format_currency(total_premium, decimals=2),
                "premium_class": premium_class,
            }
        )
    if not legs:
        legs.append(
            {
                "leg": 1,
                "action": MISSING,
                "quantity": MISSING,
                "expiration": MISSING,
                "strike": MISSING,
                "type": MISSING,
                "price": MISSING,
                "delta": MISSING,
                "otm_percent": MISSING,
                "premium": 0,
                "premium_display": MISSING,
                "premium_class": "value-neutral",
            }
        )

    option_legs_title = (
        f"Option Leg(s) for {_field_text(strategy.get('name'))} on {_field_text(underlying.get('ticker'))}"
    )

    def metric_entry(label: str, field: object, kind: str, options_field: object = None) -> Dict[str, str]:
        # Options value (preferred for main display)
        options_raw = None
        if options_field is not None:
            options_raw = _field_value(options_field)
        if options_raw is None:
            options_raw = _field_value(field)
        # Combined value
        combined_raw = _field_value(field)

        def _fmt(raw: object, kind: str) -> str:
            if kind == "percent":
                return _format_percent(raw, decimals=2)
            elif kind == "ratio":
                return _format_number(raw, decimals=2)
            else:
                return _format_currency(raw, decimals=0)

        return {
            "label": label,
            "display": _fmt(options_raw, kind),
            "class": _value_class(options_raw),
            "combined_display": _fmt(combined_raw, kind),
            "combined_class": _value_class(combined_raw),
            "sub_display": "",
        }

    metric_view = {
        "max_profit": metric_entry("Max Profit", metrics.get("max_profit"), "currency", metrics.get("max_profit_options")),
        "max_loss": metric_entry("Max Loss", metrics.get("max_loss"), "currency", metrics.get("max_loss_options")),
        "reward_risk": metric_entry("R/R Ratio", metrics.get("reward_risk"), "ratio", metrics.get("reward_risk_options")),
        "max_roi": metric_entry("Max ROI", metrics.get("max_roi"), "percent", metrics.get("max_roi_options")),
        "min_roi": metric_entry("Min ROI", metrics.get("min_roi"), "percent", metrics.get("min_roi_options")),
        "capital_basis": metric_entry("Capital Basis", metrics.get("capital_basis"), "currency", metrics.get("capital_basis_options")),
        "cost_credit": metric_entry("Net Cost", metrics.get("net_cost"), "currency", metrics.get("net_cost_options")),
        "net_prem_per_share": metric_entry(
            "Net Prem/Share", metrics.get("net_premium_per_share"), "currency"
        ),
        "net_prem_percent": metric_entry("Yield %", metrics.get("yield_percent"), "percent"),
    }

    # Net premium: use accumulated total from legs (sells positive, buys negative)
    net_premium_display = _format_currency(net_premium_accum, decimals=2)

    key_levels_rows = (
        data.get("key_levels", {}).get("rows")
        if isinstance(data.get("key_levels"), Mapping)
        else []
    )
    key_levels_display: List[Dict[str, str]] = []
    if key_levels_visible:
        for row in key_levels_rows if isinstance(key_levels_rows, list) else []:
            if not isinstance(row, Mapping):
                continue
            label = _field_text(row.get("label"))
            price_val = _field_value(row.get("underlying_price"))
            move_val = _field_value(row.get("move_pct"))
            stock_val = _field_value(row.get("stock_pnl"))
            option_val = _field_value(row.get("option_pnl"))
            option_roi_val = _field_value(row.get("option_roi"))
            net_val = _field_value(row.get("net_pnl"))
            net_roi_val = _field_value(row.get("net_roi"))
            key_levels_display.append(
                {
                    "scenario": label,
                    "price": _format_currency(price_val, decimals=2),
                    "move_percent": _format_percent(move_val, decimals=2),
                    "move_class": _value_class(move_val),
                    "stock_pnl": _format_currency(stock_val, decimals=2),
                    "stock_class": _value_class(stock_val),
                    "option_pnl": _format_currency(option_val, decimals=2),
                    "option_class": _value_class(option_val),
                    "option_roi": _format_percent(option_roi_val, decimals=2),
                    "option_roi_class": _value_class(option_roi_val),
                    "net_pnl": _format_currency(net_val, decimals=2),
                    "net_pnl_class": _value_class(net_val),
                    "net_roi": _format_percent(net_roi_val, decimals=2),
                    "net_roi_class": _value_class(net_roi_val),
                    "row_class": "wm-row-highlight" if label == "Current Market Price" else "",
                }
            )

    scenario_rows = data.get("scenarios") if isinstance(data.get("scenarios"), list) else []
    scenario_display: List[Dict[str, str]] = []
    if scenario_visible:
        for row in scenario_rows:
            if not isinstance(row, Mapping):
                continue
            label = _field_text(row.get("label"))
            narrative = _field_text(row.get("narrative"))
            type_text = label.lower()
            if "bear" in type_text:
                dot_class = "dot-red"
            elif "bull" in type_text:
                dot_class = "dot-green"
            else:
                dot_class = "dot-gray"
            scenario_display.append(
                {
                    "title": label,
                    "condition": "",
                    "description": "" if narrative == MISSING else narrative,
                    "dot_class": dot_class,
                }
            )

    disclosures_text = ""
    disclosures_block = data.get("disclosures") if isinstance(data.get("disclosures"), Mapping) else {}
    if disclosures_visible:
        disclosures_text = _field_text(disclosures_block.get("text"))
        if disclosures_text == MISSING:
            disclosures_text = DEFAULT_DISCLOSURE

    return {
        "header": header,
        "stock_details": stock_details,
        "client_position": client_block,
        "strategy_description": _field_text(strategy.get("description")),
        "option_legs_title": option_legs_title,
        "option_legs": legs,
        "net_premium": {
            "display": net_premium_display,
            "class": _value_class(net_premium_accum),
        },
        "metrics": metric_view,
        "metrics_has_stock_component": has_stock_component,
        "key_levels": key_levels_display,
        "scenario_analysis": scenario_display,
        "disclosures": disclosures_text,
        "sections": sections,
        "page": {"total": 2},
    }


# ---------------------------------------------------------------------------
# SVG payoff chart builder with strike / breakeven annotations
# ---------------------------------------------------------------------------

_SVG_WIDTH = 700.0
_SVG_HEIGHT = 350.0
_SVG_PAD_LEFT = 60.0
_SVG_PAD_RIGHT = 30.0
_SVG_PAD_TOP = 30.0
_SVG_PAD_BOTTOM = 40.0
_STRIKE_COLOR = "#E5E7EB"
_BREAKEVEN_COLOR = "#9CA3AF"
_LABEL_FONT_SIZE = 10


def _coerce_svg_float(value: object) -> Optional[float]:
    """Coerce a scalar to float, returning None on failure."""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        f = float(value)
        return f if f == f else None  # NaN check
    if isinstance(value, str):
        text = value.strip().replace(",", "").replace("%", "")
        if not text:
            return None
        try:
            return float(text)
        except ValueError:
            return None
    return None


def _coerce_svg_series(values: object) -> Optional[List[float]]:
    """Coerce a list of values to a list of floats."""
    if not isinstance(values, list) or not values:
        return None
    series: List[float] = []
    for v in values:
        num = _coerce_svg_float(v)
        if num is None:
            return None
        series.append(num)
    return series


def _svg_placeholder() -> str:
    cx = _SVG_WIDTH / 2
    cy = _SVG_HEIGHT / 2
    return (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {int(_SVG_WIDTH)} {int(_SVG_HEIGHT)}'>"
        "<rect width='100%' height='100%' fill='white'/>"
        f"<line x1='{_SVG_PAD_LEFT:.0f}' y1='{_SVG_PAD_TOP:.0f}' "
        f"x2='{_SVG_PAD_LEFT:.0f}' y2='{_SVG_HEIGHT - _SVG_PAD_BOTTOM:.0f}' stroke='#e5e7eb' stroke-width='1'/>"
        f"<line x1='{_SVG_PAD_LEFT:.0f}' y1='{_SVG_HEIGHT - _SVG_PAD_BOTTOM:.0f}' "
        f"x2='{_SVG_WIDTH - _SVG_PAD_RIGHT:.0f}' y2='{_SVG_HEIGHT - _SVG_PAD_BOTTOM:.0f}' stroke='#e5e7eb' stroke-width='1'/>"
        f"<text x='{cx:.0f}' y='{cy:.0f}' text-anchor='middle' fill='#6b7280' font-size='12'>Payoff Diagram</text>"
        "</svg>"
    )


def _xml_escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("'", "&apos;")


def _nice_ticks(lo: float, hi: float, target_count: int = 5) -> List[float]:
    """Generate round-number tick values between lo and hi."""
    span = hi - lo
    if span <= 0:
        return [lo]
    raw_step = span / target_count
    magnitude = 10 ** int(math.floor(math.log10(raw_step)))
    residual = raw_step / magnitude
    if residual <= 1.5:
        nice_step = 1 * magnitude
    elif residual <= 3.5:
        nice_step = 2.5 * magnitude
    elif residual <= 7.5:
        nice_step = 5 * magnitude
    else:
        nice_step = 10 * magnitude
    first = math.ceil(lo / nice_step) * nice_step
    ticks: List[float] = []
    v = first
    while v <= hi:
        ticks.append(v)
        v += nice_step
    return ticks


def build_payoff_svg_data_uri(model: Mapping[str, object]) -> str:
    """DEPRECATED — use build_payoff_chart_png_data_uri() instead.

    Build a complete payoff SVG as a data URI, with strike and breakeven annotations.

    This reads the ``payoff`` block from the raw report model (pre-contract),
    which contains ``price_grid``, ``stock_pnl``, ``options_pnl``, ``combined_pnl``,
    ``strikes`` and ``breakevens``.
    """
    payoff = model.get("payoff") if isinstance(model.get("payoff"), Mapping) else None
    x_values = _coerce_svg_series(payoff.get("price_grid")) if payoff else None
    stock_values = _coerce_svg_series(payoff.get("stock_pnl")) if payoff else None
    options_values = _coerce_svg_series(payoff.get("options_pnl")) if payoff else None
    combined_values = _coerce_svg_series(payoff.get("combined_pnl")) if payoff else None

    if not (x_values and stock_values and options_values and combined_values):
        svg = _svg_placeholder()
        data = base64.b64encode(svg.encode("utf-8")).decode("ascii")
        return f"data:image/svg+xml;base64,{data}"

    # Extract strikes and breakevens
    raw_strikes = payoff.get("strikes") if payoff else None
    raw_breakevens = payoff.get("breakevens") if payoff else None
    strikes: List[float] = []
    breakevens: List[float] = []
    if isinstance(raw_strikes, list):
        for s in raw_strikes:
            v = _coerce_svg_float(s)
            if v is not None:
                strikes.append(v)
    if isinstance(raw_breakevens, list):
        for b in raw_breakevens:
            v = _coerce_svg_float(b)
            if v is not None:
                breakevens.append(v)
    # Limit to spec max
    strikes = sorted(strikes)[:6]
    breakevens = sorted(breakevens)[:4]

    min_len = min(len(x_values), len(stock_values), len(options_values), len(combined_values))
    x = x_values[:min_len]
    stock = stock_values[:min_len]
    options = options_values[:min_len]
    combined = combined_values[:min_len]

    # Determine spot price — find where stock_pnl crosses zero
    spot_price = x[len(x) // 2] if x else 100.0
    # First try exact match
    for i, sp in enumerate(stock):
        if abs(sp) < 0.01:
            spot_price = x[i]
            break
    else:
        # Zero-crossing interpolation: find where stock_pnl changes sign
        for i in range(len(stock) - 1):
            if stock[i] <= 0 <= stock[i + 1] or stock[i] >= 0 >= stock[i + 1]:
                denom = stock[i + 1] - stock[i]
                if abs(denom) > 1e-10:
                    t = -stock[i] / denom
                    spot_price = x[i] + t * (x[i + 1] - x[i])
                else:
                    spot_price = x[i]
                break

    # Use ±30% around spot for x range, then expand for strikes/breakevens
    min_x = spot_price * 0.70
    max_x = spot_price * 1.30
    for pt in strikes + breakevens:
        if pt < min_x:
            min_x = pt - (spot_price * 0.05)
        if pt > max_x:
            max_x = pt + (spot_price * 0.05)

    min_y = min(min(stock), min(options), min(combined), 0.0)
    max_y = max(max(stock), max(options), max(combined), 0.0)
    if min_y == max_y:
        min_y -= 1.0
        max_y += 1.0

    width = _SVG_WIDTH
    height = _SVG_HEIGHT
    pad_left = _SVG_PAD_LEFT
    pad_right = _SVG_PAD_RIGHT
    pad_top = _SVG_PAD_TOP
    pad_bottom = _SVG_PAD_BOTTOM
    plot_w = width - pad_left - pad_right
    plot_h = height - pad_top - pad_bottom

    def sx(value: float) -> float:
        return pad_left + (value - min_x) / (max_x - min_x) * plot_w

    def sy(value: float) -> float:
        return pad_top + (max_y - value) / (max_y - min_y) * plot_h

    def polyline(points: List[tuple], stroke: str, width: float = 1.8, dash: Optional[str] = None) -> str:
        pts = " ".join(f"{sx(px):.2f},{sy(py):.2f}" for px, py in points)
        dash_attr = f" stroke-dasharray='{dash}'" if dash else ""
        return (
            f"<polyline points='{pts}' fill='none' stroke='{stroke}' stroke-width='{width}'{dash_attr} />"
        )

    # Zero axis (dashed, more visible)
    axis_y = sy(0.0)
    axis_y = max(pad_top, min(axis_y, pad_top + plot_h))
    axis_line = (
        f"<line x1='{pad_left:.2f}' y1='{axis_y:.2f}' x2='{pad_left + plot_w:.2f}' "
        f"y2='{axis_y:.2f}' stroke='#9CA3AF' stroke-width='1' stroke-dasharray='6,4' />"
    )
    # Left y-axis line
    axis_x = (
        f"<line x1='{pad_left:.2f}' y1='{pad_top:.2f}' x2='{pad_left:.2f}' "
        f"y2='{pad_top + plot_h:.2f}' stroke='#e5e7eb' stroke-width='1' />"
    )
    # Bottom x-axis line
    x_axis_line = (
        f"<line x1='{pad_left:.2f}' y1='{pad_top + plot_h:.2f}' "
        f"x2='{pad_left + plot_w:.2f}' y2='{pad_top + plot_h:.2f}' stroke='#D1D5DB' stroke-width='1' />"
    )

    def _fmt_currency(v: float) -> str:
        if abs(v) >= 1_000_000:
            return f"${v / 1_000_000:,.1f}M"
        if abs(v) >= 1_000:
            return f"${v / 1_000:,.1f}K"
        return f"${v:,.0f}"

    # Y-axis ticks (replaces old hardcoded grid lines and min/max labels)
    y_ticks = _nice_ticks(min_y, max_y, target_count=5)
    y_tick_parts: List[str] = []
    for tick_val in y_ticks:
        ty = sy(tick_val)
        if ty < pad_top or ty > pad_top + plot_h:
            continue
        # Horizontal grid line (light)
        y_tick_parts.append(
            f"<line x1='{pad_left:.2f}' y1='{ty:.2f}' x2='{pad_left + plot_w:.2f}' "
            f"y2='{ty:.2f}' stroke='#E5E7EB' stroke-width='0.5' />"
        )
        # Tick mark
        y_tick_parts.append(
            f"<line x1='{pad_left - 4:.2f}' y1='{ty:.2f}' x2='{pad_left:.2f}' "
            f"y2='{ty:.2f}' stroke='#9CA3AF' stroke-width='1' />"
        )
        # Label
        y_tick_parts.append(
            f"<text x='{pad_left - 6:.2f}' y='{ty + 3:.2f}' text-anchor='end' "
            f"fill='#9CA3AF' font-size='9' font-family='Arial,Helvetica,sans-serif'>"
            f"{_xml_escape(_fmt_currency(tick_val))}</text>"
        )

    # X-axis ticks (stock price labels along the bottom)
    x_ticks = _nice_ticks(min_x, max_x, target_count=6)
    x_tick_parts: List[str] = []
    for tick_val in x_ticks:
        tx = sx(tick_val)
        # Short tick mark
        x_tick_parts.append(
            f"<line x1='{tx:.2f}' y1='{pad_top + plot_h:.2f}' x2='{tx:.2f}' "
            f"y2='{pad_top + plot_h + 4:.2f}' stroke='#9CA3AF' stroke-width='1' />"
        )
        # Label
        x_tick_parts.append(
            f"<text x='{tx:.2f}' y='{pad_top + plot_h + 14:.2f}' text-anchor='middle' "
            f"fill='#9CA3AF' font-size='9' font-family='Arial,Helvetica,sans-serif'>"
            f"${tick_val:,.0f}</text>"
        )

    # Collect all strike/breakeven labels with dollar values, sort by x, stagger when close
    all_labels: List[tuple] = []  # (x_pixel, label_text, color, price)
    for idx, strike_price in enumerate(strikes):
        lx = sx(strike_price)
        if lx < pad_left or lx > pad_left + plot_w:
            continue
        all_labels.append((lx, f"K{idx + 1} ${strike_price:,.0f}", "#6b7280", strike_price))
    for idx, be_price in enumerate(breakevens):
        lx = sx(be_price)
        if lx < pad_left or lx > pad_left + plot_w:
            continue
        all_labels.append((lx, f"BE{idx + 1} ${be_price:,.0f}", _BREAKEVEN_COLOR, be_price))
    all_labels.sort(key=lambda t: t[0])

    # Assign staggered y positions
    stagger_levels = [pad_top + 4, pad_top + 16, pad_top + 28]
    annotation_parts: List[str] = []
    prev_x = -999.0
    prev_level = -1
    for lx, label, color, _price in all_labels:
        # Determine vertical line color
        line_color = _STRIKE_COLOR if label.startswith("K") else _BREAKEVEN_COLOR
        annotation_parts.append(
            f"<line x1='{lx:.2f}' y1='{pad_top:.2f}' x2='{lx:.2f}' "
            f"y2='{pad_top + plot_h:.2f}' stroke='{line_color}' "
            f"stroke-width='1' stroke-dasharray='4,3' />"
        )
        # Stagger: if within 60px of previous label, bump level
        if lx - prev_x < 60:
            level = (prev_level + 1) % len(stagger_levels)
        else:
            level = 0
        ly = stagger_levels[level]
        prev_x = lx
        prev_level = level
        # Background rect for readability (width based on label length)
        text_width = len(label) * 5.5
        annotation_parts.append(
            f"<rect x='{lx - text_width / 2:.2f}' y='{ly - 9:.2f}' width='{text_width:.0f}' height='12' "
            f"fill='white' fill-opacity='0.9' rx='2'/>"
        )
        annotation_parts.append(
            f"<text x='{lx:.2f}' y='{ly:.2f}' text-anchor='middle' "
            f"fill='{color}' font-size='{_LABEL_FONT_SIZE}' "
            f"font-family='Arial,Helvetica,sans-serif'>{_xml_escape(label)}</text>"
        )

    svg_parts = [
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {width:.0f} {height:.0f}' width='100%' height='100%' preserveAspectRatio='xMidYMid meet'>",
        "<rect width='100%' height='100%' fill='white'/>",
        axis_x,
        x_axis_line,
        *y_tick_parts,
        axis_line,
        *x_tick_parts,
        *annotation_parts,
        polyline(list(zip(x, stock)), "#93c5fd", width=2.0),
        polyline(list(zip(x, options)), "#c4b5fd", width=2.0),
        polyline(list(zip(x, combined)), "#4b5563", width=2.5, dash="4,3"),
        "</svg>",
    ]
    svg = "".join(svg_parts)
    encoded = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    return f"data:image/svg+xml;base64,{encoded}"


# ---------------------------------------------------------------------------
# Matplotlib payoff chart builder (replaces SVG)
# ---------------------------------------------------------------------------


def _find_spot_price(x: List[float], stock: List[float]) -> float:
    """Find the spot price where stock_pnl crosses zero."""
    # Exact match
    for i, sp in enumerate(stock):
        if abs(sp) < 0.01:
            return x[i]
    # Zero-crossing interpolation
    for i in range(len(stock) - 1):
        if stock[i] <= 0 <= stock[i + 1] or stock[i] >= 0 >= stock[i + 1]:
            denom = stock[i + 1] - stock[i]
            if abs(denom) > 1e-10:
                t = -stock[i] / denom
                return x[i] + t * (x[i + 1] - x[i])
            return x[i]
    return x[len(x) // 2] if x else 100.0


def _dollar_tick_formatter(val: float, _pos: object = None) -> str:
    """Format axis ticks as $-20K, $0, $20K etc."""
    if abs(val) >= 1_000_000:
        return f"${val / 1_000_000:,.1f}M"
    if abs(val) >= 1_000:
        sign = "-" if val < 0 else ""
        return f"{sign}${abs(val) / 1_000:,.0f}K"
    return f"${val:,.0f}"


def build_payoff_chart_png_data_uri(model: Mapping[str, object]) -> str:
    """Build a publication-quality payoff chart as a PNG data URI using matplotlib.

    Reads the ``payoff`` block from the raw report model (pre-contract),
    which contains ``price_grid``, ``stock_pnl``, ``options_pnl``, ``combined_pnl``,
    ``strikes`` and ``breakevens``.
    """
    import io as _io

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.ticker as mticker

    payoff = model.get("payoff") if isinstance(model.get("payoff"), Mapping) else None
    x_values = _coerce_svg_series(payoff.get("price_grid")) if payoff else None
    stock_values = _coerce_svg_series(payoff.get("stock_pnl")) if payoff else None
    options_values = _coerce_svg_series(payoff.get("options_pnl")) if payoff else None
    combined_values = _coerce_svg_series(payoff.get("combined_pnl")) if payoff else None

    if not (x_values and stock_values and options_values and combined_values):
        # Return a minimal placeholder PNG
        fig, ax = plt.subplots(figsize=(7, 4.5), dpi=150)
        ax.text(0.5, 0.5, "Payoff Diagram", ha="center", va="center",
                fontsize=12, color="#6b7280", transform=ax.transAxes)
        ax.set_axis_off()
        buf = _io.BytesIO()
        fig.savefig(buf, format="png", dpi=150, bbox_inches="tight", facecolor="white")
        plt.close(fig)
        buf.seek(0)
        encoded = base64.b64encode(buf.read()).decode("ascii")
        return f"data:image/png;base64,{encoded}"

    # Extract strikes and breakevens
    raw_strikes = payoff.get("strikes") if payoff else None
    raw_breakevens = payoff.get("breakevens") if payoff else None
    strikes: List[float] = []
    breakevens: List[float] = []
    if isinstance(raw_strikes, list):
        for s in raw_strikes:
            v = _coerce_svg_float(s)
            if v is not None:
                strikes.append(v)
    if isinstance(raw_breakevens, list):
        for b in raw_breakevens:
            v = _coerce_svg_float(b)
            if v is not None:
                breakevens.append(v)
    strikes = sorted(strikes)[:6]
    breakevens = sorted(breakevens)[:4]

    min_len = min(len(x_values), len(stock_values), len(options_values), len(combined_values))
    x = x_values[:min_len]
    stock = stock_values[:min_len]
    options = options_values[:min_len]
    combined = combined_values[:min_len]

    spot_price = _find_spot_price(x, stock)

    # X range: ±30% around spot, expanding for strikes/breakevens
    min_x = spot_price * 0.70
    max_x = spot_price * 1.30
    for pt in strikes + breakevens:
        if pt < min_x:
            min_x = pt - (spot_price * 0.05)
        if pt > max_x:
            max_x = pt + (spot_price * 0.05)

    # Filter data to visible range (with small padding)
    pad_frac = 0.02 * (max_x - min_x)
    vis_min = min_x - pad_frac
    vis_max = max_x + pad_frac
    vis_x, vis_stock, vis_options, vis_combined = [], [], [], []
    for i in range(len(x)):
        if vis_min <= x[i] <= vis_max:
            vis_x.append(x[i])
            vis_stock.append(stock[i])
            vis_options.append(options[i])
            vis_combined.append(combined[i])

    if not vis_x:
        vis_x, vis_stock, vis_options, vis_combined = x, stock, options, combined

    # Y range: scale to combined + options PnL (not stock, which has extreme values)
    # This ensures the meaningful payoff shapes are clearly visible
    focus_y = vis_options + vis_combined + [0.0]
    min_y = min(focus_y)
    max_y = max(focus_y)
    y_pad = (max_y - min_y) * 0.20 if max_y != min_y else 1.0
    min_y -= y_pad
    max_y += y_pad

    # --- Create figure ---
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=150)
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    # Remove top and right spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#D1D5DB")
    ax.spines["bottom"].set_color("#D1D5DB")

    # Horizontal grid lines only
    ax.yaxis.grid(True, color="#F3F4F6", linewidth=0.5)
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)

    # Zero line
    ax.axhline(y=0, color="#9CA3AF", linewidth=0.8, linestyle="--", zorder=2)

    # Current price vertical line
    ax.axvline(x=spot_price, color="#93C5FD", linewidth=0.5, linestyle=":", zorder=2)

    # Strike lines
    for idx, strike_price in enumerate(strikes):
        ax.axvline(x=strike_price, color="#D1D5DB", linewidth=1.0, linestyle="--", zorder=2)
        ax.annotate(
            f"K{idx + 1} ${strike_price:,.0f}",
            xy=(strike_price, max_y),
            xytext=(0, 2),
            textcoords="offset points",
            ha="center", va="bottom",
            fontsize=8, color="#6b7280",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.9),
            zorder=5,
        )

    # Breakeven lines
    for idx, be_price in enumerate(breakevens):
        ax.axvline(x=be_price, color="#9CA3AF", linewidth=1.0, linestyle=(0, (5, 3, 1, 3)), zorder=2)
        ax.annotate(
            f"BE{idx + 1} ${be_price:,.0f}",
            xy=(be_price, max_y),
            xytext=(0, 2),
            textcoords="offset points",
            ha="center", va="bottom",
            fontsize=8, color="#9CA3AF",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.9),
            zorder=5,
        )

    # Plot lines
    ax.plot(vis_x, vis_stock, color="#2563EB", linewidth=2.0, label="Stock P&L", solid_capstyle="round")
    ax.plot(vis_x, vis_options, color="#7C3AED", linewidth=2.0, label="Options P&L", solid_capstyle="round")
    ax.plot(vis_x, vis_combined, color="#374151", linewidth=2.5, linestyle="--", label="Combined P&L",
            dash_capstyle="round")

    # Axis limits
    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)

    # Axis labels
    ax.set_xlabel("Stock Price at Expiry", fontsize=8, color="#6b7280")
    ax.set_ylabel("Profit / Loss", fontsize=8, color="#6b7280")

    # X-axis: dollar format, round ticks
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, p: f"${v:,.0f}"))
    ax.tick_params(axis="x", labelsize=8, colors="#6b7280")
    # Use nice tick spacing based on price range
    x_span = max_x - min_x
    if x_span > 500:
        x_step = 100
    elif x_span > 200:
        x_step = 50
    elif x_span > 100:
        x_step = 25
    elif x_span > 40:
        x_step = 10
    else:
        x_step = 5
    ax.xaxis.set_major_locator(mticker.MultipleLocator(x_step))

    # Y-axis: dollar format with K suffix
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(_dollar_tick_formatter))
    ax.tick_params(axis="y", labelsize=8, colors="#6b7280")

    # Legend
    ax.legend(loc="best", fontsize=8, frameon=True, facecolor="white", edgecolor="#E5E7EB",
              framealpha=0.95)

    fig.tight_layout(pad=0.3)

    # Export to PNG buffer
    buf = _io.BytesIO()
    fig.savefig(buf, format="png", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def build_view_model(data: Mapping[str, object]) -> Dict[str, object]:
    if not isinstance(data, Mapping):
        return build_view_model_from_contract({})
    return build_view_model_from_contract(data)
