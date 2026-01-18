from contextlib import contextmanager

import pandas as pd

import adapters.bloomberg as bloomberg


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


def test_validate_tickers_filters_nulls(monkeypatch):
    class DummyQuery:
        def bdp(self, securities, fields):
            return pd.DataFrame(
                [
                    {"security": securities[0], "PX_LAST": pd.NA},
                    {"security": securities[1], "PX_LAST": 10.0},
                ]
            )

    @contextmanager
    def dummy_session():
        yield DummyQuery()

    monkeypatch.setattr(bloomberg, "with_session", dummy_session)
    df = bloomberg.validate_tickers(["AAA", "BBB"])
    assert df["security"].tolist() == ["BBB"]
