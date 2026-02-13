"""Commentary V2 Comprehensive Audit — tests all 63 strategies x cost basis scenarios.

Usage:  python tools/commentary_v2_audit.py
Output: commentary_v2_audit.md in project root

READ-ONLY diagnostic: does NOT modify any application code.
"""
from __future__ import annotations

import csv
import re
import sys
import traceback
from collections import defaultdict
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from core.models import OptionLeg, StrategyInput
from core.analysis_pack import build_analysis_pack
from core.commentary_v2 import build_commentary_v2

import numpy as np

# ── Constants ───────────────────────────────────────────────────────────

STRIKE_MAP = {
    "":        100.0,
    "ATM":     100.0,
    "LOWER":    92.0,
    "HIGHER":  108.0,
    "LOW":      85.0,
    "MID":     100.0,
    "HIGH":    115.0,
    "LOWEST":   80.0,
    "LOW-MID":  92.0,
    "HIGH-MID": 108.0,
    "HIGHEST":  120.0,
}

SPOT = 100.0
EXPIRY = "2026-04-17"
AS_OF = "2026-02-13"

_MINUS = "\u2212"  # Unicode minus sign

# Cost basis scenarios
COST_BASIS_SCENARIOS = [
    {"name": "Options Only",        "has_stock": False, "avg_cost_mult": None},
    {"name": "Cost Basis = Spot",    "has_stock": True,  "avg_cost_mult": 1.00},
    {"name": "Cost Basis far below", "has_stock": True,  "avg_cost_mult": 0.50},
    {"name": "Cost Basis at 85%",    "has_stock": True,  "avg_cost_mult": 0.85},
    {"name": "Cost Basis at 115%",   "has_stock": True,  "avg_cost_mult": 1.15},
    {"name": "Cost Basis at 150%",   "has_stock": True,  "avg_cost_mult": 1.50},
]


# ── Synthetic data helpers (reused from regression script) ──────────────


def _synthetic_premium(kind: str, strike: float, spot: float = SPOT) -> float:
    time_value = 2.50
    if kind == "call":
        intrinsic = max(spot - strike, 0.0)
    else:
        intrinsic = max(strike - spot, 0.0)
    otm_distance = abs(strike - spot) / spot
    tv_decay = max(0.3, 1.0 - otm_distance * 3.0)
    return round(intrinsic + time_value * tv_decay, 2)


def _build_legs_and_stock(row: dict) -> tuple[list[OptionLeg], float, float]:
    """Build legs and extract natural stock position from strategy_map row."""
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
            multiplier = 100
            stock_position = (
                qty * multiplier if leg_side == "LONG" else -qty * multiplier
            )
            avg_cost = SPOT
            continue

        kind = leg_type.lower()
        ratio = int(leg_ratio) if leg_ratio else 1
        position = ratio if leg_side == "LONG" else -ratio
        strike = STRIKE_MAP.get(leg_strike_key, 100.0)
        premium = _synthetic_premium(kind, strike)

        legs.append(OptionLeg(
            kind=kind,
            position=float(position),
            strike=strike,
            premium=premium,
            multiplier=100,
        ))

    return legs, stock_position, avg_cost


# ── Run one strategy x scenario ─────────────────────────────────────────


def _run_one(row: dict, scenario: dict) -> dict:
    """Run one strategy x scenario combination and return result dict."""
    sid = row.get("strategy_id", "?")
    name = row.get("strategy_name", "?")
    group = row.get("group", "?")
    template_kind = (row.get("template_kind") or "").strip().upper()
    scenario_name = scenario["name"]

    legs, natural_stock, natural_avg_cost = _build_legs_and_stock(row)

    # Determine stock position for this scenario
    if scenario["has_stock"]:
        if natural_stock != 0.0:
            # MIXED / STOCK_ONLY — keep natural stock direction, vary avg_cost
            stock_position = natural_stock
        else:
            # OPTIONS strategy — add synthetic 100-share long overlay
            stock_position = 100.0
        avg_cost = SPOT * scenario["avg_cost_mult"]
    else:
        # Scenario 1: options only — strip stock
        stock_position = 0.0
        avg_cost = 0.0

    if not legs and stock_position == 0.0:
        return {
            "sid": sid, "name": name, "group": group,
            "scenario_name": scenario_name, "template_kind": template_kind,
            "error": "No legs and no stock position",
        }

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
        "group": group,
    }

    try:
        pack = build_analysis_pack(
            strategy_input=si,
            strategy_meta=meta,
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
    except Exception:
        return {
            "sid": sid, "name": name, "group": group,
            "scenario_name": scenario_name, "template_kind": template_kind,
            "error": traceback.format_exc(),
        }

    try:
        result = build_commentary_v2(pack)
    except Exception:
        return {
            "sid": sid, "name": name, "group": group,
            "scenario_name": scenario_name, "template_kind": template_kind,
            "error": f"commentary_v2 failed: {traceback.format_exc()}",
        }

    # Extract payoff data for directional checks
    payoff = pack.get("payoff", {})
    grid = np.asarray(payoff.get("price_grid", []), dtype=float)
    cmb_pnl = np.asarray(payoff.get("combined_pnl", []), dtype=float)

    return {
        "sid": sid, "name": name, "group": group,
        "scenario_name": scenario_name, "template_kind": template_kind,
        "has_stock": stock_position != 0.0,
        "avg_cost": avg_cost,
        "scenarios": result.get("narrative_scenarios", []),
        "grid": grid,
        "cmb_pnl": cmb_pnl,
        "error": None,
    }


# ── Check functions ──────────────────────────────────────────────────────


def _extract_sentences(body: str) -> list[str]:
    """Split body into sentences."""
    parts = re.split(r'(?<=[.!?])\s+', body.strip())
    return [p.strip() for p in parts if p.strip()]


def _check_body(body: str, zone_kind: str, result: dict) -> list[dict]:
    """Run all checks on a single zone body. Returns list of findings."""
    findings = []

    def add(check_id: str, excerpt: str):
        findings.append({"check_id": check_id, "excerpt": excerpt})

    # ── MD_BOLD: Markdown bold artifacts ──
    if "**" in body:
        bold_matches = re.findall(r'\*\*[^*]+\*\*', body)
        for m in bold_matches:
            add("MD_BOLD", m)

    # ── LOSS_POSITIVE: "loss/losses ... would be/is/are/of" + positive $ ──
    loss_pos = re.search(
        r'loss(?:es)?\s+(?:would be|is|are|of)\s+\*?\*?\+?\$[\d,]+\.\d{2}',
        body, re.IGNORECASE,
    )
    if loss_pos:
        match_text = loss_pos.group()
        if f'{_MINUS}$' not in match_text and '-$' not in match_text:
            # Verify it's actually positive (has + or no sign before $)
            if '+$' in match_text or re.search(r'(?<!\S)\$', match_text):
                add("LOSS_POSITIVE", match_text)

    # ── GAIN_NEGATIVE: "gain/gains ... " + negative $ ──
    gain_neg = re.search(
        r'gain(?:s)?\s+(?:would be|is|are|of)\s+\*?\*?['
        + _MINUS + r'\-]\$[\d,]+\.\d{2}',
        body, re.IGNORECASE,
    )
    if gain_neg:
        add("GAIN_NEGATIVE", gain_neg.group())

    # ── MISLEADING_DOWNSIDE: "full downside exposure" when large profit cushion ──
    if "full downside exposure" in body.lower():
        avg_cost = result.get("avg_cost", 0.0)
        if avg_cost and avg_cost < SPOT * 0.8:
            add(
                "MISLEADING_DOWNSIDE",
                f"full downside exposure (avg_cost={avg_cost:.0f}, spot={SPOT})",
            )

    # ── CAPITAL_AT_RISK ──
    if "capital at risk" in body.lower():
        match = re.search(r'capital at risk', body, re.IGNORECASE)
        add("CAPITAL_AT_RISK", match.group() if match else "capital at risk")

    # ── ENHANCEMENT ──
    if "enhancement over" in body.lower():
        match = re.search(r'enhancement over[^.]*', body, re.IGNORECASE)
        add("ENHANCEMENT", match.group()[:80] if match else "enhancement over")

    # ── RETURN_ON_CAPITAL ──
    roi_match = re.search(
        r'return on (?:the \$[\d,.]+|capital)', body, re.IGNORECASE,
    )
    if roi_match:
        add("RETURN_ON_CAPITAL", roi_match.group())

    # ── SIGNIFICANT_LEVERAGE ──
    if "significant leverage" in body.lower():
        match = re.search(r'significant leverage[^.]*', body, re.IGNORECASE)
        add("SIGNIFICANT_LEVERAGE", match.group()[:80] if match else "significant leverage")

    # ── EMPTY_BODY ──
    if len(body.strip()) == 0:
        add("EMPTY_BODY", "(empty)")

    # ── TOO_LONG ──
    if len(body) > 800:
        add("TOO_LONG", f"Length: {len(body)} chars")

    # ── TOO_SHORT ──
    if 0 < len(body.strip()) < 30:
        add("TOO_SHORT", body.strip())

    # ── NEG_ZERO ──
    if f'{_MINUS}$0.00' in body or '-$0.00' in body or '+$0.00' in body:
        zero_match = re.search(r'[' + _MINUS + r'+\-]\$0\.00', body)
        add("NEG_ZERO", zero_match.group() if zero_match else "+/-$0.00")

    # ── CLIENT_NO_STOCK: "the client" in options-only text ──
    if not result.get("has_stock") and "the client" in body.lower():
        add("CLIENT_NO_STOCK", "the client (in options-only context)")

    # ── SHARES_NO_STOCK: "the shares" in options-only text ──
    if not result.get("has_stock") and "the shares" in body.lower():
        add("SHARES_NO_STOCK", "the shares (in options-only context)")

    # ── LOCKED_IN ──
    locked = re.search(r'(?:gains are )?locked in(?: at)?', body, re.IGNORECASE)
    if locked:
        add("LOCKED_IN", locked.group())

    # ── LOSSES_CAP_POS: "losses are capped" + positive value ──
    losses_cap = re.search(
        r'losses are capped[^.]*\*?\*?\+\$[\d,]+\.\d{2}', body, re.IGNORECASE,
    )
    if losses_cap:
        add("LOSSES_CAP_POS", losses_cap.group()[:80])

    # ── GAINS_CAP_NEG: "gains are capped" + negative value ──
    gains_cap = re.search(
        r'gains are capped[^.]*\*?\*?[' + _MINUS + r'\-]\$[\d,]+\.\d{2}',
        body, re.IGNORECASE,
    )
    if gains_cap:
        add("GAINS_CAP_NEG", gains_cap.group()[:80])

    # ── FRAG_START: sentence fragment starting with "but ", "and ", ", but" ──
    sentences = _extract_sentences(body)
    for s in sentences:
        s_lower = s.lower().strip()
        if (
            s_lower.startswith("but ")
            or s_lower.startswith("and ")
            or s_lower.startswith(", but")
        ):
            add("FRAG_START", s[:80])

    # ── DUPLICATE_SENT: same sentence appears twice in one body ──
    if len(sentences) > 1:
        seen: set[str] = set()
        for s in sentences:
            normalized = s.strip().lower()
            if normalized in seen and len(normalized) > 10:
                add("DUPLICATE_SENT", s[:80])
            seen.add(normalized)

    # ── DECLINE_RISING / RISE_FALLING: directional mismatch ──
    grid = result.get("grid")
    cmb_pnl = result.get("cmb_pnl")
    if grid is not None and cmb_pnl is not None and len(grid) > 2:
        if zone_kind == "bearish":
            # Sample P&L at two points in the bearish zone
            lo = float(grid[max(1, len(grid) // 10)])
            hi = SPOT * 0.95
            pnl_lo = float(np.interp(lo, grid, cmb_pnl))
            pnl_hi = float(np.interp(hi, grid, cmb_pnl))
            # "rising" = P&L increases as stock price increases
            rising = pnl_hi > pnl_lo + 1.0

            if "position declines" in body.lower() and rising:
                add(
                    "DECLINE_RISING",
                    f"'position declines' but P&L rises ({pnl_lo:.0f}->{pnl_hi:.0f})",
                )
            if "position rises" in body.lower() and not rising:
                add(
                    "RISE_FALLING",
                    f"'position rises' but P&L falls ({pnl_lo:.0f}->{pnl_hi:.0f})",
                )

        elif zone_kind == "bullish":
            lo = SPOT * 1.05
            hi = float(grid[min(len(grid) - 2, len(grid) * 9 // 10)])
            pnl_lo = float(np.interp(lo, grid, cmb_pnl))
            pnl_hi = float(np.interp(hi, grid, cmb_pnl))
            rising = pnl_hi > pnl_lo + 1.0

            if "position declines" in body.lower() and rising:
                add(
                    "DECLINE_RISING",
                    f"'position declines' but P&L rises ({pnl_lo:.0f}->{pnl_hi:.0f})",
                )
            if "position rises" in body.lower() and not rising:
                add(
                    "RISE_FALLING",
                    f"'position rises' but P&L falls ({pnl_lo:.0f}->{pnl_hi:.0f})",
                )

    return findings


# ── Main ─────────────────────────────────────────────────────────────────


def main():
    csv_path = PROJECT_ROOT / "data" / "strategy_map.csv"
    out_path = PROJECT_ROOT / "commentary_v2_audit.md"

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Loaded {len(rows)} strategies from {csv_path}")

    all_findings: list[dict] = []
    total_zones = 0
    strategies_with_issues: set[str] = set()
    error_results: list[dict] = []
    total_runs = 0

    for idx, row in enumerate(rows, 1):
        template_kind = (row.get("template_kind") or "").strip().upper()
        name = row.get("strategy_name", "?")

        # Determine which scenarios to run
        if template_kind == "OPTIONS":
            scenarios_to_run = [COST_BASIS_SCENARIOS[0]]  # Options only
        elif template_kind == "STOCK_ONLY":
            # Stock-only: skip "Options Only" (no legs), run with-stock scenarios
            scenarios_to_run = COST_BASIS_SCENARIOS[1:]
        else:
            # MIXED: all 6
            scenarios_to_run = COST_BASIS_SCENARIOS

        for scenario in scenarios_to_run:
            total_runs += 1
            result = _run_one(row, scenario)

            if result.get("error"):
                error_results.append(result)
                continue

            for s in result.get("scenarios", []):
                zone_kind = s.get("kind", "?")
                body = s.get("body", "")
                total_zones += 1

                zone_findings = _check_body(body, zone_kind, result)
                for f in zone_findings:
                    all_findings.append({
                        "sid": result["sid"],
                        "name": result["name"],
                        "group": result["group"],
                        "scenario_name": result["scenario_name"],
                        "zone": zone_kind,
                        "check_id": f["check_id"],
                        "excerpt": f["excerpt"],
                        "full_body": body,
                    })
                    strategies_with_issues.add(result["sid"])

        if idx % 10 == 0:
            print(f"  ... processed {idx}/{len(rows)} strategies")

    # ── Aggregate by check ──
    check_counts: dict[str, int] = defaultdict(int)
    check_examples: dict[str, str] = {}
    for f in all_findings:
        check_counts[f["check_id"]] += 1
        if f["check_id"] not in check_examples:
            check_examples[f["check_id"]] = f["name"]

    clean_strategies = len(rows) - len(strategies_with_issues)

    # ── Print summary to stdout ──
    print(f"\n{'=' * 60}")
    print("COMMENTARY V2 AUDIT SUMMARY")
    print(f"{'=' * 60}")
    print(f"Total runs (strategy x scenario):    {total_runs}")
    print(f"Total zones checked:                 {total_zones}")
    print(f"Issues found:                        {len(all_findings)}")
    print(f"Unique strategies with issues:       {len(strategies_with_issues)} / {len(rows)}")
    print(f"Clean strategies:                    {clean_strategies} / {len(rows)}")
    print(f"Errors (could not build pack):       {len(error_results)}")
    print()

    if check_counts:
        print(f"{'Check ID':<25} {'Count':>6}  Example Strategy")
        print(f"{'-' * 25} {'-' * 6}  {'-' * 30}")
        for check_id in sorted(check_counts.keys()):
            count = check_counts[check_id]
            example = check_examples.get(check_id, "?")
            print(f"{check_id:<25} {count:>6}  {example}")

    if error_results:
        print(f"\nErrors:")
        for r in error_results:
            err_short = r["error"].strip().split("\n")[-1][:100]
            print(f"  {r['name']} ({r['scenario_name']}): {err_short}")

    print()

    # ── Write audit report ──
    with open(out_path, "w", encoding="utf-8") as out:
        out.write("# Commentary V2 Audit Report\n\n")
        out.write(f"Generated: {date.today().isoformat()}\n\n")

        out.write("## Summary\n")
        out.write(f"- Total runs (strategy x scenario): {total_runs}\n")
        out.write(
            f"- Total test cases: {total_zones}"
            " (strategies x scenarios x zones)\n"
        )
        out.write(f"- Issues found: {len(all_findings)}\n")
        out.write(
            f"- Unique strategies with issues:"
            f" {len(strategies_with_issues)} / {len(rows)}\n"
        )
        out.write(f"- Clean strategies: {clean_strategies} / {len(rows)}\n")
        out.write(f"- Errors: {len(error_results)}\n\n")

        out.write("## Issue Categories\n")
        out.write("| Check ID | Count | Example Strategy |\n")
        out.write("|----------|-------|------------------|\n")
        for check_id in sorted(check_counts.keys()):
            count = check_counts[check_id]
            example = check_examples.get(check_id, "?")
            out.write(f"| {check_id} | {count} | {example} |\n")
        out.write("\n")

        if error_results:
            out.write("## Errors\n\n")
            for r in error_results:
                err = r["error"]
                if len(err) > 300:
                    err = err[:300] + "..."
                out.write(
                    f"- **{r['name']}** (ID={r['sid']},"
                    f" scenario={r['scenario_name']}):"
                    f" `{err.strip()}`\n"
                )
            out.write("\n")

        out.write("## Detailed Findings\n\n")

        # Group by strategy + scenario
        grouped: dict[tuple, list[dict]] = defaultdict(list)
        for f in all_findings:
            key = (f["sid"], f["name"], f["scenario_name"])
            grouped[key].append(f)

        for (sid, name, scenario_name), group_findings in sorted(grouped.items()):
            out.write(
                f"### Strategy: {name} (ID={sid})"
                f" -- Cost Basis: {scenario_name}\n\n"
            )
            for f in group_findings:
                out.write(f"**Zone**: {f['zone']}\n")
                out.write(f"**Check**: {f['check_id']}\n")
                out.write(f"**Text**: \"{f['excerpt']}\"\n")
                # Escape any markdown in full body
                safe_body = f["full_body"].replace("\n", " ")
                out.write(f"**Full body**: \"{safe_body}\"\n\n")

    print(f"Audit report written to {out_path}")


if __name__ == "__main__":
    main()
