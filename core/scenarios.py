from __future__ import annotations

import math
from typing import List

import pandas as pd

from core.models import StrategyInput
from core.payoff import _compute_pnl_for_price


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


def _option_capital_basis(strategy: StrategyInput) -> float:
    if not strategy.legs:
        return 1.0
    # Deterministic placeholder for ROI sizing until a full policy is defined.
    net_premium = sum(leg.position * leg.premium for leg in strategy.legs)
    multiplier = strategy.legs[0].multiplier
    basis = abs(net_premium * multiplier)
    return max(1.0, float(basis))


def compute_scenario_table(
    input: StrategyInput, points: list[float]
) -> pd.DataFrame:
    option_only = StrategyInput(
        spot=input.spot,
        stock_position=0.0,
        avg_cost=0.0,
        legs=input.legs,
    )
    option_basis = _option_capital_basis(input)
    stock_basis = abs(input.stock_position * input.avg_cost)
    total_basis = option_basis + stock_basis if input.stock_position != 0 else option_basis

    rows = []
    for price in points:
        option_pnl = _compute_pnl_for_price(option_only, price)
        combined_pnl = _compute_pnl_for_price(input, price)
        stock_pnl = combined_pnl - option_pnl
        rows.append(
            {
                "price": price,
                "option_pnl": option_pnl,
                "stock_pnl": stock_pnl,
                "combined_pnl": combined_pnl,
                "option_roi": option_pnl / option_basis,
                "net_roi": combined_pnl / total_basis,
            }
        )

    return pd.DataFrame(rows)
