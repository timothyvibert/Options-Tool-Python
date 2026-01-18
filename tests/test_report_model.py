from reporting.report_model import build_report_model


def test_report_model_minimal_state():
    state = {
        "underlying_ticker": "SPY US Equity",
        "spot_value": 100.0,
        "analysis_strategy_name": "Test Strategy",
        "chain_expiry": "2026-03-20",
        "analysis_scenario_table": [],
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
