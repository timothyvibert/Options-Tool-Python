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


def _assert_no_stock_language(text: str) -> None:
    lowered = text.lower()
    assert "shares" not in lowered
    assert "stock-only" not in lowered
    assert "called away" not in lowered
    assert "overlay" not in lowered


def _has_overlay_delta(text: str) -> bool:
    lowered = text.lower()
    leads = [
        "relative to holding the shares alone",
        "net effect versus stock-only",
        "compared with stock-only",
    ]
    return any(lead in lowered for lead in leads)


def _has_breakdown(text: str) -> bool:
    lowered = text.lower()
    return "for context" in lowered and "options contribute" in lowered


def test_narrative_covered_call_full():
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=1000.0,
        avg_cost=100.0,
        legs=[OptionLeg(kind="call", position=-10.0, strike=110.0, premium=2.0)],
    )
    pack = _build_pack(strategy_input)
    narrative = pack.get("narrative_scenarios")
    assert narrative is not None
    trace = narrative.get("trace", {})
    assert trace.get("rule_id") == "covered_call_v3"

    bear_body = narrative.get("bear", {}).get("body", "").lower()
    bull = narrative.get("bull", {})
    bull_body = bull.get("body", "").lower()

    assert "full position" in bull_body
    assert "maximum loss" not in bear_body
    assert "capped" in bull_body or "called away" in bull_body
    assert "at expiry" in bull_body
    assert "above $110.00" in bull.get("condition", "").lower()


def test_narrative_partial_collar_meta():
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=1000.0,
        avg_cost=100.0,
        legs=[
            OptionLeg(kind="put", position=8.0, strike=90.0, premium=1.0),
            OptionLeg(kind="call", position=-8.0, strike=110.0, premium=2.0),
        ],
    )
    pack = _build_pack(strategy_input)
    narrative = pack.get("narrative_scenarios")
    assert narrative is not None

    bear = narrative.get("bear")
    bull = narrative.get("bull")
    assert bear is not None
    assert bull is not None

    bear_condition = bear.get("condition", "").lower()
    assert "below $90.00" in bear_condition
    assert "downside" not in bear_condition
    assert "upside" not in bear_condition
    assert "%" not in bear_condition

    bear_body = bear.get("body", "").lower()
    assert "~80% of the position" in bear_body
    assert "800 of 1,000 shares" in bear_body
    assert "partially protected" in bear_body
    assert "at expiry" in bear_body
    assert not (_has_overlay_delta(bear_body) and _has_breakdown(bear_body))

    bull_body = bull.get("body", "").lower()
    assert "partially capped" in bull_body
    assert "at expiry" in bull_body
    assert "above $110.00" in bull.get("condition", "").lower()
    assert not (_has_overlay_delta(bull_body) and _has_breakdown(bull_body))

    base_body = narrative.get("base", {}).get("body", "").lower()
    assert "realized" not in base_body
    assert (" paid" in base_body) or (" received" in base_body)
    assert not (_has_overlay_delta(base_body) and _has_breakdown(base_body))


def test_narrative_bull_call_spread_options_only():
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[
            OptionLeg(kind="call", position=1.0, strike=100.0, premium=3.0),
            OptionLeg(kind="call", position=-1.0, strike=110.0, premium=1.0),
        ],
    )
    pack = _build_pack(strategy_input)
    narrative = pack.get("narrative_scenarios")
    assert narrative is not None

    base_body = narrative.get("base", {}).get("body", "").lower()
    assert "breakeven" in base_body
    assert "debit" in base_body
    assert "retain premium" not in base_body
    assert "at expiry" in base_body

    bull_body = narrative.get("bull", {}).get("body", "")
    assert "gains are capped" in bull_body.lower()
    assert "maximum profit" in bull_body.lower()
    assert "at expiry" in bull_body.lower()
    assert "ROI at $110.00 is 400.0%" in bull_body

    for key in ["bear", "base", "bull"]:
        body = narrative.get(key, {}).get("body", "")
        _assert_no_stock_language(body)


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
        assert "at expiry" in scenario.get("body", "").lower()
    trace = narrative.get("trace")
    assert trace.get("rule_id") == "fallback_generic"
    assert trace.get("reason") == "fallback_used_no_matching_rule"


def test_narrative_credit_condor_options_only():
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
    base_body = narrative.get("base", {}).get("body", "").lower()
    assert "retains the net credit" in base_body
    bear_body = narrative.get("bear", {}).get("body", "").lower()
    bull_body = narrative.get("bull", {}).get("body", "").lower()
    assert "losses increase" in bear_body
    assert "losses increase" in bull_body
    for key in ["bear", "base", "bull"]:
        body = narrative.get(key, {}).get("body", "")
        _assert_no_stock_language(body)
