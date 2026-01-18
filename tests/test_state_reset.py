from ui_state import reset_leg_state_on_context_change


def test_reset_leg_state_clears_tickers_and_premiums():
    state = {
        "bbg_ticker_0": "OLD",
        "bbg_ticker_input_0": "OLD",
        "bbg_ticker_val_0": "OLD",
        "prem_0": 1.25,
        "manual_prem_0": False,
        "strike_0": 100.0,
        "bbg_ticker_1": "KEEP",
        "prem_1": 2.5,
        "manual_prem_1": True,
        "strike_1": 110.0,
        "bbg_snapshot_df": "cached",
        "snapshot_cache": "cached",
    }

    changed = reset_leg_state_on_context_change(
        state, "SPY US Equity", "SPY US Equity", "2026-03-20", leg_count=2
    )
    assert changed is False
    assert state["bbg_ticker_0"] == "OLD"

    changed = reset_leg_state_on_context_change(
        state, "SPY US Equity", "SPY US Equity", "2026-04-17", leg_count=2
    )
    assert changed is True
    assert state["bbg_ticker_0"] == ""
    assert state["bbg_ticker_input_0"] == ""
    assert state["bbg_ticker_val_0"] == ""
    assert state["bbg_ticker_1"] == ""
    assert state["prem_0"] == 0.0
    assert state["prem_1"] == 2.5
    assert state["strike_0"] == 100.0
    assert state["strike_1"] == 110.0
    assert "bbg_snapshot_df" not in state
    assert "snapshot_cache" not in state
