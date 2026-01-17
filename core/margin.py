from __future__ import annotations

from core.models import StrategyInput
from core.payoff import _compute_pnl_for_price, compute_payoff


LNG_LE_9M = "LNG_LE_9M"
SH_OPT = "SH_OPT"
SH_PUT_CALL = "SH_PUT_CALL"
SPR = "SPR"
CCOV = "CCOV"
PPRT = "PPRT"
COL_EQ = "COL_EQ"


def classify_strategy(input: StrategyInput) -> str:
    legs = [leg for leg in input.legs if leg.kind.lower() in {"call", "put"}]
    has_stock = input.stock_position != 0
    all_long = bool(legs) and all(leg.position > 0 for leg in legs)
    all_short = bool(legs) and all(leg.position < 0 for leg in legs)

    short_calls = [leg for leg in legs if leg.kind.lower() == "call" and leg.position < 0]
    long_calls = [leg for leg in legs if leg.kind.lower() == "call" and leg.position > 0]
    short_puts = [leg for leg in legs if leg.kind.lower() == "put" and leg.position < 0]
    long_puts = [leg for leg in legs if leg.kind.lower() == "put" and leg.position > 0]

    if has_stock and input.stock_position > 0:
        if short_calls and long_puts and not long_calls and not short_puts:
            return COL_EQ
        if short_calls and not long_calls and not short_puts and not long_puts:
            return CCOV
        if long_puts and not long_calls and not short_calls and not short_puts:
            return PPRT

    if not has_stock:
        if all_long:
            return LNG_LE_9M
        if all_short:
            if short_calls and short_puts:
                return SH_PUT_CALL
            return SH_OPT

    payoff = compute_payoff(input)
    bounded = not payoff.get("unlimited_upside", False) and not payoff.get(
        "unlimited_downside", False
    )
    if bounded:
        return SPR
    if all_short or any(leg.position < 0 for leg in legs):
        return SH_OPT
    return LNG_LE_9M


def _option_only_input(input: StrategyInput) -> StrategyInput:
    return StrategyInput(
        spot=input.spot,
        stock_position=0.0,
        avg_cost=0.0,
        legs=input.legs,
    )


def _short_option_margin(leg, spot: float) -> float:
    quantity = abs(leg.position)
    underlying_value = quantity * spot * leg.multiplier
    if leg.kind.lower() == "call":
        otm_value = max(leg.strike - spot, 0.0) * quantity * leg.multiplier
    else:
        otm_value = max(spot - leg.strike, 0.0) * quantity * leg.multiplier
    premium_component = quantity * leg.premium * leg.multiplier
    return premium_component + max(
        0.2 * underlying_value - otm_value,
        0.1 * underlying_value,
    )


def compute_margin_proxy(
    input: StrategyInput, payoff_result: dict, mode: str = "CBOE"
) -> float:
    _ = mode
    classification = classify_strategy(input)
    spot = float(input.spot)

    if classification == LNG_LE_9M:
        total = sum(
            leg.position * leg.premium * leg.multiplier
            for leg in input.legs
            if leg.position > 0
        )
        return max(1.0, float(total))

    if classification == SPR:
        option_only = _option_only_input(input)
        price_grid = payoff_result.get("price_grid", [])
        if not price_grid:
            payoff_result = compute_payoff(input)
            price_grid = payoff_result.get("price_grid", [])
        option_pnl = [
            _compute_pnl_for_price(option_only, price) for price in price_grid
        ]
        if not option_pnl:
            return 1.0
        return max(1.0, abs(min(option_pnl)))

    if classification in {SH_OPT, SH_PUT_CALL}:
        total = 0.0
        for leg in input.legs:
            if leg.position < 0:
                total += _short_option_margin(leg, spot)
        return max(1.0, total)

    if classification == CCOV:
        return max(1.0, 0.5 * abs(input.stock_position) * spot)

    if classification in {PPRT, COL_EQ}:
        net_put_premium = sum(
            leg.position * leg.premium * leg.multiplier
            for leg in input.legs
            if leg.kind.lower() == "put"
        )
        total = 0.5 * abs(input.stock_position) * spot + max(
            net_put_premium, 0.0
        )
        return max(1.0, total)

    return 1.0
