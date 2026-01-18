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
        underlying_profile=None,
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

    summary_rows = pack["summary"]["rows"]
    assert summary_rows
    assert any(
        row.get("options") not in {"--", None} for row in summary_rows
    )
