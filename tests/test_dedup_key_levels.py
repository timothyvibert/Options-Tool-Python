"""Tests for _dedup_key_levels retroactive removal and IV source annotation."""

from core.analysis_pack import _dedup_key_levels, build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.roi import NET_PREMIUM


class TestDedupKeyLevels:
    """Fix 2A: non-ALWAYS_KEEP entries at a price should be removed
    when an ALWAYS_KEEP entry arrives at the same price."""

    def test_downside_removed_when_breakeven_at_same_price(self):
        levels = [
            {"id": "downside", "label": "Downside (47%) at 70.83",
             "price": 70.83, "source": "downside"},
            {"id": "breakeven_1", "label": "Breakeven 1 at 70.83",
             "price": 70.83, "source": "breakeven"},
        ]
        result = _dedup_key_levels(levels)
        labels = [lv["label"] for lv in result]
        assert "Breakeven 1 at 70.83" in labels
        assert "Downside (47%) at 70.83" not in labels

    def test_upside_removed_when_strike_at_same_price(self):
        levels = [
            {"id": "upside", "label": "Upside (48%) at 200.00",
             "price": 200.0, "source": "upside"},
            {"id": "strike_2", "label": "Upper Strike at 200.00",
             "price": 200.0, "source": "strike"},
        ]
        result = _dedup_key_levels(levels)
        labels = [lv["label"] for lv in result]
        assert "Upper Strike at 200.00" in labels
        assert "Upside (48%) at 200.00" not in labels

    def test_always_keep_entries_both_survive_at_same_price(self):
        """Two ALWAYS_KEEP sources at the same price should both survive."""
        levels = [
            {"id": "strike_1", "label": "Strike 1", "price": 100.0, "source": "strike"},
            {"id": "spot", "label": "Spot", "price": 100.0, "source": "spot"},
        ]
        result = _dedup_key_levels(levels)
        labels = [lv["label"] for lv in result]
        assert "Strike 1" in labels
        assert "Spot" in labels
        assert len(result) == 2

    def test_non_always_keep_different_source_at_different_price(self):
        """Non-ALWAYS_KEEP entries at different prices should both survive."""
        levels = [
            {"id": "downside", "label": "Downside", "price": 80.0, "source": "downside"},
            {"id": "upside", "label": "Upside", "price": 120.0, "source": "upside"},
        ]
        result = _dedup_key_levels(levels)
        assert len(result) == 2

    def test_duplicate_same_source_same_price_deduplicated(self):
        levels = [
            {"id": "down_1", "label": "Downside A", "price": 80.0, "source": "downside"},
            {"id": "down_2", "label": "Downside B", "price": 80.0, "source": "downside"},
        ]
        result = _dedup_key_levels(levels)
        assert len(result) == 1
        assert result[0]["label"] == "Downside A"

    def test_sentinel_none_price_always_kept(self):
        levels = [
            {"id": "infinity", "label": "Stock to Infinity", "price": None, "source": "sentinel"},
            {"id": "spot", "label": "Spot", "price": 100.0, "source": "spot"},
        ]
        result = _dedup_key_levels(levels)
        assert len(result) == 2

    def test_breakeven_then_downside_at_same_price(self):
        """When breakeven comes FIRST, downside should be skipped."""
        levels = [
            {"id": "breakeven_1", "label": "Breakeven 1 at 70.83",
             "price": 70.83, "source": "breakeven"},
            {"id": "downside", "label": "Downside (47%) at 70.83",
             "price": 70.83, "source": "downside"},
        ]
        result = _dedup_key_levels(levels)
        labels = [lv["label"] for lv in result]
        assert "Breakeven 1 at 70.83" in labels
        assert "Downside (47%) at 70.83" not in labels
        assert len(result) == 1

    def test_multiple_non_always_keep_removed_by_single_always_keep(self):
        """Multiple low-priority entries at the same price removed by one high-priority."""
        levels = [
            {"id": "down", "label": "Downside", "price": 100.0, "source": "downside"},
            {"id": "target", "label": "Target", "price": 100.0, "source": "target"},
            {"id": "spot", "label": "Spot", "price": 100.0, "source": "spot"},
        ]
        result = _dedup_key_levels(levels)
        labels = [lv["label"] for lv in result]
        assert "Spot" in labels
        assert "Downside" not in labels
        assert "Target" not in labels
        assert len(result) == 1

    def test_result_sorted_by_price(self):
        levels = [
            {"id": "c", "label": "C", "price": 120.0, "source": "strike"},
            {"id": "a", "label": "A", "price": 80.0, "source": "strike"},
            {"id": "b", "label": "B", "price": 100.0, "source": "spot"},
            {"id": "inf", "label": "Inf", "price": None, "source": "sentinel"},
        ]
        result = _dedup_key_levels(levels)
        prices = [lv.get("price") for lv in result]
        assert prices == [80.0, 100.0, 120.0, None]


class TestIVSourceAnnotation:
    """Fix 2B: iv_used_pct should show '(ATM)' suffix when using fallback."""

    def _build_pack(self, per_leg_iv=None, atm_iv=0.2):
        legs = [
            OptionLeg(kind="call", position=-10, strike=110, premium=5.0),
            OptionLeg(kind="put", position=-10, strike=90, premium=3.0),
        ]
        si = StrategyInput(spot=100.0, legs=legs)
        bbg = {"per_leg_iv": per_leg_iv or [], "leg_quotes": []}
        return build_analysis_pack(
            strategy_input=si,
            strategy_meta={"as_of": "2026-01-18", "expiry": "2026-06-20"},
            pricing_mode="MID",
            roi_policy=NET_PREMIUM,
            vol_mode="ATM",
            atm_iv=atm_iv,
            underlying_profile=None,
            bbg_leg_snapshots=bbg,
            scenario_mode="STANDARD",
            downside_tgt=0.9,
            upside_tgt=1.1,
        )

    def test_atm_fallback_shows_clean_pct(self):
        """When no per-leg IVs, iv_used_pct should be a clean percentage (no ATM suffix)."""
        pack = self._build_pack(per_leg_iv=[None, None])
        probs = pack.get("probabilities", {})
        iv_pct = probs.get("iv_used_pct", "")
        assert "%" in iv_pct, f"Expected percentage, got '{iv_pct}'"
        assert "(ATM)" not in iv_pct, f"Should not have ATM suffix, got '{iv_pct}'"
        assert probs.get("iv_source") == "atm_fallback"

    def test_no_per_leg_iv_shows_clean_pct(self):
        """When per_leg_iv is empty, iv_used_pct should be a clean percentage."""
        pack = self._build_pack(per_leg_iv=[])
        probs = pack.get("probabilities", {})
        iv_pct = probs.get("iv_used_pct", "")
        assert "%" in iv_pct, f"Expected percentage, got '{iv_pct}'"
        assert "(ATM)" not in iv_pct, f"Should not have ATM suffix, got '{iv_pct}'"

    def test_with_per_leg_iv_no_atm_suffix(self):
        """When per-leg IVs are provided, iv_used_pct should NOT contain '(ATM)'."""
        pack = self._build_pack(per_leg_iv=[0.45, 0.55])
        probs = pack.get("probabilities", {})
        iv_pct = probs.get("iv_used_pct", "")
        assert "(ATM)" not in iv_pct, f"Got ATM suffix when real IVs provided: '{iv_pct}'"
        assert probs.get("iv_source") == "vega_weighted"

    def test_with_per_leg_iv_reflects_weighted_value(self):
        """When per-leg IVs are provided, iv_used should be vega-weighted, not 0.2."""
        pack = self._build_pack(per_leg_iv=[0.45, 0.55])
        probs = pack.get("probabilities", {})
        iv_used = probs.get("iv_used", 0)
        assert iv_used > 0.3, f"IV used {iv_used} should be > 0.3 (not ATM fallback)"
        iv_pct = probs.get("iv_used_pct", "")
        assert "20.0" not in iv_pct, f"IV should not be 20.0%, got {iv_pct}"
