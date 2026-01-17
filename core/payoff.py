from __future__ import annotations

from typing import Dict, List

from core.models import OptionLeg, StrategyInput


def _build_price_grid(spot: float, steps: int = 300) -> List[float]:
    max_price = 3.0 * spot
    if steps < 2:
        return [0.0, max_price]
    step = max_price / (steps - 1)
    return [i * step for i in range(steps)]


def _inject_strikes(grid: List[float], legs: List[OptionLeg]) -> List[float]:
    strikes = {leg.strike for leg in legs}
    combined = list(grid) + list(strikes)
    combined.sort()
    deduped: List[float] = []
    last = None
    for value in combined:
        if last is None or value != last:
            deduped.append(value)
            last = value
    return deduped


def _option_intrinsic(leg: OptionLeg, price: float) -> float:
    if leg.kind.lower() == "call":
        return max(price - leg.strike, 0.0)
    return max(leg.strike - price, 0.0)


def _compute_pnl_for_price(strategy: StrategyInput, price: float) -> float:
    option_total = 0.0
    for leg in strategy.legs:
        intrinsic = _option_intrinsic(leg, price)
        option_total += leg.position * (intrinsic - leg.premium) * leg.multiplier
    stock_total = strategy.stock_position * (price - strategy.avg_cost)
    return option_total + stock_total


def _detect_breakevens(grid: List[float], pnl: List[float]) -> List[float]:
    breakevens: List[float] = []
    for i in range(len(grid) - 1):
        y0 = pnl[i]
        y1 = pnl[i + 1]
        if y0 == 0.0:
            breakevens.append(grid[i])
            continue
        if y0 * y1 < 0.0:
            x0 = grid[i]
            x1 = grid[i + 1]
            breakeven = x0 - y0 * (x1 - x0) / (y1 - y0)
            breakevens.append(breakeven)
    breakevens = sorted(set(round(b, 8) for b in breakevens))
    return breakevens


def _detect_unlimited(grid: List[float], pnl: List[float]) -> Dict[str, bool]:
    if len(grid) < 2:
        return {"unlimited_upside": False, "unlimited_downside": False}
    slope_high = (pnl[-1] - pnl[-2]) / (grid[-1] - grid[-2])
    slope_low = (pnl[1] - pnl[0]) / (grid[1] - grid[0])
    return {
        "unlimited_upside": slope_high > 0.0,
        "unlimited_downside": slope_low < 0.0,
    }


def compute_payoff(strategy: StrategyInput) -> Dict[str, object]:
    grid = _build_price_grid(strategy.spot, steps=300)
    grid = _inject_strikes(grid, strategy.legs)
    pnl = [_compute_pnl_for_price(strategy, price) for price in grid]
    breakevens = _detect_breakevens(grid, pnl)
    unlimited = _detect_unlimited(grid, pnl)
    return {
        "price_grid": grid,
        "pnl": pnl,
        "breakevens": breakevens,
        **unlimited,
    }
