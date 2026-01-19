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
        "margin_requirement",
        "option_roi",
        "net_roi",
        "commentary",
        "scenario",
    ]
    assert len(table) == len(points)


def test_scenario_labels_for_strikes_breakevens():
    strategy = StrategyInput(
        spot=100.0,
        legs=[
            OptionLeg(kind="call", position=1, strike=90.0, premium=2.0),
            OptionLeg(kind="put", position=1, strike=110.0, premium=2.0),
        ],
    )
    payoff = compute_payoff(strategy)
    points = build_scenario_points(strategy, payoff, mode="STANDARD")
    table = compute_scenario_table(
        strategy,
        points,
        payoff_result=payoff,
        roi_policy=NET_PREMIUM,
    )
    strike_row_low = table.loc[table["price"] == 90.0].iloc[0]
    strike_row_high = table.loc[table["price"] == 110.0].iloc[0]
    assert strike_row_low["scenario"] == "Lower Strike"
    assert strike_row_high["scenario"] == "Upper Strike"

    breakevens = sorted(payoff["breakevens"])
    if breakevens:
        breakeven_row = table.loc[table["price"] == breakevens[0]].iloc[0]
        assert breakeven_row["scenario"].startswith("Breakeven")


def test_scenario_labels_for_downside_upside():
    strategy = StrategyInput(
        spot=100.0,
        legs=[
            OptionLeg(kind="call", position=1, strike=90.0, premium=2.0),
        ],
    )
    payoff = compute_payoff(strategy)
    points = build_scenario_points(
        strategy, payoff, mode="STANDARD", downside_tgt=0.8, upside_tgt=1.2
    )
    table = compute_scenario_table(
        strategy,
        points,
        payoff_result=payoff,
        roi_policy=NET_PREMIUM,
    )
    min_price = min(points)
    max_price = max(points)
    downside_label = table.loc[table["price"] == min_price].iloc[0]["scenario"]
    upside_label = table.loc[table["price"] == max_price].iloc[0]["scenario"]
    assert downside_label == "Downside (20%)"
    assert upside_label == "Upside (20%)"


def test_scenario_labels_non_empty():
    strategy = StrategyInput(
        spot=100.0,
        legs=[
            OptionLeg(kind="call", position=1, strike=95.0, premium=2.0),
            OptionLeg(kind="call", position=1, strike=105.0, premium=2.0),
        ],
    )
    payoff = compute_payoff(strategy)
    points = build_scenario_points(
        strategy, payoff, mode="STANDARD", downside_tgt=0.85, upside_tgt=1.15
    )
    table = compute_scenario_table(
        strategy,
        points,
        payoff_result=payoff,
        roi_policy=NET_PREMIUM,
    )
    labels = table["scenario"].tolist()
    assert all(isinstance(label, str) and label.strip() for label in labels)
    assert "Current Market Price" in labels
    assert "Lower Strike" in labels
    assert "Upper Strike" in labels


def test_scenario_labels_for_four_strikes_unique():
    strategy = StrategyInput(
        spot=100.0,
        legs=[
            OptionLeg(kind="put", position=1, strike=90.0, premium=1.0),
            OptionLeg(kind="put", position=-1, strike=95.0, premium=2.0),
            OptionLeg(kind="call", position=-1, strike=105.0, premium=2.0),
            OptionLeg(kind="call", position=1, strike=110.0, premium=1.0),
        ],
    )
    payoff = compute_payoff(strategy)
    points = build_scenario_points(strategy, payoff, mode="STANDARD")
    table = compute_scenario_table(
        strategy,
        points,
        payoff_result=payoff,
        roi_policy=NET_PREMIUM,
    )
    labels = {
        table.loc[table["price"] == 90.0].iloc[0]["scenario"],
        table.loc[table["price"] == 95.0].iloc[0]["scenario"],
        table.loc[table["price"] == 105.0].iloc[0]["scenario"],
        table.loc[table["price"] == 110.0].iloc[0]["scenario"],
    }
    assert labels == {
        "Strike (Lowest)",
        "Strike (Lower Middle)",
        "Strike (Upper Middle)",
        "Strike (Highest)",
    }
