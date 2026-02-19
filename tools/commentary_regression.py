"""Commentary regression diagnostic — captures narrative output for all 63 strategies.

Usage:  python tools/commentary_regression.py
Output: commentary_regression.md in project root

READ-ONLY diagnostic: does NOT modify any application code.
"""
from __future__ import annotations

import csv
import sys
import os
import traceback
from datetime import date
from pathlib import Path

# Ensure project root is on sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from core.models import OptionLeg, StrategyInput
from core.analysis_pack import build_analysis_pack

# ── Strike mapping from CSV descriptors to synthetic prices ──
STRIKE_MAP = {
    "":        100.0,   # fallback (ATM)
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


def _synthetic_premium(kind: str, strike: float, spot: float = SPOT) -> float:
    """Generate a realistic premium based on moneyness.

    Uses a simple intrinsic + time value model so that different strikes
    produce different premiums, avoiding zero-capital-basis edge cases.
    """
    time_value = 2.50  # base time value
    if kind == "call":
        intrinsic = max(spot - strike, 0.0)
    else:
        intrinsic = max(strike - spot, 0.0)
    # OTM options get smaller time value
    otm_distance = abs(strike - spot) / spot
    tv_decay = max(0.3, 1.0 - otm_distance * 3.0)
    return round(intrinsic + time_value * tv_decay, 2)


def _build_legs_and_stock(row: dict) -> tuple[list[OptionLeg], float, float]:
    """Parse CSV row into (option_legs, stock_position, avg_cost)."""
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
            multiplier = 100  # 1 "contract" = 100 shares
            stock_position = qty * multiplier if leg_side == "LONG" else -qty * multiplier
            avg_cost = SPOT
            continue

        # Option leg
        kind = leg_type.lower()  # "call" or "put"
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


def _format_scenario(scenario: dict | None) -> str:
    if scenario is None:
        return "  (None)\n"
    lines = []
    lines.append(f"  **{scenario.get('title', '?')}**")
    lines.append(f"  Condition: {scenario.get('condition', '--')}")
    body = scenario.get("body", "--")
    lines.append(f"  Body: {body}")
    overlay = scenario.get("overlay_pnl")
    stock_only = scenario.get("stock_only_pnl")
    delta = scenario.get("delta_vs_stock")
    if overlay is not None or delta is not None:
        lines.append(f"  overlay_pnl={overlay}, stock_only_pnl={stock_only}, delta_vs_stock={delta}")
    anchors = scenario.get("anchors", [])
    if anchors:
        anchor_strs = [f"{a.get('label','?')}@{a.get('price','?')}" for a in anchors]
        lines.append(f"  Anchors: {', '.join(anchor_strs)}")
    return "\n".join(lines) + "\n"


def _format_commentary_blocks(blocks: list[dict] | None) -> str:
    if not blocks:
        return "  (None)\n"
    lines = []
    for block in blocks:
        level = block.get("level", "?")
        text = block.get("text", "--")
        lines.append(f"  - **{level}**: {text}")
    return "\n".join(lines) + "\n"


def _run_one(row: dict, with_stock_override: bool) -> dict:
    """Run analysis for one strategy. Returns result dict."""
    sid = row.get("strategy_id", "?")
    name = row.get("strategy_name", "?")
    group = row.get("group", "?")
    subgroup = row.get("subgroup", "?")

    legs, stock_position, avg_cost = _build_legs_and_stock(row)

    # For "with stock" variant, ensure there's a stock position
    if with_stock_override and stock_position == 0.0:
        stock_position = 100.0
        avg_cost = SPOT

    # Stock-only strategies (no option legs)
    if not legs and stock_position == 0.0:
        return {
            "sid": sid, "name": name, "group": group, "subgroup": subgroup,
            "error": "No legs and no stock position",
            "variant": "with_stock" if with_stock_override else "options_only",
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
        "subgroup": subgroup,
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
            "sid": sid, "name": name, "group": group, "subgroup": subgroup,
            "error": traceback.format_exc(),
            "variant": "with_stock" if with_stock_override else "options_only",
        }

    narrative = pack.get("narrative_scenarios", {})
    commentary = pack.get("commentary_blocks", [])
    trace = narrative.get("trace", {}) if isinstance(narrative, dict) else {}

    return {
        "sid": sid, "name": name, "group": group, "subgroup": subgroup,
        "variant": "with_stock" if with_stock_override else "options_only",
        "narrative": narrative,
        "commentary": commentary,
        "rule_id": trace.get("rule_id"),
        "rule_version": trace.get("version"),
        "error": None,
    }


def main():
    csv_path = PROJECT_ROOT / "data" / "strategy_map.csv"
    out_path = PROJECT_ROOT / "commentary_regression.md"

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Loaded {len(rows)} strategies from {csv_path}")

    results: list[dict] = []
    for row in rows:
        template_kind = (row.get("template_kind") or "").upper()

        # Options-only variant
        r_opt = _run_one(row, with_stock_override=False)
        results.append(r_opt)

        # With-stock variant (skip if already MIXED or STOCK_ONLY with stock)
        r_stk = _run_one(row, with_stock_override=True)
        results.append(r_stk)

    # ── Aggregate stats ──
    total_strategies = len(rows)
    total_runs = len(results)
    errors = [r for r in results if r.get("error")]
    empty_narratives = []
    for r in results:
        if r.get("error"):
            continue
        narr = r.get("narrative", {})
        if not narr:
            empty_narratives.append(r)
            continue
        bear = narr.get("bear")
        base = narr.get("base")
        bull = narr.get("bull")
        if not bear and not base and not bull:
            empty_narratives.append(r)

    # Check for identical bodies across strategies (generic templating)
    body_sets: dict[str, list[str]] = {}
    for r in results:
        if r.get("error"):
            continue
        narr = r.get("narrative", {})
        for kind in ["bear", "base", "bull"]:
            scenario = narr.get(kind) if isinstance(narr, dict) else None
            if isinstance(scenario, dict):
                body = scenario.get("body", "")
                if body and body != "--":
                    body_sets.setdefault(body, []).append(f"{r['name']}({r['variant']})")

    duplicate_bodies = {body: names for body, names in body_sets.items() if len(names) >= 4}

    # Distinct rule IDs used
    rule_ids_used = set()
    for r in results:
        if r.get("error"):
            continue
        rid = r.get("rule_id")
        if rid:
            rule_ids_used.add(rid)

    # ── Write output ──
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Commentary Regression Report\n\n")
        f.write(f"Generated: {date.today().isoformat()}\n\n")

        f.write("## Summary\n\n")
        f.write(f"- **Total strategies in CSV**: {total_strategies}\n")
        f.write(f"- **Total runs** (options-only + with-stock): {total_runs}\n")
        f.write(f"- **Errors**: {len(errors)}\n")
        f.write(f"- **Empty/None narratives**: {len(empty_narratives)}\n")
        f.write(f"- **Distinct rule IDs matched**: {sorted(rule_ids_used) if rule_ids_used else 'None'}\n")
        f.write(f"- **Duplicate body texts** (same body across 4+ runs): {len(duplicate_bodies)}\n")

        if errors:
            f.write("\n### Errors\n\n")
            for r in errors:
                f.write(f"- **{r['name']}** (ID={r['sid']}, variant={r['variant']}): ")
                err = r["error"]
                # Truncate long tracebacks
                if len(err) > 300:
                    err = err[:300] + "..."
                f.write(f"`{err.strip()}`\n")

        if duplicate_bodies:
            f.write("\n### Duplicate Body Texts (possible generic templating)\n\n")
            for body, names in sorted(duplicate_bodies.items(), key=lambda x: -len(x[1])):
                truncated = body[:120] + "..." if len(body) > 120 else body
                f.write(f"- **{len(names)} runs** share: \"{truncated}\"\n")
                f.write(f"  Strategies: {', '.join(names[:8])}")
                if len(names) > 8:
                    f.write(f" ... and {len(names)-8} more")
                f.write("\n")

        f.write("\n---\n\n")
        f.write("## Per-Strategy Results\n\n")

        # Group by strategy ID
        for row in rows:
            sid = row.get("strategy_id", "?")
            name = row.get("strategy_name", "?")
            group = row.get("group", "?")
            subgroup = row.get("subgroup", "?")
            template_kind = row.get("template_kind", "?")

            strategy_results = [r for r in results if r["sid"] == sid]

            f.write(f"## Strategy: {name} (ID={sid}, Group={group}, Subgroup={subgroup}, Kind={template_kind})\n\n")

            for r in strategy_results:
                variant_label = "With Underlying Position" if r["variant"] == "with_stock" else "Options Only"
                f.write(f"### {variant_label}\n\n")

                if r.get("error"):
                    f.write(f"**ERROR**: `{r['error'].strip()[:500]}`\n\n")
                    continue

                rule_id = r.get("rule_id", "None")
                rule_ver = r.get("rule_version", "None")
                f.write(f"**Rule matched**: {rule_id} (v{rule_ver})\n\n")

                f.write("**Commentary Blocks:**\n")
                f.write(_format_commentary_blocks(r.get("commentary")))
                f.write("\n")

                f.write("**Narrative Scenarios:**\n\n")
                narr = r.get("narrative", {})
                if isinstance(narr, dict):
                    for kind in ["bear", "base", "bull"]:
                        scenario = narr.get(kind)
                        f.write(_format_scenario(scenario))
                        f.write("\n")
                else:
                    f.write("  (No narrative data)\n\n")

            f.write("---\n\n")

    print(f"Output written to {out_path}")
    print(f"  {total_strategies} strategies, {len(errors)} errors, {len(empty_narratives)} empty")


if __name__ == "__main__":
    main()
