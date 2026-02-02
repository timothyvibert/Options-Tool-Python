import os
import tempfile

import pytest

from core.analysis_pack import build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.roi import NET_PREMIUM
from reporting.report_model import build_report_model
from reporting.report_pdf import build_report_pdf_v2


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


def test_report_pdf_v2_smoke():
    reportlab = pytest.importorskip("reportlab")
    assert reportlab is not None

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
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp_path = tmp.name
    try:
        build_report_pdf_v2(tmp_path, report_model=report_model)
        assert os.path.exists(tmp_path)
        size = os.path.getsize(tmp_path)
        assert size > 10_000
        with open(tmp_path, "rb") as handle:
            payload = handle.read()
        page_count = payload.count(b"/Type /Page") - payload.count(b"/Type /Pages")
        assert page_count == 2
        assert b"Page 3 of 2" not in payload
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
