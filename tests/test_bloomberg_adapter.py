import sys
import types

import pandas as pd

from adapters.bloomberg import build_leg_price_updates, validate_tickers
from core.pricing import DEALABLE, MID


def test_build_leg_price_updates_respects_override_and_dealable():
    legs = [
        {"index": 0, "ticker": "OPT1", "position": 1, "manual_override": False},
        {"index": 1, "ticker": "OPT2", "position": -1, "manual_override": True},
        {"index": 2, "ticker": "OPT3", "position": -1, "manual_override": False},
    ]
    snapshot = pd.DataFrame(
        [
            {"security": "OPT1", "BID": 1.0, "ASK": 2.0, "PX_MID": 1.5},
            {"security": "OPT2", "BID": 0.9, "ASK": 1.1, "PX_MID": 1.0},
            {"security": "OPT3", "BID": 0.8, "ASK": 1.2, "PX_MID": 1.0},
        ]
    )
    updates = build_leg_price_updates(legs, snapshot, DEALABLE)
    assert updates[0] == 2.0
    assert 1 not in updates
    assert updates[2] == 0.8


def test_build_leg_price_updates_mid_fallback():
    legs = [
        {"index": 0, "ticker": "OPT1", "position": 1, "manual_override": False}
    ]
    snapshot = pd.DataFrame(
        [{"security": "OPT1", "BID": 1.0, "ASK": 3.0, "PX_MID": None}]
    )
    updates = build_leg_price_updates(legs, snapshot, MID)
    assert updates[0] == 2.0


def test_bloomberg_session_uses_context_manager(monkeypatch):
    events = []

    class FakeBQuery:
        counter = 0

        def __init__(self):
            self.id = FakeBQuery.counter
            FakeBQuery.counter += 1
            self.entered = False

        def __enter__(self):
            self.entered = True
            events.append((self.id, "enter"))
            return self

        def __exit__(self, exc_type, exc, tb):
            events.append((self.id, "exit"))
            self.entered = False

        def _check(self, label: str) -> None:
            assert self.entered
            events.append((self.id, label))

        def bdp(self, securities, fields):
            self._check("bdp")
            return pd.DataFrame(
                {
                    "security": securities,
                    "PX_LAST": [101.0] * len(securities),
                }
            )

        def bsrch(self, query):
            self._check("bsrch")
            return pd.DataFrame({"security": ["TEST US Equity"]})

    fake_module = types.ModuleType("polars_bloomberg")
    fake_module.BQuery = FakeBQuery
    monkeypatch.setitem(sys.modules, "polars_bloomberg", fake_module)

    from adapters import bloomberg

    assert bloomberg.fetch_spot("TEST US Equity") == 101.0
    assert bloomberg.resolve_security("TEST") == "TEST US Equity"
    valid = validate_tickers(["TEST 1/17/25 C100 Equity"])
    assert not valid.empty

    def _assert_enter_before(label: str) -> None:
        seen = {}
        for idx, (call_id, event) in enumerate(events):
            seen.setdefault(call_id, {})[event] = idx
        for call_id, marks in seen.items():
            if label not in marks:
                continue
            assert "enter" in marks
            assert marks["enter"] < marks[label]

    _assert_enter_before("bdp")
    _assert_enter_before("bsrch")
