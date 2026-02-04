from core.analysis_pack import build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.roi import NET_PREMIUM
from reporting.contract_v1.adapter import build_report_contract_v1
from reporting.contract_v1.validate import validate_report_contract_v1
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


def test_report_contract_v1_validation():
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
    contract = build_report_contract_v1(report_model)
    validate_report_contract_v1(contract)
