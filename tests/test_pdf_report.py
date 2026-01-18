import os
import tempfile

import pandas as pd
import pytest

pytest.importorskip("reportlab")

from reporting.report_pdf import build_report_pdf


def test_build_report_pdf_creates_file():
    scenario_df = pd.DataFrame(
        {
            "price": [90 + i for i in range(10)],
            "option_pnl": [i * 10.0 for i in range(10)],
            "stock_pnl": [i * 5.0 for i in range(10)],
            "combined_pnl": [i * 15.0 for i in range(10)],
            "margin_requirement": [1000.0 for _ in range(10)],
            "option_roi": [0.01 * i for i in range(10)],
            "net_roi": [0.02 * i for i in range(10)],
            "commentary": [
                "Sample commentary text with enough length to expand the PDF output."
                for _ in range(10)
            ],
        }
    )
    inputs = {
        "ticker": "ABC",
        "resolved_ticker": "ABC US Equity",
        "strategy_name": "Covered Call",
        "expiry": "2025-01-01",
        "pricing_mode": "MID",
        "spot": 100.0,
        "stock_position": 100.0,
        "avg_cost": 100.0,
        "roi_policy": "NET_PREMIUM",
        "legs": [
            {"type": "Call", "side": "Short", "qty": -1, "strike": 110.0, "premium": 2.0}
        ],
    }
    summary = {
        "min_pnl": -500.0,
        "max_pnl": 800.0,
        "breakevens": [98.0, 112.0],
        "pop": "55.0%",
        "margin_proxy": 5000.0,
        "capital_basis": 8000.0,
    }
    notes = [
        "Expiry-only payoff; interim PnL is not modeled.",
        "Probability of profit is model-based and uses a lognormal distribution.",
        "Margin is a proxy and does not reflect broker-specific rules.",
        "This report is for informational purposes only and is not investment advice.",
    ]

    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    tmp_file.close()
    try:
        build_report_pdf(
            tmp_file.name,
            title="Options Strategy Report",
            as_of="2025-01-01 12:00:00",
            inputs=inputs,
            summary=summary,
            scenario_df=scenario_df,
            notes=notes,
        )
        assert os.path.exists(tmp_file.name)
        assert os.path.getsize(tmp_file.name) > 5 * 1024
    finally:
        if os.path.exists(tmp_file.name):
            os.remove(tmp_file.name)
