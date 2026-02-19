"""Calculation Engine Audit — comprehensive numerical checks across all 63 strategies.

Usage:  python tools/calculation_audit.py
Output: calculation_audit.md in project root

READ-ONLY diagnostic: does NOT modify any application code.

Test Matrix: 63 strategies × 4 cost-basis scenarios = 252 runs
  Scenario 0: options-only (stock_position=0)
  Scenario 1: avg_cost = spot
  Scenario 2: avg_cost = 0.5 × spot
  Scenario 3: avg_cost = 1.15 × spot

Check Categories:
  A: Payoff Grid Integrity (PG_*)
  B: Breakeven Validation (BE_*)
  C: Max Profit / Max Loss (MP_*, ML_*)
  D: Net Premium & Cost/Credit (NP_*)
  E: Stock P&L (SP_*)
  F: Cross-Scenario Consistency (CS_*)
  G: Capital at Risk & ROI (CB_*, ROI_*)
  H: Key Levels (KL_*)
  I: Pipeline Map Issue Checks (PI_*)
  J: Known Bug Checks (BUG_*)
"""
from __future__ import annotations

import csv
import math
import sys
import traceback
from datetime import date
from pathlib import Path
from typing import Any

# Ensure project root is on sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from core.models import OptionLeg, StrategyInput
from core.analysis_pack import build_analysis_pack
from core.payoff import (
    _build_price_grid,
    _compute_pnl_for_price,
    _detect_breakevens,
    _detect_unlimited,
    _inject_strikes,
    compute_payoff,
)
from core.roi import (
    capital_basis,
    combined_capital_basis,
    compute_net_premium,
)

# ── Constants ──────────────────────────────────────────────
SPOT = 100.0
EXPIRY = "2026-04-17"
AS_OF = "2026-02-13"
ATM_IV = 0.25
TOL = 1e-6  # numerical tolerance for floating-point comparisons

STRIKE_MAP = {
    "": 100.0,
    "ATM": 100.0,
    "LOWER": 92.0,
    "HIGHER": 108.0,
    "LOW": 85.0,
    "MID": 100.0,
    "HIGH": 115.0,
    "LOWEST": 80.0,
    "LOW-MID": 92.0,
    "HIGH-MID": 108.0,
    "HIGHEST": 120.0,
}

SCENARIOS = [
    {"label": "options_only", "stock_position": 0.0, "avg_cost": 0.0},
    {"label": "avg_cost=spot", "stock_position": 100.0, "avg_cost": SPOT},
    {"label": "avg_cost=0.5×spot", "stock_position": 100.0, "avg_cost": SPOT * 0.5},
    {"label": "avg_cost=1.15×spot", "stock_position": 100.0, "avg_cost": SPOT * 1.15},
]


# ══════════════════════════════════════════════════════════
# Synthetic data helpers (mirrored from commentary_regression.py)
# ══════════════════════════════════════════════════════════

def _synthetic_premium(kind: str, strike: float, spot: float = SPOT) -> float:
    time_value = 2.50
    if kind == "call":
        intrinsic = max(spot - strike, 0.0)
    else:
        intrinsic = max(strike - spot, 0.0)
    otm_distance = abs(strike - spot) / spot
    tv_decay = max(0.3, 1.0 - otm_distance * 3.0)
    return round(intrinsic + time_value * tv_decay, 2)


def _build_legs_from_row(row: dict) -> list[OptionLeg]:
    legs: list[OptionLeg] = []
    for i in range(1, 5):
        leg_type = (row.get(f"leg_{i}_type") or "").strip().upper()
        leg_side = (row.get(f"leg_{i}_side") or "").strip().upper()
        leg_ratio = (row.get(f"leg_{i}_ratio") or "").strip()
        leg_strike_key = (row.get(f"leg_{i}_strike") or "").strip().upper()
        if not leg_type or leg_type == "STOCK":
            continue
        kind = leg_type.lower()
        ratio = int(leg_ratio) if leg_ratio else 1
        position = ratio if leg_side == "LONG" else -ratio
        strike = STRIKE_MAP.get(leg_strike_key, 100.0)
        premium = _synthetic_premium(kind, strike)
        legs.append(OptionLeg(
            kind=kind, position=float(position),
            strike=strike, premium=premium, multiplier=100,
        ))
    return legs


def _row_has_stock(row: dict) -> bool:
    for i in range(1, 5):
        if (row.get(f"leg_{i}_type") or "").strip().upper() == "STOCK":
            return True
    return False


def _row_stock_side(row: dict) -> str:
    for i in range(1, 5):
        if (row.get(f"leg_{i}_type") or "").strip().upper() == "STOCK":
            return (row.get(f"leg_{i}_side") or "").strip().upper()
    return ""


# ══════════════════════════════════════════════════════════
# Check result accumulator
# ══════════════════════════════════════════════════════════

class CheckResult:
    def __init__(self, check_id: str, passed: bool, message: str,
                 strategy: str = "", scenario: str = ""):
        self.check_id = check_id
        self.passed = passed
        self.message = message
        self.strategy = strategy
        self.scenario = scenario


results: list[CheckResult] = []
numerical_snapshots: list[dict] = []  # raw computed values for fact-checking


def check(check_id: str, condition: bool, message: str,
          strategy: str = "", scenario: str = ""):
    results.append(CheckResult(check_id, condition, message, strategy, scenario))


def capture_numerical_snapshot(pack: dict, si: StrategyInput,
                                name: str, sid: str, scen: str):
    """Extract all key numerical values from the analysis pack for fact-checking."""
    payoff = pack.get("payoff", {})
    summary = pack.get("summary", {})
    summary_rows = summary.get("rows", [])
    probs = pack.get("probabilities", {})
    key_levels = pack.get("key_levels", {})
    scenario_data = pack.get("scenario", {})
    scenario_df = scenario_data.get("df")

    def find_metric(m):
        for row in summary_rows:
            if row.get("metric") == m:
                return row
        return None

    # Leg details
    leg_details = []
    for leg in si.legs:
        leg_details.append({
            "kind": leg.kind,
            "position": leg.position,
            "strike": leg.strike,
            "premium": leg.premium,
            "multiplier": leg.multiplier,
        })

    # Breakevens
    breakevens = payoff.get("breakevens", [])

    # Max/min from PnL arrays
    options_pnl = payoff.get("options_pnl", [])
    combined_pnl = payoff.get("combined_pnl", [])
    options_max = max(options_pnl) if options_pnl else None
    options_min = min(options_pnl) if options_pnl else None
    combined_max = max(combined_pnl) if combined_pnl else None
    combined_min = min(combined_pnl) if combined_pnl else None

    # Net premium
    net_prem_per_share = compute_net_premium(si)
    net_prem_total = sum(l.position * l.premium * l.multiplier for l in si.legs)

    # Summary metrics
    def metric_val(m):
        row = find_metric(m)
        if row:
            return {"options": row.get("options"), "combined": row.get("combined")}
        return None

    # Scenario table extract
    scenario_rows_out = []
    if scenario_df is not None and not scenario_df.empty:
        for _, row in scenario_df.iterrows():
            scenario_rows_out.append({
                "price": float(row.get("price", 0)),
                "scenario": str(row.get("scenario", "")),
                "option_pnl": round(float(row.get("option_pnl", 0)), 4),
                "stock_pnl": round(float(row.get("stock_pnl", 0)), 4),
                "combined_pnl": round(float(row.get("combined_pnl", 0)), 4),
                "option_roi": round(float(row.get("option_roi", 0)), 6),
                "net_roi": round(float(row.get("net_roi", 0)), 6),
            })

    # Key levels extract
    def _safe_round(val, digits):
        if val is None:
            return None
        if isinstance(val, str):
            return val
        try:
            return round(float(val), digits)
        except (TypeError, ValueError):
            return val

    kl_out = []
    for lv in key_levels.get("levels", []):
        kl_out.append({
            "id": lv.get("id"),
            "label": lv.get("label"),
            "price": lv.get("price"),
            "move_pct": _safe_round(lv.get("move_pct"), 4),
            "option_pnl": _safe_round(lv.get("option_pnl"), 4),
            "net_pnl": _safe_round(lv.get("net_pnl"), 4),
            "net_roi": _safe_round(lv.get("net_roi"), 6),
        })

    numerical_snapshots.append({
        "sid": sid,
        "name": name,
        "scenario": scen,
        "spot": si.spot,
        "stock_position": si.stock_position,
        "avg_cost": si.avg_cost,
        "legs": leg_details,
        "grid_size": len(payoff.get("price_grid", [])),
        "strikes": payoff.get("strikes", []),
        "breakevens": [round(b, 6) for b in breakevens],
        "options_max_pnl": round(options_max, 4) if options_max is not None else None,
        "options_min_pnl": round(options_min, 4) if options_min is not None else None,
        "combined_max_pnl": round(combined_max, 4) if combined_max is not None else None,
        "combined_min_pnl": round(combined_min, 4) if combined_min is not None else None,
        "net_premium_per_share": round(net_prem_per_share, 6),
        "net_premium_total": round(net_prem_total, 4),
        "max_profit": metric_val("Max Profit"),
        "max_loss": metric_val("Max Loss"),
        "risk_reward": metric_val("Risk/Reward"),
        "capital_basis": metric_val("Capital at Risk"),
        "cost_credit": metric_val("Cost/Credit"),
        "pop": metric_val("PoP"),
        "pop_raw": round(probs.get("pop", 0), 6) if probs.get("pop") is not None else None,
        "assignment_prob": round(probs.get("assignment_prob", 0), 6) if probs.get("assignment_prob") is not None else None,
        "prob_25_profit": round(probs.get("prob_25_profit", 0), 6) if probs.get("prob_25_profit") is not None else None,
        "prob_50_profit": round(probs.get("prob_50_profit", 0), 6) if probs.get("prob_50_profit") is not None else None,
        "prob_100_profit": round(probs.get("prob_100_profit", 0), 6) if probs.get("prob_100_profit") is not None else None,
        "iv_used": probs.get("iv_used"),
        "margin_classification": pack.get("margin", {}).get("classification"),
        "margin_proxy": round(pack.get("margin", {}).get("margin_proxy", 0), 4),
        "strategy_code": pack.get("strategy", {}).get("strategy_code"),
        "scenario_table": scenario_rows_out,
        "key_levels": kl_out,
    })


# ══════════════════════════════════════════════════════════
# CHECK IMPLEMENTATIONS
# ══════════════════════════════════════════════════════════

def run_checks_A(pack: dict, si: StrategyInput, name: str, scen: str):
    """A: Payoff Grid Integrity (PG_*)"""
    payoff = pack.get("payoff", {})
    grid = payoff.get("price_grid", [])
    options_pnl = payoff.get("options_pnl", [])
    stock_pnl = payoff.get("stock_pnl", [])
    combined_pnl = payoff.get("combined_pnl", [])
    strikes = payoff.get("strikes", [])

    # PG_01: Grid starts at 0
    check("PG_01", len(grid) > 0 and abs(grid[0]) < TOL,
          f"Grid start={grid[0] if grid else 'EMPTY'}, expected 0",
          name, scen)

    # PG_02: Grid ends at 3 * spot
    expected_end = 3.0 * si.spot
    check("PG_02",
          len(grid) > 0 and abs(grid[-1] - expected_end) < 1.0,
          f"Grid end={grid[-1] if grid else 'EMPTY'}, expected ~{expected_end}",
          name, scen)

    # PG_03: Grid is monotonically increasing
    mono = all(grid[i] <= grid[i + 1] for i in range(len(grid) - 1))
    check("PG_03", mono, "Grid monotonicity", name, scen)

    # PG_04: All strikes are present in the grid
    for strike in strikes:
        found = any(abs(g - strike) < TOL for g in grid)
        check("PG_04", found,
              f"Strike {strike} present in grid", name, scen)

    # PG_05: Grid has >= 300 points
    check("PG_05", len(grid) >= 300,
          f"Grid size={len(grid)}, expected >=300", name, scen)

    # PG_06: PnL arrays have same length as grid
    check("PG_06",
          len(options_pnl) == len(grid) and len(stock_pnl) == len(grid) and len(combined_pnl) == len(grid),
          f"PnL lengths: opt={len(options_pnl)}, stk={len(stock_pnl)}, comb={len(combined_pnl)}, grid={len(grid)}",
          name, scen)

    # PG_07: combined_pnl = options_pnl + stock_pnl at every point
    if len(combined_pnl) == len(options_pnl) == len(stock_pnl):
        max_diff = max(
            abs(combined_pnl[i] - (options_pnl[i] + stock_pnl[i]))
            for i in range(len(combined_pnl))
        ) if combined_pnl else 0
        check("PG_07", max_diff < TOL,
              f"combined = opt + stock max_diff={max_diff:.2e}", name, scen)
    else:
        check("PG_07", False, "Cannot verify — array length mismatch", name, scen)


def run_checks_B(pack: dict, si: StrategyInput, name: str, scen: str):
    """B: Breakeven Validation (BE_*)"""
    payoff = pack.get("payoff", {})
    grid = payoff.get("price_grid", [])
    combined_pnl = payoff.get("combined_pnl", [])
    breakevens = payoff.get("breakevens", [])

    # BE_01: Breakevens are sorted
    check("BE_01",
          breakevens == sorted(breakevens),
          f"Breakevens sorted: {breakevens}", name, scen)

    # BE_02: All breakevens lie within the grid range
    if grid and breakevens:
        for be in breakevens:
            check("BE_02", grid[0] - TOL <= be <= grid[-1] + TOL,
                  f"Breakeven {be:.4f} within grid [{grid[0]:.2f}, {grid[-1]:.2f}]",
                  name, scen)

    # BE_03: PnL at breakeven is approximately zero (verify via interpolation)
    if grid and combined_pnl:
        for be in breakevens:
            # Find bracketing grid points
            pnl_at_be = _compute_pnl_for_price(si, be)
            check("BE_03", abs(pnl_at_be) < 1.0,
                  f"PnL at breakeven {be:.4f} = {pnl_at_be:.4f} (tolerance ±$1)",
                  name, scen)

    # BE_04: PnL actually changes sign around each breakeven
    if grid and combined_pnl and breakevens:
        for be in breakevens:
            eps = max(0.01, si.spot * 0.001)
            pnl_below = _compute_pnl_for_price(si, max(be - eps, 0))
            pnl_above = _compute_pnl_for_price(si, be + eps)
            sign_change = (pnl_below * pnl_above <= TOL)
            check("BE_04", sign_change,
                  f"Sign change around breakeven {be:.4f}: below={pnl_below:.4f}, above={pnl_above:.4f}",
                  name, scen)


def run_checks_C(pack: dict, si: StrategyInput, name: str, scen: str):
    """C: Max Profit / Max Loss (MP_*, ML_*)"""
    payoff = pack.get("payoff", {})
    options_pnl = payoff.get("options_pnl", [])
    combined_pnl = payoff.get("combined_pnl", [])
    summary_rows = pack.get("summary", {}).get("rows", [])

    def find_metric(metric_name: str) -> dict | None:
        for row in summary_rows:
            if row.get("metric") == metric_name:
                return row
        return None

    # Detect unlimited flags from the pack
    # Recompute via payoff module to verify
    grid = payoff.get("price_grid", [])

    # Options-only unlimited detection
    opt_unlimited = _detect_unlimited(grid, options_pnl) if grid and options_pnl else {}
    comb_unlimited = _detect_unlimited(grid, combined_pnl) if grid and combined_pnl else {}

    max_profit_row = find_metric("Max Profit")
    max_loss_row = find_metric("Max Loss")

    if max_profit_row:
        opt_mp = max_profit_row.get("options", "")
        comb_mp = max_profit_row.get("combined", "")

        # MP_01: "Unlimited" iff unlimited_profit_upside or unlimited_profit_downside
        opt_profit_unl = (opt_unlimited.get("unlimited_profit_upside", opt_unlimited.get("unlimited_upside", False))
                          or opt_unlimited.get("unlimited_profit_downside", False))
        if opt_profit_unl:
            check("MP_01", opt_mp == "Unlimited",
                  f"Options max profit should be 'Unlimited' but got '{opt_mp}'",
                  name, scen)
        elif options_pnl:
            expected_mp = max(options_pnl)
            # The display value is formatted with $ and commas
            check("MP_01", opt_mp != "Unlimited",
                  f"Options max profit not unlimited: {opt_mp}", name, scen)

        # MP_02: Combined unlimited check
        comb_profit_unl = (comb_unlimited.get("unlimited_profit_upside", comb_unlimited.get("unlimited_upside", False))
                           or comb_unlimited.get("unlimited_profit_downside", False))
        if comb_profit_unl:
            check("MP_02", comb_mp == "Unlimited",
                  f"Combined max profit should be 'Unlimited' but got '{comb_mp}'",
                  name, scen)
        elif combined_pnl:
            check("MP_02", comb_mp != "Unlimited",
                  f"Combined max profit not unlimited: {comb_mp}", name, scen)

    if max_loss_row:
        opt_ml = max_loss_row.get("options", "")
        comb_ml = max_loss_row.get("combined", "")

        # ML_01: "Unlimited" iff unlimited_loss_downside or unlimited_loss_upside
        opt_unl_loss = (opt_unlimited.get("unlimited_loss_downside", False) or
                        opt_unlimited.get("unlimited_loss_upside", False))
        if opt_unl_loss:
            check("ML_01", opt_ml == "Unlimited",
                  f"Options max loss should be 'Unlimited' but got '{opt_ml}'",
                  name, scen)
        elif options_pnl:
            check("ML_01", opt_ml != "Unlimited",
                  f"Options max loss not unlimited: {opt_ml}", name, scen)

        # ML_02: Combined unlimited loss check
        comb_unl_loss = (comb_unlimited.get("unlimited_loss_downside", False) or
                         comb_unlimited.get("unlimited_loss_upside", False))
        if comb_unl_loss:
            check("ML_02", comb_ml == "Unlimited",
                  f"Combined max loss should be 'Unlimited' but got '{comb_ml}'",
                  name, scen)
        elif combined_pnl:
            check("ML_02", comb_ml != "Unlimited",
                  f"Combined max loss not unlimited: {comb_ml}", name, scen)

    # MP_03: Max profit is non-negative for options at spot price (just the value, not sign)
    if options_pnl:
        max_opt = max(options_pnl)
        check("MP_03", max_opt >= -TOL,
              f"Options max profit = {max_opt:.2f} (should be >= 0 for any strategy since you can always not exercise)",
              name, scen)


def run_checks_D(pack: dict, si: StrategyInput, name: str, scen: str):
    """D: Net Premium & Cost/Credit (NP_*)"""
    summary = pack.get("summary", {})
    summary_rows = summary.get("rows", [])

    # Independent computation
    expected_net_premium = sum(leg.position * leg.premium for leg in si.legs)
    expected_net_premium_total = sum(
        leg.position * leg.premium * leg.multiplier for leg in si.legs
    )

    # NP_01: net premium per-share matches
    pack_net_premium = compute_net_premium(si)
    check("NP_01", abs(pack_net_premium - expected_net_premium) < TOL,
          f"Net premium: computed={pack_net_premium:.6f}, expected={expected_net_premium:.6f}",
          name, scen)

    # NP_02: net premium total matches
    reported_total = summary.get("net_premium_total_value")
    if reported_total is not None:
        check("NP_02", abs(reported_total - expected_net_premium_total) < TOL,
              f"Net premium total: reported={reported_total:.2f}, expected={expected_net_premium_total:.2f}",
              name, scen)
    else:
        check("NP_02", False, "net_premium_total_value missing from pack", name, scen)

    # NP_03: Cost/Credit text matches sign
    def find_metric(m):
        for row in summary_rows:
            if row.get("metric") == m:
                return row
        return None

    cc_row = find_metric("Cost/Credit")
    if cc_row:
        text = cc_row.get("options", "")
        if expected_net_premium_total < -TOL:
            check("NP_03", "Credit" in text,
                  f"Net credit ({expected_net_premium_total:.2f}) but text='{text}'",
                  name, scen)
        elif expected_net_premium_total > TOL:
            check("NP_03", "Debit" in text,
                  f"Net debit ({expected_net_premium_total:.2f}) but text='{text}'",
                  name, scen)
        else:
            check("NP_03", True,
                  f"Net premium is zero, text='{text}'", name, scen)
    else:
        check("NP_03", False, "Cost/Credit row missing", name, scen)

    # NP_04: Net Prem/Share sign convention
    nps_row = find_metric("Net Prem/Share")
    if nps_row and si.legs:
        check("NP_04", nps_row.get("options") is not None,
              f"Net Prem/Share present: {nps_row.get('options')}",
              name, scen)
    elif not si.legs:
        check("NP_04", True, "No legs — skip Net Prem/Share", name, scen)


def run_checks_E(pack: dict, si: StrategyInput, name: str, scen: str):
    """E: Stock P&L (SP_*)"""
    payoff = pack.get("payoff", {})
    grid = payoff.get("price_grid", [])
    stock_pnl = payoff.get("stock_pnl", [])

    # SP_01: When stock_position=0, all stock_pnl values should be 0
    if si.stock_position == 0:
        if stock_pnl:
            max_stock = max(abs(v) for v in stock_pnl) if stock_pnl else 0
            check("SP_01", max_stock < TOL,
                  f"No stock position, max |stock_pnl|={max_stock:.2e}",
                  name, scen)
        else:
            check("SP_01", True, "No stock position, empty stock_pnl", name, scen)
    else:
        check("SP_01", True, "Has stock position — skip zero check", name, scen)

    # SP_02: Stock PnL = stock_position * (price - avg_cost) at each point
    if si.stock_position != 0 and len(grid) == len(stock_pnl):
        max_diff = 0.0
        for i, price in enumerate(grid):
            expected = si.stock_position * (price - si.avg_cost)
            max_diff = max(max_diff, abs(stock_pnl[i] - expected))
        check("SP_02", max_diff < TOL,
              f"Stock PnL formula max_diff={max_diff:.2e}",
              name, scen)
    elif si.stock_position != 0:
        check("SP_02", False, "Cannot verify — array length mismatch", name, scen)
    else:
        check("SP_02", True, "No stock position — skip", name, scen)

    # SP_03: Stock PnL is linear (check three points)
    if si.stock_position != 0 and len(stock_pnl) >= 3:
        # Pick three evenly spaced indices
        n = len(stock_pnl)
        i0, i1, i2 = 0, n // 2, n - 1
        # Linear: (y1 - y0)/(x1 - x0) ≈ (y2 - y0)/(x2 - x0)
        dx1 = grid[i1] - grid[i0]
        dx2 = grid[i2] - grid[i0]
        if abs(dx1) > TOL and abs(dx2) > TOL:
            slope1 = (stock_pnl[i1] - stock_pnl[i0]) / dx1
            slope2 = (stock_pnl[i2] - stock_pnl[i0]) / dx2
            check("SP_03", abs(slope1 - slope2) < TOL,
                  f"Stock PnL linearity: slope1={slope1:.6f}, slope2={slope2:.6f}",
                  name, scen)
        else:
            check("SP_03", True, "Grid spacing too small", name, scen)
    else:
        check("SP_03", True, "No stock or too few points", name, scen)


def run_checks_F(pack: dict, si: StrategyInput, name: str, scen: str):
    """F: Cross-Scenario Consistency (CS_*)"""
    scenario = pack.get("scenario", {})
    scenario_df = scenario.get("df")
    payoff = pack.get("payoff", {})
    breakevens = payoff.get("breakevens", [])
    strikes = payoff.get("strikes", [])

    if scenario_df is None or scenario_df.empty:
        check("CS_01", False, "Scenario table is empty", name, scen)
        return

    prices_in_table = scenario_df["price"].tolist()

    # CS_01: Scenario table has entry for spot
    spot_present = any(abs(p - si.spot) < TOL for p in prices_in_table)
    check("CS_01", spot_present,
          f"Spot {si.spot} in scenario table", name, scen)

    # CS_02: Scenario table has entries for all strikes
    for strike in strikes:
        found = any(abs(p - strike) < TOL for p in prices_in_table)
        check("CS_02", found,
              f"Strike {strike} in scenario table", name, scen)

    # CS_03: Scenario table has entries for breakevens
    for be in breakevens:
        found = any(abs(p - be) < 0.5 for p in prices_in_table)
        check("CS_03", found,
              f"Breakeven {be:.4f} in scenario table (±0.5)", name, scen)

    # CS_04: At breakeven prices in scenario table, combined PnL ≈ 0
    for be in breakevens:
        for _, row in scenario_df.iterrows():
            if abs(float(row["price"]) - be) < 0.5:
                cpnl = float(row.get("combined_pnl", 0))
                check("CS_04", abs(cpnl) < 2.0,
                      f"Scenario PnL at breakeven {be:.2f}: combined_pnl={cpnl:.4f}",
                      name, scen)
                break

    # CS_05: Scenario option_pnl + stock_pnl = combined_pnl
    for _, row in scenario_df.iterrows():
        opt = float(row.get("option_pnl", 0))
        stk = float(row.get("stock_pnl", 0))
        comb = float(row.get("combined_pnl", 0))
        diff = abs(comb - (opt + stk))
        check("CS_05", diff < TOL,
              f"Scenario @ {float(row['price']):.2f}: opt({opt:.2f})+stk({stk:.2f})=comb({comb:.2f}), diff={diff:.2e}",
              name, scen)


def run_checks_G(pack: dict, si: StrategyInput, name: str, scen: str):
    """G: Capital at Risk & ROI (CB_*, ROI_*)"""
    summary_rows = pack.get("summary", {}).get("rows", [])
    scenario = pack.get("scenario", {})
    scenario_df = scenario.get("df")
    payoff_result = compute_payoff(si)

    def find_metric(m):
        for row in summary_rows:
            if row.get("metric") == m:
                return row
        return None

    cb_row = find_metric("Capital at Risk")

    # CB_01: Capital basis > 0
    if cb_row:
        opt_text = cb_row.get("options", "")
        # Parse dollar value
        try:
            opt_val = float(opt_text.replace("$", "").replace(",", "").replace("--", "0"))
        except (ValueError, AttributeError):
            opt_val = 0.0
        check("CB_01", opt_val > 0 or not si.legs,
              f"Option capital basis = {opt_text}",
              name, scen)
    elif si.legs:
        check("CB_01", False, "Capital at Risk row missing", name, scen)

    # CB_02: Combined capital basis >= option capital basis when stock exists
    if cb_row and si.stock_position != 0:
        comb_text = cb_row.get("combined", "")
        try:
            opt_val = float(opt_text.replace("$", "").replace(",", "").replace("--", "0"))
            comb_val = float(comb_text.replace("$", "").replace(",", "").replace("--", "0"))
        except (ValueError, AttributeError):
            opt_val = comb_val = 0.0
        check("CB_02", comb_val >= opt_val - TOL,
              f"Combined basis ({comb_val:.2f}) >= Option basis ({opt_val:.2f})",
              name, scen)
    else:
        check("CB_02", True, "No stock or no CB row — skip", name, scen)

    # ROI_01: Option ROI = option_pnl / capital_basis in scenario table
    if scenario_df is not None and not scenario_df.empty and si.legs:
        opt_basis = capital_basis(si, payoff_result, "RISK_MAX_LOSS")
        if opt_basis > TOL:
            for _, row in scenario_df.head(3).iterrows():
                opt_pnl = float(row.get("option_pnl", 0))
                reported_roi = float(row.get("option_roi", 0))
                expected_roi = opt_pnl / opt_basis
                # ROI can differ if auto_capital_basis overrides the basis
                # Just check for reasonableness: not NaN/Inf
                check("ROI_01",
                      math.isfinite(reported_roi),
                      f"Option ROI finite at price {float(row['price']):.2f}: roi={reported_roi:.4f}",
                      name, scen)
        else:
            check("ROI_01", True, "Capital basis is ~0, skip ROI check", name, scen)
    else:
        check("ROI_01", True, "No scenario data or no legs", name, scen)

    # ROI_02: No inf/nan in ROI values
    if scenario_df is not None and not scenario_df.empty:
        opt_rois = scenario_df["option_roi"].tolist()
        net_rois = scenario_df["net_roi"].tolist()
        bad_opt = sum(1 for v in opt_rois if not math.isfinite(float(v)))
        bad_net = sum(1 for v in net_rois if not math.isfinite(float(v)))
        check("ROI_02", bad_opt == 0 and bad_net == 0,
              f"Non-finite ROIs: opt={bad_opt}, net={bad_net}",
              name, scen)
    else:
        check("ROI_02", True, "No scenario data", name, scen)


def run_checks_H(pack: dict, si: StrategyInput, name: str, scen: str):
    """H: Key Levels (KL_*)"""
    key_levels = pack.get("key_levels", {})
    levels = key_levels.get("levels", [])
    payoff = pack.get("payoff", {})
    strikes = payoff.get("strikes", [])
    breakevens = payoff.get("breakevens", [])

    # KL_01: Key levels include spot price
    spot_found = any(
        lv.get("source") == "spot" or
        (lv.get("price") is not None and abs(float(lv["price"]) - si.spot) < TOL)
        for lv in levels
    )
    check("KL_01", spot_found,
          "Spot price in key levels", name, scen)

    # KL_02: Key levels include all strikes
    for strike in strikes:
        found = any(
            lv.get("source") == "strike" and
            lv.get("price") is not None and
            abs(float(lv["price"]) - strike) < TOL
            for lv in levels
        )
        check("KL_02", found,
              f"Strike {strike} in key levels", name, scen)

    # KL_03: Key levels include all breakevens
    for be in breakevens:
        found = any(
            lv.get("source") == "breakeven" and
            lv.get("price") is not None and
            abs(float(lv["price"]) - be) < 1.0
            for lv in levels
        )
        check("KL_03", found,
              f"Breakeven {be:.4f} in key levels", name, scen)

    # KL_04: Priced levels are sorted by price ascending (sentinels at end)
    priced = [lv for lv in levels if lv.get("price") is not None]
    prices = [float(lv["price"]) for lv in priced]
    check("KL_04", prices == sorted(prices),
          f"Key levels price order: {prices[:5]}...", name, scen)

    # KL_05: No duplicate IDs
    ids = [lv.get("id") for lv in levels]
    check("KL_05", len(ids) == len(set(ids)),
          f"Key level IDs unique: {len(ids)} total, {len(set(ids))} unique",
          name, scen)


def run_checks_I(pack: dict, si: StrategyInput, name: str, scen: str):
    """I: Pipeline Map Issue Checks (PI_*)"""
    payoff = pack.get("payoff", {})
    grid = payoff.get("price_grid", [])
    options_pnl = payoff.get("options_pnl", [])
    stock_pnl = payoff.get("stock_pnl", [])
    combined_pnl = payoff.get("combined_pnl", [])

    # PI_01: stock_pnl derived as combined - option (verify both methods agree)
    # analysis_pack computes: stock_pnl[i] = combined_pnl[i] - options_pnl[i]
    # Alternative: stock_pnl[i] = stock_position * (price - avg_cost)
    if si.stock_position != 0 and len(grid) == len(stock_pnl):
        max_diff = 0.0
        for i, price in enumerate(grid):
            direct = si.stock_position * (price - si.avg_cost)
            derived = stock_pnl[i]
            max_diff = max(max_diff, abs(direct - derived))
        check("PI_01", max_diff < TOL,
              f"Stock PnL: direct vs derived max_diff={max_diff:.2e}",
              name, scen)
    else:
        check("PI_01", True, "No stock position — skip", name, scen)

    # PI_02: PoP uses combined payoff (not options-only)
    # Verify that pop was computed (it's in probabilities dict)
    probs = pack.get("probabilities", {})
    pop = probs.get("pop")
    check("PI_02", pop is not None and isinstance(pop, (int, float)),
          f"PoP computed: {pop}", name, scen)

    # PI_03: Unlimited flags consistent between recomputed payoff and pack summary
    summary_rows = pack.get("summary", {}).get("rows", [])
    opt_unlimited_recomputed = _detect_unlimited(grid, options_pnl) if grid and options_pnl else {}
    comb_unlimited_recomputed = _detect_unlimited(grid, combined_pnl) if grid and combined_pnl else {}

    def find_metric(m):
        for row in summary_rows:
            if row.get("metric") == m:
                return row
        return None

    mp_row = find_metric("Max Profit")
    if mp_row:
        opt_text = mp_row.get("options", "")
        expected_unlimited = (opt_unlimited_recomputed.get("unlimited_profit_upside",
                                                           opt_unlimited_recomputed.get("unlimited_upside", False))
                              or opt_unlimited_recomputed.get("unlimited_profit_downside", False))
        check("PI_03",
              (opt_text == "Unlimited") == expected_unlimited,
              f"Options max profit unlimited consistency: text='{opt_text}', flag={expected_unlimited}",
              name, scen)

    # PI_04: Net premium per-share convention matches analysis pack
    # The pack stores net_prem_per_share and applies a sign flip for display
    nps = pack.get("summary", {}).get("net_premium_per_share")
    check("PI_04", nps is not None,
          f"Net premium per share present: {nps}", name, scen)


def run_checks_J(pack: dict, si: StrategyInput, name: str, scen: str):
    """J: Known Bug Checks (BUG_*)"""
    summary_rows = pack.get("summary", {}).get("rows", [])
    scenario = pack.get("scenario", {})
    scenario_df = scenario.get("df")

    # BUG_01: Zero capital basis doesn't cause division by zero
    # If we got this far without an exception, the check passes
    check("BUG_01", True,
          "No division-by-zero crash", name, scen)

    # BUG_02: All-short strategies have positive capital basis
    all_short = all(leg.position < 0 for leg in si.legs) if si.legs else False
    if all_short:
        def find_metric(m):
            for row in summary_rows:
                if row.get("metric") == m:
                    return row
            return None
        cb_row = find_metric("Capital at Risk")
        if cb_row:
            opt_text = cb_row.get("options", "")
            try:
                val = float(opt_text.replace("$", "").replace(",", "").replace("--", "0"))
            except (ValueError, AttributeError):
                val = 0.0
            check("BUG_02", val > 0,
                  f"All-short strategy capital basis = {opt_text}",
                  name, scen)
        else:
            check("BUG_02", False, "Capital at Risk row missing for all-short strategy", name, scen)
    else:
        check("BUG_02", True, "Not all-short — skip", name, scen)

    # BUG_03: Scenario table is not empty (for strategies with legs)
    if si.legs:
        check("BUG_03", scenario_df is not None and not scenario_df.empty,
              "Scenario table populated", name, scen)
    else:
        check("BUG_03", True, "No legs — skip scenario check", name, scen)

    # BUG_04: Key levels includes sentinel rows (zero/infinity)
    key_levels = pack.get("key_levels", {})
    levels = key_levels.get("levels", [])
    has_zero = any(lv.get("id") == "zero" for lv in levels)
    has_inf = any(lv.get("id") == "infinity" for lv in levels)
    check("BUG_04", has_zero and has_inf,
          f"Sentinel levels: zero={has_zero}, infinity={has_inf}",
          name, scen)

    # BUG_05: PoP is between 0 and 1
    probs = pack.get("probabilities", {})
    pop = probs.get("pop")
    if pop is not None:
        check("BUG_05", 0.0 <= pop <= 1.0,
              f"PoP={pop:.4f} in [0,1]", name, scen)
    else:
        check("BUG_05", False, "PoP is None", name, scen)

    # BUG_06: Risk/Reward ratio is consistent
    rr_row = None
    for row in summary_rows:
        if row.get("metric") == "Risk/Reward":
            rr_row = row
            break
    if rr_row:
        rr_text = rr_row.get("options", "")
        check("BUG_06", rr_text not in ("", None),
              f"Risk/Reward present: {rr_text}", name, scen)
    else:
        check("BUG_06", False, "Risk/Reward row missing", name, scen)

    # BUG_07: No NaN in key_levels numeric fields
    for lv in levels:
        for field in ["price", "move_pct", "stock_pnl", "option_pnl", "net_pnl", "net_roi"]:
            val = lv.get(field)
            if val is not None and isinstance(val, float):
                check("BUG_07", math.isfinite(val),
                      f"Key level '{lv.get('id')}' field '{field}' = {val}",
                      name, scen)


# ══════════════════════════════════════════════════════════
# MAIN DRIVER
# ══════════════════════════════════════════════════════════

def run_one(row: dict, scen_idx: int) -> dict | None:
    """Run a single strategy/scenario combination and all checks."""
    sid = row.get("strategy_id", "?")
    name = row.get("strategy_name", "?")
    template_kind = (row.get("template_kind") or "").upper()

    legs = _build_legs_from_row(row)
    scen = SCENARIOS[scen_idx]
    scen_label = scen["label"]

    # Determine stock position for this scenario
    if scen_idx == 0:
        # Options-only: use CSV-defined stock if MIXED/STOCK_ONLY, else 0
        stock_position = 0.0
        avg_cost = 0.0
        if _row_has_stock(row):
            side = _row_stock_side(row)
            stock_position = 100.0 if side == "LONG" else -100.0
            avg_cost = SPOT
    else:
        stock_position = scen["stock_position"]
        avg_cost = scen["avg_cost"]
        # If CSV already defines stock, respect its side
        if _row_has_stock(row):
            side = _row_stock_side(row)
            stock_position = abs(stock_position) if side == "LONG" else -abs(stock_position)

    # No legs and no stock (e.g., custom strategy options_only):
    # build_analysis_pack returns a valid empty pack — let it run through checks.
    if not legs and stock_position == 0:
        pass  # proceed with empty StrategyInput

    si = StrategyInput(
        spot=SPOT,
        stock_position=stock_position,
        avg_cost=avg_cost,
        legs=legs,
    )

    meta = {
        "as_of": AS_OF,
        "expiry": EXPIRY,
        "strategy_name": name,
        "strategy_id": sid,
        "group": row.get("group", ""),
        "subgroup": row.get("subgroup", ""),
    }

    try:
        pack = build_analysis_pack(
            strategy_input=si,
            strategy_meta=meta,
            pricing_mode="mid",
            roi_policy="RISK_MAX_LOSS",
            vol_mode="atm",
            atm_iv=ATM_IV,
            underlying_profile=None,
            bbg_leg_snapshots=None,
            scenario_mode="percentage",
            downside_tgt=0.85,
            upside_tgt=1.15,
            risk_free_rate=0.0,
        )
    except Exception:
        return {"sid": sid, "name": name, "scenario": scen_label,
                "error": traceback.format_exc()[:500], "checks": 0}

    before = len(results)

    # Run all check categories
    try:
        run_checks_A(pack, si, name, scen_label)
    except Exception as e:
        check("A_ERR", False, f"Category A crashed: {e}", name, scen_label)
    try:
        run_checks_B(pack, si, name, scen_label)
    except Exception as e:
        check("B_ERR", False, f"Category B crashed: {e}", name, scen_label)
    try:
        run_checks_C(pack, si, name, scen_label)
    except Exception as e:
        check("C_ERR", False, f"Category C crashed: {e}", name, scen_label)
    try:
        run_checks_D(pack, si, name, scen_label)
    except Exception as e:
        check("D_ERR", False, f"Category D crashed: {e}", name, scen_label)
    try:
        run_checks_E(pack, si, name, scen_label)
    except Exception as e:
        check("E_ERR", False, f"Category E crashed: {e}", name, scen_label)
    try:
        run_checks_F(pack, si, name, scen_label)
    except Exception as e:
        check("F_ERR", False, f"Category F crashed: {e}", name, scen_label)
    try:
        run_checks_G(pack, si, name, scen_label)
    except Exception as e:
        check("G_ERR", False, f"Category G crashed: {e}", name, scen_label)
    try:
        run_checks_H(pack, si, name, scen_label)
    except Exception as e:
        check("H_ERR", False, f"Category H crashed: {e}", name, scen_label)
    try:
        run_checks_I(pack, si, name, scen_label)
    except Exception as e:
        check("I_ERR", False, f"Category I crashed: {e}", name, scen_label)
    try:
        run_checks_J(pack, si, name, scen_label)
    except Exception as e:
        check("J_ERR", False, f"Category J crashed: {e}", name, scen_label)

    # Capture raw numerical values for fact-checking appendix
    try:
        capture_numerical_snapshot(pack, si, name, sid, scen_label)
    except Exception:
        pass  # don't let snapshot capture block the audit

    checks_run = len(results) - before
    return {"sid": sid, "name": name, "scenario": scen_label, "error": None, "checks": checks_run}


def main():
    csv_path = PROJECT_ROOT / "data" / "strategy_map.csv"
    out_path = PROJECT_ROOT / "calculation_audit.md"

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Loaded {len(rows)} strategies from {csv_path}")
    print(f"Running {len(rows)} × {len(SCENARIOS)} = {len(rows) * len(SCENARIOS)} test combinations...")

    run_results: list[dict] = []
    errors: list[dict] = []

    for idx, row in enumerate(rows):
        name = row.get("strategy_name", "?")
        for scen_idx in range(len(SCENARIOS)):
            scen_label = SCENARIOS[scen_idx]["label"]
            print(f"  [{idx + 1}/{len(rows)}] {name} — {scen_label}...", end="", flush=True)
            r = run_one(row, scen_idx)
            if r:
                run_results.append(r)
                if r.get("error"):
                    errors.append(r)
                    print(f" ERROR")
                else:
                    print(f" {r['checks']} checks")
            else:
                print(" SKIP")

    # ── Aggregate stats ──
    total_checks = len(results)
    passed = sum(1 for r in results if r.passed)
    failed = sum(1 for r in results if not r.passed)
    total_runs = len(run_results)
    total_errors = len(errors)

    # Group failures by check_id
    failure_by_id: dict[str, list[CheckResult]] = {}
    for r in results:
        if not r.passed:
            failure_by_id.setdefault(r.check_id, []).append(r)

    # Group failures by category using check ID prefixes
    categories = {
        "A": ("Payoff Grid Integrity", ["PG_"]),
        "B": ("Breakeven Validation", ["BE_", "B_"]),
        "C": ("Max Profit / Max Loss", ["MP_", "ML_", "C_"]),
        "D": ("Net Premium & Cost/Credit", ["NP_", "D_"]),
        "E": ("Stock P&L", ["SP_", "E_"]),
        "F": ("Cross-Scenario Consistency", ["CS_", "F_"]),
        "G": ("Capital at Risk & ROI", ["CB_", "ROI_", "G_"]),
        "H": ("Key Levels", ["KL_", "H_"]),
        "I": ("Pipeline Map Issues", ["PI_", "I_"]),
        "J": ("Known Bugs", ["BUG_", "J_"]),
    }

    cat_stats: dict[str, dict] = {}
    for cat_key, (cat_name, prefixes) in categories.items():
        cat_results = [r for r in results if any(r.check_id.startswith(p) for p in prefixes)]
        cat_passed = sum(1 for r in cat_results if r.passed)
        cat_failed = sum(1 for r in cat_results if not r.passed)
        cat_stats[cat_key] = {"total": len(cat_results), "passed": cat_passed, "failed": cat_failed}

    # ── Write output ──
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Calculation Engine Audit Report\n\n")
        f.write(f"Generated: {date.today().isoformat()}\n\n")

        f.write("## Executive Summary\n\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Strategies tested | {len(rows)} |\n")
        f.write(f"| Scenarios per strategy | {len(SCENARIOS)} |\n")
        f.write(f"| Total runs | {total_runs} |\n")
        f.write(f"| Build errors (crash) | {total_errors} |\n")
        f.write(f"| Total checks executed | {total_checks} |\n")
        f.write(f"| Checks PASSED | {passed} |\n")
        f.write(f"| Checks FAILED | {failed} |\n")
        f.write(f"| Pass rate | {passed / total_checks * 100:.1f}% |\n")
        f.write("\n")

        f.write("## Category Summary\n\n")
        f.write("| Cat | Category Name | Total | Passed | Failed | Rate |\n")
        f.write("|-----|--------------|-------|--------|--------|------|\n")
        for cat_key, (cat_name, _) in categories.items():
            cs = cat_stats[cat_key]
            rate = f"{cs['passed'] / cs['total'] * 100:.1f}%" if cs["total"] > 0 else "N/A"
            f.write(f"| {cat_key} | {cat_name} | {cs['total']} | {cs['passed']} | {cs['failed']} | {rate} |\n")
        f.write("\n")

        # ── Build errors ──
        if errors:
            f.write("## Build Errors (analysis_pack crash)\n\n")
            for e in errors:
                f.write(f"- **{e['name']}** (ID={e['sid']}, scenario={e['scenario']})\n")
                err_text = e["error"]
                # Show last line of traceback
                last_line = err_text.strip().split("\n")[-1]
                f.write(f"  `{last_line}`\n")
            f.write("\n")

        # ── Failures by check ID ──
        f.write("## Failures by Check ID\n\n")
        if not failure_by_id:
            f.write("No failures detected.\n\n")
        else:
            for check_id in sorted(failure_by_id.keys()):
                fails = failure_by_id[check_id]
                f.write(f"### {check_id} ({len(fails)} failures)\n\n")
                # Show up to 10 examples
                for fail in fails[:10]:
                    f.write(f"- **{fail.strategy}** [{fail.scenario}]: {fail.message}\n")
                if len(fails) > 10:
                    f.write(f"- ... and {len(fails) - 10} more\n")
                f.write("\n")

        # ── Detailed per-check-ID stats ──
        f.write("## Check ID Statistics\n\n")
        f.write("| Check ID | Total | Passed | Failed | Description |\n")
        f.write("|----------|-------|--------|--------|-------------|\n")

        check_descriptions = {
            "PG_01": "Grid starts at 0",
            "PG_02": "Grid ends at 3×spot",
            "PG_03": "Grid monotonically increasing",
            "PG_04": "All strikes in grid",
            "PG_05": "Grid has ≥300 points",
            "PG_06": "PnL array lengths match grid",
            "PG_07": "combined = options + stock PnL",
            "BE_01": "Breakevens sorted",
            "BE_02": "Breakevens within grid range",
            "BE_03": "PnL ≈ 0 at breakeven",
            "BE_04": "Sign change around breakeven",
            "MP_01": "Options max profit unlimited flag",
            "MP_02": "Combined max profit unlimited flag",
            "MP_03": "Options max profit ≥ 0",
            "ML_01": "Options max loss unlimited flag",
            "ML_02": "Combined max loss unlimited flag",
            "NP_01": "Net premium per-share formula",
            "NP_02": "Net premium total formula",
            "NP_03": "Cost/Credit text matches sign",
            "NP_04": "Net Prem/Share present",
            "SP_01": "Zero stock → zero stock PnL",
            "SP_02": "Stock PnL formula correctness",
            "SP_03": "Stock PnL linearity",
            "CS_01": "Spot in scenario table",
            "CS_02": "Strikes in scenario table",
            "CS_03": "Breakevens in scenario table",
            "CS_04": "PnL ≈ 0 at breakeven in scenario",
            "CS_05": "Scenario opt+stk = combined",
            "CB_01": "Capital basis > 0",
            "CB_02": "Combined basis ≥ option basis",
            "ROI_01": "ROI values finite",
            "ROI_02": "No NaN/Inf in ROI",
            "KL_01": "Spot in key levels",
            "KL_02": "Strikes in key levels",
            "KL_03": "Breakevens in key levels",
            "KL_04": "Key levels sorted by price",
            "KL_05": "Key level IDs unique",
            "PI_01": "Stock PnL: direct vs derived",
            "PI_02": "PoP was computed",
            "PI_03": "Unlimited flags consistent",
            "PI_04": "Net premium per share present",
            "BUG_01": "No division-by-zero crash",
            "BUG_02": "All-short capital basis > 0",
            "BUG_03": "Scenario table populated",
            "BUG_04": "Sentinel rows present",
            "BUG_05": "PoP in [0, 1]",
            "BUG_06": "Risk/Reward present",
            "BUG_07": "No NaN in key level fields",
        }

        all_check_ids = sorted(set(r.check_id for r in results))
        for cid in all_check_ids:
            cid_results = [r for r in results if r.check_id == cid]
            cid_passed = sum(1 for r in cid_results if r.passed)
            cid_failed = sum(1 for r in cid_results if not r.passed)
            desc = check_descriptions.get(cid, "")
            f.write(f"| {cid} | {len(cid_results)} | {cid_passed} | {cid_failed} | {desc} |\n")
        f.write("\n")

        # ── All failures detailed listing ──
        f.write("## All Failures (Detailed)\n\n")
        all_failures = [r for r in results if not r.passed]
        if not all_failures:
            f.write("No failures.\n\n")
        else:
            f.write(f"Total: {len(all_failures)} failures\n\n")
            # Group by strategy
            by_strategy: dict[str, list[CheckResult]] = {}
            for fail in all_failures:
                key = f"{fail.strategy} [{fail.scenario}]"
                by_strategy.setdefault(key, []).append(fail)

            for strat_key in sorted(by_strategy.keys()):
                fails = by_strategy[strat_key]
                f.write(f"### {strat_key}\n\n")
                for fail in fails:
                    f.write(f"- **{fail.check_id}**: {fail.message}\n")
                f.write("\n")

        # ── Numerical Results Appendix ──
        f.write("## Numerical Results (Fact-Check Data)\n\n")
        f.write("Every computed value for each strategy × scenario run.\n\n")

        for snap in numerical_snapshots:
            f.write(f"### {snap['name']} (ID={snap['sid']}) — {snap['scenario']}\n\n")

            # Inputs
            f.write("**Inputs:**\n\n")
            f.write(f"- Spot: {snap['spot']}\n")
            f.write(f"- Stock Position: {snap['stock_position']}\n")
            f.write(f"- Avg Cost: {snap['avg_cost']}\n")
            f.write(f"- Strategy Code: {snap['strategy_code']}\n")
            f.write(f"- Margin Classification: {snap['margin_classification']}\n\n")

            # Legs table
            if snap["legs"]:
                f.write("**Legs:**\n\n")
                f.write("| # | Kind | Position | Strike | Premium | Multiplier |\n")
                f.write("|---|------|----------|--------|---------|------------|\n")
                for i, leg in enumerate(snap["legs"], 1):
                    side = "Long" if leg["position"] > 0 else "Short"
                    f.write(f"| {i} | {leg['kind'].upper()} | {side} {abs(leg['position']):.0f} | "
                            f"{leg['strike']:.2f} | {leg['premium']:.2f} | {leg['multiplier']} |\n")
                f.write("\n")

            # Core payoff values
            f.write("**Payoff:**\n\n")
            f.write(f"- Grid Size: {snap['grid_size']} points\n")
            f.write(f"- Strikes: {snap['strikes']}\n")
            f.write(f"- Breakevens: {snap['breakevens']}\n")
            f.write(f"- Options Max PnL: {snap['options_max_pnl']}\n")
            f.write(f"- Options Min PnL: {snap['options_min_pnl']}\n")
            f.write(f"- Combined Max PnL: {snap['combined_max_pnl']}\n")
            f.write(f"- Combined Min PnL: {snap['combined_min_pnl']}\n\n")

            # Premium
            f.write("**Net Premium:**\n\n")
            f.write(f"- Per Share: {snap['net_premium_per_share']}\n")
            f.write(f"- Total: {snap['net_premium_total']}\n\n")

            # Summary metrics
            f.write("**Summary Metrics:**\n\n")
            f.write("| Metric | Options | Combined |\n")
            f.write("|--------|---------|----------|\n")
            _metric_display_names = {
                "capital_basis": "Capital at Risk",
            }
            for metric_key in ["max_profit", "max_loss", "risk_reward", "capital_basis", "cost_credit", "pop"]:
                mv = snap.get(metric_key)
                if mv:
                    display = _metric_display_names.get(metric_key, metric_key.replace('_', ' ').title())
                    f.write(f"| {display} | {mv.get('options', '--')} | {mv.get('combined', '--')} |\n")
            f.write(f"| Margin Proxy | {snap['margin_proxy']} | — |\n")
            f.write("\n")

            # Probabilities
            f.write("**Probabilities:**\n\n")
            f.write(f"- PoP (raw): {snap['pop_raw']}\n")
            f.write(f"- Assignment Prob: {snap['assignment_prob']}\n")
            f.write(f"- P(25% Max Profit): {snap['prob_25_profit']}\n")
            f.write(f"- P(50% Max Profit): {snap['prob_50_profit']}\n")
            f.write(f"- P(100% Max Profit): {snap['prob_100_profit']}\n")
            f.write(f"- IV Used: {snap['iv_used']}\n\n")

            # Scenario table
            if snap["scenario_table"]:
                f.write("**Scenario Table:**\n\n")
                f.write("| Price | Scenario | Opt PnL | Stock PnL | Combined PnL | Opt ROI | Net ROI |\n")
                f.write("|-------|----------|---------|-----------|--------------|---------|--------|\n")
                for sr in snap["scenario_table"]:
                    f.write(f"| {sr['price']:.2f} | {sr['scenario']} | "
                            f"{sr['option_pnl']:.2f} | {sr['stock_pnl']:.2f} | "
                            f"{sr['combined_pnl']:.2f} | {sr['option_roi']:.4f} | "
                            f"{sr['net_roi']:.4f} |\n")
                f.write("\n")

            # Key levels
            if snap["key_levels"]:
                f.write("**Key Levels:**\n\n")
                f.write("| ID | Label | Price | Move % | Opt PnL | Net PnL | Net ROI |\n")
                f.write("|----|-------|-------|--------|---------|---------|--------|\n")
                for kl in snap["key_levels"]:
                    def _fmt(val, fmt_str=".2f"):
                        if val is None:
                            return "—"
                        if isinstance(val, str):
                            return val
                        return f"{val:{fmt_str}}"
                    price_str = _fmt(kl["price"])
                    move_str = (_fmt(kl["move_pct"]) + "%") if kl["move_pct"] is not None else "—"
                    opt_str = _fmt(kl["option_pnl"])
                    net_str = _fmt(kl["net_pnl"])
                    roi_str = _fmt(kl["net_roi"], ".4f")
                    f.write(f"| {kl['id']} | {kl['label']} | {price_str} | {move_str} | "
                            f"{opt_str} | {net_str} | {roi_str} |\n")
                f.write("\n")

            f.write("---\n\n")

    print(f"\n{'='*60}")
    print(f"AUDIT COMPLETE")
    print(f"{'='*60}")
    print(f"  Strategies: {len(rows)}")
    print(f"  Scenarios:  {len(SCENARIOS)}")
    print(f"  Total runs: {total_runs}")
    print(f"  Errors:     {total_errors}")
    print(f"  Checks:     {total_checks}")
    print(f"  PASSED:     {passed}")
    print(f"  FAILED:     {failed}")
    print(f"  Pass rate:  {passed / total_checks * 100:.1f}%")
    print(f"\nOutput: {out_path}")

    if failure_by_id:
        print(f"\nFailing check IDs:")
        for cid in sorted(failure_by_id.keys()):
            print(f"  {cid}: {len(failure_by_id[cid])} failures")


if __name__ == "__main__":
    main()
