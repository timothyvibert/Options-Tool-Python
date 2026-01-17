from core.margin import CCOV, PPRT, SPR, classify_strategy, compute_margin_proxy
from core.models import OptionLeg, StrategyInput
from core.payoff import compute_payoff


def test_classify_covered_call():
    strategy = StrategyInput(
        spot=100.0,
        stock_position=100.0,
        avg_cost=100.0,
        legs=[OptionLeg(kind="call", position=-1, strike=110.0, premium=2.0)],
    )
    assert classify_strategy(strategy) == CCOV


def test_classify_protective_put():
    strategy = StrategyInput(
        spot=100.0,
        stock_position=100.0,
        avg_cost=100.0,
        legs=[OptionLeg(kind="put", position=1, strike=90.0, premium=2.0)],
    )
    assert classify_strategy(strategy) == PPRT


def test_classify_spread():
    strategy = StrategyInput(
        spot=100.0,
        legs=[
            OptionLeg(kind="call", position=1, strike=95.0, premium=5.0),
            OptionLeg(kind="call", position=-1, strike=110.0, premium=2.0),
        ],
    )
    assert classify_strategy(strategy) == SPR


def test_margin_proxy_positive():
    strategy = StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="call", position=-1, strike=110.0, premium=2.0)],
    )
    payoff = compute_payoff(strategy)
    margin = compute_margin_proxy(strategy, payoff)
    assert margin > 0.0
