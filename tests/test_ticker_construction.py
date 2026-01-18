import pandas as pd

import adapters.bloomberg as bloomberg


def test_construct_option_ticker_spy_example():
    ticker = bloomberg.construct_option_ticker(
        "SPY US Equity", "2026-03-20", "PUT", 685
    )
    assert ticker == "SPY US 3/20/26 P685 Equity"


def test_resolve_option_ticker_from_strike_offsets(monkeypatch):
    calls = []

    def fake_validate(tickers):
        calls.append(tickers)
        if len(calls) == 1:
            return pd.DataFrame(columns=["security"])
        return pd.DataFrame({"security": tickers})

    monkeypatch.setattr(bloomberg, "validate_tickers", fake_validate)
    result = bloomberg.resolve_option_ticker_from_strike(
        "SPY US Equity",
        "2026-03-20",
        "PUT",
        685,
        offsets=[1.0, -1.0],
    )
    expected = [
        bloomberg.construct_option_ticker(
            "SPY US Equity", "2026-03-20", "PUT", 686
        ),
        bloomberg.construct_option_ticker(
            "SPY US Equity", "2026-03-20", "PUT", 684
        ),
    ]
    assert calls[1] == expected
    assert result == expected[0]
