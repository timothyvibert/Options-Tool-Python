from __future__ import annotations

from core.models import StrategyInput
from core.payoff import _compute_pnl_for_price


RISK_MAX_LOSS = "RISK_MAX_LOSS"
NET_PREMIUM = "NET_PREMIUM"
CASH_SECURED = "CASH_SECURED"
MARGIN_PROXY = "MARGIN_PROXY"


def compute_net_premium(input: StrategyInput) -> float:
    return sum(leg.position * leg.premium for leg in input.legs)


def is_pure_short_puts(input: StrategyInput) -> bool:
    if input.stock_position != 0 or not input.legs:
        return False
    for leg in input.legs:
        if leg.kind.lower() != "put" or leg.position >= 0:
            return False
    return True


def _net_call_position(input: StrategyInput) -> float:
    return sum(
        leg.position for leg in input.legs if leg.kind.lower() == "call"
    )


def _multiplier(input: StrategyInput) -> int:
    if not input.legs:
        return 100
    return input.legs[0].multiplier


def capital_basis(
    input: StrategyInput, payoff_result: dict, policy: str
) -> float:
    if not input.legs:
        return 1.0

    policy_key = policy.upper()
    if policy_key == NET_PREMIUM:
        net_premium = compute_net_premium(input)
        return abs(net_premium * _multiplier(input))

    if policy_key == CASH_SECURED:
        if is_pure_short_puts(input):
            total = 0.0
            for leg in input.legs:
                total += abs(leg.position) * leg.strike * leg.multiplier
            return total
        return capital_basis(input, payoff_result, MARGIN_PROXY)

    if policy_key == RISK_MAX_LOSS:
        if _net_call_position(input) < 0:
            return capital_basis(input, payoff_result, MARGIN_PROXY)
        option_only = StrategyInput(
            spot=input.spot,
            stock_position=0.0,
            avg_cost=0.0,
            legs=input.legs,
        )
        price_grid = payoff_result.get("price_grid", [])
        if not price_grid:
            return capital_basis(input, payoff_result, MARGIN_PROXY)
        option_pnl = [
            _compute_pnl_for_price(option_only, price) for price in price_grid
        ]
        return abs(min(option_pnl))

    if policy_key == MARGIN_PROXY:
        # TODO: replace placeholder with margin engine.
        net_premium = compute_net_premium(input)
        return max(1.0, abs(net_premium) * _multiplier(input))

    raise ValueError(f"Unknown ROI policy: {policy}")


def combined_capital_basis(
    input: StrategyInput, option_capital_basis: float
) -> float:
    if input.stock_position != 0:
        return abs(input.stock_position * input.avg_cost) + option_capital_basis
    return option_capital_basis
