import pandas as pd

from adapters.bloomberg import build_leg_price_updates
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
