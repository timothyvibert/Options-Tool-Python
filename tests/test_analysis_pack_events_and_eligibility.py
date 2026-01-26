import pandas as pd

from core.analysis_pack import build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.roi import NET_PREMIUM


def _build_pack(underlying_profile):
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="call", position=1.0, strike=100.0, premium=2.0)],
    )
    return build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={
            "strategy_name": "Test Strategy",
            "as_of": "2026-01-01",
            "expiry": "2026-02-01",
        },
        pricing_mode="MID",
        roi_policy=NET_PREMIUM,
        vol_mode="ATM",
        atm_iv=0.2,
        underlying_profile=underlying_profile,
        bbg_leg_snapshots=None,
        scenario_mode="STANDARD",
        downside_tgt=0.8,
        upside_tgt=1.2,
    )


def test_analysis_pack_includes_earnings_risk_fields():
    pack = _build_pack({"EXPECTED_REPORT_DT": "2026-01-15"})
    underlying = pack.get("underlying", {})
    earnings_risk = underlying.get("earnings_risk", {})
    assert isinstance(earnings_risk, dict)
    assert earnings_risk.get("days_to_earnings") == 14
    assert earnings_risk.get("before_expiry") is True


def test_analysis_pack_includes_eligibility_block():
    pack = _build_pack({"EXPECTED_REPORT_DT": "2026-01-15"})
    strategy = pack.get("strategy", {})
    strategy_code = strategy.get("strategy_code")
    assert isinstance(strategy_code, str) and strategy_code

    eligibility = pack.get("eligibility", {})
    assert eligibility.get("strategy_code") == strategy_code
    table = eligibility.get("table")
    assert isinstance(table, pd.DataFrame)
    assert list(table.columns) == ["account_type", "eligibility"]
    assert "error" in eligibility
