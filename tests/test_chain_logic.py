from contextlib import contextmanager

import pandas as pd

import adapters.bloomberg as bloomberg


def test_chain_strikes_and_ticker_selection():
    chain = pd.DataFrame(
        [
            {"option_ticker": "C90", "strike": 90, "put_call": "C", "expiry": "2025-01-01"},
            {"option_ticker": "C100", "strike": 100, "put_call": "CALL", "expiry": "2025-01-01"},
            {"option_ticker": "P100", "strike": 100, "put_call": "P", "expiry": "2025-01-01"},
            {"option_ticker": "C110", "strike": 110, "put_call": "CALL", "expiry": "2025-01-01"},
        ]
    )
    call_strikes = bloomberg.chain_strikes(chain, "CALL")
    put_strikes = bloomberg.chain_strikes(chain, "PUT")
    assert call_strikes == [90.0, 100.0, 110.0]
    assert put_strikes == [100.0]
    assert bloomberg.select_chain_ticker(chain, "CALL", 100.0) == "C100"
    assert bloomberg.select_chain_ticker(chain, "PUT", 100.0) == "P100"


def test_resolve_security_fallback_with_bsrch():
    class DummyQuery:
        def __init__(self, results):
            self._results = results

        def bsrch(self, _query):
            return self._results

    @contextmanager
    def dummy_session():
        yield DummyQuery(pd.DataFrame({"security": ["ABC US Equity"]}))

    @contextmanager
    def empty_session():
        yield DummyQuery(pd.DataFrame(columns=["security"]))

    original = bloomberg.with_session
    try:
        bloomberg.with_session = dummy_session
        assert bloomberg.resolve_security("ABC") == "ABC US Equity"
        bloomberg.with_session = empty_session
        assert bloomberg.resolve_security("ABC") == "ABC"
    finally:
        bloomberg.with_session = original
