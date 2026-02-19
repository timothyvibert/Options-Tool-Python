from __future__ import annotations

import math
from typing import Optional

import pandas as pd

from core.advisory import (
    build_commentary_context,
    compute_scenario_key,
    load_advisory_templates,
    render_commentary,
    resolve_archetype,
    select_template,
)
from core.margin import compute_margin_proxy
from core.models import StrategyInput
from core.payoff import _compute_pnl_for_price
from core.roi import NET_PREMIUM, capital_basis, combined_capital_basis


def _price_key(value: float) -> float:
    return round(float(value), 6)


def _unique_sorted(values: list[float]) -> list[float]:
    deduped: list[float] = []
    for value in sorted(values):
        if not deduped or abs(value - deduped[-1]) > 1e-6:
            deduped.append(value)
    return deduped


def _strike_label_map(strikes: list[float]) -> dict[float, str]:
    if not strikes:
        return {}
    ordered = _unique_sorted(strikes)
    if len(ordered) == 1:
        return {ordered[0]: "Strike"}
    if len(ordered) == 2:
        return {ordered[0]: "Lower Strike", ordered[1]: "Upper Strike"}
    if len(ordered) == 4:
        return {
            ordered[0]: "Strike (Lowest)",
            ordered[1]: "Strike (Lower Middle)",
            ordered[2]: "Strike (Upper Middle)",
            ordered[3]: "Strike (Highest)",
        }
    labels = {ordered[0]: "Strike (Lowest)", ordered[-1]: "Strike (Highest)"}
    for strike in ordered[1:-1]:
        labels[strike] = "Strike (Middle)"
    return labels


def _breakeven_label_map(breakevens: list[float]) -> dict[float, str]:
    labels: dict[float, str] = {}
    ordered = _unique_sorted(breakevens)
    for idx, value in enumerate(ordered, start=1):
        labels[value] = f"Breakeven {idx}"
    return labels


def _move_label(prefix: str, spot: float, price: float) -> str:
    if spot == 0:
        return f"{prefix} (--%)"
    pct = abs((price / spot - 1.0) * 100.0)
    return f"{prefix} ({int(round(pct))}%)"


def _scenario_fallback_label(price: float) -> str:
    return f"Scenario @ {price:.2f}"


def build_scenario_points(
    input: StrategyInput,
    payoff_result: dict,
    mode: str,
    downside_tgt: float = 0.8,
    upside_tgt: float = 1.2,
) -> list[float]:
    points = set()
    spot = float(input.spot)
    points.add(spot)

    if input.stock_position != 0:
        points.add(float(input.avg_cost))

    for leg in input.legs:
        strike = leg.strike
        if isinstance(strike, (int, float)) and math.isfinite(strike):
            points.add(float(strike))

    for breakeven in payoff_result.get("breakevens", []):
        if isinstance(breakeven, (int, float)) and math.isfinite(breakeven):
            points.add(float(breakeven))

    if mode.upper() == "INFINITY":
        points.add(0.0)
        points.add(spot * 1000.0)
    else:
        points.add(spot * float(downside_tgt))
        points.add(spot * float(upside_tgt))

    return sorted(points)


def compute_scenario_table(
    input: StrategyInput,
    points: list[float],
    payoff_result: dict,
    roi_policy: str = NET_PREMIUM,
    strategy_row: Optional[pd.Series] = None,
    downside_tgt: Optional[float] = None,
    upside_tgt: Optional[float] = None,
) -> pd.DataFrame:
    option_only = StrategyInput(
        spot=input.spot,
        stock_position=0.0,
        avg_cost=0.0,
        legs=input.legs,
    )
    option_basis = capital_basis(input, payoff_result, roi_policy)
    total_basis = combined_capital_basis(input, option_basis)
    margin_requirement = compute_margin_proxy(input, payoff_result)
    templates_df = load_advisory_templates()
    archetype = resolve_archetype(input, strategy_row)
    spot = float(input.spot)
    strike_values = []
    for leg in input.legs:
        strike = leg.strike
        if isinstance(strike, (int, float)) and math.isfinite(strike):
            strike_values.append(float(strike))
    strike_labels = _strike_label_map(strike_values)
    breakeven_labels = _breakeven_label_map(
        [
            float(value)
            for value in payoff_result.get("breakevens", [])
            if isinstance(value, (int, float)) and math.isfinite(value)
        ]
    )
    label_map: dict[float, str] = {}
    for strike, label in strike_labels.items():
        label_map[_price_key(strike)] = label
    for breakeven, label in breakeven_labels.items():
        label_map[_price_key(breakeven)] = label
    if downside_tgt is not None:
        ds_price = spot * downside_tgt
        label_map[_price_key(ds_price)] = _move_label("Downside", spot, ds_price)
    if upside_tgt is not None:
        us_price = spot * upside_tgt
        label_map[_price_key(us_price)] = _move_label("Upside", spot, us_price)
    label_map[_price_key(spot)] = "Current Market Price"

    def _clean(v: float) -> float:
        """Normalise near-zero values so they never display as -0.00."""
        return 0.0 if abs(v) < 0.005 else v

    def _clean_roi(v: float) -> float:
        """Normalise near-zero ROI so they never display as -0.0000."""
        return 0.0 if abs(v) < 5e-7 else v

    rows = []
    for price in points:
        scenario_label = label_map.get(_price_key(price))
        if not scenario_label:
            scenario_label = _scenario_fallback_label(price)
        option_pnl = _clean(_compute_pnl_for_price(option_only, price))
        combined_pnl = _clean(_compute_pnl_for_price(input, price))
        stock_pnl = _clean(combined_pnl - option_pnl)
        option_roi = _clean_roi(option_pnl / option_basis)
        net_roi = _clean_roi(combined_pnl / total_basis)
        scenario_key = compute_scenario_key(input, payoff_result, price)
        template = select_template(archetype, scenario_key, templates_df)
        context = build_commentary_context(input, option_roi, net_roi)
        commentary = render_commentary(template, context)
        rows.append(
            {
                "price": price,
                "option_pnl": option_pnl,
                "stock_pnl": stock_pnl,
                "combined_pnl": combined_pnl,
                "margin_requirement": margin_requirement,
                "option_roi": option_roi,
                "net_roi": net_roi,
                "commentary": commentary,
                "scenario": scenario_label,
            }
        )

    return pd.DataFrame(rows)
