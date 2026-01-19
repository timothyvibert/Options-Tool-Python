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


def test_report_model_dividend_warning():
    state = {
        "analysis_pack": {
            "underlying": {
                "dividend_risk": {
                    "ex_div_date": "2026-03-13",
                    "before_expiry": True,
                }
            }
        }
    }
    model = build_report_model(state)
    warnings = model.get("warnings", {})
    assert warnings.get("dividend")


def test_report_model_no_dividend_warning():
    state = {
        "analysis_pack": {
            "underlying": {
                "dividend_risk": {
                    "ex_div_date": "2026-03-13",
                    "before_expiry": False,
                }
            }
        }
    }
    model = build_report_model(state)
    warnings = model.get("warnings", {})
    assert warnings.get("dividend") is None


def test_report_model_scenario_analysis_cards():
    state = {
        "analysis_pack": {
            "narrative_scenarios": {
                "Bearish": {
                    "title": "Bearish Case",
                    "condition": "If stock falls",
                    "body": "Downside narrative.",
                },
                "Stagnant": {
                    "title": "Stagnant Case",
                    "condition": "If stock stays",
                    "body": "Neutral narrative.",
                },
                "Bullish": {
                    "title": "Bullish Case",
                    "condition": "If stock rises",
                    "body": "Upside narrative.",
                },
            }
        }
    }
    model = build_report_model(state)
    cards = model.get("scenario_analysis_cards")
    assert isinstance(cards, list)
    assert len(cards) == 3
    assert [card.get("title") for card in cards] == [
        "Bearish Case",
        "Stagnant Case",
        "Bullish Case",
    ]
    for card in cards:
        assert isinstance(card.get("title"), str)
        assert isinstance(card.get("condition"), str)
        assert isinstance(card.get("body"), str)


def test_report_model_key_levels_rows():
    levels = [
        {"id": "spot", "label": "Spot", "price": 100.0},
        {"id": "downside", "label": "Downside (20%)", "price": 80.0},
    ]
    state = {"analysis_pack": {"key_levels": {"levels": levels}}}
    model = build_report_model(state)
    assert model.get("key_levels_rows") == levels
    display_rows = model.get("key_levels_display_rows")
    assert isinstance(display_rows, list)
    assert len(display_rows) == 2


def test_report_model_key_levels_display_formatting():
    levels = [
        {
            "id": "spot",
            "label": "Spot",
            "price": 100.0,
            "move_pct": 0.0,
            "stock_pnl": 1e-10,
            "option_pnl": -1e-8,
            "net_pnl": 1e-7,
            "option_roi": 0.1,
            "net_roi": 5.0,
        }
    ]
    state = {"analysis_pack": {"key_levels": {"levels": levels}}}
    model = build_report_model(state)
    display_rows = model.get("key_levels_display_rows")
    assert display_rows
    row = display_rows[0]
    assert row["Price"] == "100.00"
    assert row["Move %"] == "0.0"
    assert row["Stock PnL"] == "0.00"
    assert row["Option PnL"] == "0.00"
    assert row["Net PnL"] == "0.00"
    assert row["Option ROI"].endswith("%")
    assert row["Option ROI"] == "10.0%"
    assert row["Net ROI"] == "5.0%"


def test_report_model_scenario_analysis_missing():
    state = {"analysis_pack": {}}
    model = build_report_model(state)
    assert model.get("scenario_analysis_cards") == []
    assert model.get("key_levels_rows") == []


def test_report_model_key_levels_order_preserved():
    levels = [
        {"id": "spot", "label": "Current Market Price", "price": 100.0},
        {"id": "downside", "label": "Downside (20%)", "price": 80.0},
        {"id": "upside", "label": "Upside (20%)", "price": 120.0},
        {"id": "strike_1", "label": "Strike (Lowest)", "price": 90.0},
    ]
    state = {"analysis_pack": {"key_levels": {"levels": levels}}}
    model = build_report_model(state)
    key_levels_rows = model.get("key_levels_rows")
    assert [row.get("label") for row in key_levels_rows] == [
        "Current Market Price",
        "Downside (20%)",
        "Upside (20%)",
        "Strike (Lowest)",
    ]
    display_rows = model.get("key_levels_display_rows")
    assert [row.get("Scenario") for row in display_rows] == [
        "Downside (20%)",
        "Strike (Lowest)",
        "Current Market Price",
        "Upside (20%)",
    ]


def test_report_model_key_levels_by_price_ordering():
    levels = [
        {"id": "spot", "label": "Current Market Price", "price": 35.71},
        {"id": "downside", "label": "Downside (20%)", "price": 28.568},
        {"id": "upside", "label": "Upside (20%)", "price": 42.852},
        {"id": "strike_1", "label": "Strike (Lowest)", "price": 30.0},
        {"id": "strike_2", "label": "Strike (Lower Middle)", "price": 32.0},
        {"id": "strike_3", "label": "Strike (Upper Middle)", "price": 38.0},
        {"id": "strike_4", "label": "Strike (Highest)", "price": 40.0},
        {"id": "breakeven_1", "label": "Breakeven 1", "price": 31.855},
        {"id": "breakeven_2", "label": "Breakeven 2", "price": 38.145},
        {"id": "zero", "label": "Stock to Zero", "price": 0.0},
        {"id": "infinity", "label": "Stock to Infinity", "price": None},
    ]
    state = {"analysis_pack": {"key_levels": {"levels": levels}}}
    model = build_report_model(state)
    assert model.get("key_levels_rows") == levels
    ordered = model.get("key_levels_rows_by_price")
    assert [row.get("label") for row in ordered] == [
        "Stock to Zero",
        "Downside (20%)",
        "Strike (Lowest)",
        "Breakeven 1",
        "Strike (Lower Middle)",
        "Current Market Price",
        "Strike (Upper Middle)",
        "Breakeven 2",
        "Strike (Highest)",
        "Upside (20%)",
        "Stock to Infinity",
    ]
    display_rows = model.get("key_levels_display_rows")
    assert [row.get("Scenario") for row in display_rows] == [
        "Stock to Zero",
        "Downside (20%)",
        "Strike (Lowest)",
        "Breakeven 1",
        "Strike (Lower Middle)",
        "Current Market Price",
        "Strike (Upper Middle)",
        "Breakeven 2",
        "Strike (Highest)",
        "Upside (20%)",
        "Stock to Infinity",
    ]
