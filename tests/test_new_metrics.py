"""Tests for new summary metrics: Risk/Reward, Breakeven, Treasury, auto capital basis."""

import pytest

from core.analysis_pack import (
    _auto_capital_basis,
    _risk_reward,
    build_analysis_pack,
)
from core.models import OptionLeg, StrategyInput
from core.roi import CASH_SECURED, NET_PREMIUM


# ── Unit tests for _risk_reward ──


def test_risk_reward_normal():
    assert _risk_reward(1000, -500) == "2.00x"


def test_risk_reward_zero_loss():
    assert _risk_reward(500, 0) == "\u221e"


def test_risk_reward_zero_both():
    assert _risk_reward(0, 0) == "N/A"


def test_risk_reward_loss_only():
    assert _risk_reward(0, -200) == "0.00x"


# ── Unit tests for _auto_capital_basis ──


def test_auto_capital_basis_cash_secured_put():
    legs = [OptionLeg(kind="put", position=-1, strike=90, premium=3)]
    result = _auto_capital_basis("CSP", legs, shares=0, avg_cost=0, margin_proxy=5000)
    assert result["mode"] == "cash_secured"
    assert result["amount"] == 90 * 1 * 100  # 9000
    assert "Cash-Secured" in result["label"]


def test_auto_capital_basis_covered_call():
    legs = [OptionLeg(kind="call", position=-1, strike=110, premium=2)]
    result = _auto_capital_basis("CC", legs, shares=100, avg_cost=100, margin_proxy=5000)
    assert result["mode"] == "stock_cost"
    assert result["amount"] == 100 * 100  # 10000


def test_auto_capital_basis_bull_call_spread():
    legs = [
        OptionLeg(kind="call", position=1, strike=100, premium=5),
        OptionLeg(kind="call", position=-1, strike=110, premium=2),
    ]
    result = _auto_capital_basis("BCS", legs, shares=0, avg_cost=0, margin_proxy=300)
    assert result["mode"] == "max_loss"
    assert result["amount"] == 300


def test_auto_capital_basis_default():
    legs = [OptionLeg(kind="call", position=1, strike=100, premium=5)]
    result = _auto_capital_basis("UNKNOWN", legs, shares=0, avg_cost=0, margin_proxy=2000)
    assert result["mode"] == "margin"
    assert result["amount"] == 2000


# ── Integration tests: new rows in analysis pack ──


def _build_pack(**overrides):
    """Helper to build analysis pack with sensible defaults."""
    defaults = dict(
        strategy_input=StrategyInput(
            spot=100.0,
            stock_position=0.0,
            avg_cost=0.0,
            legs=[OptionLeg(kind="call", position=1, strike=100, premium=2)],
        ),
        strategy_meta={
            "strategy_name": "Long Call",
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
        downside_tgt=0.9,
        upside_tgt=1.1,
    )
    defaults.update(overrides)
    return build_analysis_pack(**defaults)


def _metric_row(pack, name):
    for row in pack["summary"]["rows"]:
        if row.get("metric") == name:
            return row
    return None


def test_risk_reward_in_summary():
    pack = _build_pack()
    row = _metric_row(pack, "Risk/Reward")
    assert row is not None
    # Long call: max profit >> max loss, so ratio should be a number
    assert row["options"] not in ("", None)
    assert row["combined"] not in ("", None)


def test_closest_breakeven_in_summary():
    pack = _build_pack()
    row = _metric_row(pack, "Closest Breakeven")
    assert row is not None
    # Long call at 100 strike, 2 premium -> breakeven at 102
    assert row["options"].startswith("$")


def test_be_distance_in_summary():
    pack = _build_pack()
    row = _metric_row(pack, "BE Distance %")
    assert row is not None
    # Should be a +/- percentage
    assert "%" in row["options"]


def test_no_treasury_for_long_call():
    pack = _build_pack()
    # Long call is NOT cash-secured, so no treasury rows
    assert _metric_row(pack, "Treasury Obligation") is None
    assert _metric_row(pack, "Treasury Interest") is None
    assert _metric_row(pack, "Treasury Return %") is None


def test_treasury_for_cash_secured_put():
    pack = _build_pack(
        strategy_input=StrategyInput(
            spot=100.0,
            stock_position=0.0,
            avg_cost=0.0,
            legs=[OptionLeg(kind="put", position=-1, strike=95, premium=3)],
        ),
        strategy_meta={
            "strategy_name": "Cash Secured Put",
            "as_of": "2026-01-18",
            "expiry": "2026-03-20",
        },
        roi_policy=CASH_SECURED,
        risk_free_rate=0.05,
    )
    treasury_row = _metric_row(pack, "Treasury Obligation")
    assert treasury_row is not None
    # 1 short put at 95 strike, multiplier 100 => $9,500.00
    assert treasury_row["options"] == "$9,500.00"

    interest_row = _metric_row(pack, "Treasury Interest")
    assert interest_row is not None
    assert interest_row["options"].startswith("$")

    pct_row = _metric_row(pack, "Treasury Return %")
    assert pct_row is not None
    assert "%" in pct_row["options"]


def test_auto_capital_basis_in_policies():
    pack = _build_pack()
    policies = pack.get("policies", {})
    auto_basis = policies.get("auto_capital_basis")
    assert auto_basis is not None
    assert "mode" in auto_basis
    assert "amount" in auto_basis
    assert "label" in auto_basis


def test_breakeven_present_or_na():
    """Closest Breakeven is either a dollar value or N/A depending on strategy."""
    pack = _build_pack(
        strategy_input=StrategyInput(
            spot=100.0,
            stock_position=0.0,
            avg_cost=0.0,
            legs=[],
        ),
    )
    be_row = _metric_row(pack, "Closest Breakeven")
    assert be_row is not None
    # With no legs, breakeven value is either N/A or a dollar amount
    assert be_row["options"] == "N/A" or be_row["options"].startswith("$")

    dist_row = _metric_row(pack, "BE Distance %")
    assert dist_row is not None
    assert dist_row["options"] == "N/A" or "%" in dist_row["options"]
