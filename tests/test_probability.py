from core.models import OptionLeg, StrategyInput
from core.payoff import _compute_pnl_for_price
from core.probability import (
    effective_sigma,
    leg_pop_at_expiry,
    prob_finish_above,
    strategy_pop,
)


def test_prob_finish_above_monotonic():
    S = 100.0
    p_low = prob_finish_above(S, 90.0, 0.0, 0.0, 0.2, 1.0)
    p_high = prob_finish_above(S, 110.0, 0.0, 0.0, 0.2, 1.0)
    assert p_low > p_high


def test_leg_pop_long_short_complement():
    long_call = OptionLeg(kind="call", position=1, strike=100.0, premium=2.0)
    short_call = OptionLeg(kind="call", position=-1, strike=100.0, premium=2.0)
    p_long = leg_pop_at_expiry(long_call, 100.0, 0.0, 0.0, 0.2, 1.0)
    p_short = leg_pop_at_expiry(short_call, 100.0, 0.0, 0.0, 0.2, 1.0)
    assert abs((p_long + p_short) - 1.0) < 1e-6


def test_vega_weighted_sigma_between_bounds():
    strategy = StrategyInput(
        spot=100.0,
        legs=[
            OptionLeg(kind="call", position=1, strike=90.0, premium=5.0),
            OptionLeg(kind="put", position=1, strike=110.0, premium=5.0),
        ],
    )
    sigmas = [0.15, 0.35]
    sigma = effective_sigma(
        strategy,
        sigmas,
        mode="VEGA_WEIGHTED",
        r=0.0,
        q=0.0,
        t=0.5,
        atm_iv=0.2,
    )
    assert min(sigmas) <= sigma <= max(sigmas)


def test_strategy_pop_stock_overlay_increases_pop():
    base = StrategyInput(spot=100.0, legs=[])
    with_stock = StrategyInput(
        spot=100.0, stock_position=1.0, avg_cost=100.0, legs=[]
    )
    pop_base = strategy_pop(
        base,
        _compute_pnl_for_price,
        S0=100.0,
        r=0.0,
        q=0.0,
        sigma_mode="ATM",
        atm_iv=0.2,
        per_leg_iv=[],
        t=1.0,
    )
    pop_stock = strategy_pop(
        with_stock,
        _compute_pnl_for_price,
        S0=100.0,
        r=0.0,
        q=0.0,
        sigma_mode="ATM",
        atm_iv=0.2,
        per_leg_iv=[],
        t=1.0,
    )
    assert pop_stock > pop_base
    assert pop_stock > 0.3
