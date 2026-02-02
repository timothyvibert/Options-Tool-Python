import pandas as pd
import pytest

from core.analysis_pack import build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.roi import NET_PREMIUM
from reporting.report_model import build_report_model


def _build_pack() -> dict:
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=[OptionLeg(kind="call", position=1.0, strike=105.0, premium=3.0)],
    )
    return build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={
            "strategy_name": "Long Call",
            "as_of": "2025-01-02",
            "expiry": "2025-06-21",
            "underlying_ticker": "TEST",
            "resolved_underlying": "TEST US Equity",
        },
        pricing_mode="MID",
        roi_policy=NET_PREMIUM,
        vol_mode="ATM",
        atm_iv=0.2,
        underlying_profile={},
        bbg_leg_snapshots=None,
        scenario_mode="STANDARD",
        downside_tgt=0.8,
        upside_tgt=1.2,
    )


def test_report_model_v2_fields():
    pack = _build_pack()
    report_model = build_report_model(
        {
            "analysis_pack": pack,
            "underlying_snapshot": {},
            "spot": 100.0,
            "expiry": "2025-06-21",
            "ticker": "TEST",
            "resolved_underlying": "TEST US Equity",
        }
    )

    scenario_table = report_model.get("scenario_table")
    assert isinstance(scenario_table, dict)
    top10 = scenario_table.get("top10_df")
    assert isinstance(top10, pd.DataFrame)
    assert "move_pct" in top10.columns
    spot_mask = (top10["price"] - 100.0).abs() <= 1e-6
    assert spot_mask.any()
    assert top10.loc[spot_mask, "move_pct"].iloc[0] == pytest.approx(0.0, abs=1e-6)

    structure = report_model.get("structure")
    assert isinstance(structure, dict)
    legs = structure.get("legs")
    assert isinstance(legs, list) and legs
    for leg in legs:
        assert leg.get("Expiry") == "2025-06-21"

    commentary_blocks = report_model.get("commentary_blocks")
    assert isinstance(commentary_blocks, dict)
    assert isinstance(commentary_blocks.get("blocks"), list)
