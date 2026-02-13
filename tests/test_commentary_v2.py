"""Tests for the payoff-driven commentary engine (core/commentary_v2.py)."""
from __future__ import annotations

import csv
import re
from pathlib import Path

import pytest

from core.models import OptionLeg, StrategyInput
from core.analysis_pack import build_analysis_pack
from core.commentary_v2 import build_commentary_v2


# ── Helpers ──────────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SPOT = 100.0
EXPIRY = "2026-04-17"
AS_OF = "2026-02-13"
META_BASE = {
    "as_of": AS_OF,
    "expiry": EXPIRY,
    "strategy_id": "test",
}
PACK_KWARGS = dict(
    pricing_mode="mid",
    roi_policy="RISK_MAX_LOSS",
    vol_mode="atm",
    atm_iv=0.25,
    underlying_profile=None,
    bbg_leg_snapshots=None,
    scenario_mode="percentage",
    downside_tgt=0.85,
    upside_tgt=1.15,
    risk_free_rate=0.0,
)


def _build_pack(
    legs: list[OptionLeg],
    stock_position: float = 0.0,
    avg_cost: float = 0.0,
    name: str = "Test",
) -> dict:
    si = StrategyInput(
        spot=SPOT,
        stock_position=stock_position,
        avg_cost=avg_cost,
        legs=legs,
    )
    meta = {**META_BASE, "strategy_name": name}
    return build_analysis_pack(strategy_input=si, strategy_meta=meta, **PACK_KWARGS)


def _get_scenario(result: dict, kind: str) -> dict:
    for s in result["narrative_scenarios"]:
        if s["kind"] == kind:
            return s
    raise KeyError(f"No {kind} scenario found")


# ── Covered call ─────────────────────────────────────────────────────────


class TestCoveredCall:
    @pytest.fixture(autouse=True)
    def setup(self):
        legs = [OptionLeg(kind="call", position=-1.0, strike=108.0,
                          premium=2.50, multiplier=100)]
        pack = _build_pack(legs, stock_position=100.0, avg_cost=100.0,
                           name="Covered Call")
        self.result = build_commentary_v2(pack)

    def test_three_scenarios(self):
        assert len(self.result["narrative_scenarios"]) == 3

    def test_bearish_mentions_cushion(self):
        bear = _get_scenario(self.result, "bearish")
        body = bear["body"].lower()
        assert "cushion" in body or "options" in body or "premium" in body

    def test_bullish_mentions_cap(self):
        bull = _get_scenario(self.result, "bullish")
        assert "cap" in bull["body"].lower()

    def test_no_double_dash(self):
        for s in self.result["narrative_scenarios"]:
            assert "--" not in s["body"]
            assert "--" not in s["condition"]


# ── Iron condor ──────────────────────────────────────────────────────────


class TestIronCondor:
    @pytest.fixture(autouse=True)
    def setup(self):
        legs = [
            OptionLeg(kind="put", position=1.0, strike=80.0,
                      premium=0.50, multiplier=100),
            OptionLeg(kind="put", position=-1.0, strike=92.0,
                      premium=2.00, multiplier=100),
            OptionLeg(kind="call", position=-1.0, strike=108.0,
                      premium=2.00, multiplier=100),
            OptionLeg(kind="call", position=1.0, strike=120.0,
                      premium=0.50, multiplier=100),
        ]
        pack = _build_pack(legs, name="Iron Condor")
        self.result = build_commentary_v2(pack)

    def test_bearish_mentions_cap_or_hedge(self):
        bear = _get_scenario(self.result, "bearish")
        body = bear["body"].lower()
        assert "cap" in body or "limit" in body or "floor" in body

    def test_bullish_mentions_cap_or_hedge(self):
        bull = _get_scenario(self.result, "bullish")
        body = bull["body"].lower()
        assert "cap" in body or "limit" in body or "ceiling" in body

    def test_no_double_dash(self):
        for s in self.result["narrative_scenarios"]:
            assert "--" not in s["body"]


# ── Long call ────────────────────────────────────────────────────────────


class TestLongCall:
    @pytest.fixture(autouse=True)
    def setup(self):
        legs = [OptionLeg(kind="call", position=1.0, strike=100.0,
                          premium=5.00, multiplier=100)]
        pack = _build_pack(legs, name="Long Call")
        self.result = build_commentary_v2(pack)

    def test_bearish_limited_loss(self):
        bear = _get_scenario(self.result, "bearish")
        body = bear["body"].lower()
        assert "cap" in body or "limit" in body

    def test_bullish_has_content(self):
        bull = _get_scenario(self.result, "bullish")
        assert len(bull["body"]) > 20

    def test_no_stock_decomposition(self):
        for s in self.result["narrative_scenarios"]:
            assert "the shares" not in s["body"].lower()


# ── Protective put with stock at profit ──────────────────────────────────


class TestProtectivePutProfitable:
    @pytest.fixture(autouse=True)
    def setup(self):
        legs = [OptionLeg(kind="put", position=1.0, strike=95.0,
                          premium=3.00, multiplier=100)]
        pack = _build_pack(legs, stock_position=100.0, avg_cost=90.0,
                           name="Protective Put Profitable")
        self.result = build_commentary_v2(pack)

    def test_bearish_mentions_profitable(self):
        bear = _get_scenario(self.result, "bearish")
        body = bear["body"].lower()
        assert ("profitable" in body or "gain" in body
                or "locked" in body or "+$" in body.replace("\u2212", "-"))


# ── Stock only ───────────────────────────────────────────────────────────


class TestStockOnly:
    @pytest.fixture(autouse=True)
    def setup(self):
        pack = _build_pack([], stock_position=100.0, avg_cost=100.0,
                           name="Stock Only")
        self.result = build_commentary_v2(pack)

    def test_no_crash(self):
        assert "narrative_scenarios" in self.result
        assert len(self.result["narrative_scenarios"]) == 3

    def test_no_double_dash(self):
        for s in self.result["narrative_scenarios"]:
            assert "--" not in s["body"]

    def test_has_commentary_blocks(self):
        assert len(self.result["commentary_blocks"]) >= 3


# ── Options only (no stock) ─────────────────────────────────────────────


class TestOptionsOnly:
    @pytest.fixture(autouse=True)
    def setup(self):
        legs = [
            OptionLeg(kind="call", position=1.0, strike=100.0,
                      premium=5.00, multiplier=100),
            OptionLeg(kind="call", position=-1.0, strike=108.0,
                      premium=2.50, multiplier=100),
        ]
        pack = _build_pack(legs, name="Bull Call Spread")
        self.result = build_commentary_v2(pack)

    def test_no_stock_decomposition(self):
        for s in self.result["narrative_scenarios"]:
            assert "the shares" not in s["body"].lower()

    def test_no_double_dash(self):
        for s in self.result["narrative_scenarios"]:
            assert "--" not in s["body"]
            assert "--" not in s["condition"]


# ── 63-strategy regression ───────────────────────────────────────────────


STRIKE_MAP = {
    "": 100.0, "ATM": 100.0, "LOWER": 92.0, "HIGHER": 108.0,
    "LOW": 85.0, "MID": 100.0, "HIGH": 115.0,
    "LOWEST": 80.0, "LOW-MID": 92.0, "HIGH-MID": 108.0, "HIGHEST": 120.0,
}


def _synthetic_premium(kind: str, strike: float, spot: float = SPOT) -> float:
    time_value = 2.50
    if kind == "call":
        intrinsic = max(spot - strike, 0.0)
    else:
        intrinsic = max(strike - spot, 0.0)
    otm_distance = abs(strike - spot) / spot
    tv_decay = max(0.3, 1.0 - otm_distance * 3.0)
    return round(intrinsic + time_value * tv_decay, 2)


def _load_strategies() -> list[dict]:
    csv_path = PROJECT_ROOT / "data" / "strategy_map.csv"
    if not csv_path.exists():
        return []
    with open(csv_path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _row_to_pack(row: dict) -> dict:
    """Build an analysis pack from a strategy_map CSV row."""
    legs: list[OptionLeg] = []
    stock_position = 0.0
    avg_cost = 0.0
    for i in range(1, 5):
        leg_type = (row.get(f"leg_{i}_type") or "").strip().upper()
        leg_side = (row.get(f"leg_{i}_side") or "").strip().upper()
        leg_ratio = (row.get(f"leg_{i}_ratio") or "").strip()
        leg_strike_key = (row.get(f"leg_{i}_strike") or "").strip().upper()
        if not leg_type:
            continue
        if leg_type == "STOCK":
            qty = int(leg_ratio) if leg_ratio else 1
            stock_position = qty * 100.0 if leg_side == "LONG" else -qty * 100.0
            avg_cost = SPOT
            continue
        kind = leg_type.lower()
        ratio = int(leg_ratio) if leg_ratio else 1
        position = float(ratio if leg_side == "LONG" else -ratio)
        strike = STRIKE_MAP.get(leg_strike_key, 100.0)
        premium = _synthetic_premium(kind, strike)
        legs.append(OptionLeg(
            kind=kind, position=position, strike=strike,
            premium=premium, multiplier=100,
        ))
    if not legs and stock_position == 0.0:
        raise ValueError("No legs or stock")
    si = StrategyInput(spot=SPOT, stock_position=stock_position,
                       avg_cost=avg_cost, legs=legs)
    meta = {**META_BASE, "strategy_name": row.get("strategy_name", "?")}
    return build_analysis_pack(strategy_input=si, strategy_meta=meta,
                               **PACK_KWARGS)


@pytest.fixture(scope="module")
def all_strategies():
    rows = _load_strategies()
    if not rows:
        pytest.skip("strategy_map.csv not found or empty")
    packs = []
    for row in rows:
        sid = row.get("strategy_id", "?")
        name = row.get("strategy_name", "?")
        try:
            pack = _row_to_pack(row)
            packs.append((sid, name, pack))
        except Exception:
            continue  # skip strategies that can't build a pack (e.g. custom)
    return packs


def test_all_strategies_no_errors(all_strategies):
    """Every strategy produces commentary without exceptions."""
    failures = []
    for sid, name, pack in all_strategies:
        try:
            result = build_commentary_v2(pack)
            assert "narrative_scenarios" in result
            assert len(result["narrative_scenarios"]) == 3
        except Exception as exc:
            failures.append(f"{name} (ID={sid}): {exc}")
    assert not failures, "Failures:\n" + "\n".join(failures)


def test_all_strategies_no_empty_bodies(all_strategies):
    """No scenario has an empty body."""
    empties = []
    for sid, name, pack in all_strategies:
        try:
            result = build_commentary_v2(pack)
            for s in result["narrative_scenarios"]:
                if not s["body"] or len(s["body"].strip()) < 10:
                    empties.append(f"{name} (ID={sid}) {s['kind']}: empty body")
        except Exception:
            pass
    assert not empties, "Empty bodies:\n" + "\n".join(empties)


def test_all_strategies_no_dash_placeholders(all_strategies):
    """No '--' placeholders in bodies or conditions."""
    dashes = []
    for sid, name, pack in all_strategies:
        try:
            result = build_commentary_v2(pack)
            for s in result["narrative_scenarios"]:
                if "--" in s["body"] or "--" in s["condition"]:
                    dashes.append(f"{name} (ID={sid}) {s['kind']}")
        except Exception:
            pass
    assert not dashes, "Dash placeholders:\n" + "\n".join(dashes)
