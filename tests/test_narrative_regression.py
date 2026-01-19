import json
import os
from pathlib import Path

from core.analysis_pack import build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.roi import NET_PREMIUM


def _build_pack(strategy_input: StrategyInput):
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
    assert "called away" not in lowered
    assert "stock-only" not in lowered
    assert "overlay" not in lowered


def _assert_expiry_language(text: str) -> None:
    assert "at expiry" in text.lower()

# To dump artifacts:
# PowerShell: set NARRATIVE_REGRESSION_DUMP=1; python -m pytest -q tests/test_narrative_regression.py
# Bash: NARRATIVE_REGRESSION_DUMP=1 python -m pytest -q tests/test_narrative_regression.py


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


def _has_premium_contradiction(text: str) -> bool:
    lowered = text.lower()
    if "realized" not in lowered:
        return False
    return (" paid" in lowered) or (" received" in lowered)


def _should_dump_artifacts() -> bool:
    value = os.getenv("NARRATIVE_REGRESSION_DUMP", "").strip().lower()
    return value in {"1", "true", "yes", "y", "on"}


def _extract_anchors(pack: dict) -> dict:
    key_levels = pack.get("key_levels", {})
    levels = key_levels.get("levels", []) if isinstance(key_levels, dict) else []
    strikes = []
    breakevens = []
    spot = None
    for level in levels:
        if not isinstance(level, dict):
            continue
        label = str(level.get("label") or level.get("scenario") or "").lower()
        price = level.get("price")
        if label == "current market price":
            spot = price
        if "strike" in label and price is not None:
            strikes.append(price)
        if "breakeven" in label and price is not None:
            breakevens.append(price)
    strikes_sorted = sorted(strikes)
    breakevens_sorted = sorted(breakevens)
    return {
        "spot": spot,
        "lower_strike": strikes_sorted[0] if strikes_sorted else None,
        "upper_strike": strikes_sorted[-1] if strikes_sorted else None,
        "breakeven": breakevens_sorted,
    }


def _coverage_info(strategy_input: StrategyInput, narrative: dict) -> dict:
    trace = narrative.get("trace", {}) if isinstance(narrative, dict) else {}
    coverage = trace.get("coverage", {}) if isinstance(trace, dict) else {}
    shares = abs(strategy_input.stock_position)
    if not shares:
        return {
            "coverage_ratio": None,
            "covered_shares_call": None,
            "protected_shares_put": None,
            "collared_shares": None,
            "coverage_phrase": None,
        }
    short_calls = sum(
        abs(leg.position) for leg in strategy_input.legs if leg.kind.lower() == "call" and leg.position < 0
    )
    long_puts = sum(
        abs(leg.position) for leg in strategy_input.legs if leg.kind.lower() == "put" and leg.position > 0
    )
    covered_shares_call = int(round(short_calls * 100)) if short_calls else None
    protected_shares_put = int(round(long_puts * 100)) if long_puts else None
    collared_shares = None
    if covered_shares_call and protected_shares_put:
        collared_shares = min(covered_shares_call, protected_shares_put, int(shares))
    coverage_shares = collared_shares or covered_shares_call or protected_shares_put
    coverage_ratio = None
    coverage_phrase = None
    if shares and coverage_shares:
        coverage_ratio = coverage_shares / shares
        pct = int(round(coverage_ratio * 100))
        if coverage_ratio >= 0.99:
            coverage_phrase = f"full position ({int(shares):,} of {int(shares):,} shares)"
        else:
            coverage_phrase = f"~{pct}% of the position ({int(coverage_shares):,} of {int(shares):,} shares)"
    return {
        "coverage_ratio": coverage.get("coverage_ratio", coverage_ratio),
        "covered_shares_call": covered_shares_call,
        "protected_shares_put": protected_shares_put,
        "collared_shares": collared_shares,
        "coverage_phrase": coverage.get("coverage_clause") or coverage_phrase,
    }


def _scenario_payload(narrative: dict, key: str) -> dict:
    scenario = narrative.get(key, {}) if isinstance(narrative, dict) else {}
    trace = narrative.get("trace") if isinstance(narrative, dict) else None
    return {
        "title": scenario.get("title"),
        "condition": scenario.get("condition"),
        "body": scenario.get("body"),
        "rule_trace": trace,
    }


def test_narrative_regression_harness():
    artifact_results = {}
    cases = [
        {
            "name": "collar_partial",
            "input": StrategyInput(
                spot=625.0,
                stock_position=1000.0,
                avg_cost=620.0,
                legs=[
                    OptionLeg(kind="put", position=8.0, strike=600.0, premium=4.0),
                    OptionLeg(kind="call", position=-8.0, strike=650.0, premium=3.0),
                ],
            ),
            "partial_phrase": "(800 of 1,000 shares)",
            "options_only": False,
            "covered_call": False,
            "debit_spread": False,
        },
        {
            "name": "covered_call_full",
            "input": StrategyInput(
                spot=35.0,
                stock_position=1000.0,
                avg_cost=35.0,
                legs=[OptionLeg(kind="call", position=-10.0, strike=40.0, premium=1.2)],
            ),
            "partial_phrase": None,
            "options_only": False,
            "covered_call": True,
            "debit_spread": False,
        },
        {
            "name": "protective_put_partial",
            "input": StrategyInput(
                spot=35.0,
                stock_position=1000.0,
                avg_cost=35.0,
                legs=[OptionLeg(kind="put", position=8.0, strike=30.0, premium=1.5)],
            ),
            "partial_phrase": "(800 of 1,000 shares)",
            "options_only": False,
            "covered_call": False,
            "debit_spread": False,
        },
        {
            "name": "bull_call_spread_debit",
            "input": StrategyInput(
                spot=100.0,
                stock_position=0.0,
                avg_cost=0.0,
                legs=[
                    OptionLeg(kind="call", position=1.0, strike=100.0, premium=3.0),
                    OptionLeg(kind="call", position=-1.0, strike=110.0, premium=1.0),
                ],
            ),
            "partial_phrase": None,
            "options_only": True,
            "covered_call": False,
            "debit_spread": True,
        },
        {
            "name": "iron_condor_credit",
            "input": StrategyInput(
                spot=100.0,
                stock_position=0.0,
                avg_cost=0.0,
                legs=[
                    OptionLeg(kind="put", position=1.0, strike=90.0, premium=1.0),
                    OptionLeg(kind="put", position=-1.0, strike=95.0, premium=2.0),
                    OptionLeg(kind="call", position=-1.0, strike=105.0, premium=2.0),
                    OptionLeg(kind="call", position=1.0, strike=110.0, premium=1.0),
                ],
            ),
            "partial_phrase": None,
            "options_only": True,
            "covered_call": False,
            "debit_spread": False,
        },
    ]

    banned_phrases = [
        "can lose value",
        "may decay",
        "time value",
        "could retain value",
        "might lose value",
    ]

    for case in cases:
        pack = _build_pack(case["input"])
        narrative = pack.get("narrative_scenarios")
        assert narrative is not None
        trace = narrative.get("trace", {})
        coverage = trace.get("coverage", {}) if isinstance(trace, dict) else {}
        coverage_info = _coverage_info(case["input"], narrative)
        if case["options_only"]:
            assert coverage.get("coverage_clause") in {None, ""}
            assert coverage_info["covered_shares_call"] is None
            assert coverage_info["protected_shares_put"] is None
            assert coverage_info["collared_shares"] is None
        if case["name"] == "bull_call_spread_debit":
            assert trace.get("rule_id") != "fallback_generic"
        for key in ["bear", "base", "bull"]:
            scenario = narrative.get(key)
            assert scenario is not None
            condition = scenario.get("condition", "")
            body = scenario.get("body", "")
            assert condition
            assert "Downside (" not in condition
            assert "Upside (" not in condition
            _assert_expiry_language(body)
            for phrase in banned_phrases:
                assert phrase not in body.lower()
            if case["options_only"]:
                _assert_no_stock_language(body)
            if case["covered_call"]:
                assert "maximum loss" not in body.lower()
            if case["debit_spread"]:
                if key == "bear":
                    assert "debit" in body.lower()
                assert "retain premium" not in body.lower()
            assert not (_has_overlay_delta(body) and _has_breakdown(body))
            assert not _has_premium_contradiction(body)
            if case["partial_phrase"]:
                assert case["partial_phrase"] in body

        if case["debit_spread"]:
            bull_body = narrative.get("bull", {}).get("body", "").lower()
            assert "capped" in bull_body
            assert "maximum profit" in bull_body

        artifact_results[case["name"]] = {
            "case_name": case["name"],
            "bearish": _scenario_payload(narrative, "bear"),
            "stagnant": _scenario_payload(narrative, "base"),
            "bullish": _scenario_payload(narrative, "bull"),
            "coverage": coverage_info,
            "anchors": _extract_anchors(pack),
        }

    if _should_dump_artifacts():
        out_path = Path("tests") / "artifacts" / "narrative_regression.json"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with out_path.open("w", encoding="utf-8") as handle:
            json.dump(artifact_results, handle, indent=2, sort_keys=True, default=str)
