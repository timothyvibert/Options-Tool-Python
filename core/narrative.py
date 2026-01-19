from __future__ import annotations

from typing import Any, Dict, Iterable, List, Mapping, Optional

import math

from core.margin import classify_strategy
from core.models import StrategyInput
from core.narrative_rules import RULES, TEMPLATES
from core.payoff import compute_payoff


def _to_float(value: object) -> Optional[float]:
    if isinstance(value, (int, float)):
        if isinstance(value, float) and math.isnan(value):
            return None
        return float(value)
    if isinstance(value, str):
        text = value.strip()
        if text == "":
            return None
        sign = 1.0
        if text.startswith("(") and text.endswith(")"):
            sign = -1.0
            text = text[1:-1].strip()
        if text.endswith("%"):
            text = text[:-1].strip()
        if text.lower().startswith(("credit", "debit")):
            parts = text.split()
            text = parts[-1] if parts else ""
        text = text.replace("$", "").replace(",", "")
        try:
            return sign * float(text)
        except ValueError:
            return None
    return None


def _is_missing(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip() == ""
    return False


def _format_price(value: Optional[float]) -> str:
    if value is None:
        return "--"
    return f"${value:,.2f}"


def _format_currency(value: Optional[float]) -> Optional[str]:
    if value is None:
        return None
    return f"${value:,.2f}"


def _format_currency_abs(value: Optional[float]) -> Optional[str]:
    if value is None:
        return None
    return f"${abs(value):,.2f}"


def _normalize_label(value: object) -> str:
    if value is None:
        return ""
    text = str(value).lower().strip()
    for ch in [" ", "-", "_", "(", ")", "/"]:
        text = text.replace(ch, "")
    return text


def _levels_by_label(levels: Iterable[Mapping[str, object]]) -> dict[str, dict]:
    mapping: dict[str, dict] = {}
    for level in levels:
        if not isinstance(level, Mapping):
            continue
        label = level.get("label")
        if _is_missing(label):
            label = level.get("Scenario") or level.get("scenario")
        key = _normalize_label(label)
        if key and key not in mapping:
            mapping[key] = dict(level)
    return mapping


def _find_level(
    label_map: Mapping[str, Mapping[str, object]],
    labels: List[str],
) -> Optional[Mapping[str, object]]:
    for label in labels:
        key = _normalize_label(label)
        if key in label_map:
            return label_map[key]
    return None


def _level_net_pnl(level: Optional[Mapping[str, object]]) -> Optional[float]:
    if not isinstance(level, Mapping):
        return None
    for key in ["net_pnl", "Net PnL", "combined_pnl"]:
        if key in level:
            value = _to_float(level.get(key))
            if value is not None:
                return value
    return None


def _summary_value(
    summary_rows: Optional[List[Mapping[str, object]]],
    metric_name: str,
) -> Optional[float]:
    if not summary_rows:
        return None
    for row in summary_rows:
        if not isinstance(row, Mapping):
            continue
        if row.get("metric") == metric_name:
            value = row.get("combined") or row.get("options")
            parsed = _to_float(value)
            if parsed is not None:
                return parsed
    return None


def _condition_text(
    kind: str,
    anchors: List[Mapping[str, object]],
    exclude_zero: bool = False,
) -> str:
    prices = [
        _to_float(anchor.get("price"))
        for anchor in anchors
        if _to_float(anchor.get("price")) is not None
    ]
    if exclude_zero:
        non_zero = [price for price in prices if abs(price) > 1e-6]
        if non_zero:
            prices = non_zero
    prices = sorted(prices)
    if not prices:
        return "--"
    if kind == "bear":
        return f"If stock falls to {_format_price(prices[0])} or below"
    if kind == "bull":
        return f"If stock rises to {_format_price(prices[-1])} or above"
    if len(prices) >= 2:
        return (
            f"If stock stays between {_format_price(prices[0])} and "
            f"{_format_price(prices[-1])}"
        )
    return f"If stock stays near {_format_price(prices[0])}"


class _SafeDict(dict):
    def __missing__(self, key: str) -> str:
        return "--"


def _render_template(template_id: str, context: Mapping[str, object]) -> str:
    template = TEMPLATES.get(template_id, "--")
    return template.format_map(_SafeDict({k: str(v) for k, v in context.items()}))


def _match_rule(
    rule: Mapping[str, object], context: Mapping[str, object]
) -> tuple[bool, list[dict]]:
    matched: list[dict] = []
    conditions = rule.get("conditions", [])
    for condition in conditions:
        if not isinstance(condition, Mapping):
            return False, []
        field = condition.get("field")
        op = condition.get("op", "==")
        value = condition.get("value")
        actual = context.get(field)
        ok = False
        if op == "==":
            ok = actual == value
        elif op == "in":
            ok = actual in (value or [])
        if not ok:
            return False, []
        matched.append({"field": field, "op": op, "value": value, "actual": actual})
    return True, matched


def _level_map(levels: Iterable[Mapping[str, object]]) -> dict[str, dict]:
    mapping: dict[str, dict] = {}
    for level in levels:
        if not isinstance(level, Mapping):
            continue
        level_id = level.get("id")
        if isinstance(level_id, str) and level_id:
            mapping[level_id] = dict(level)
    return mapping


def _strike_levels(levels: Iterable[Mapping[str, object]]) -> list[dict]:
    strikes = []
    for level in levels:
        if not isinstance(level, Mapping):
            continue
        label = level.get("label")
        if _is_missing(label):
            label = level.get("Scenario") or level.get("scenario")
        label_text = str(label).strip().lower() if label is not None else ""
        if "strike" not in label_text:
            continue
        price = _to_float(level.get("price"))
        if price is None:
            continue
        payload = dict(level)
        payload["_label_text"] = label_text
        payload["_price"] = price
        strikes.append(payload)
    strikes.sort(key=lambda item: item["_price"])
    return strikes


def _short_strike_bounds(
    strike_levels: list[dict],
) -> tuple[Optional[dict], Optional[dict]]:
    if not strike_levels:
        return None, None
    lower_middle = next(
        (
            level
            for level in strike_levels
            if "lower middle" in level.get("_label_text", "")
        ),
        None,
    )
    upper_middle = next(
        (
            level
            for level in strike_levels
            if "upper middle" in level.get("_label_text", "")
        ),
        None,
    )
    if lower_middle and upper_middle:
        return lower_middle, upper_middle
    if len(strike_levels) >= 4:
        return strike_levels[1], strike_levels[2]
    if len(strike_levels) == 2:
        return strike_levels[0], strike_levels[1]
    return None, None


def _format_signed_currency(value: Optional[float]) -> Optional[str]:
    if value is None:
        return None
    sign = "-" if value < 0 else "+"
    return f"{sign}${abs(value):,.2f}"


def _pick_primary_anchor(
    anchors: List[Mapping[str, object]],
) -> Optional[Mapping[str, object]]:
    for anchor in anchors:
        if _to_float(anchor.get("price")) is not None:
            return anchor
    return anchors[0] if anchors else None


def build_narrative_scenarios(
    strategy_input: StrategyInput,
    key_levels: Mapping[str, object],
    payoff_result: Optional[Mapping[str, object]] = None,
    summary_rows: Optional[List[Mapping[str, object]]] = None,
) -> Dict[str, object]:
    levels = key_levels.get("levels") if isinstance(key_levels, Mapping) else None
    if not isinstance(levels, list):
        return {
            "bear": None,
            "base": None,
            "bull": None,
            "trace": {"rule_id": None, "version": None, "reason": "no key levels"},
        }

    legs = [leg for leg in strategy_input.legs if leg.kind.lower() in {"call", "put"}]
    has_stock = strategy_input.stock_position != 0
    short_calls = [leg for leg in legs if leg.kind.lower() == "call" and leg.position < 0]
    long_calls = [leg for leg in legs if leg.kind.lower() == "call" and leg.position > 0]
    short_puts = [leg for leg in legs if leg.kind.lower() == "put" and leg.position < 0]
    long_puts = [leg for leg in legs if leg.kind.lower() == "put" and leg.position > 0]
    iron_condor = bool(short_calls and long_calls and short_puts and long_puts and not has_stock)

    if payoff_result is None:
        payoff_result = compute_payoff(strategy_input)
    defined_risk = not payoff_result.get("unlimited_upside", False) and not payoff_result.get(
        "unlimited_downside", False
    )

    classification = classify_strategy(strategy_input)
    context = {
        "classification": classification,
        "has_stock_position": has_stock,
        "has_short_call": bool(short_calls),
        "has_short_put": bool(short_puts),
        "has_long_call": bool(long_calls),
        "has_long_put": bool(long_puts),
        "iron_condor": iron_condor,
        "defined_risk": defined_risk,
    }

    selected_rule = None
    matched_conditions: list[dict] = []
    for rule in RULES:
        ok, matched = _match_rule(rule, context)
        if ok:
            selected_rule = rule
            matched_conditions = matched
            break

    level_lookup = _level_map(levels)
    label_lookup = _levels_by_label(levels)
    inputs_used = dict(context)
    if selected_rule is None:
        return {
            "bear": None,
            "base": None,
            "bull": None,
            "trace": {
                "rule_id": None,
                "version": None,
                "matched_conditions": [],
                "inputs_used": inputs_used,
                "anchors_used": {},
                "reason": "no matching rule",
            },
        }

    spot_level = _find_level(label_lookup, ["Current Market Price", "Spot"])
    lower_long = _find_level(
        label_lookup, ["Strike (Lowest)", "Lower Strike", "Strike Lowest"]
    )
    upper_long = _find_level(
        label_lookup, ["Strike (Highest)", "Upper Strike", "Strike Highest"]
    )

    strike_levels = _strike_levels(levels)
    lower_short, upper_short = _short_strike_bounds(strike_levels)

    max_profit = _summary_value(summary_rows, "Max Profit")
    max_loss = _summary_value(summary_rows, "Max Loss")
    net_premium = _summary_value(summary_rows, "Net Prem/Share")

    if max_profit is None:
        candidate = None
        if lower_short is not None:
            candidate = _level_net_pnl(lower_short)
        if candidate is None and spot_level is not None:
            candidate = _level_net_pnl(spot_level)
        if candidate is None:
            candidate = _level_net_pnl(lower_long) or _level_net_pnl(upper_long)
        max_profit = candidate

    if max_loss is None:
        candidates = []
        for level in [lower_long, upper_long]:
            value = _level_net_pnl(level)
            if value is not None:
                candidates.append(value)
        if candidates:
            max_loss = min(candidates)

    max_profit_text = _format_currency(max_profit)
    max_loss_text = _format_currency_abs(max_loss)
    net_premium_text = _format_currency(net_premium)

    anchors_used: dict[str, list[str]] = {}
    scenarios: dict[str, object] = {}
    templates = selected_rule.get("templates", {})
    scenario_anchors = selected_rule.get("scenario_anchors", {})
    for kind, title in [
        ("bear", "Bearish Case"),
        ("base", "Stagnant Case"),
        ("bull", "Bullish Case"),
    ]:
        anchor_ids = scenario_anchors.get(kind, [])
        if not isinstance(anchor_ids, list):
            anchor_ids = []
        anchors = [level_lookup[a_id] for a_id in anchor_ids if a_id in level_lookup]
        anchors_used[kind] = [anchor.get("id") for anchor in anchors if "id" in anchor]
        condition = ""
        if context.get("iron_condor") and lower_short and upper_short:
            lower_price = _to_float(lower_short.get("price"))
            upper_price = _to_float(upper_short.get("price"))
            if lower_price is not None and upper_price is not None:
                if kind == "bear":
                    condition = f"If stock falls below {_format_price(lower_price)}"
                elif kind == "bull":
                    condition = f"If stock rises above {_format_price(upper_price)}"
                else:
                    condition = (
                        f"If stock stays {_format_price(lower_price)}-"
                        f"{_format_price(upper_price)}"
                    )
        if not condition:
            condition = _condition_text(kind, anchors, exclude_zero=True)
        primary = _pick_primary_anchor(anchors)
        price = _to_float(primary.get("price")) if primary else None
        overlay_pnl = _to_float(primary.get("net_pnl")) if primary else None
        if has_stock:
            stock_only_pnl = (
                strategy_input.stock_position * (price - strategy_input.avg_cost)
                if price is not None
                else None
            )
        else:
            stock_only_pnl = 0.0
        delta_vs_stock = (
            overlay_pnl - stock_only_pnl
            if overlay_pnl is not None and stock_only_pnl is not None
            else None
        )
        scenario_pnl_text = _format_signed_currency(overlay_pnl)
        lower_long_price = _to_float(lower_long.get("price")) if lower_long else None
        upper_long_price = _to_float(upper_long.get("price")) if upper_long else None
        context_values = {
            "anchor_price": _format_price(price) if price is not None else "--",
            "max_profit": max_profit_text or "--",
            "max_loss": max_loss_text or "--",
            "net_premium": net_premium_text or "--",
            "lower_long": _format_price(lower_long_price) if lower_long_price is not None else "--",
            "upper_long": _format_price(upper_long_price) if upper_long_price is not None else "--",
            "scenario_pnl": scenario_pnl_text or "--",
        }
        body = _render_template(templates.get(kind, ""), context_values)
        if "$" not in body and scenario_pnl_text:
            if body and body.strip() != "--":
                body = f"{body} Net P&L at this level is {scenario_pnl_text}."
            else:
                body = f"Net P&L at this level is {scenario_pnl_text}."
        if has_stock:
            delta_text = _format_signed_currency(delta_vs_stock)
            if delta_text is not None:
                overlay_note = (
                    " Compared with holding the stock alone, this overlay changes "
                    f"P&L by {delta_text} at this scenario."
                )
                body = f"{body}{overlay_note}" if body else overlay_note.strip()
        scenarios[kind] = {
            "title": title,
            "condition": condition,
            "body": body,
            "anchors": [
                {
                    "id": anchor.get("id"),
                    "label": anchor.get("label"),
                    "price": anchor.get("price"),
                }
                for anchor in anchors
            ],
            "overlay_pnl": overlay_pnl,
            "stock_only_pnl": stock_only_pnl,
            "delta_vs_stock": delta_vs_stock,
        }

    return {
        "bear": scenarios.get("bear"),
        "base": scenarios.get("base"),
        "bull": scenarios.get("bull"),
        "trace": {
            "rule_id": selected_rule.get("rule_id"),
            "version": selected_rule.get("version"),
            "matched_conditions": matched_conditions,
            "inputs_used": inputs_used,
            "anchors_used": anchors_used,
        },
    }
