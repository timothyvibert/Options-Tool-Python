"""Commentary V2 regression — captures payoff-driven commentary for all 63 strategies.

Usage:  python tools/commentary_v2_regression.py
Output: commentary_v2_regression.md in project root

READ-ONLY diagnostic: does NOT modify any application code.
"""
from __future__ import annotations

import csv
import sys
import traceback
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from core.models import OptionLeg, StrategyInput
from core.analysis_pack import build_analysis_pack
from core.commentary_v2 import build_commentary_v2

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
            stock_position = qty * multiplier if leg_side == "LONG" else -qty * multiplier
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


def _run_one(row: dict, with_stock_override: bool) -> dict:
    sid = row.get("strategy_id", "?")
    name = row.get("strategy_name", "?")
    group = row.get("group", "?")

    legs, stock_position, avg_cost = _build_legs_and_stock(row)

    if with_stock_override and stock_position == 0.0:
        stock_position = 100.0
        avg_cost = SPOT

    if not legs and stock_position == 0.0:
        return {
            "sid": sid, "name": name, "group": group,
            "variant": "with_stock" if with_stock_override else "options_only",
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
            "variant": "with_stock" if with_stock_override else "options_only",
            "error": traceback.format_exc(),
        }

    try:
        result = build_commentary_v2(pack)
    except Exception:
        return {
            "sid": sid, "name": name, "group": group,
            "variant": "with_stock" if with_stock_override else "options_only",
            "error": f"commentary_v2 failed: {traceback.format_exc()}",
        }

    strategy_code = pack.get("strategy", {}).get("strategy_code", "?")

    return {
        "sid": sid, "name": name, "group": group,
        "variant": "with_stock" if with_stock_override else "options_only",
        "strategy_code": strategy_code,
        "scenarios": result.get("narrative_scenarios", []),
        "blocks": result.get("commentary_blocks", []),
        "error": None,
    }


def main():
    csv_path = PROJECT_ROOT / "data" / "strategy_map.csv"
    out_path = PROJECT_ROOT / "commentary_v2_regression.md"

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Loaded {len(rows)} strategies from {csv_path}")

    results: list[dict] = []
    for row in rows:
        r_opt = _run_one(row, with_stock_override=False)
        results.append(r_opt)
        r_stk = _run_one(row, with_stock_override=True)
        results.append(r_stk)

    # ── Aggregate stats ──
    total_runs = len(results)
    errors = [r for r in results if r.get("error")]
    body_lengths: list[int] = []
    loss_mentions = 0
    client_mentions = 0
    dash_placeholders = 0
    empty_bodies = 0

    for r in results:
        if r.get("error"):
            continue
        for s in r.get("scenarios", []):
            body = s.get("body", "")
            body_lengths.append(len(body))
            if "\u2212$" in body or "-$" in body:
                loss_mentions += 1
            if "the client" in body.lower():
                client_mentions += 1
            if "--" in body:
                dash_placeholders += 1
            if not body or len(body.strip()) < 10:
                empty_bodies += 1

    avg_body_len = sum(body_lengths) / max(len(body_lengths), 1)

    # ── Write output ──
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Commentary V2 Regression Report\n\n")
        f.write(f"Generated: {date.today().isoformat()}\n\n")

        f.write("## Summary\n\n")
        f.write(f"- **Total strategies in CSV**: {len(rows)}\n")
        f.write(f"- **Total runs** (options-only + with-stock): {total_runs}\n")
        f.write(f"- **Errors**: {len(errors)}\n")
        f.write(f"- **Average body length**: {avg_body_len:.0f} chars\n")
        f.write(f"- **Bodies mentioning losses** (\u2212$): {loss_mentions}\n")
        f.write(f"- **Bodies mentioning 'the client'**: {client_mentions}\n")
        f.write(f"- **Bodies with '--' placeholders**: {dash_placeholders}\n")
        f.write(f"- **Empty bodies**: {empty_bodies}\n")

        if errors:
            f.write("\n### Errors\n\n")
            for r in errors:
                err = r["error"]
                if len(err) > 300:
                    err = err[:300] + "..."
                f.write(f"- **{r['name']}** (ID={r['sid']}, variant={r['variant']}): `{err.strip()}`\n")

        f.write("\n---\n\n")
        f.write("## Per-Strategy Results\n\n")

        for row in rows:
            sid = row.get("strategy_id", "?")
            name = row.get("strategy_name", "?")
            group = row.get("group", "?")

            strategy_results = [r for r in results if r["sid"] == sid]
            code = "?"
            for r in strategy_results:
                if r.get("strategy_code"):
                    code = r["strategy_code"]
                    break

            f.write(f"## Strategy: {name} (ID={sid}, Code={code})\n\n")

            for r in strategy_results:
                variant_label = "With Underlying Position" if r["variant"] == "with_stock" else "Options Only"
                f.write(f"### {variant_label}\n\n")

                if r.get("error"):
                    f.write(f"**ERROR**: `{r['error'].strip()[:500]}`\n\n")
                    continue

                for s in r.get("scenarios", []):
                    kind_label = s.get("kind", "?").capitalize()
                    condition = s.get("condition", "--")
                    body = s.get("body", "--")
                    f.write(f"**{kind_label}**: {condition}\n")
                    f.write(f"{body}\n\n")

            f.write("---\n\n")

    print(f"Output written to {out_path}")
    print(f"  {len(rows)} strategies, {len(errors)} errors, {empty_bodies} empty bodies")
    print(f"  avg body length: {avg_body_len:.0f} chars, dash placeholders: {dash_placeholders}")


if __name__ == "__main__":
    main()
