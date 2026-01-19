from core.analysis_pack import build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.roi import NET_PREMIUM


def _build_pack(strategy_input):
    return build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={
            "strategy_name": "Test Strategy",
            "as_of": "2026-01-18",
            "expiry": "2026-03-20",
        },
        pricing_mode="MID",
        roi_policy=NET_PREMIUM,
        vol_mode="ATM",
        atm_iv=0.2,
        underlying_profile=None,
        bbg_leg_snapshots=None,
        scenario_mode="STANDARD",
        downside_tgt=0.8,
        upside_tgt=1.2,
    )


def test_narrative_covered_call():
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=100.0,
        avg_cost=100.0,
        legs=[OptionLeg(kind="call", position=-1.0, strike=110.0, premium=2.0)],
    )
    pack = _build_pack(strategy_input)
    narrative = pack.get("narrative_scenarios")
    assert narrative is not None
    for key, title in [
        ("bear", "Bearish Case"),
        ("base", "Stagnant Case"),
        ("bull", "Bullish Case"),
    ]:
        scenario = narrative.get(key)
        assert scenario is not None
        assert scenario.get("title") == title
        assert scenario.get("condition")
        assert scenario.get("body")
    trace = narrative.get("trace")
    assert trace.get("rule_id") == "covered_call_v1"
    bear = narrative.get("bear")
    assert bear.get("delta_vs_stock") is not None
    assert bear.get("delta_vs_stock") > 0
    assert "Compared with holding the stock alone" in bear.get("body", "")


def test_narrative_protective_put():
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=100.0,
        avg_cost=100.0,
        legs=[OptionLeg(kind="put", position=1.0, strike=95.0, premium=2.0)],
    )
    pack = _build_pack(strategy_input)
    narrative = pack.get("narrative_scenarios")
    assert narrative is not None
    assert narrative.get("bear") is not None
    assert narrative.get("base") is not None
    assert narrative.get("bull") is not None
    trace = narrative.get("trace")
    assert trace.get("rule_id") == "protective_put_v1"
    bear = narrative.get("bear")
    assert "Compared with holding the stock alone" in bear.get("body", "")


def test_narrative_iron_condor():
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[
            OptionLeg(kind="put", position=1.0, strike=90.0, premium=1.0),
            OptionLeg(kind="put", position=-1.0, strike=95.0, premium=2.0),
            OptionLeg(kind="call", position=-1.0, strike=105.0, premium=2.0),
            OptionLeg(kind="call", position=1.0, strike=110.0, premium=1.0),
        ],
    )
    pack = _build_pack(strategy_input)
    narrative = pack.get("narrative_scenarios")
    assert narrative is not None
    assert narrative.get("bear") is not None
    assert narrative.get("base") is not None
    assert narrative.get("bull") is not None
    trace = narrative.get("trace")
    assert trace.get("rule_id") == "iron_condor_v1"
    bear = narrative.get("bear")
    assert bear.get("stock_only_pnl") == 0.0
    assert bear.get("delta_vs_stock") is not None
    assert "$0.00" not in bear.get("condition", "")
    assert "below $95.00" in bear.get("condition", "")
    base = narrative.get("base")
    assert "$95.00-$105.00" in base.get("condition", "")
    bull = narrative.get("bull")
    assert "above $105.00" in bull.get("condition", "")
    for scenario in [bear, base, bull]:
        body = scenario.get("body", "")
        assert "$" in body
    base_body = base.get("body", "").lower()
    assert "premium" in base_body or "profit" in base_body
    assert "maximum loss" in bear.get("body", "").lower()
    assert "maximum loss" in bull.get("body", "").lower()


def test_narrative_no_match():
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[
            OptionLeg(kind="call", position=1.0, strike=110.0, premium=2.0),
            OptionLeg(kind="put", position=1.0, strike=90.0, premium=2.0),
        ],
    )
    pack = _build_pack(strategy_input)
    narrative = pack.get("narrative_scenarios")
    assert narrative is not None
    for key in ["bear", "base", "bull"]:
        scenario = narrative.get(key)
        assert scenario is not None
        assert scenario.get("condition")
        assert scenario.get("body")
    trace = narrative.get("trace")
    assert trace.get("rule_id") == "fallback_generic"
    assert trace.get("reason") == "fallback_used_no_matching_rule"
