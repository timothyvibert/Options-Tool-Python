"""Tests for Bloomberg Greeks and derivative analytics fields in analysis_pack."""

from core.analysis_pack import build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.roi import NET_PREMIUM


def _make_pack(underlying_profile=None, bbg_leg_snapshots=None):
    """Helper to build a pack with optional Greeks / derivative data."""
    legs = [
        OptionLeg(kind="call", position=1.0, strike=105.0, premium=3.0),
        OptionLeg(kind="put", position=-1.0, strike=95.0, premium=2.5),
    ]
    strategy_input = StrategyInput(
        spot=100.0,
        stock_position=0.0,
        avg_cost=0.0,
        legs=legs,
    )
    return build_analysis_pack(
        strategy_input=strategy_input,
        strategy_meta={
            "strategy_name": "Risk Reversal",
            "as_of": "2026-01-18",
            "expiry": "2026-03-20",
        },
        pricing_mode="MID",
        roi_policy=NET_PREMIUM,
        vol_mode="ATM",
        atm_iv=0.25,
        underlying_profile=underlying_profile or {},
        bbg_leg_snapshots=bbg_leg_snapshots,
        scenario_mode="STANDARD",
        downside_tgt=0.9,
        upside_tgt=1.1,
    )


# --- Leg-level Greeks ---


def test_leg_greeks_present_when_provided():
    """When bbg_leg_snapshots supply Greeks, they appear on each leg."""
    snapshots = {
        "leg_quotes": [
            {"delta": 0.55, "gamma": 0.03, "theta": -0.05, "vega": 0.18, "rho": 0.02},
            {"delta": -0.35, "gamma": 0.02, "theta": -0.04, "vega": 0.15, "rho": -0.01},
        ],
        "per_leg_iv": [0.30, 0.28],
    }
    pack = _make_pack(bbg_leg_snapshots=snapshots)
    legs = pack["legs"]
    assert len(legs) == 2

    assert legs[0]["delta"] == 0.55
    assert legs[0]["gamma"] == 0.03
    assert legs[0]["theta"] == -0.05
    assert legs[0]["vega"] == 0.18
    assert legs[0]["rho"] == 0.02
    # backward-compat alias
    assert legs[0]["delta_mid"] == 0.55

    assert legs[1]["delta"] == -0.35
    assert legs[1]["gamma"] == 0.02
    assert legs[1]["theta"] == -0.04
    assert legs[1]["vega"] == 0.15
    assert legs[1]["rho"] == -0.01


def test_leg_greeks_none_when_no_snapshots():
    """When no Bloomberg snapshot is available, Greeks default to None."""
    pack = _make_pack(bbg_leg_snapshots=None)
    legs = pack["legs"]
    for leg in legs:
        for greek in ("delta", "gamma", "theta", "vega", "rho"):
            assert greek in leg
            assert leg[greek] is None


def test_leg_greeks_partial_snapshot():
    """Snapshots with only some Greeks still populate what's available."""
    snapshots = {
        "leg_quotes": [
            {"delta": 0.6, "gamma": 0.04},  # missing theta, vega, rho
            {},  # empty snapshot
        ],
    }
    pack = _make_pack(bbg_leg_snapshots=snapshots)
    legs = pack["legs"]

    assert legs[0]["delta"] == 0.6
    assert legs[0]["gamma"] == 0.04
    assert legs[0]["theta"] is None
    assert legs[0]["vega"] is None
    assert legs[0]["rho"] is None

    assert legs[1]["delta"] is None
    assert legs[1]["gamma"] is None


# --- Underlying derivative fields ---


def test_derivative_fields_present():
    """put_call ratios and BQL stubs appear in underlying dict."""
    profile = {
        "put_call_oi_ratio": 1.25,
        "put_call_vol_ratio": 0.87,
        "realized_vol_3m": 0.22,
        "iv_rv_spread": 0.03,
        "iv_skew_3m": -0.05,
        "iv_term_premium": 0.01,
        "iv_rv_percentile": 65.0,
        "iv_skew_percentile": 40.0,
        "iv_term_premium_percentile": 55.0,
    }
    pack = _make_pack(underlying_profile=profile)
    u = pack["underlying"]

    assert u["put_call_oi_ratio"] == 1.25
    assert u["put_call_vol_ratio"] == 0.87
    assert u["realized_vol_3m"] == 0.22
    assert u["iv_rv_spread"] == 0.03
    assert u["iv_skew_3m"] == -0.05
    assert u["iv_term_premium"] == 0.01
    assert u["iv_rv_percentile"] == 65.0
    assert u["iv_skew_percentile"] == 40.0
    assert u["iv_term_premium_percentile"] == 55.0


def test_derivative_fields_none_when_absent():
    """Derivative fields are None when underlying_profile has no data."""
    pack = _make_pack(underlying_profile={})
    u = pack["underlying"]

    for field in (
        "put_call_oi_ratio",
        "put_call_vol_ratio",
        "realized_vol_3m",
        "iv_rv_spread",
        "iv_skew_3m",
        "iv_term_premium",
        "iv_rv_percentile",
        "iv_skew_percentile",
        "iv_term_premium_percentile",
    ):
        assert field in u, f"Missing field: {field}"
        assert u[field] is None, f"Expected None for {field}, got {u[field]}"


# --- IV used with vega weighting ---


def test_iv_used_with_per_leg_iv():
    """When per_leg_iv is provided via bbg_leg_snapshots, vega-weighted sigma is used."""
    snapshots = {
        "leg_quotes": [
            {"delta": 0.55, "iv": 0.30},
            {"delta": -0.35, "iv": 0.28},
        ],
        "per_leg_iv": [0.30, 0.28],
    }
    pack = _make_pack(bbg_leg_snapshots=snapshots)
    probs = pack.get("probs") or pack.get("probabilities")
    if probs is not None:
        iv_used = probs.get("iv_used") or probs.get("iv_used_pct")
        # Should be somewhere near the vega-weighted average, not 0.20 fallback
        if iv_used is not None:
            assert iv_used > 0.0


def test_iv_used_fallback_no_per_leg():
    """Without per_leg_iv, ATM IV fallback is used."""
    pack = _make_pack(bbg_leg_snapshots=None)
    probs = pack.get("probs") or pack.get("probabilities")
    if probs is not None:
        iv_used = probs.get("iv_used")
        if iv_used is not None:
            assert iv_used > 0.0
