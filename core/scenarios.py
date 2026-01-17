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

    rows = []
    for price in points:
        option_pnl = _compute_pnl_for_price(option_only, price)
        combined_pnl = _compute_pnl_for_price(input, price)
        stock_pnl = combined_pnl - option_pnl
        option_roi = option_pnl / option_basis
        net_roi = combined_pnl / total_basis
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
            }
        )

    return pd.DataFrame(rows)
