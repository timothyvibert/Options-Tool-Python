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
    result = option_total + stock_total
    # Eliminate IEEE -0.0 (negative zero) at the source
    return result + 0.0


def _detect_breakevens(grid: List[float], pnl: List[float]) -> List[float]:
    if not grid or not pnl:
        return []

    _BE_TOLERANCE = 0.50  # P&L values within ±$0.50 of zero are "at zero"

    # Global flat-curve check: if entire P&L curve varies by less than $1,
    # there are no meaningful breakevens (e.g. Conversion, Box Spreads).
    pnl_range = max(pnl) - min(pnl)
    if pnl_range < 1.0:
        return []

    # Standard breakeven detection (zero-crossings and exact zeros)
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

    # If 0 or 1 breakevens, no consolidation needed
    if len(breakevens) <= 1:
        return breakevens

    # Group consecutive breakevens into clusters where P&L is flat near
    # zero between them.  This uses P&L flatness rather than fixed-gap
    # proximity so it handles floating-point noise across wide flat regions
    # (e.g. vertical spread + stock where combined P&L ≈ 0 between strikes).
    _EPS = 1e-6  # tolerance for grid-point matching (avoids round() drift)
    clusters: List[List[float]] = [[breakevens[0]]]
    for be in breakevens[1:]:
        prev_be = clusters[-1][-1]
        # Check P&L between previous breakeven and this one
        pnl_between = [
            pnl[i] for i in range(len(grid))
            if prev_be - _EPS <= grid[i] <= be + _EPS
        ]
        if pnl_between:
            range_val = max(pnl_between) - min(pnl_between)
            mid_val = (max(pnl_between) + min(pnl_between)) / 2.0
            if range_val < _BE_TOLERANCE * 2 and abs(mid_val) <= _BE_TOLERANCE:
                # P&L is flat at zero between them — same cluster
                clusters[-1].append(be)
                continue
        clusters.append([be])

    # Consolidate each cluster
    consolidated: List[float] = []
    for cluster in clusters:
        if len(cluster) == 1:
            consolidated.append(cluster[0])
            continue
        # Multi-breakeven cluster — check if P&L is flat in this range
        cluster_start = cluster[0]
        cluster_end = cluster[-1]
        pnl_in_range = [
            pnl[i] for i in range(len(grid))
            if cluster_start - _EPS <= grid[i] <= cluster_end + _EPS
        ]
        if not pnl_in_range:
            consolidated.append(cluster[0])
            consolidated.append(cluster[-1])
            continue
        range_max = max(pnl_in_range)
        range_min = min(pnl_in_range)
        if (range_max - range_min) < _BE_TOLERANCE * 2:
            # P&L is flat in this range
            flat_mid = (range_max + range_min) / 2.0
            if abs(flat_mid) <= _BE_TOLERANCE:
                # Flat at zero — single breakeven at cluster midpoint
                consolidated.append(round((cluster_start + cluster_end) / 2.0, 8))
            # else: flat but not at zero — no breakeven for this cluster
        else:
            # P&L varies but multiple crossings — keep first and last
            consolidated.append(cluster[0])
            consolidated.append(cluster[-1])

    return consolidated


def _detect_unlimited(grid: List[float], pnl: List[float]) -> Dict[str, bool]:
    if len(grid) < 2:
        return {
            "unlimited_upside": False, "unlimited_downside": False,
            "unlimited_loss_upside": False,
            "unlimited_profit_upside": False,
            "unlimited_profit_downside": False,
            "unlimited_loss_downside": False,
        }
    slope_high = (pnl[-1] - pnl[-2]) / (grid[-1] - grid[-2])
    slope_low = (pnl[1] - pnl[0]) / (grid[1] - grid[0])
    # Use a small tolerance to avoid floating-point noise (e.g. -3e-12)
    # triggering unlimited flags for strategies with truly flat payoffs.
    _EPS = 1e-6
    has_slope_low = slope_low < -_EPS
    return {
        # Legacy flags (kept for backward compatibility)
        "unlimited_upside": slope_high > _EPS,
        "unlimited_downside": has_slope_low,
        "unlimited_loss_upside": slope_high < -_EPS,
        # Directional flags — distinguish profit vs loss at each extreme
        "unlimited_profit_upside": slope_high > _EPS,          # long call: profit rises as price → ∞
        "unlimited_profit_downside": has_slope_low and pnl[0] > 0,  # long put: profit at price → 0
        "unlimited_loss_downside": has_slope_low and pnl[0] < 0,    # loss grows as price → 0
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
