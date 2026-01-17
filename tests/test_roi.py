from core.models import OptionLeg, StrategyInput
from core.payoff import compute_payoff
from core.roi import (
    CASH_SECURED,
    RISK_MAX_LOSS,
    capital_basis,
    compute_net_premium,
    is_pure_short_puts,
)


def test_net_premium_sign_convention():
    long_call = StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="call", position=1, strike=100.0, premium=2.0)],
    )
    short_put = StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="put", position=-1, strike=100.0, premium=3.0)],
    )
    assert compute_net_premium(long_call) == 2.0
    assert compute_net_premium(short_put) == -3.0


def test_pure_short_puts_detection():
    short_puts = StrategyInput(
        spot=100.0,
        legs=[
            OptionLeg(kind="put", position=-2, strike=90.0, premium=2.0)
        ],
    )
    with_stock = StrategyInput(
        spot=100.0,
        stock_position=10.0,
        avg_cost=100.0,
        legs=[OptionLeg(kind="put", position=-1, strike=90.0, premium=2.0)],
    )
    assert is_pure_short_puts(short_puts) is True
    assert is_pure_short_puts(with_stock) is False


def test_cash_secured_basis_short_put():
    strategy = StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="put", position=-2, strike=50.0, premium=2.0)],
    )
    payoff = compute_payoff(strategy)
    basis = capital_basis(strategy, payoff, CASH_SECURED)
    assert basis == 2 * 50.0 * 100


def test_risk_max_loss_for_long_call():
    strategy = StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="call", position=1, strike=100.0, premium=2.0)],
    )
    payoff = compute_payoff(strategy)
    basis = capital_basis(strategy, payoff, RISK_MAX_LOSS)
    assert basis == 2.0 * 100
