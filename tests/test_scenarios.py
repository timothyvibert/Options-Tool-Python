from core.models import OptionLeg, StrategyInput
from core.payoff import compute_payoff
from core.roi import NET_PREMIUM
from core.scenarios import build_scenario_points, compute_scenario_table


def _make_strategy() -> StrategyInput:
    return StrategyInput(
        spot=100.0,
        legs=[
            OptionLeg(kind="call", position=1, strike=95.0, premium=5.0),
            OptionLeg(kind="put", position=1, strike=105.0, premium=5.0),
        ],
    )


def test_scenario_points_include_spot_strikes_breakevens():
    strategy = _make_strategy()
    payoff = compute_payoff(strategy)
    points = build_scenario_points(strategy, payoff, mode="STANDARD")
    assert strategy.spot in points
    assert 95.0 in points
    assert 105.0 in points
    for breakeven in payoff["breakevens"]:
        assert breakeven in points


def test_scenario_points_infinity_mode_bounds():
    strategy = _make_strategy()
    payoff = compute_payoff(strategy)
    points = build_scenario_points(strategy, payoff, mode="INFINITY")
    assert 0.0 in points
    assert 1000.0 * strategy.spot in points


def test_scenario_table_columns_and_rows():
    strategy = _make_strategy()
    points = [80.0, 100.0, 120.0]
    payoff = compute_payoff(strategy)
    table = compute_scenario_table(
        strategy,
        points,
        payoff_result=payoff,
        roi_policy=NET_PREMIUM,
    )
    assert list(table.columns) == [
        "price",
        "option_pnl",
        "stock_pnl",
        "combined_pnl",
        "option_roi",
        "net_roi",
    ]
    assert len(table) == len(points)
