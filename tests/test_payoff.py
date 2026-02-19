from core.models import OptionLeg, StrategyInput
from core.payoff import compute_payoff


def _get_pnl_at(price_grid, pnl, price):
    idx = price_grid.index(price)
    return pnl[idx]


def test_long_call():
    strategy = StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="call", position=1, strike=100.0, premium=5.0)],
    )
    results = compute_payoff(strategy)
    pnl_at_300 = _get_pnl_at(results["price_grid"], results["pnl"], 300.0)
    assert pnl_at_300 == (200.0 - 5.0) * 100


def test_short_call():
    strategy = StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="call", position=-1, strike=100.0, premium=5.0)],
    )
    results = compute_payoff(strategy)
    pnl_at_300 = _get_pnl_at(results["price_grid"], results["pnl"], 300.0)
    assert pnl_at_300 == -1 * (200.0 - 5.0) * 100


def test_long_put():
    strategy = StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="put", position=1, strike=100.0, premium=5.0)],
    )
    results = compute_payoff(strategy)
    pnl_at_0 = _get_pnl_at(results["price_grid"], results["pnl"], 0.0)
    assert pnl_at_0 == (100.0 - 0.0 - 5.0) * 100


def test_short_put():
    strategy = StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="put", position=-1, strike=100.0, premium=5.0)],
    )
    results = compute_payoff(strategy)
    pnl_at_0 = _get_pnl_at(results["price_grid"], results["pnl"], 0.0)
    assert pnl_at_0 == -1 * (100.0 - 0.0 - 5.0) * 100


def test_stock_overlay():
    strategy = StrategyInput(
        spot=100.0,
        stock_position=10,
        avg_cost=100.0,
        legs=[],
    )
    results = compute_payoff(strategy)
    pnl_at_300 = _get_pnl_at(results["price_grid"], results["pnl"], 300.0)
    assert pnl_at_300 == 10 * (300.0 - 100.0)


def test_unlimited_upside():
    strategy = StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="call", position=1, strike=100.0, premium=1.0)],
    )
    results = compute_payoff(strategy)
    assert results["unlimited_upside"] is True
    assert results["unlimited_downside"] is False


def test_unlimited_downside_naked_short_call():
    strategy = StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="call", position=-1, strike=100.0, premium=5.0)],
    )
    results = compute_payoff(strategy)
    assert results["unlimited_upside"] is False
    assert results["unlimited_downside"] is False  # stock going to 0 doesn't cause loss
    assert results["unlimited_loss_upside"] is True  # loss grows as stock rises


def test_short_put_no_unlimited():
    strategy = StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="put", position=-1, strike=100.0, premium=5.0)],
    )
    results = compute_payoff(strategy)
    assert results["unlimited_upside"] is False
    assert results["unlimited_downside"] is False
    assert results["unlimited_loss_upside"] is False


# ── Directional unlimited flags ──────────────────────────────────────────

def test_directional_flags_long_call():
    """Long call: profit rises as price → ∞, no loss at either extreme."""
    results = compute_payoff(StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="call", position=1, strike=100.0, premium=5.0)],
    ))
    assert results["unlimited_profit_upside"] is True
    assert results["unlimited_profit_downside"] is False
    assert results["unlimited_loss_upside"] is False
    assert results["unlimited_loss_downside"] is False


def test_directional_flags_long_put():
    """Long put: profit grows as price → 0, max loss is premium (finite)."""
    results = compute_payoff(StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="put", position=1, strike=95.0, premium=2.50)],
    ))
    assert results["unlimited_profit_upside"] is False
    assert results["unlimited_profit_downside"] is True
    assert results["unlimited_loss_upside"] is False
    assert results["unlimited_loss_downside"] is False


def test_directional_flags_short_call():
    """Short call: loss grows as price → ∞, max profit is premium (finite)."""
    results = compute_payoff(StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="call", position=-1, strike=105.0, premium=3.0)],
    ))
    assert results["unlimited_profit_upside"] is False
    assert results["unlimited_profit_downside"] is False
    assert results["unlimited_loss_upside"] is True
    assert results["unlimited_loss_downside"] is False


def test_directional_flags_short_put():
    """Short put: loss is bounded (price can't go below 0), all False."""
    results = compute_payoff(StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="put", position=-1, strike=95.0, premium=2.50)],
    ))
    assert results["unlimited_profit_upside"] is False
    assert results["unlimited_profit_downside"] is False
    assert results["unlimited_loss_upside"] is False
    assert results["unlimited_loss_downside"] is False
