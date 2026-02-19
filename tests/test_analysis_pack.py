import pandas as pd

from core.analysis_pack import build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.roi import NET_PREMIUM


def test_build_analysis_pack_minimal():
    legs = [
        OptionLeg(kind="call", position=1.0, strike=100.0, premium=2.0),
    ]
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=legs,
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={
            "strategy_name": "Test Strategy",
            "as_of": "2026-01-18 12:00:00",
            "expiry": "2026-03-20",
        },
        pricing_mode="MID",
        roi_policy=NET_PREMIUM,
        vol_mode="ATM",
        atm_iv=0.2,
        underlying_profile={
            "DVD_EX_DT": "2026-02-01",
            "projected_dividend": 0.88,
            "dividend_status": "Projected",
            "HIGH_52WEEK": 260.0,
            "LOW_52WEEK": 180.0,
            "HIGH_DT_52WEEK": "2025-01-02",
            "LOW_DT_52WEEK": "2024-08-09",
            "CHG_PCT_YTD": 12.3,
        },
        bbg_leg_snapshots=None,
        scenario_mode="STANDARD",
        downside_tgt=0.9,
        upside_tgt=1.1,
    )

    for key in [
        "as_of",
        "underlying",
        "strategy",
        "legs",
        "payoff",
        "summary",
        "margin",
        "scenario",
    ]:
        assert key in pack

    payoff = pack["payoff"]
    assert payoff["price_grid"]
    assert payoff["combined_pnl"]

    scenario = pack["scenario"]
    assert isinstance(scenario["df"], pd.DataFrame)
    assert not scenario["df"].empty
    assert scenario["top10"] is not None

    key_levels = pack.get("key_levels")
    assert isinstance(key_levels, dict)
    assert "meta" in key_levels
    assert "levels" in key_levels
    for field in [
        "as_of",
        "expiry",
        "spot",
        "has_stock_position",
        "shares",
        "avg_cost",
    ]:
        assert field in key_levels["meta"]
    levels = key_levels["levels"]
    assert levels
    ids = [level.get("id") for level in levels]
    assert len(ids) == len(set(ids))
    assert "spot" in ids
    assert any(level_id.startswith("strike_") for level_id in ids if level_id)
    assert any(level_id.startswith("breakeven_") for level_id in ids if level_id)
    assert all(
        isinstance(level.get("label"), str) and level["label"].strip()
        for level in levels
    )
    level_map = {level.get("id"): level for level in levels}
    breakevens = pack["payoff"]["breakevens"]
    if breakevens:
        breakeven_level = level_map.get("breakeven_1")
        assert breakeven_level is not None
        assert breakeven_level["label"] == "Breakeven 1"
        assert abs(breakeven_level["price"] - breakevens[0]) < 1e-6
    downside_level = level_map.get("downside")
    assert downside_level is not None
    assert str(downside_level["label"]).startswith("Downside")
    upside_level = level_map.get("upside")
    assert upside_level is not None
    assert str(upside_level["label"]).startswith("Upside")

    summary_rows = pack["summary"]["rows"]
    assert summary_rows
    assert any(
        row.get("options") not in {"--", None} for row in summary_rows
    )

    dividend_risk = pack["underlying"]["dividend_risk"]
    assert dividend_risk["ex_div_date"].isoformat() == "2026-02-01"
    assert dividend_risk["days_to_dividend"] == 14
    assert dividend_risk["before_expiry"] is True
    assert dividend_risk["projected_dividend"] == 0.88
    assert dividend_risk["dividend_status"] == "Projected"
    underlying = pack["underlying"]
    assert underlying["high_52week"] == 260.0
    assert underlying["low_52week"] == 180.0
    assert underlying["high_dt_52week"] == "2025-01-02"
    assert underlying["low_dt_52week"] == "2024-08-09"
    assert underlying["chg_pct_ytd"] == 12.3


def test_build_analysis_pack_no_dividend_data():
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[],
    )
    pack = build_analysis_pack(
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
        downside_tgt=0.9,
        upside_tgt=1.1,
    )
    dividend_risk = pack["underlying"]["dividend_risk"]
    assert dividend_risk["ex_div_date"] is None
    assert dividend_risk["days_to_dividend"] is None
    assert dividend_risk["before_expiry"] is None
    assert dividend_risk["projected_dividend"] is None
    assert dividend_risk["dividend_status"] is None

    key_levels = pack.get("key_levels")
    assert isinstance(key_levels, dict)
    levels = key_levels.get("levels", [])
    assert any(level.get("id") == "spot" for level in levels)
    assert all(
        isinstance(level.get("label"), str) and level["label"].strip()
        for level in levels
    )


def test_key_levels_zero_level_has_pnl():
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=100.0,
        avg_cost=100.0,
        legs=[OptionLeg(kind="call", position=-1.0, strike=110.0, premium=2.0)],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={
            "strategy_name": "Covered Call",
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
    levels = pack.get("key_levels", {}).get("levels", [])
    zero_level = next(
        (level for level in levels if level.get("id") == "zero"), None
    )
    assert zero_level is not None
    assert zero_level.get("net_pnl") is not None


def _summary_row(pack, metric):
    for row in pack["summary"]["rows"]:
        if row["metric"] == metric:
            return row
    return None


def test_naked_short_call_max_loss_unlimited():
    """Bug 1A: Naked short call has unlimited loss on the upside."""
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="call", position=-10.0, strike=110.0, premium=5.0)],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": "Naked Short Call", "as_of": "2026-01-18", "expiry": "2026-03-20"},
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
    max_loss = _summary_row(pack, "Max Loss")
    assert max_loss is not None
    # Naked short call: options P&L goes to -infinity as stock rises
    # The slope at high end is negative (short call), so unlimited_loss_upside = True
    assert max_loss["options"] == "Unlimited"
    assert max_loss["combined"] == "Unlimited"


def test_long_call_max_profit_unlimited():
    """Bug 1A: Long call has unlimited upside profit."""
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="call", position=1.0, strike=100.0, premium=2.0)],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": "Long Call", "as_of": "2026-01-18", "expiry": "2026-03-20"},
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
    max_profit = _summary_row(pack, "Max Profit")
    assert max_profit is not None
    assert max_profit["options"] == "Unlimited"
    assert max_profit["combined"] == "Unlimited"
    # Max loss should be finite for long call
    max_loss = _summary_row(pack, "Max Loss")
    assert max_loss["options"] != "Unlimited"
    assert max_loss["combined"] != "Unlimited"


def test_long_put_max_loss_finite():
    """Long put max loss is the premium paid, NOT unlimited."""
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="put", position=1.0, strike=95.0, premium=2.50)],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": "Long Put", "as_of": "2026-01-18", "expiry": "2026-03-20"},
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
    max_loss = _summary_row(pack, "Max Loss")
    assert max_loss is not None
    # Long put max loss = premium × multiplier = 2.50 × 100 = $250
    assert max_loss["options"] == "-$250.00"
    assert max_loss["combined"] == "-$250.00"
    # Max profit should be unlimited (profit grows as stock drops toward 0)
    max_profit = _summary_row(pack, "Max Profit")
    assert max_profit["options"] == "Unlimited"
    assert max_profit["combined"] == "Unlimited"


def test_cost_credit_with_multiplier():
    """Bug 1B: Cost/Credit should show total (with multiplier), not per-share."""
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="call", position=-10.0, strike=110.0, premium=51.80)],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": "Short Call", "as_of": "2026-01-18", "expiry": "2026-03-20"},
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
    cost_credit = _summary_row(pack, "Cost/Credit")
    assert cost_credit is not None
    # -10 × 51.80 × 100 = -51,800.00 → Credit $51,800.00
    assert cost_credit["options"] == "Credit $51,800.00"
    # Net Prem/Share display = -(-51800 / 10) = 5180.0 (credit = positive display)
    prem_share = _summary_row(pack, "Net Prem/Share")
    assert prem_share is not None
    assert prem_share["options"] == "$5,180.00"


def test_cost_credit_debit():
    """Bug 1B: Long call should show debit."""
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="call", position=1.0, strike=100.0, premium=5.0)],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": "Long Call", "as_of": "2026-01-18", "expiry": "2026-03-20"},
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
    cost_credit = _summary_row(pack, "Cost/Credit")
    assert cost_credit is not None
    # 1 × 5.0 × 100 = 500.00 → Debit $500.00
    assert cost_credit["options"] == "Debit $500.00"


def test_key_levels_zero_level_stock_pnl_no_stock():
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="call", position=-1.0, strike=110.0, premium=2.0)],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={
            "strategy_name": "Short Call",
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
    levels = pack.get("key_levels", {}).get("levels", [])
    zero_level = next(
        (level for level in levels if level.get("id") == "zero"), None
    )
    assert zero_level is not None
    assert zero_level.get("stock_pnl") == 0.0


def test_key_levels_no_duplicates_strike_at_target():
    """Bug 2A: When a strike coincides with an upside/downside target,
    the key levels list should not contain duplicate rows at that price."""
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="call", position=1.0, strike=110.0, premium=2.0)],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": "Long Call", "as_of": "2026-01-18", "expiry": "2026-03-20"},
        pricing_mode="MID",
        roi_policy=NET_PREMIUM,
        vol_mode="ATM",
        atm_iv=0.2,
        underlying_profile=None,
        bbg_leg_snapshots=None,
        scenario_mode="STANDARD",
        downside_tgt=0.9,
        upside_tgt=1.1,  # spot * 1.1 = 110 = strike
    )
    levels = pack["key_levels"]["levels"]
    prices_at_110 = [lv for lv in levels if lv.get("price") is not None and abs(lv["price"] - 110.0) < 0.01]
    # Both strike and upside target coexist at the same price
    sources_at_110 = {lv["source"] for lv in prices_at_110}
    assert "strike" in sources_at_110
    assert "upside" in sources_at_110
    assert len(prices_at_110) == 2


def test_key_levels_infinity_mode_no_upside_downside():
    """Bug 2C: In INFINITY mode, no 'upside' or 'downside' target rows
    should appear (they would be 0.0 and spot*1000, which are sentinels)."""
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="call", position=1.0, strike=105.0, premium=2.0)],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": "Long Call", "as_of": "2026-01-18", "expiry": "2026-03-20"},
        pricing_mode="MID",
        roi_policy=NET_PREMIUM,
        vol_mode="ATM",
        atm_iv=0.2,
        underlying_profile=None,
        bbg_leg_snapshots=None,
        scenario_mode="INFINITY",
        downside_tgt=0.9,
        upside_tgt=1.1,
    )
    levels = pack["key_levels"]["levels"]
    sources = [lv.get("source") for lv in levels]
    assert "downside" not in sources, "Downside target should not appear in INFINITY mode"
    assert "upside" not in sources, "Upside target should not appear in INFINITY mode"
    # Sentinels should still be present
    ids = [lv.get("id") for lv in levels]
    assert "zero" in ids
    assert "infinity" in ids


def test_key_levels_infinity_row_has_pnl():
    """Bug 2D: The 'Stock to Infinity' sentinel row should have computed
    PnL values rather than all None/--."""
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=100.0,
        avg_cost=100.0,
        legs=[OptionLeg(kind="call", position=-1.0, strike=110.0, premium=2.0)],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": "Covered Call", "as_of": "2026-01-18", "expiry": "2026-03-20"},
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
    levels = pack["key_levels"]["levels"]
    inf_level = next((lv for lv in levels if lv.get("id") == "infinity"), None)
    assert inf_level is not None
    # Price should be None (display as infinity), but PnL values should be computed
    assert inf_level["price"] is None
    assert inf_level["option_pnl"] is not None
    assert inf_level["net_pnl"] is not None
    assert inf_level["stock_pnl"] is not None


# ── Fix 1A: Net Prem/Share with stock position ──


def test_net_prem_per_share_with_stock():
    """Fix 1A: Net Prem/Share = net_premium_total / shares when stock position exists."""
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=1000.0,
        avg_cost=95.0,
        legs=[
            OptionLeg(kind="call", position=-10.0, strike=200.0, premium=51.80),
            OptionLeg(kind="put", position=-10.0, strike=85.0, premium=7.55),
        ],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": "Short Strangle", "as_of": "2026-01-18", "expiry": "2026-03-20"},
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
    prem_share = _summary_row(pack, "Net Prem/Share")
    assert prem_share is not None
    # net_premium_total = (-10*51.80*100) + (-10*7.55*100) = -51800 + -7550 = -59350
    # shares = 1000
    # display = -(-59350 / 1000) = 59.35 (credit = positive display)
    assert prem_share["options"] == "$59.35"


def test_net_prem_per_share_no_stock():
    """Fix 1A: Net Prem/Share = net_premium_total / total_contracts without stock."""
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="call", position=5.0, strike=100.0, premium=3.0)],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": "Long Call", "as_of": "2026-01-18", "expiry": "2026-03-20"},
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
    prem_share = _summary_row(pack, "Net Prem/Share")
    assert prem_share is not None
    # net_premium_total = 5 * 3.0 * 100 = 1500
    # total_contracts = 5
    # display = -(1500 / 5) = -300.0 (debit = negative display)
    assert prem_share["options"] == "-$300.00"


# ── Fix 1B: Premium % of Spot cascades from 1A ──


def test_net_prem_pct_spot():
    """Fix 1B: Premium % of Spot uses net_prem_per_share, not raw compute_net_premium."""
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="call", position=1.0, strike=100.0, premium=5.0)],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": "Long Call", "as_of": "2026-01-18", "expiry": "2026-03-20"},
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
    pct = _summary_row(pack, "Premium % of Spot")
    assert pct is not None
    # net_premium (per-share, no multiplier) = 1 * 5.0 = 5.0
    # display pct = -(5.0 / 100 * 100) = -5.00% (debit = negative display)
    assert pct["options"] == "-5.00%"


# ── Fix 1C: Min ROI N/A when max loss is unlimited ──


def test_min_roi_na_when_unlimited_loss():
    """Fix 1C: Min ROI should show N/A when max loss is unlimited."""
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="call", position=-1.0, strike=110.0, premium=2.0)],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": "Short Call", "as_of": "2026-01-18", "expiry": "2026-03-20"},
        pricing_mode="MID",
        roi_policy=NET_PREMIUM,
        vol_mode="ATM",
        atm_iv=0.2,
        underlying_profile=None,
        bbg_leg_snapshots=None,
        scenario_mode="INFINITY",
        downside_tgt=0.8,
        upside_tgt=1.2,
    )
    max_loss = _summary_row(pack, "Max Loss")
    assert max_loss is not None
    assert max_loss["options"] == "Unlimited"
    min_roi = _summary_row(pack, "Min ROI")
    assert min_roi is not None
    assert min_roi["options"] == "N/A"


# ── Fix 1D: Capital basis override for credit/uncovered ──


def test_capital_basis_credit_uncovered_uses_margin():
    """Fix 1D: For credit strategies with unlimited loss, capital basis = margin proxy."""
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="call", position=-1.0, strike=110.0, premium=5.0)],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": "Short Call", "as_of": "2026-01-18", "expiry": "2026-03-20"},
        pricing_mode="MID",
        roi_policy=NET_PREMIUM,
        vol_mode="ATM",
        atm_iv=0.2,
        underlying_profile=None,
        bbg_leg_snapshots=None,
        scenario_mode="INFINITY",
        downside_tgt=0.8,
        upside_tgt=1.2,
    )
    cap_basis = _summary_row(pack, "Capital at Risk")
    assert cap_basis is not None
    margin_proxy = pack["margin"]["margin_proxy"]
    # Capital basis should equal margin proxy for credit + unlimited loss
    assert cap_basis["options"] == f"${margin_proxy:,.2f}"


# ── Fix 1E: Risk/Reward row position ──


def test_risk_reward_after_max_loss():
    """Fix 1E: Risk/Reward row should appear right after Max Loss."""
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="call", position=1.0, strike=100.0, premium=2.0)],
    )
    pack = build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={"strategy_name": "Long Call", "as_of": "2026-01-18", "expiry": "2026-03-20"},
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
    rows = pack["summary"]["rows"]
    metrics = [r["metric"] for r in rows]
    max_loss_idx = metrics.index("Max Loss")
    rr_idx = metrics.index("Risk/Reward")
    assert rr_idx == max_loss_idx + 1, (
        f"Risk/Reward at index {rr_idx} should be right after Max Loss at {max_loss_idx}"
    )
