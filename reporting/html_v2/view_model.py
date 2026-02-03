from __future__ import annotations

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
        return "text-red-600" if value < 0 else "text-gray-900"
    if isinstance(value, str):
        if "-" in value and value not in ("---", MISSING, "--"):
            return "text-red-600"
    return "text-gray-900"


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
            dot_class = "text-[#E60000]"
        elif "bull" in type_text:
            dot_class = "text-[#00A550]"
        else:
            dot_class = "text-gray-400"
        scenarios.append(
            {
                "title": title,
                "condition": _to_text(card.get("condition")),
                "description": _to_text(card.get("body") or card.get("description")),
                "dot_class": dot_class,
            }
        )
    labels = [
        ("Bearish", "text-[#E60000]"),
        ("Stagnant", "text-gray-400"),
        ("Bullish", "text-[#00A550]"),
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
            "change_class": "text-gray-900",
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


def build_view_model_from_contract(contract: Mapping[str, object]) -> Dict[str, object]:
    header = contract.get("header") if isinstance(contract.get("header"), Mapping) else {}
    structure = contract.get("structure") if isinstance(contract.get("structure"), Mapping) else {}
    metrics_rows = contract.get("metrics", {}).get("rows") if isinstance(contract.get("metrics"), Mapping) else []
    metrics_rows = metrics_rows if isinstance(metrics_rows, list) else []
    key_levels_rows = (
        contract.get("key_levels_display_rows_by_price")
        if isinstance(contract.get("key_levels_display_rows_by_price"), list)
        else contract.get("key_levels_display_rows")
    )
    if not isinstance(key_levels_rows, list):
        key_levels_rows = contract.get("key_levels") if isinstance(contract.get("key_levels"), list) else []
    scenario_cards = contract.get("scenario_analysis_cards")
    scenario_cards = scenario_cards if isinstance(scenario_cards, list) else []
    stock_banner = contract.get("stock_banner") if isinstance(contract.get("stock_banner"), Mapping) else {}

    last_price = _to_number(header.get("last_price")) or 0.0
    shares = _to_number(header.get("shares")) or _to_number(stock_banner.get("shares")) or 0.0
    avg_cost = _to_number(header.get("avg_cost")) or _to_number(stock_banner.get("avg_cost")) or 0.0
    mkt_value = last_price * shares
    cost_value = avg_cost * shares
    pnl_dollar = mkt_value - cost_value
    pnl_percent = (pnl_dollar / cost_value * 100.0) if cost_value else 0.0

    move_text = _to_text(
        header.get("ten_day_change")
        or header.get("chg_pct_ytd")
        or stock_banner.get("chg_pct_ytd")
        or "0.00%"
    )

    option_legs: List[Dict[str, object]] = []
    legs = structure.get("legs") if isinstance(structure.get("legs"), list) else []
    if legs:
        for idx, leg in enumerate(legs):
            if not isinstance(leg, Mapping):
                continue
            side_text = _to_text(leg.get("side"))
            side_info = _normalize_side(side_text)
            qty = _to_number(leg.get("qty")) or 1
            strike_num = _to_number(leg.get("strike")) or 0.0
            premium_num = _to_number(leg.get("premium")) or 0.0
            price_num = abs(premium_num)
            option_legs.append(
                {
                    "leg": int(_to_number(leg.get("leg")) or (idx + 1)),
                    "action": side_info["action"],
                    "quantity": int(qty) if float(qty).is_integer() else qty,
                    "expiration": _to_text(leg.get("Expiry") or leg.get("expiry")),
                    "strike": _format_currency(strike_num, decimals=2),
                    "type": side_info["type"] or _to_text(leg.get("type") or leg.get("kind")),
                    "price": f"at {_format_currency(price_num, decimals=2)}",
                    "delta": _format_number(leg.get("delta") or 0, decimals=2),
                    "otm_percent": MISSING,
                    "premium": premium_num,
                    "premium_display": _format_currency(premium_num, decimals=2),
                }
            )
    if not option_legs:
        option_legs.append(
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
            }
        )

    net_premium_value = _to_number(structure.get("net_premium_total")) or 0.0
    net_premium_display = _format_currency(net_premium_value, decimals=2)

    metrics = _build_metrics(metrics_rows)
    metric_view = _build_metric_view(metrics)

    option_legs_title = (
        f"Option Leg(s) for {_to_text(header.get('strategy_name'))} on {_to_text(header.get('ticker'))}"
    )

    return {
        "header": {
            "title": _to_text(header.get("strategy_name")),
            "subtitle": "Wealth Management Option Strategy",
            "date": _format_date(header.get("report_time") or header.get("as_of")),
            "disclaimer": (
                "The illustration is intended for informational and internal use. "
                "Although it can be shared with clients approved for trading Options or "
                "have received a copy of the Option Disclosure Document. For specific stock "
                "ratings relative to UBS INV research, CIO research, and/or SPGMI's Quality "
                "ranking, please refer to the research tab on ConsultWorks. Commissions or fees not included."
            ),
        },
        "stock_details": {
            "ticker": _to_text(header.get("ticker")),
            "name": _to_text(header.get("name")),
            "sector": _to_text(header.get("sector")),
            "ubs_rating": _to_text(header.get("ubs_rating") or header.get("ubs_grp_rating") or "N/A"),
            "ubs_target": _format_currency(
                _to_number(header.get("target") or header.get("ubs_grp_target")) or 0.0
            ),
            "cio_rating": _to_text(header.get("cio_rating") or header.get("ubs_cio_rating") or "N/A"),
            "last_price": _format_currency(last_price, decimals=2),
            "ten_day_change": move_text,
            "change_class": "text-red-600" if "-" in move_text else "text-green-600",
            "change_symbol": "-" if "-" in move_text else "+",
            "fifty_two_week_high": _format_currency(
                _to_number(header.get("high_52w") or stock_banner.get("high_52w")) or 0.0,
                decimals=0,
            ),
            "fifty_two_week_low": _format_currency(
                _to_number(header.get("low_52w") or stock_banner.get("low_52w")) or 0.0,
                decimals=0,
            ),
            "dividend_yield": _format_percent(
                _to_number(header.get("dividend_yield") or stock_banner.get("dividend_yield")) or 0.0,
                decimals=2,
            ),
            "earnings_date": _to_text(header.get("earnings_date") or stock_banner.get("earnings_date")),
        },
        "client_position": (
            {
                "shares": f"{shares:,.0f}",
                "avg_cost": _format_currency(avg_cost, decimals=2),
                "mkt_value": _format_currency(mkt_value, decimals=2),
                "pnl_dollar": _format_currency(pnl_dollar, decimals=2),
                "pnl_percent": f"{pnl_percent:.2f}",
                "pnl_class": "text-green-600" if pnl_dollar >= 0 else "text-red-600",
                "pnl_badge_class": "bg-green-100 text-green-800"
                if pnl_dollar >= 0
                else "bg-red-100 text-red-800",
            }
            if shares
            else None
        ),
        "strategy_description": _strategy_description(contract),
        "option_legs_title": option_legs_title,
        "option_legs": option_legs,
        "net_premium": {
            "display": net_premium_display,
            "class": "text-red-600" if net_premium_value < 0 else "text-gray-900",
        },
        "metrics": metric_view,
        "key_levels": _build_key_levels(key_levels_rows),
        "scenario_analysis": _build_scenarios(scenario_cards),
        "disclosures": _join_disclosures(
            contract.get("disclosures_text")
            or contract.get("disclosures")
            or contract.get("disclaimers")
            or ""
        ),
        "page": {"total": 2},
    }


def build_view_model(data: Mapping[str, object]) -> Dict[str, object]:
    if not isinstance(data, Mapping):
        return build_view_model_from_contract({})
    if _looks_like_template_data(data):
        return _from_template_data(data)
    return build_view_model_from_contract(data)
