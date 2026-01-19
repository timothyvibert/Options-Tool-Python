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
        "commentary_blocks",
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
