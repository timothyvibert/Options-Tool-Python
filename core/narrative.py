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


def _format_total_from_per_share(
    per_share: Optional[float],
    contract_count: Optional[int],
) -> Optional[str]:
    if per_share is None or not contract_count:
        return None
    total = per_share * 100.0 * contract_count
    return f"${abs(total):,.2f}"


def _format_roi_ratio(value: Optional[float]) -> Optional[str]:
    if value is None:
        return None
    return f"{value * 100.0:.1f}%"


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


def _breakeven_levels(levels: Iterable[Mapping[str, object]]) -> list[dict]:
    breakevens = []
    for level in levels:
        if not isinstance(level, Mapping):
            continue
        label = level.get("label")
        if _is_missing(label):
            label = level.get("Scenario") or level.get("scenario")
        label_text = str(label).strip().lower() if label is not None else ""
        if "breakeven" not in label_text:
            continue
        price = _to_float(level.get("price"))
        if price is None:
            continue
        payload = dict(level)
        payload["_price"] = price
        breakevens.append(payload)
    breakevens.sort(key=lambda item: item["_price"])
    return breakevens


def _summary_metric(
    summary_rows: Optional[List[Mapping[str, object]]],
    metric_name: str,
    prefer: str = "combined",
) -> Optional[float]:
    if not summary_rows:
        return None
    for row in summary_rows:
        if not isinstance(row, Mapping):
            continue
        if row.get("metric") != metric_name:
            continue
        if prefer == "options":
            value = row.get("options") or row.get("combined")
        else:
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
    seen_prices = set()
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
        if price in seen_prices:
            continue
        seen_prices.add(price)
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


def _pick_leg_strike(
    legs: Iterable,
    kind: str,
    position_sign: int,
    prefer: str,
) -> Optional[float]:
    strikes = []
    for leg in legs:
        if leg.kind.lower() != kind:
            continue
        if position_sign < 0 and leg.position >= 0:
            continue
        if position_sign > 0 and leg.position <= 0:
            continue
        strikes.append(float(leg.strike))
    if not strikes:
        return None
    strikes.sort()
    return strikes[0] if prefer == "min" else strikes[-1]


def _format_signed_currency(value: Optional[float]) -> Optional[str]:
    if value is None:
        return None
    sign = "-" if value < 0 else "+"
    return f"{sign}${abs(value):,.2f}"


def _infer_contract_count(analysis_pack: Mapping[str, object]) -> Optional[int]:
    if not isinstance(analysis_pack, Mapping):
        return None
    legs_data = analysis_pack.get("legs")
    strategy_input = analysis_pack.get("strategy_input")
    if not isinstance(legs_data, list) and isinstance(strategy_input, StrategyInput):
        legs_data = [
            {
                "kind": leg.kind,
                "ratio": abs(leg.position),
                "position": leg.position,
            }
            for leg in strategy_input.legs
        ]
    if not isinstance(legs_data, list):
        return None
    quantities = []
    for leg in legs_data:
        if not isinstance(leg, Mapping):
            continue
        kind = str(leg.get("kind") or leg.get("type") or "").lower()
        if kind not in {"call", "put"}:
            continue
        qty = _to_float(leg.get("ratio"))
        if qty is None or qty <= 0:
            position = _to_float(leg.get("position"))
            if position is not None:
                qty = abs(position)
        if qty and qty > 0:
            quantities.append(qty)
    if not quantities:
        return None
    return int(round(min(quantities)))


def _premium_context(
    strategy_input: StrategyInput,
    summary_rows: Optional[List[Mapping[str, object]]],
    contract_count: Optional[int] = None,
    is_credit: Optional[bool] = None,
    is_debit: Optional[bool] = None,
) -> dict:
    per_share = _summary_metric(summary_rows, "Net Prem/Share", prefer="options")
    if per_share is None or abs(per_share) < 1e-9:
        return {
            "per_share": None,
            "total": None,
            "direction": None,
            "contract_count": contract_count,
        }
    multiplier = None
    if strategy_input.legs:
        multiplier = strategy_input.legs[0].multiplier
    total = None
    if contract_count:
        total = per_share * (multiplier or 100.0) * contract_count
    if is_credit is True:
        direction = "received"
    elif is_debit is True:
        direction = "paid"
    else:
        direction = "received" if per_share < 0 else "paid"
    return {
        "per_share": per_share,
        "total": total,
        "direction": direction,
        "contract_count": contract_count,
    }


def _premium_sentence(premium_ctx: Mapping[str, object]) -> Optional[str]:
    per_share = premium_ctx.get("per_share")
    total = premium_ctx.get("total")
    direction = premium_ctx.get("direction")
    contract_count = premium_ctx.get("contract_count")
    if direction is None:
        return None
    if total is not None:
        base = f"Net option premium (total): {_format_currency_abs(total)}"
        if contract_count:
            base = f"{base} on {int(contract_count)} contracts"
        return f"{base} {direction}."
    if per_share is not None:
        return (
            f"Net option premium: {_format_currency_abs(per_share)} per share {direction}."
        )
    return None


def _overlay_sentence(kind: str, delta_vs_stock: Optional[float]) -> Optional[str]:
    delta_text = _format_signed_currency(delta_vs_stock)
    if delta_text is None:
        return None
    if kind == "bear":
        lead = "Relative to holding the shares alone, the option overlay changes the outcome by"
    elif kind == "base":
        lead = "Net effect versus stock-only at this level is"
    else:
        lead = "Compared with stock-only, the overlay changes results by"
    return f"{lead} {delta_text}."


def _join_sentences(sentences: Iterable[str]) -> str:
    return " ".join([sentence.strip() for sentence in sentences if sentence])


def _level_value(level: Optional[Mapping[str, object]], keys: Iterable[str]) -> Optional[float]:
    if not isinstance(level, Mapping):
        return None
    for key in keys:
        if key in level:
            value = _to_float(level.get(key))
            if value is not None:
                return value
    return None


def _has_breakdown_data(level: Optional[Mapping[str, object]], has_stock: bool) -> bool:
    if not has_stock or not isinstance(level, Mapping):
        return False
    option_pnl = _level_value(level, ["option_pnl", "Option PnL"])
    stock_pnl = _level_value(level, ["stock_pnl", "Stock PnL"])
    return option_pnl is not None or stock_pnl is not None


def _pnl_sentence(
    level: Optional[Mapping[str, object]],
    has_stock: bool,
    anchor_price: Optional[float],
) -> str:
    price_value = anchor_price
    if price_value is None and isinstance(level, Mapping):
        price_value = _to_float(level.get("price"))
    price_text = _format_price(price_value) if price_value is not None else "this price"
    combined = _level_value(level, ["net_pnl", "Net PnL", "combined_pnl"])
    if has_stock:
        combined_text = _format_signed_currency(combined)
        if combined_text is None:
            return ""
        sentence = f"At {price_text}, combined P&L would be {combined_text}."
        option_pnl = _level_value(level, ["option_pnl", "Option PnL"])
        stock_pnl = _level_value(level, ["stock_pnl", "Stock PnL"])
        if option_pnl is not None or stock_pnl is not None:
            option_text = (
                _format_signed_currency(option_pnl) if option_pnl is not None else None
            )
            stock_text = (
                _format_signed_currency(stock_pnl) if stock_pnl is not None else None
            )
            details = []
            if option_text:
                details.append(f"options contribute {option_text}")
            if stock_text:
                details.append(f"the shares contribute {stock_text}")
            if details:
                sentence = f"{sentence} For context, at this price " + " and ".join(details) + "."
        return sentence
    option_pnl = _level_value(level, ["option_pnl", "Option PnL"])
    if option_pnl is None:
        option_pnl = combined
    option_text = _format_signed_currency(option_pnl)
    if option_text is None:
        return ""
    return f"At {price_text}, options P&L would be {option_text}."


def _numbers_sentence(
    kind: str,
    family: str,
    has_stock: bool,
    premium_ctx: Mapping[str, object],
    max_profit: Optional[float],
    max_loss: Optional[float],
    pnl_sentence: str,
    is_partial: bool,
    roi_value: Optional[float],
    breakeven_price: Optional[float],
    include_breakeven: bool,
    anchor_price: Optional[float],
    is_credit: Optional[bool],
    is_debit: Optional[bool],
    option_structure: str,
    is_capped_profit: bool,
    is_defined_risk: bool,
) -> Optional[str]:
    premium_sentence = _premium_sentence(premium_ctx)
    max_profit_text = _format_currency(max_profit)
    max_loss_text = _format_currency_abs(max_loss)
    roi_text = _format_roi_ratio(roi_value)
    breakeven_text = _format_price(breakeven_price) if breakeven_price is not None else None

    def strip_period(text: str) -> str:
        return text[:-1] if text.endswith(".") else text

    if not has_stock:
        parts: list[str] = []
        anchor_text = _format_price(anchor_price) if anchor_price is not None else None
        contract_count = premium_ctx.get("contract_count")
        debit_text = None
        if premium_ctx.get("direction") == "paid":
            total = premium_ctx.get("total")
            per_share = premium_ctx.get("per_share")
            total_text = _format_total_from_per_share(per_share, contract_count)
            if total_text and per_share is not None:
                debit_text = f"{total_text} total ({_format_currency_abs(per_share)} per share)"
            elif total is not None:
                debit_text = _format_currency_abs(total)
            elif per_share is not None:
                debit_text = f"{_format_currency_abs(per_share)} per share"
        if is_debit and option_structure in {"call_spread", "put_spread"}:
            if kind == "bear":
                if debit_text:
                    parts.append(f"Maximum loss equals the debit paid: {debit_text}.")
                elif max_loss_text and is_defined_risk:
                    parts.append(f"Maximum loss is {max_loss_text}.")
                if roi_text and anchor_text:
                    parts.append(f"ROI at {anchor_text} is {roi_text}.")
            elif kind == "base":
                if include_breakeven and breakeven_text:
                    parts.append(f"Breakeven is around {breakeven_text}.")
                if debit_text:
                    parts.append(
                        f"Maximum loss remains limited to the debit paid: {debit_text}."
                    )
                elif max_loss_text and is_defined_risk:
                    parts.append(f"Maximum loss is {max_loss_text}.")
                if max_profit_text and is_capped_profit:
                    parts.append(f"Maximum profit is {max_profit_text}.")
            else:
                if max_profit_text and is_capped_profit:
                    parts.append(f"Maximum profit is {max_profit_text}.")
                if roi_text and anchor_text:
                    parts.append(f"ROI at {anchor_text} is {roi_text}.")
            if parts:
                return " ".join(parts)
            return None

        if is_credit:
            if kind == "base" and premium_sentence:
                parts.append(strip_period(premium_sentence))
            if kind in {"bear", "bull"} and max_loss_text and is_defined_risk:
                parts.append(f"Maximum loss is {max_loss_text}.")
            if include_breakeven and breakeven_text:
                parts.append(f"Breakeven is around {breakeven_text}.")
            if parts:
                return " ".join(parts)

        if kind == "base" and max_profit_text and not is_debit:
            parts.append(f"Maximum profit is {max_profit_text}.")
        if kind in {"bear", "bull"} and max_loss_text and is_defined_risk:
            parts.append(f"Maximum loss is {max_loss_text}.")
        if include_breakeven and breakeven_text:
            parts.append(f"Breakeven is around {breakeven_text}.")
        if roi_text and anchor_text and kind != "base":
            parts.append(f"ROI at {anchor_text} is {roi_text}.")
        if not parts and pnl_sentence:
            parts.append(strip_period(pnl_sentence))
        if parts:
            return " ".join(parts)
        return None
    if family == "covered_call":
        if kind in {"bear", "base"} and premium_sentence:
            return premium_sentence
        if kind in {"base", "bull"} and max_profit_text:
            return f"Maximum combined profit (at expiry): {max_profit_text}."
        return pnl_sentence or premium_sentence
    if family == "protective_put":
        if kind == "bear" and max_loss_text and not is_partial:
            return f"Maximum combined loss (at expiry): {max_loss_text}."
        if kind == "base" and premium_sentence:
            return premium_sentence
        return pnl_sentence or premium_sentence
    if family == "collar":
        if kind == "bear" and max_loss_text and not is_partial:
            return f"Maximum combined loss (at expiry): {max_loss_text}."
        if kind == "bull" and max_profit_text and not is_partial:
            return f"Maximum combined profit (at expiry): {max_profit_text}."
        if kind == "base" and premium_sentence:
            return premium_sentence
        return pnl_sentence or premium_sentence
    if family == "condor":
        if kind == "base" and max_profit_text:
            return f"Maximum profit: {max_profit_text}."
        if kind in {"bear", "bull"} and max_loss_text:
            return f"Maximum loss: {max_loss_text}."
        return pnl_sentence or premium_sentence
    if premium_sentence:
        return premium_sentence
    return pnl_sentence or None


def _resolve_family(
    context: Mapping[str, object],
    selected_rule: Optional[Mapping[str, object]] = None,
) -> str:
    if selected_rule and selected_rule.get("strategy_family"):
        family = str(selected_rule.get("strategy_family")).lower()
        if "condor" in family:
            return "condor"
        if "covered" in family:
            return "covered_call"
        if "protective" in family:
            return "protective_put"
        if "collar" in family:
            return "collar"
        return family
    classification = context.get("classification")
    if classification == "CCOV":
        return "covered_call"
    if classification == "PPRT":
        return "protective_put"
    if classification == "COL_EQ":
        return "collar"
    if context.get("iron_condor"):
        return "condor"
    return "generic"


def _strike_condition(
    kind: str,
    lower_bound: Optional[float],
    upper_bound: Optional[float],
    spot_price: Optional[float],
) -> str:
    if kind == "bear":
        if lower_bound is not None:
            return f"If stock falls below {_format_price(lower_bound)}"
        if spot_price is not None:
            return f"If stock falls below {_format_price(spot_price)}"
    if kind == "bull":
        if upper_bound is not None:
            return f"If stock rises above {_format_price(upper_bound)}"
        if spot_price is not None:
            return f"If stock rises above {_format_price(spot_price)}"
    if lower_bound is not None and upper_bound is not None:
        low = min(lower_bound, upper_bound)
        high = max(lower_bound, upper_bound)
        return (
            f"If stock stays between {_format_price(low)} and {_format_price(high)}"
        )
    if spot_price is not None and lower_bound is not None:
        low = min(spot_price, lower_bound)
        high = max(spot_price, lower_bound)
        return (
            f"If stock stays between {_format_price(low)} and {_format_price(high)}"
        )
    if spot_price is not None and upper_bound is not None:
        low = min(spot_price, upper_bound)
        high = max(spot_price, upper_bound)
        return (
            f"If stock stays between {_format_price(low)} and {_format_price(high)}"
        )
    if spot_price is not None:
        return f"If stock stays near {_format_price(spot_price)}"
    if lower_bound is not None:
        return f"If stock stays near {_format_price(lower_bound)}"
    if upper_bound is not None:
        return f"If stock stays near {_format_price(upper_bound)}"
    return "Key level unavailable"


def _compute_overlay_coverage(analysis_pack: Mapping[str, object]) -> dict:
    coverage = {
        "has_stock_position": False,
        "shares": 0,
        "covered_shares_call": None,
        "protected_shares_put": None,
        "collared_shares": None,
        "coverage_ratio": None,
        "coverage_phrase": None,
        "coverage_clause": None,
        "coverage_scope": None,
        "contract_count": None,
        "is_partial": False,
    }
    if not isinstance(analysis_pack, Mapping):
        return coverage
    key_levels = analysis_pack.get("key_levels")
    meta = {}
    if isinstance(key_levels, Mapping):
        meta = key_levels.get("meta") if isinstance(key_levels.get("meta"), Mapping) else key_levels
    has_stock = bool(meta.get("has_stock_position", False))
    shares_value = meta.get("shares")
    if shares_value is None:
        shares_value = analysis_pack.get("shares")
    strategy_input = analysis_pack.get("strategy_input")
    if shares_value is None and isinstance(strategy_input, StrategyInput):
        shares_value = abs(strategy_input.stock_position)
        has_stock = bool(strategy_input.stock_position)
    shares = _to_float(shares_value)
    if shares is None or shares <= 0:
        coverage["has_stock_position"] = has_stock
        return coverage
    shares_int = int(round(abs(shares)))
    coverage["has_stock_position"] = has_stock
    coverage["shares"] = shares_int
    if not has_stock:
        return coverage

    legs_data = analysis_pack.get("legs")
    if not isinstance(legs_data, list) and isinstance(strategy_input, StrategyInput):
        legs_data = [
            {
                "kind": leg.kind,
                "side": "Short" if leg.position < 0 else "Long",
                "ratio": abs(leg.position),
                "multiplier": leg.multiplier,
            }
            for leg in strategy_input.legs
        ]

    short_call_contracts = 0.0
    long_put_contracts = 0.0
    if isinstance(legs_data, list):
        for leg in legs_data:
            if not isinstance(leg, Mapping):
                continue
            kind = str(leg.get("kind") or leg.get("type") or "").lower()
            side = str(leg.get("side") or "").lower()
            ratio = _to_float(leg.get("ratio")) or 0.0
            multiplier = _to_float(leg.get("multiplier")) or 100.0
            position = leg.get("position")
            if kind == "":
                continue
            if position is not None and _to_float(position) is not None:
                side = "short" if _to_float(position) < 0 else "long"
                ratio = abs(_to_float(position))
            if kind == "call" and ("short" in side):
                short_call_contracts += ratio
                coverage["covered_shares_call"] = int(
                    round(short_call_contracts * multiplier)
                )
            if kind == "put" and ("long" in side):
                long_put_contracts += ratio
                coverage["protected_shares_put"] = int(
                    round(long_put_contracts * multiplier)
                )

    covered_shares = coverage.get("covered_shares_call") or 0
    protected_shares = coverage.get("protected_shares_put") or 0
    collared_shares = None
    if covered_shares and protected_shares:
        collared_shares = min(covered_shares, protected_shares, shares_int)
        coverage["collared_shares"] = collared_shares
    coverage_shares = None
    contract_count = None
    coverage_scope = "the shares"
    if collared_shares:
        coverage_scope = "the collared shares"
        coverage_shares = collared_shares
        contract_count = int(round(min(short_call_contracts, long_put_contracts)))
    elif covered_shares:
        coverage_scope = "the covered shares"
        coverage_shares = min(covered_shares, shares_int)
        contract_count = int(round(short_call_contracts)) if short_call_contracts else None
    elif protected_shares:
        coverage_scope = "the protected shares"
        coverage_shares = min(protected_shares, shares_int)
        contract_count = int(round(long_put_contracts)) if long_put_contracts else None

    if coverage_shares:
        coverage["coverage_ratio"] = coverage_shares / shares_int
        coverage["contract_count"] = contract_count
        ratio = coverage["coverage_ratio"]
        coverage["is_partial"] = ratio is not None and 0 < ratio < 0.99
        pct = int(round(ratio * 100)) if ratio is not None else None
        if ratio is not None and ratio >= 0.99:
            coverage_clause = (
                f"the full position ({shares_int:,} of {shares_int:,} shares)"
            )
            coverage["coverage_phrase"] = f"This overlay applies to {coverage_clause}."
            coverage["coverage_clause"] = coverage_clause
            coverage["coverage_scope"] = coverage_scope
        else:
            coverage_clause = (
                f"~{pct}% of the position "
                f"({coverage_shares:,} of {shares_int:,} shares)"
            )
            coverage["coverage_phrase"] = f"This overlay applies to {coverage_clause}."
            coverage["coverage_clause"] = coverage_clause
            coverage["coverage_scope"] = coverage_scope
    elif has_stock:
        coverage_clause = f"the position ({shares_int:,} shares)"
        coverage["coverage_phrase"] = f"This overlay applies to {coverage_clause}."
        coverage["coverage_clause"] = coverage_clause
        coverage["coverage_scope"] = "the shares"
    return coverage


def _build_narrative_context(analysis_pack: Mapping[str, object]) -> dict:
    context = {
        "has_stock_position": False,
        "shares": 0,
        "overlay_type": "none",
        "coverage_ratio": None,
        "coverage_clause": None,
        "coverage_scope": None,
        "is_partial": False,
        "contract_count": None,
        "is_credit": None,
        "is_debit": None,
        "option_structure": "mixed",
        "is_capped_profit": False,
        "is_defined_risk": False,
    }
    if not isinstance(analysis_pack, Mapping):
        return context

    key_levels = analysis_pack.get("key_levels")
    meta = {}
    if isinstance(key_levels, Mapping):
        meta = key_levels.get("meta") if isinstance(key_levels.get("meta"), Mapping) else key_levels
    strategy_input = analysis_pack.get("strategy_input")
    has_stock = bool(meta.get("has_stock_position", False))
    shares_value = meta.get("shares")
    if shares_value is None and isinstance(strategy_input, StrategyInput):
        shares_value = abs(strategy_input.stock_position)
        has_stock = bool(strategy_input.stock_position)
    shares = _to_float(shares_value)
    context["has_stock_position"] = has_stock
    if shares is not None:
        context["shares"] = int(round(abs(shares)))

    coverage_context = _compute_overlay_coverage(analysis_pack)
    context["coverage_ratio"] = coverage_context.get("coverage_ratio")
    context["coverage_clause"] = coverage_context.get("coverage_clause")
    context["coverage_scope"] = coverage_context.get("coverage_scope")
    context["is_partial"] = bool(coverage_context.get("is_partial"))
    inferred_contracts = _infer_contract_count(analysis_pack)
    context["contract_count"] = coverage_context.get("contract_count") or inferred_contracts
    if not has_stock:
        context["coverage_ratio"] = None
        context["coverage_clause"] = None
        context["coverage_scope"] = None
        context["is_partial"] = False

    legs_data = []
    if isinstance(strategy_input, StrategyInput):
        for leg in strategy_input.legs:
            legs_data.append(
                {
                    "kind": leg.kind,
                    "position": leg.position,
                    "side": "Short" if leg.position < 0 else "Long",
                }
            )
    elif isinstance(analysis_pack.get("legs"), list):
        legs_data = analysis_pack.get("legs")

    has_calls = False
    has_puts = False
    has_short_call = False
    has_long_call = False
    has_short_put = False
    has_long_put = False
    for leg in legs_data:
        if not isinstance(leg, Mapping):
            continue
        kind = str(leg.get("kind") or leg.get("type") or "").lower()
        side = str(leg.get("side") or "").lower()
        position = _to_float(leg.get("position"))
        if position is not None:
            side = "short" if position < 0 else "long"
        if kind == "call":
            has_calls = True
            if "short" in side:
                has_short_call = True
            if "long" in side:
                has_long_call = True
        if kind == "put":
            has_puts = True
            if "short" in side:
                has_short_put = True
            if "long" in side:
                has_long_put = True

    if has_stock:
        if has_short_call and has_long_put:
            context["overlay_type"] = "collar"
        elif has_short_call:
            context["overlay_type"] = "covered_call"
        elif has_long_put:
            context["overlay_type"] = "protective_put"

    option_structure = "mixed"
    if not has_stock:
        if has_calls and not has_puts:
            if has_short_call and has_long_call:
                option_structure = "call_spread"
            elif has_short_call:
                option_structure = "short_call"
            elif has_long_call:
                option_structure = "long_call"
        elif has_puts and not has_calls:
            if has_short_put and has_long_put:
                option_structure = "put_spread"
            elif has_short_put:
                option_structure = "short_put"
            elif has_long_put:
                option_structure = "long_put"
        elif has_calls and has_puts:
            if has_short_call and has_long_call and has_short_put and has_long_put:
                option_structure = "condor"
            else:
                option_structure = "mixed"
    context["option_structure"] = option_structure

    summary_rows = analysis_pack.get("summary_rows")
    if summary_rows is None:
        summary = analysis_pack.get("summary")
        if isinstance(summary, Mapping):
            summary_rows = summary.get("rows")

    cost_credit = None
    if isinstance(summary_rows, list):
        for row in summary_rows:
            if not isinstance(row, Mapping):
                continue
            if row.get("metric") == "Cost/Credit":
                cost_credit = row.get("options") or row.get("combined")
                break
    if isinstance(cost_credit, str):
        lowered = cost_credit.lower()
        if "credit" in lowered:
            context["is_credit"] = True
            context["is_debit"] = False
        elif "debit" in lowered:
            context["is_credit"] = False
            context["is_debit"] = True

    if context["is_credit"] is None and context["is_debit"] is None:
        net_premium = _summary_metric(summary_rows, "Net Prem/Share", prefer="options")
        if net_premium is not None:
            context["is_credit"] = net_premium < 0
            context["is_debit"] = net_premium > 0

    max_profit = _summary_metric(summary_rows, "Max Profit", prefer="options")
    max_loss = _summary_metric(summary_rows, "Max Loss", prefer="options")
    context["is_defined_risk"] = max_loss is not None
    context["is_capped_profit"] = (
        not has_stock
        and option_structure in {"call_spread", "put_spread", "condor"}
        and max_profit is not None
    )
    return context


def _fallback_condition(
    kind: str,
    lower_price: Optional[float],
    upper_price: Optional[float],
    spot_price: Optional[float],
) -> str:
    return _strike_condition(kind, lower_price, upper_price, spot_price)


def _fallback_body(
    kind: str,
    lower_long_price: Optional[float],
    upper_long_price: Optional[float],
    pnl_sentence: str,
    has_short_strikes: bool,
) -> str:
    if has_short_strikes:
        if kind == "bear":
            base = "Below the lower strike, losses typically increase toward the hedge strike."
            if lower_long_price is not None:
                base = (
                    "Below the lower strike, losses typically increase toward the hedge strike "
                    f"({_format_price(lower_long_price)})."
                )
        elif kind == "bull":
            base = "Above the upper strike, losses typically increase toward the hedge strike."
            if upper_long_price is not None:
                base = (
                    "Above the upper strike, losses typically increase toward the hedge strike "
                    f"({_format_price(upper_long_price)})."
                )
        else:
            base = "Between the strikes, the strategy seeks to perform best."
    else:
        if kind == "bear":
            base = "Below the key strike, losses can increase."
        elif kind == "bull":
            base = "Above the key strike, losses can increase."
        else:
            base = "Within the key range, the strategy seeks to perform best."
    if pnl_sentence:
        return f"{base} {pnl_sentence}".strip()
    return base


def _build_fallback_narratives_from_key_levels(
    levels: List[Mapping[str, object]],
    strategy_input: StrategyInput,
    summary_rows: Optional[List[Mapping[str, object]]],
    context: Mapping[str, object],
) -> Dict[str, object]:
    label_lookup = _levels_by_label(levels)
    strike_levels = _strike_levels(levels)
    lower_short, upper_short = _short_strike_bounds(strike_levels)
    breakeven_levels = _breakeven_levels(levels)
    lower_long = _find_level(
        label_lookup, ["Strike (Lowest)", "Lower Strike", "Strike Lowest"]
    )
    upper_long = _find_level(
        label_lookup, ["Strike (Highest)", "Upper Strike", "Strike Highest"]
    )
    spot_level = _find_level(label_lookup, ["Current Market Price", "Spot"])
    has_stock = bool(context.get("has_stock_position", strategy_input.stock_position != 0))

    lower_short_price = _to_float(lower_short.get("price")) if lower_short else None
    upper_short_price = _to_float(upper_short.get("price")) if upper_short else None
    lower_long_price = _to_float(lower_long.get("price")) if lower_long else None
    upper_long_price = _to_float(upper_long.get("price")) if upper_long else None
    spot_price = _to_float(spot_level.get("price")) if spot_level else None
    breakeven_min = (
        _to_float(breakeven_levels[0].get("price")) if breakeven_levels else None
    )

    if lower_short is None and strike_levels:
        lower_short = strike_levels[0]
        lower_short_price = _to_float(lower_short.get("price"))
    if upper_short is None and strike_levels:
        upper_short = strike_levels[-1]
        upper_short_price = _to_float(upper_short.get("price"))

    family = _resolve_family(context, None)
    narrative_ctx = _build_narrative_context(
        {
            "key_levels": {"meta": {"has_stock_position": has_stock, "shares": strategy_input.stock_position}},
            "strategy_input": strategy_input,
            "summary_rows": summary_rows,
        }
    )
    premium_ctx = _premium_context(
        strategy_input,
        summary_rows,
        contract_count=narrative_ctx.get("contract_count"),
        is_credit=narrative_ctx.get("is_credit"),
        is_debit=narrative_ctx.get("is_debit"),
    )
    prefer = "combined" if has_stock else "options"
    max_profit = _summary_metric(summary_rows, "Max Profit", prefer=prefer)
    max_loss = _summary_metric(summary_rows, "Max Loss", prefer=prefer)
    coverage_clause = (
        narrative_ctx.get("coverage_clause") if has_stock else None
    ) or ""
    coverage_scope = (
        narrative_ctx.get("coverage_scope") if has_stock else None
    ) or ("the shares" if has_stock else "")
    is_partial = bool(narrative_ctx.get("is_partial")) if has_stock else False

    is_credit = narrative_ctx.get("is_credit")
    is_debit = narrative_ctx.get("is_debit")
    option_structure = narrative_ctx.get("option_structure", "mixed")

    coverage_tail_bull = ""
    coverage_tail_bear = ""
    if has_stock and is_partial:
        if family in {"covered_call", "collar"}:
            coverage_tail_bull = " Uncovered shares continue to participate."
        if family in {"protective_put", "collar"}:
            coverage_tail_bear = " Unprotected shares still participate in downside."

    def _fallback_base_body(kind: str) -> str:
        if has_stock:
            coverage_text = f" for {coverage_clause}" if coverage_clause else ""
            if kind == "bear":
                anchor = lower_short_price or spot_price
                anchor_text = _format_price(anchor) if anchor is not None else "the key level"
                opener = f"Below {anchor_text}, downside is the focus{coverage_text}."
            elif kind == "bull":
                anchor = upper_short_price or spot_price
                anchor_text = _format_price(anchor) if anchor is not None else "the key level"
                opener = f"Above {anchor_text}, upside is the focus{coverage_text}."
            else:
                low = lower_short_price or spot_price
                high = upper_short_price or spot_price
                if low is not None and high is not None:
                    opener = (
                        f"Between {_format_price(min(low, high))} and {_format_price(max(low, high))}, "
                        f"outcomes are stock-driven{coverage_text}."
                    )
                else:
                    opener = "Around current levels, outcomes are stock-driven."

            if family == "covered_call":
                strike_text = _format_price(upper_short_price) if upper_short_price is not None else "the call strike"
                if kind == "bear":
                    mechanics = (
                        f"At expiry below {strike_text}, the call expires worthless on {coverage_scope}."
                    )
                elif kind == "bull":
                    mechanics = (
                        f"At expiry above {strike_text}, shares may be called away at the strike and upside is capped on {coverage_scope}.{coverage_tail_bull}"
                    )
                else:
                    mechanics = (
                        f"At expiry between { _format_price(spot_price) if spot_price is not None else strike_text } and {strike_text}, "
                        f"the call expires worthless on {coverage_scope}."
                    )
                return _join_sentences([opener, mechanics])

            if family == "protective_put":
                strike_text = _format_price(lower_short_price) if lower_short_price is not None else "the put strike"
                if kind == "bear":
                    mechanics = (
                        f"At expiry below {strike_text}, the put settles at intrinsic value and downside is protected on {coverage_scope}.{coverage_tail_bear}"
                    )
                elif kind == "bull":
                    mechanics = (
                        f"At expiry above {_format_price(spot_price) if spot_price is not None else strike_text}, "
                        f"the put expires worthless and gains follow the shares on {coverage_scope}."
                    )
                else:
                    mechanics = (
                        f"At expiry between {strike_text} and {_format_price(spot_price) if spot_price is not None else strike_text}, "
                        f"protection remains in place on {coverage_scope}."
                    )
                return _join_sentences([opener, mechanics])

            if family == "collar":
                put_text = _format_price(lower_short_price) if lower_short_price is not None else "the put strike"
                call_text = _format_price(upper_short_price) if upper_short_price is not None else "the call strike"
                if kind == "bear":
                    mechanics = (
                        f"At expiry below {put_text}, downside is protected on {coverage_scope}.{coverage_tail_bear}"
                    )
                elif kind == "bull":
                    mechanics = (
                        f"At expiry above {call_text}, shares may be called away at the strike and upside is capped on {coverage_scope}.{coverage_tail_bull}"
                    )
                else:
                    mechanics = (
                        f"At expiry between {put_text} and {call_text}, the put expires worthless and the call stays out of the money; "
                        f"the call stays out of the money on {coverage_scope}."
                    )
                return _join_sentences([opener, mechanics])

            mechanics = (
                "At expiry, option payoffs settle to intrinsic value and are applied to the shares."
            )
            return _join_sentences([opener, mechanics])
        has_short_strikes = lower_short_price is not None and upper_short_price is not None
        opener = "Around the key level, the range is defined by the strikes."
        if has_short_strikes:
            if kind == "bear":
                opener = f"Below {_format_price(lower_short_price)}, downside is the focus."
            elif kind == "bull":
                opener = f"Above {_format_price(upper_short_price)}, upside is the focus."
            else:
                opener = (
                    f"Between {_format_price(lower_short_price)} and {_format_price(upper_short_price)}, "
                    "the range is defined by the strikes."
                )
        if option_structure in {"call_spread", "put_spread"} and has_short_strikes:
            lower_text = _format_price(lower_short_price) if lower_short_price is not None else "--"
            upper_text = _format_price(upper_short_price) if upper_short_price is not None else "--"
            if option_structure == "call_spread":
                if is_debit:
                    if kind == "bear":
                        mechanics = (
                            f"At expiry below {lower_text}, both calls expire worthless."
                        )
                    elif kind == "bull":
                        mechanics = (
                            f"At expiry above {upper_text}, gains are capped at maximum profit."
                        )
                    else:
                        mechanics = (
                            f"At expiry between {lower_text} and {upper_text}, intrinsic value builds toward maximum profit."
                        )
                else:
                    if kind == "bull":
                        mechanics = (
                            "At expiry above the short strike, losses increase toward the hedge strike."
                        )
                        if upper_long_price is not None:
                            mechanics = (
                                "At expiry above the short strike, losses increase toward the hedge strike "
                                f"({_format_price(upper_long_price)})."
                            )
                    else:
                        mechanics = (
                            f"At expiry below {lower_text}, the spread seeks to retain the net credit."
                            if kind == "bear"
                            else f"At expiry between {lower_text} and {upper_text}, the spread seeks to retain the net credit."
                        )
                return _join_sentences([opener, mechanics])
            if option_structure == "put_spread":
                if is_debit:
                    if kind == "bear":
                        mechanics = (
                            f"At expiry below {lower_text}, gains are capped at maximum profit."
                        )
                    elif kind == "bull":
                        mechanics = (
                            f"At expiry above {upper_text}, both puts expire worthless."
                        )
                    else:
                        mechanics = (
                            f"At expiry between {lower_text} and {upper_text}, intrinsic value builds toward maximum profit."
                        )
                else:
                    if kind == "bear":
                        mechanics = (
                            "At expiry below the short strike, losses increase toward the hedge strike."
                        )
                        if lower_long_price is not None:
                            mechanics = (
                                "At expiry below the short strike, losses increase toward the hedge strike "
                                f"({_format_price(lower_long_price)})."
                            )
                    else:
                        mechanics = (
                            f"At expiry above {upper_text}, the spread seeks to retain the net credit."
                            if kind == "bull"
                            else f"At expiry between {lower_text} and {upper_text}, the spread seeks to retain the net credit."
                        )
                return _join_sentences([opener, mechanics])

        if has_short_strikes:
            if kind == "bear":
                mechanics = "At expiry below the lower strike, losses increase toward the hedge strike."
                if lower_long_price is not None:
                    mechanics = (
                        "At expiry below the lower strike, losses increase toward the hedge strike "
                        f"({_format_price(lower_long_price)})."
                    )
            elif kind == "bull":
                mechanics = "At expiry above the upper strike, losses increase toward the hedge strike."
                if upper_long_price is not None:
                    mechanics = (
                        "At expiry above the upper strike, losses increase toward the hedge strike "
                        f"({_format_price(upper_long_price)})."
                    )
            else:
                if is_debit:
                    mechanics = "At expiry between the strikes, intrinsic value builds toward maximum profit."
                else:
                    mechanics = "At expiry between the strikes, the strategy seeks to retain the net credit."
            return _join_sentences([opener, mechanics])

        if kind == "bear":
            mechanics = "At expiry below the key level, losses can increase."
        elif kind == "bull":
            mechanics = "At expiry above the key level, losses can increase."
        else:
            mechanics = "At expiry within the key range, the strategy seeks to perform best."
        return _join_sentences([opener, mechanics])

    anchors_used: dict[str, list[dict]] = {}
    scenarios: dict[str, object] = {}
    for kind, title in [
        ("bear", "Bearish Case"),
        ("base", "Stagnant Case"),
        ("bull", "Bullish Case"),
    ]:
        if kind == "bear":
            anchor = lower_short or spot_level
        elif kind == "bull":
            anchor = upper_short or spot_level
        else:
            anchor = spot_level or lower_short or upper_short
        anchor_list = [anchor] if anchor is not None else []
        anchors_used[kind] = [
            {"label": row.get("label"), "price": row.get("price")}
            for row in anchor_list
            if isinstance(row, Mapping)
        ]
        condition = _fallback_condition(
            kind, lower_short_price, upper_short_price, spot_price
        )
        pnl_sentence = _pnl_sentence(anchor, has_stock, _to_float(anchor.get("price")) if isinstance(anchor, Mapping) else None)
        roi_value = _level_value(anchor, ["net_roi", "Net ROI", "option_roi", "Option ROI"])
        include_breakeven = kind == "base" and breakeven_min is not None
        numbers_sentence = _numbers_sentence(
            kind,
            family,
            has_stock,
            premium_ctx,
            max_profit,
            max_loss,
            pnl_sentence,
            is_partial,
            roi_value,
            breakeven_min,
            include_breakeven,
            _to_float(anchor.get("price")) if isinstance(anchor, Mapping) else None,
            narrative_ctx.get("is_credit") if isinstance(narrative_ctx, Mapping) else None,
            narrative_ctx.get("is_debit") if isinstance(narrative_ctx, Mapping) else None,
            narrative_ctx.get("option_structure") if isinstance(narrative_ctx, Mapping) else "mixed",
            bool(narrative_ctx.get("is_capped_profit")) if isinstance(narrative_ctx, Mapping) else False,
            bool(narrative_ctx.get("is_defined_risk")) if isinstance(narrative_ctx, Mapping) else False,
        )
        overlay_pnl = _level_value(anchor, ["net_pnl", "Net PnL", "combined_pnl"])
        price = _to_float(anchor.get("price")) if isinstance(anchor, Mapping) else None
        stock_only_pnl = None
        if has_stock:
            stock_only_pnl = _level_value(anchor, ["stock_pnl", "Stock PnL"])
            if stock_only_pnl is None and price is not None:
                stock_only_pnl = (
                    strategy_input.stock_position * (price - strategy_input.avg_cost)
                )
        else:
            stock_only_pnl = 0.0
        delta_vs_stock = None
        if overlay_pnl is not None and stock_only_pnl is not None:
            delta_vs_stock = overlay_pnl - stock_only_pnl
        breakdown_present = _has_breakdown_data(anchor, has_stock)
        overlay_sentence = (
            _overlay_sentence(kind, delta_vs_stock)
            if has_stock and not breakdown_present
            else None
        )
        base_body = _fallback_base_body(kind)
        body = _join_sentences(
            [base_body, overlay_sentence or "", numbers_sentence or ""]
        )
        scenarios[kind] = {
            "title": title,
            "condition": condition,
            "body": body,
            "anchors": [
                {
                    "label": row.get("label"),
                    "price": row.get("price"),
                }
                for row in anchor_list
                if isinstance(row, Mapping)
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
            "rule_id": "fallback_generic",
            "version": "fallback_v2",
            "reason": "fallback_used_no_matching_rule",
            "anchors_used": anchors_used,
            "coverage": narrative_ctx,
        },
    }


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
    narrative_ctx = _build_narrative_context(
        {
            "key_levels": key_levels,
            "strategy_input": strategy_input,
            "summary_rows": summary_rows,
        }
    )
    context["is_credit"] = narrative_ctx.get("is_credit")
    context["is_debit"] = narrative_ctx.get("is_debit")
    context["option_structure"] = narrative_ctx.get("option_structure")

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
        fallback = _build_fallback_narratives_from_key_levels(
            levels,
            strategy_input,
            summary_rows,
            context,
        )
        trace = fallback.get("trace", {})
        trace = dict(trace)
        trace["matched_conditions"] = []
        trace["inputs_used"] = inputs_used
        trace["coverage"] = narrative_ctx
        fallback["trace"] = trace
        return fallback

    spot_level = _find_level(label_lookup, ["Current Market Price", "Spot"])
    lower_long = _find_level(
        label_lookup, ["Strike (Lowest)", "Lower Strike", "Strike Lowest"]
    )
    upper_long = _find_level(
        label_lookup, ["Strike (Highest)", "Upper Strike", "Strike Highest"]
    )

    strike_levels = _strike_levels(levels)
    lower_short, upper_short = _short_strike_bounds(strike_levels)
    lower_strike = strike_levels[0] if strike_levels else None
    upper_strike = strike_levels[-1] if strike_levels else None
    breakeven_levels = _breakeven_levels(levels)

    spot_price = _to_float(spot_level.get("price")) if spot_level else None
    lower_short_price = _to_float(lower_short.get("price")) if lower_short else None
    upper_short_price = _to_float(upper_short.get("price")) if upper_short else None
    lower_long_price = _to_float(lower_long.get("price")) if lower_long else None
    upper_long_price = _to_float(upper_long.get("price")) if upper_long else None
    lower_strike_price = _to_float(lower_strike.get("price")) if lower_strike else None
    upper_strike_price = _to_float(upper_strike.get("price")) if upper_strike else None
    breakeven_min = (
        _to_float(breakeven_levels[0].get("price")) if breakeven_levels else None
    )
    breakeven_max = (
        _to_float(breakeven_levels[-1].get("price")) if breakeven_levels else None
    )

    cap_strike_price = _pick_leg_strike(legs, "call", -1, "min")
    if cap_strike_price is None:
        cap_strike_price = upper_short_price or upper_strike_price or lower_short_price
    put_strike_price = _pick_leg_strike(legs, "put", 1, "max")
    if put_strike_price is None:
        put_strike_price = lower_short_price or lower_long_price or lower_strike_price

    prefer = "combined" if has_stock else "options"
    max_profit = _summary_metric(summary_rows, "Max Profit", prefer=prefer)
    max_loss = _summary_metric(summary_rows, "Max Loss", prefer=prefer)
    premium_ctx = _premium_context(
        strategy_input,
        summary_rows,
        contract_count=narrative_ctx.get("contract_count"),
        is_credit=narrative_ctx.get("is_credit"),
        is_debit=narrative_ctx.get("is_debit"),
    )

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
    family = _resolve_family(context, selected_rule)
    coverage_clause = (
        narrative_ctx.get("coverage_clause") if has_stock else None
    ) or ""
    coverage_scope = (
        narrative_ctx.get("coverage_scope") if has_stock else None
    ) or ("the shares" if has_stock else "")
    is_partial = bool(narrative_ctx.get("is_partial")) if has_stock else False
    cap_phrase = "partially capped" if is_partial else "capped"
    protection_phrase = "partially protected" if is_partial else "protected"
    coverage_tail_bull = ""
    coverage_tail_bear = ""
    if has_stock and is_partial:
        if family in {"covered_call", "collar"}:
            coverage_tail_bull = " Uncovered shares continue to participate."
        if family in {"protective_put", "collar"}:
            coverage_tail_bear = " Unprotected shares still participate in downside."

    is_credit = narrative_ctx.get("is_credit")
    is_debit = narrative_ctx.get("is_debit")
    option_structure = narrative_ctx.get("option_structure", "mixed")
    is_capped_profit = bool(narrative_ctx.get("is_capped_profit"))
    is_defined_risk = bool(narrative_ctx.get("is_defined_risk"))

    def _level_by_price(target: Optional[float]) -> Optional[Mapping[str, object]]:
        if target is None:
            return None
        for level in levels:
            if not isinstance(level, Mapping):
                continue
            price = _to_float(level.get("price"))
            if price is not None and abs(price - target) <= 1e-6:
                return level
        return None

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

        lower_bound = None
        upper_bound = None
        if has_stock and family == "covered_call":
            lower_bound = spot_price
            upper_bound = cap_strike_price or upper_strike_price
        elif has_stock and family == "protective_put":
            lower_bound = put_strike_price or lower_strike_price
            upper_bound = spot_price
        elif has_stock and family == "collar":
            lower_bound = put_strike_price or lower_strike_price
            upper_bound = cap_strike_price or upper_strike_price
        else:
            lower_bound = (
                lower_short_price
                or lower_strike_price
                or breakeven_min
            )
            upper_bound = (
                upper_short_price
                or upper_strike_price
                or breakeven_max
            )
        condition = _strike_condition(kind, lower_bound, upper_bound, spot_price)

        primary = None
        if has_stock:
            if kind == "bear":
                primary = _level_by_price(put_strike_price) or spot_level
            elif kind == "bull":
                primary = _level_by_price(cap_strike_price) or spot_level
            else:
                primary = spot_level or _level_by_price(put_strike_price) or _level_by_price(cap_strike_price)
        else:
            if kind == "bear":
                primary = _level_by_price(lower_bound) or lower_short or lower_strike
            elif kind == "bull":
                primary = _level_by_price(upper_bound) or upper_short or upper_strike
            else:
                primary = spot_level or _level_by_price(lower_bound) or _level_by_price(upper_bound)
        primary = primary or _pick_primary_anchor(anchors)
        price = _to_float(primary.get("price")) if primary else None
        overlay_pnl = _level_value(primary, ["net_pnl", "Net PnL", "combined_pnl"])
        stock_only_pnl = None
        if has_stock:
            stock_only_pnl = _level_value(primary, ["stock_pnl", "Stock PnL"])
            if stock_only_pnl is None and price is not None:
                stock_only_pnl = (
                    strategy_input.stock_position * (price - strategy_input.avg_cost)
                )
        else:
            stock_only_pnl = 0.0
        delta_vs_stock = (
            overlay_pnl - stock_only_pnl
            if overlay_pnl is not None and stock_only_pnl is not None
            else None
        )
        scenario_pnl_text = _format_signed_currency(overlay_pnl)
        roi_value = _level_value(primary, ["net_roi", "Net ROI", "option_roi", "Option ROI"])
        include_breakeven = kind == "base" and breakeven_min is not None
        context_values = {
            "spot": _format_price(spot_price) if spot_price is not None else "--",
            "anchor_price": _format_price(price) if price is not None else "--",
            "max_profit": max_profit_text or "--",
            "max_loss": max_loss_text or "--",
            "lower_short": _format_price(lower_short_price)
            if lower_short_price is not None
            else "--",
            "upper_short": _format_price(upper_short_price)
            if upper_short_price is not None
            else "--",
            "lower_long": _format_price(lower_long_price)
            if lower_long_price is not None
            else "--",
            "upper_long": _format_price(upper_long_price)
            if upper_long_price is not None
            else "--",
            "cap_strike": _format_price(cap_strike_price)
            if cap_strike_price is not None
            else "--",
            "put_strike": _format_price(put_strike_price)
            if put_strike_price is not None
            else "--",
            "premium_total": _format_currency_abs(premium_ctx.get("total"))
            if premium_ctx.get("total") is not None
            else "--",
            "scenario_pnl": scenario_pnl_text or "--",
            "coverage_clause": coverage_clause,
            "coverage_scope": coverage_scope,
            "cap_phrase": cap_phrase,
            "protection_phrase": protection_phrase,
            "coverage_tail_bear": coverage_tail_bear,
            "coverage_tail_bull": coverage_tail_bull,
        }
        base_body = _render_template(templates.get(kind, ""), context_values).strip()
        if base_body == "--":
            base_body = ""
        pnl_sentence = _pnl_sentence(primary, has_stock, price)
        numbers_sentence = _numbers_sentence(
            kind,
            family,
            has_stock,
            premium_ctx,
            max_profit,
            max_loss,
            pnl_sentence,
            is_partial,
            roi_value,
            breakeven_min,
            include_breakeven,
            price,
            is_credit,
            is_debit,
            option_structure,
            is_capped_profit,
            is_defined_risk,
        )
        breakdown_present = _has_breakdown_data(primary, has_stock)
        overlay_sentence = (
            _overlay_sentence(kind, delta_vs_stock)
            if has_stock and not breakdown_present
            else None
        )
        body = _join_sentences(
            [base_body, overlay_sentence or "", numbers_sentence or ""]
        )
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

    def _missing(scenario: Optional[Mapping[str, object]]) -> bool:
        if not isinstance(scenario, Mapping):
            return True
        condition = scenario.get("condition")
        body = scenario.get("body")
        if _is_missing(condition) or _is_missing(body):
            return True
        return False

    if any(_missing(scenarios.get(key)) for key in ["bear", "base", "bull"]):
        fallback = _build_fallback_narratives_from_key_levels(
            levels,
            strategy_input,
            summary_rows,
            context,
        )
        trace = fallback.get("trace", {})
        trace = dict(trace)
        trace["matched_conditions"] = matched_conditions
        trace["inputs_used"] = inputs_used
        trace["coverage"] = narrative_ctx
        fallback["trace"] = trace
        return fallback

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
            "coverage": narrative_ctx,
        },
    }
