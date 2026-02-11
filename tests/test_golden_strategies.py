"""Golden tests for representative strategy archetypes.

Conventions:
- Option multiplier assumed 100.
- OptionLeg.premium is stored as a positive number; position sign drives cashflow.
- Stock PnL uses shares * (price - avg_cost).
"""

import pytest

from core.analysis_pack import build_analysis_pack
from core.margin import SPR
from core.models import OptionLeg, StrategyInput
from core.payoff import compute_payoff
from core.roi import (
    CASH_SECURED,
    NET_PREMIUM,
    RISK_MAX_LOSS,
    capital_basis,
    combined_capital_basis,
)
from core.scenarios import build_scenario_points, compute_scenario_table


AS_OF = "2025-01-02"
EXPIRY = "2025-06-21"


def _build_pack(strategy_input: StrategyInput, roi_policy: str, name: str) -> dict:
    return build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": name, "as_of": AS_OF, "expiry": EXPIRY},
        pricing_mode="MID",
        roi_policy=roi_policy,
        vol_mode="ATM",
        atm_iv=0.2,
        underlying_profile={},
        bbg_leg_snapshots=None,
        scenario_mode="STANDARD",
        downside_tgt=0.8,
        upside_tgt=1.2,
    )


def _build_scenario_df(
    strategy_input: StrategyInput, payoff_result: dict, roi_policy: str
):
    points = build_scenario_points(
        strategy_input,
        payoff_result,
        mode="STANDARD",
        downside_tgt=0.8,
        upside_tgt=1.2,
    )
    scenario_df = compute_scenario_table(
        strategy_input,
        points,
        payoff_result=payoff_result,
        roi_policy=roi_policy,
        strategy_row=None,
        downside_tgt=0.8,
        upside_tgt=1.2,
    )
    return points, scenario_df


def _assert_required_scenarios(scenario_df):
    scenarios = scenario_df["scenario"].tolist()
    assert "Current Market Price" in scenarios
    assert any(str(label).startswith("Downside") for label in scenarios)
    assert any(str(label).startswith("Upside") for label in scenarios)


def _assert_pack_keys(pack):
    for key in ["payoff", "summary", "scenario", "key_levels", "narrative_scenarios"]:
        assert key in pack


def test_golden_covered_call():
    # Strategy map: Covered Call (strategy_id=8)
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=100.0,
        avg_cost=100.0,
        legs=[OptionLeg(kind="call", position=-1.0, strike=110.0, premium=2.0)],
    )
    payoff_result = compute_payoff(strategy_input)
    assert payoff_result["breakevens"] == pytest.approx([98.0], abs=1e-6)

    combined_pnl = payoff_result["pnl"]
    assert max(combined_pnl) == pytest.approx(1200.0, abs=1e-6)
    assert min(combined_pnl) == pytest.approx(-9800.0, abs=1e-6)

    option_basis = capital_basis(strategy_input, payoff_result, NET_PREMIUM)
    total_basis = combined_capital_basis(strategy_input, option_basis)
    assert option_basis == pytest.approx(200.0, abs=1e-6)
    assert total_basis == pytest.approx(10200.0, abs=1e-6)

    points, scenario_df = _build_scenario_df(
        strategy_input, payoff_result, NET_PREMIUM
    )
    assert min(points) == pytest.approx(80.0, abs=1e-6)
    assert max(points) == pytest.approx(120.0, abs=1e-6)
    _assert_required_scenarios(scenario_df)

    pack = _build_pack(strategy_input, NET_PREMIUM, "Covered Call")
    _assert_pack_keys(pack)


def test_golden_collar():
    # Strategy map: Collar (strategy_id=12)
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=100.0,
        avg_cost=100.0,
        legs=[
            OptionLeg(kind="put", position=1.0, strike=90.0, premium=1.5),
            OptionLeg(kind="call", position=-1.0, strike=110.0, premium=2.0),
        ],
    )
    payoff_result = compute_payoff(strategy_input)
    assert payoff_result["breakevens"] == pytest.approx([99.5], abs=1e-6)

    combined_pnl = payoff_result["pnl"]
    assert max(combined_pnl) == pytest.approx(1050.0, abs=1e-6)
    assert min(combined_pnl) == pytest.approx(-950.0, abs=1e-6)

    option_basis = capital_basis(strategy_input, payoff_result, NET_PREMIUM)
    total_basis = combined_capital_basis(strategy_input, option_basis)
    assert option_basis == pytest.approx(50.0, abs=1e-6)
    assert total_basis == pytest.approx(10050.0, abs=1e-6)

    points, scenario_df = _build_scenario_df(
        strategy_input, payoff_result, NET_PREMIUM
    )
    assert min(points) == pytest.approx(80.0, abs=1e-6)
    assert max(points) == pytest.approx(120.0, abs=1e-6)
    _assert_required_scenarios(scenario_df)

    pack = _build_pack(strategy_input, NET_PREMIUM, "Collar")
    _assert_pack_keys(pack)


def test_golden_protective_put():
    # Strategy map: Protective Put (stock + long put)
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=100.0,
        avg_cost=100.0,
        legs=[OptionLeg(kind="put", position=1.0, strike=95.0, premium=1.25)],
    )
    payoff_result = compute_payoff(strategy_input)
    assert payoff_result["breakevens"] == pytest.approx([101.25], abs=1e-6)
    assert min(payoff_result["pnl"]) == pytest.approx(-625.0, abs=1e-6)
    assert payoff_result["unlimited_upside"] is True
    assert payoff_result["unlimited_downside"] is False

    option_basis = capital_basis(strategy_input, payoff_result, NET_PREMIUM)
    total_basis = combined_capital_basis(strategy_input, option_basis)
    assert option_basis == pytest.approx(125.0, abs=1e-6)
    assert total_basis == pytest.approx(10125.0, abs=1e-6)

    points, scenario_df = _build_scenario_df(
        strategy_input, payoff_result, NET_PREMIUM
    )
    assert min(points) == pytest.approx(80.0, abs=1e-6)
    assert max(points) == pytest.approx(120.0, abs=1e-6)
    _assert_required_scenarios(scenario_df)

    pack = _build_pack(strategy_input, NET_PREMIUM, "Protective Put")
    _assert_pack_keys(pack)


def test_golden_cash_secured_put():
    # Strategy map: Cash-Secured Put (short put)
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="put", position=-1.0, strike=95.0, premium=2.5)],
    )
    payoff_result = compute_payoff(strategy_input)
    assert payoff_result["breakevens"] == pytest.approx([92.5], abs=1e-6)
    assert max(payoff_result["pnl"]) == pytest.approx(250.0, abs=1e-6)
    assert min(payoff_result["pnl"]) == pytest.approx(-9250.0, abs=1e-6)
    assert payoff_result["unlimited_upside"] is False
    assert payoff_result["unlimited_downside"] is False

    option_basis = capital_basis(strategy_input, payoff_result, CASH_SECURED)
    total_basis = combined_capital_basis(strategy_input, option_basis)
    assert option_basis == pytest.approx(9500.0, abs=1e-6)
    assert total_basis == pytest.approx(9500.0, abs=1e-6)

    points, scenario_df = _build_scenario_df(
        strategy_input, payoff_result, CASH_SECURED
    )
    assert min(points) == pytest.approx(80.0, abs=1e-6)
    assert max(points) == pytest.approx(120.0, abs=1e-6)
    _assert_required_scenarios(scenario_df)
    assert "Breakeven 1" in scenario_df["scenario"].tolist()

    pack = _build_pack(strategy_input, CASH_SECURED, "Cash-Secured Put")
    _assert_pack_keys(pack)


def test_golden_bull_call_spread():
    # Strategy map: Bull Call Spread (strategy_id=13)
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[
            OptionLeg(kind="call", position=1.0, strike=95.0, premium=7.0),
            OptionLeg(kind="call", position=-1.0, strike=105.0, premium=3.0),
        ],
    )
    payoff_result = compute_payoff(strategy_input)
    assert payoff_result["breakevens"] == pytest.approx([99.0], abs=1e-6)

    combined_pnl = payoff_result["pnl"]
    assert max(combined_pnl) == pytest.approx(600.0, abs=1e-6)
    assert min(combined_pnl) == pytest.approx(-400.0, abs=1e-6)

    option_basis = capital_basis(strategy_input, payoff_result, RISK_MAX_LOSS)
    total_basis = combined_capital_basis(strategy_input, option_basis)
    assert option_basis == pytest.approx(400.0, abs=1e-6)
    assert total_basis == pytest.approx(400.0, abs=1e-6)

    points, scenario_df = _build_scenario_df(
        strategy_input, payoff_result, RISK_MAX_LOSS
    )
    assert min(points) == pytest.approx(80.0, abs=1e-6)
    assert max(points) == pytest.approx(120.0, abs=1e-6)
    _assert_required_scenarios(scenario_df)

    pack = _build_pack(strategy_input, RISK_MAX_LOSS, "Bull Call Spread")
    _assert_pack_keys(pack)


def test_golden_bull_put_credit_spread():
    # Strategy map: Bull Put Spread (credit)
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[
            OptionLeg(kind="put", position=-1.0, strike=100.0, premium=5.0),
            OptionLeg(kind="put", position=1.0, strike=90.0, premium=2.0),
        ],
    )
    payoff_result = compute_payoff(strategy_input)
    assert payoff_result["breakevens"] == pytest.approx([97.0], abs=1e-6)
    assert max(payoff_result["pnl"]) == pytest.approx(300.0, abs=1e-6)
    assert min(payoff_result["pnl"]) == pytest.approx(-700.0, abs=1e-6)
    assert payoff_result["unlimited_upside"] is False
    assert payoff_result["unlimited_downside"] is False

    option_basis = capital_basis(strategy_input, payoff_result, RISK_MAX_LOSS)
    total_basis = combined_capital_basis(strategy_input, option_basis)
    assert option_basis == pytest.approx(700.0, abs=1e-6)
    assert total_basis == pytest.approx(700.0, abs=1e-6)

    points, scenario_df = _build_scenario_df(
        strategy_input, payoff_result, RISK_MAX_LOSS
    )
    assert min(points) == pytest.approx(80.0, abs=1e-6)
    assert max(points) == pytest.approx(120.0, abs=1e-6)
    _assert_required_scenarios(scenario_df)
    spot_mask = (scenario_df["price"] - float(strategy_input.spot)).abs() <= 1e-6
    assert scenario_df.loc[spot_mask, "scenario"].iloc[0] == "Current Market Price"
    assert "Breakeven 1" in scenario_df["scenario"].tolist()

    pack = _build_pack(strategy_input, RISK_MAX_LOSS, "Bull Put Spread (Credit)")
    _assert_pack_keys(pack)
    assert pack["margin"]["classification"] == SPR
    assert float(pack["margin"]["margin_proxy"]) == pytest.approx(700.0, abs=1e-6)


def test_golden_long_straddle():
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[
            OptionLeg(kind="call", position=1.0, strike=102.0, premium=4.0),
            OptionLeg(kind="put", position=1.0, strike=102.0, premium=4.0),
        ],
    )
    payoff_result = compute_payoff(strategy_input)
    assert payoff_result["breakevens"] == pytest.approx([94.0, 110.0], abs=1e-6)
    assert min(payoff_result["pnl"]) == pytest.approx(-800.0, abs=1e-6)
    assert payoff_result["unlimited_upside"] is True

    option_basis = capital_basis(strategy_input, payoff_result, NET_PREMIUM)
    total_basis = combined_capital_basis(strategy_input, option_basis)
    assert option_basis == pytest.approx(800.0, abs=1e-6)
    assert total_basis == pytest.approx(800.0, abs=1e-6)

    points, scenario_df = _build_scenario_df(
        strategy_input, payoff_result, NET_PREMIUM
    )
    assert min(points) == pytest.approx(80.0, abs=1e-6)
    assert max(points) == pytest.approx(120.0, abs=1e-6)
    _assert_required_scenarios(scenario_df)
    assert "Breakeven 1" in scenario_df["scenario"].tolist()
    assert "Breakeven 2" in scenario_df["scenario"].tolist()

    pack = _build_pack(strategy_input, NET_PREMIUM, "Long Straddle")
    _assert_pack_keys(pack)


def test_golden_iron_condor():
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[
            OptionLeg(kind="put", position=-1.0, strike=95.0, premium=2.0),
            OptionLeg(kind="put", position=1.0, strike=90.0, premium=0.75),
            OptionLeg(kind="call", position=-1.0, strike=105.0, premium=2.0),
            OptionLeg(kind="call", position=1.0, strike=110.0, premium=0.75),
        ],
    )
    payoff_result = compute_payoff(strategy_input)
    assert payoff_result["breakevens"] == pytest.approx([92.5, 107.5], abs=1e-6)
    assert max(payoff_result["pnl"]) == pytest.approx(250.0, abs=1e-6)
    assert min(payoff_result["pnl"]) == pytest.approx(-250.0, abs=1e-6)
    assert payoff_result["unlimited_upside"] is False
    assert payoff_result["unlimited_downside"] is False

    option_basis = capital_basis(strategy_input, payoff_result, RISK_MAX_LOSS)
    total_basis = combined_capital_basis(strategy_input, option_basis)
    assert option_basis == pytest.approx(250.0, abs=1e-6)
    assert total_basis == pytest.approx(250.0, abs=1e-6)

    points, scenario_df = _build_scenario_df(
        strategy_input, payoff_result, RISK_MAX_LOSS
    )
    assert min(points) == pytest.approx(80.0, abs=1e-6)
    assert max(points) == pytest.approx(120.0, abs=1e-6)
    _assert_required_scenarios(scenario_df)
    assert "Breakeven 1" in scenario_df["scenario"].tolist()
    assert "Breakeven 2" in scenario_df["scenario"].tolist()

    pack = _build_pack(strategy_input, RISK_MAX_LOSS, "Iron Condor")
    _assert_pack_keys(pack)
    assert pack["margin"]["classification"] == SPR
    assert float(pack["margin"]["margin_proxy"]) == pytest.approx(250.0, abs=1e-6)
