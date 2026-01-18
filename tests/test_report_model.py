import pandas as pd

from reporting.report_model import build_report_model


def test_report_model_minimal_state():
    state = {
        "underlying_ticker": "SPY US Equity",
        "spot_value": 100.0,
        "analysis_strategy_name": "Test Strategy",
        "chain_expiry": "2026-03-20",
        "analysis_scenario_df": [],
        "analysis_payoff": {
            "price_grid": [90.0, 100.0, 110.0],
            "combined_pnl": [-10.0, 0.0, 10.0],
            "strikes": [100.0],
            "breakevens": [100.0],
        },
    }
    model = build_report_model(state)
    for key in [
        "page_meta",
        "header",
        "structure",
        "payoff",
        "metrics",
        "key_levels",
        "scenario_table",
        "commentary_blocks",
        "disclaimers",
    ]:
        assert key in model

    header = model["header"]
    for key in ["ticker", "last_price", "strategy_name", "expiry"]:
        assert key in header

    scenario_table = model["scenario_table"]
    assert isinstance(scenario_table["top10"], list)

    payoff = model["payoff"]
    assert payoff["price_grid"]


def test_report_model_dataframe_scenario():
    scenario_df = pd.DataFrame(
        [
            {
                "Scenario": "Spot",
                "Price": 100.0,
                "Move %": "0.00%",
                "Stock PnL": 0.0,
                "Option PnL": 1.0,
                "Option ROI": "1.00%",
                "Net PnL": 1.0,
                "Net ROI": "1.00%",
            }
        ]
    )
    state = {
        "underlying_ticker": "SPY US Equity",
        "spot_value": 100.0,
        "analysis_strategy_name": "Test Strategy",
        "chain_expiry": "2026-03-20",
        "analysis_scenario_df": scenario_df,
        "analysis_payoff": {
            "price_grid": [90.0, 100.0, 110.0],
            "combined_pnl": [-10.0, 0.0, 10.0],
            "strikes": [100.0],
            "breakevens": [100.0],
        },
    }
    model = build_report_model(state)
    assert model["scenario_table"]["top10"]
