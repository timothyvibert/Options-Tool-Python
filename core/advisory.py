from __future__ import annotations

import math
import re
from pathlib import Path
from typing import Dict, Optional, Tuple

import pandas as pd

from core.margin import (
    CCOV,
    COL_EQ,
    PPRT,
    SH_PUT_CALL,
    classify_strategy,
)
from core.models import StrategyInput
from core.payoff import _compute_pnl_for_price


_ADVISORY_TEMPLATES: Optional[pd.DataFrame] = None


def load_advisory_templates() -> pd.DataFrame:
    global _ADVISORY_TEMPLATES
    if _ADVISORY_TEMPLATES is None:
        path = Path(__file__).resolve().parents[1] / "data" / "scenario_advisory_map.csv"
        _ADVISORY_TEMPLATES = pd.read_csv(path)
    return _ADVISORY_TEMPLATES


def _normalize_archetype(value: object) -> Optional[str]:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return None
    text = str(value).strip()
    if text == "":
        return None
    return text.upper()


def _numeric_strikes(input: StrategyInput) -> list[float]:
    strikes = []
    for leg in input.legs:
        if isinstance(leg.strike, (int, float)) and math.isfinite(leg.strike):
            strikes.append(float(leg.strike))
    return strikes


def _strike_bounds(input: StrategyInput) -> Tuple[Optional[float], Optional[float]]:
    strikes = _numeric_strikes(input)
    if not strikes:
        return None, None
    return min(strikes), max(strikes)


def _format_value(value: Optional[float]) -> str:
    if value is None:
        return "N/A"
    return f"{value:.2f}"


def _single_leg_archetype(input: StrategyInput) -> Optional[str]:
    if len(input.legs) != 1:
        return None
    leg = input.legs[0]
    if leg.kind.lower() == "call":
        return "LONG_CALL" if leg.position > 0 else "SHORT_CALL"
    if leg.kind.lower() == "put":
        return "LONG_PUT" if leg.position > 0 else "SHORT_PUT"
    return None


def _straddle_or_strangle(input: StrategyInput, side: str) -> Optional[str]:
    calls = [leg for leg in input.legs if leg.kind.lower() == "call"]
    puts = [leg for leg in input.legs if leg.kind.lower() == "put"]
    if not calls or not puts:
        return None
    strike_matches = {
        strike for strike in {leg.strike for leg in calls} & {leg.strike for leg in puts}
        if isinstance(strike, (int, float))
    }
    if strike_matches:
        return f"STRADDLE_{side}"
    return f"STRANGLE_{side}"


def resolve_archetype(
    input: StrategyInput, strategy_row: Optional[pd.Series]
) -> str:
    if strategy_row is not None and "archetype" in strategy_row.index:
        archetype = _normalize_archetype(strategy_row.get("archetype"))
        if archetype:
            return archetype

    if not input.legs and input.stock_position != 0:
        return "STOCK_LONG" if input.stock_position > 0 else "STOCK_SHORT"

    calls = [leg for leg in input.legs if leg.kind.lower() == "call"]
    puts = [leg for leg in input.legs if leg.kind.lower() == "put"]
    short_calls = [leg for leg in calls if leg.position < 0]
    long_calls = [leg for leg in calls if leg.position > 0]
    short_puts = [leg for leg in puts if leg.position < 0]
    long_puts = [leg for leg in puts if leg.position > 0]

    if input.stock_position > 0:
        if short_calls and long_puts and not long_calls and not short_puts:
            return "COLLAR"
        if short_calls and not long_calls and not short_puts and not long_puts:
            return "COVERED_CALL"
        if long_puts and not long_calls and not short_calls and not short_puts:
            return "PROTECTIVE_PUT"

    single_leg = _single_leg_archetype(input)
    if single_leg:
        return single_leg

    all_long = input.legs and all(leg.position > 0 for leg in input.legs)
    all_short = input.legs and all(leg.position < 0 for leg in input.legs)
    if all_long:
        straddle = _straddle_or_strangle(input, "LONG")
        if straddle:
            return straddle
    if all_short:
        straddle = _straddle_or_strangle(input, "SHORT")
        if straddle:
            return straddle

    classification = classify_strategy(input)
    classification_map = {
        CCOV: "COVERED_CALL",
        PPRT: "PROTECTIVE_PUT",
        COL_EQ: "COLLAR",
    }
    if classification == SH_PUT_CALL:
        straddle = _straddle_or_strangle(input, "SHORT")
        return straddle or "GENERIC"
    return classification_map.get(classification, "GENERIC")


def compute_scenario_key(
    input: StrategyInput, payoff_result: dict, scenario_price: float
) -> str:
    lower_strike, upper_strike = _strike_bounds(input)
    spot = float(input.spot)
    delta = spot * 0.01
    if delta <= 0:
        delta = 0.01
    pnl_low = _compute_pnl_for_price(input, scenario_price - delta)
    pnl_high = _compute_pnl_for_price(input, scenario_price + delta)
    slope = (pnl_high - pnl_low) / (2 * delta)
    slope_tol = 1e-6

    region = "BETWEEN_BOUNDS"
    if lower_strike is not None and scenario_price < lower_strike:
        region = "BELOW_LOWER_BOUND"
    if upper_strike is not None and scenario_price > upper_strike:
        region = "ABOVE_UPPER_BOUND"

    if lower_strike is None and upper_strike is None:
        if payoff_result.get("unlimited_upside") and slope > slope_tol:
            return "UNLIMITED_UPSIDE"
        if payoff_result.get("unlimited_downside") and slope < -slope_tol:
            return "UNLIMITED_RISK"
        if payoff_result.get("unlimited_loss_upside") and slope < -slope_tol:
            return "UNLIMITED_RISK"
        return region

    if region == "ABOVE_UPPER_BOUND" and payoff_result.get("unlimited_upside"):
        if slope > slope_tol:
            return "UNLIMITED_UPSIDE"
    if region == "ABOVE_UPPER_BOUND" and payoff_result.get("unlimited_loss_upside"):
        if slope < -slope_tol:
            return "UNLIMITED_RISK"
    if region == "BELOW_LOWER_BOUND" and payoff_result.get("unlimited_downside"):
        if slope < -slope_tol:
            return "UNLIMITED_RISK"
    return region


def render_commentary(template: str, context: Dict[str, object]) -> str:
    if template is None:
        return ""

    def replace(match: re.Match) -> str:
        key = match.group(1)
        value = context.get(key)
        if value is None:
            return ""
        return str(value)

    return re.sub(r"\{([^}]+)\}", replace, template)


def select_template(archetype: str, key: str, templates_df: pd.DataFrame) -> str:
    if templates_df.empty:
        return ""

    archetype_key = archetype.strip().upper()
    scenario_key = key.strip().upper()

    def lookup(archetype_value: str, key_value: str) -> Optional[str]:
        match = templates_df[
            (templates_df["archetype"] == archetype_value)
            & (templates_df["scenario_key"] == key_value)
        ]
        if match.empty:
            return None
        return str(match.iloc[0]["template"])

    fallbacks = [
        (archetype_key, scenario_key),
        (archetype_key, "BETWEEN_BOUNDS"),
        ("GENERIC", scenario_key),
        ("GENERIC", "BETWEEN_BOUNDS"),
    ]
    for archetype_value, key_value in fallbacks:
        template = lookup(archetype_value, key_value)
        if template:
            return template
    return ""


def build_commentary_context(
    input: StrategyInput, option_roi: float, net_roi: float
) -> Dict[str, str]:
    lower_strike, upper_strike = _strike_bounds(input)
    strikes = _numeric_strikes(input)
    primary_strike = None
    if strikes:
        primary_strike = min(strikes, key=lambda value: abs(value - input.spot))
    center_strike = None
    if lower_strike is not None and upper_strike is not None:
        center_strike = (lower_strike + upper_strike) / 2.0

    return {
        "Spot": _format_value(float(input.spot)),
        "LowerStrikeFmt": _format_value(lower_strike),
        "UpperStrikeFmt": _format_value(upper_strike),
        "PrimaryStrikeFmt": _format_value(primary_strike),
        "CenterStrikeFmt": _format_value(center_strike),
        "FloorStrikeFmt": _format_value(lower_strike),
        "CapStrikeFmt": _format_value(upper_strike),
        "OptionROI": _format_value(option_roi),
        "NetROI": _format_value(net_roi),
    }
