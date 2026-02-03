import pytest

from core.analysis_pack import build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.roi import NET_PREMIUM
from reporting.html_v2.renderer import build_report_pdf_html
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


def test_report_pdf_html_v2_smoke():
    pytest.importorskip("weasyprint")
    pytest.importorskip("jinja2")

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

    try:
        pdf_bytes = build_report_pdf_html(report_model)
    except RuntimeError as exc:
        message = str(exc)
        if "system libraries are missing" in message:
            pytest.skip(message)
        raise

    assert pdf_bytes.startswith(b"%PDF")
    assert len(pdf_bytes) > 20000
