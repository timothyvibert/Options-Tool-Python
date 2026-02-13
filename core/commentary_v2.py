"""Commentary V2 — payoff-driven commentary engine.

Derives commentary from the analysis pack payoff grid and computed metrics.
No strategy-name templates, no rule matching — works for all strategies.
"""
from __future__ import annotations

from typing import Optional

import numpy as np

_MINUS = "\u2212"  # Unicode minus sign


# ── Formatting ──────────────────────────────────────────────────────────


def _fmt_price(v: float) -> str:
    return f"${v:,.2f}"


def _fmt_pnl(v: float, bold: bool = True) -> str:
    if v >= 0:
        s = f"+${v:,.2f}"
    else:
        s = f"{_MINUS}${abs(v):,.2f}"
    return f"**{s}**" if bold else s


def _fmt_pct(v: float) -> str:
    return f"{v:.1f}%"


# ── Data extraction ─────────────────────────────────────────────────────


def _parse_metric(
    rows: list, name: str, prefer: str = "combined",
) -> Optional[str]:
    for r in rows:
        if not isinstance(r, dict):
            continue
        if r.get("metric") == name:
            if prefer == "combined":
                return r.get("combined") or r.get("options")
            return r.get("options") or r.get("combined")
    return None


def _is_unlimited(text: object) -> bool:
    return isinstance(text, str) and text.strip() == "Unlimited"


def _parse_dollar(text: object) -> Optional[float]:
    if text is None or not isinstance(text, str):
        return None
    s = text.strip()
    if s in ("N/A", "Unlimited", "--", ""):
        return None
    neg = False
    if s.startswith("(") and s.endswith(")"):
        neg = True
        s = s[1:-1].strip()
    s = s.replace("$", "").replace(",", "")
    if s.startswith("-") or s.startswith(_MINUS):
        neg = True
        s = s.lstrip("-" + _MINUS)
    elif s.startswith("+"):
        s = s[1:]
    try:
        v = float(s)
    except (ValueError, TypeError):
        return None
    return -v if neg else v


def _extract(pack: dict) -> dict:
    """Pull all needed fields from the analysis pack into a flat dict."""
    underlying = pack.get("underlying") or {}
    spot = underlying.get("spot")
    if spot is None:
        spot = (pack.get("key_levels") or {}).get("meta", {}).get("spot", 100.0)
    spot = float(spot)

    payoff = pack.get("payoff") or {}
    grid = np.asarray(payoff.get("price_grid", []), dtype=float)
    opt_pnl = np.asarray(payoff.get("options_pnl", []), dtype=float)
    stk_pnl = np.asarray(payoff.get("stock_pnl", []), dtype=float)
    cmb_pnl = np.asarray(payoff.get("combined_pnl", []), dtype=float)
    strikes = sorted(payoff.get("strikes", []))
    breakevens = sorted(payoff.get("breakevens", []))

    legs = pack.get("legs") or []
    meta = (pack.get("key_levels") or {}).get("meta") or {}
    has_stock = bool(meta.get("has_stock_position", False))
    avg_cost = meta.get("avg_cost")
    if avg_cost is not None:
        avg_cost = float(avg_cost)
    shares = int(meta.get("shares", 0) or 0)

    ticker = underlying.get("ticker") or underlying.get("resolved_underlying")
    if isinstance(ticker, str):
        ticker = ticker.strip()
        if ticker.endswith(" Equity"):
            ticker = ticker[:-7].strip()
    if not ticker:
        ticker = "the stock"

    summary = pack.get("summary") or {}
    rows = summary.get("rows") or []
    net_prem = float(summary.get("net_premium_total_value", 0.0) or 0.0)
    # Code convention: positive = debit paid, negative = credit received
    prefer = "combined" if has_stock else "options"
    mp_str = _parse_metric(rows, "Max Profit", prefer)
    ml_str = _parse_metric(rows, "Max Loss", prefer)

    return dict(
        spot=spot, grid=grid, opt_pnl=opt_pnl, stk_pnl=stk_pnl,
        cmb_pnl=cmb_pnl, strikes=strikes, breakevens=breakevens,
        legs=legs, has_stock=has_stock, avg_cost=avg_cost, shares=shares,
        ticker=ticker, summary_rows=rows, net_prem=net_prem,
        mp_str=mp_str, ml_str=ml_str,
        mp_unlimited=_is_unlimited(mp_str),
        ml_unlimited=_is_unlimited(ml_str),
        mp_val=_parse_dollar(mp_str) if not _is_unlimited(mp_str) else None,
        ml_val=_parse_dollar(ml_str) if not _is_unlimited(ml_str) else None,
    )


# ── Payoff analysis ─────────────────────────────────────────────────────


def _find_flat_region(
    grid: np.ndarray, pnl: np.ndarray, direction: str = "left",
) -> tuple[Optional[float], Optional[float]]:
    """Detect capped (flat) P&L regions.

    direction="left"  → scan from low prices rightward  (downside floor)
    direction="right" → scan from high prices leftward  (upside ceiling)

    Returns (edge_price, flat_pnl_value) or (None, None).
    """
    n = len(pnl)
    if n < 10:
        return None, None
    tol = 1.0
    min_pts = 5

    if direction == "left":
        ref = float(pnl[0])
        edge = 0
        for i in range(1, n):
            if abs(float(pnl[i]) - ref) <= tol:
                edge = i
            else:
                break
        if edge >= min_pts:
            return float(grid[edge]), ref
    else:
        ref = float(pnl[-1])
        edge = n - 1
        for i in range(n - 2, -1, -1):
            if abs(float(pnl[i]) - ref) <= tol:
                edge = i
            else:
                break
        if (n - 1 - edge) >= min_pts:
            return float(grid[edge]), ref
    return None, None


def _zone_is_flat(
    grid: np.ndarray, pnl: np.ndarray, lo: float, hi: float,
) -> tuple[bool, Optional[float]]:
    mask = (grid >= lo) & (grid <= hi)
    z = pnl[mask]
    if len(z) < 3:
        return False, None
    if float(np.max(z) - np.min(z)) < 1.0:
        return True, float(np.mean(z))
    return False, None


def _compute_slope(
    grid: np.ndarray, pnl: np.ndarray, lo: float, hi: float,
) -> float:
    """Normalized slope in a zone.  1.0 ≈ dollar-for-dollar per contract."""
    mask = (grid >= lo) & (grid <= hi)
    zp, zv = grid[mask], pnl[mask]
    if len(zp) < 2:
        return 0.0
    dx = float(zp[-1] - zp[0])
    if dx < 0.01:
        return 0.0
    return float(zv[-1] - zv[0]) / dx / 100.0


# ── Zone determination ──────────────────────────────────────────────────


def _determine_zones(
    strikes: list[float], spot: float,
) -> tuple[float, float, float, float]:
    """Return (bear_upper, stag_lower, stag_upper, bull_lower)."""
    if not strikes:
        return spot, spot * 0.97, spot * 1.03, spot
    ss = sorted(strikes)
    n = len(ss)
    if n == 1:
        k = ss[0]
        if abs(k - spot) / max(spot, 1e-9) < 0.01:
            return k, k, k, k
        if k > spot:
            return spot, spot, k, k
        return k, k, spot, spot
    if n == 2:
        return ss[0], ss[0], ss[1], ss[1]
    if n == 4:
        return ss[1], ss[1], ss[2], ss[2]
    if n == 3:
        return ss[0], ss[0], ss[2], ss[2]
    return ss[1], ss[1], ss[-2], ss[-2]


# ── Anchor selection ────────────────────────────────────────────────────


def _pick_anchor(
    kind: str, zones: tuple, spot: float,
    strikes: list[float], grid: np.ndarray, pnl: np.ndarray,
) -> float:
    bear_up, _, _, bull_lo = zones
    ss = sorted(strikes) if strikes else []

    if kind == "bearish":
        fp, _ = _find_flat_region(grid, pnl, "left")
        if fp is not None and fp > 0:
            return fp
        tgt = spot * 0.85
        if ss:
            sw = (ss[-1] - ss[0]) if len(ss) > 1 else spot * 0.1
            alt = ss[0] - sw
            if alt > 0:
                tgt = max(alt, tgt)
        return max(tgt, float(grid[1]))

    if kind == "bullish":
        fp, _ = _find_flat_region(grid, pnl, "right")
        if fp is not None:
            return fp
        tgt = spot * 1.15
        if ss:
            sw = (ss[-1] - ss[0]) if len(ss) > 1 else spot * 0.1
            alt = ss[-1] + sw
            tgt = min(alt, tgt)
        return min(tgt, float(grid[-2]))

    return spot  # stagnant


# ── Leg helpers ─────────────────────────────────────────────────────────


def _leg_flags(legs: list[dict]) -> dict:
    lc = [l for l in legs if l.get("kind", "").upper() == "CALL"
          and l.get("side", "").lower() == "long"]
    sc = [l for l in legs if l.get("kind", "").upper() == "CALL"
          and l.get("side", "").lower() == "short"]
    lp = [l for l in legs if l.get("kind", "").upper() == "PUT"
          and l.get("side", "").lower() == "long"]
    sp = [l for l in legs if l.get("kind", "").upper() == "PUT"
          and l.get("side", "").lower() == "short"]
    return dict(long_calls=lc, short_calls=sc, long_puts=lp, short_puts=sp)


# ── Sentence builders ──────────────────────────────────────────────────


def _mechanics(ctx: dict) -> str:
    """Sentence 1: what mechanically happens in this zone."""
    kind = ctx["kind"]
    is_flat = ctx["is_flat"]
    flat_pnl = ctx["flat_pnl"]
    flat_edge = ctx["flat_edge"]
    slope = ctx["slope"]
    has_stock = ctx["has_stock"]
    opt_at = ctx["opt_at_anchor"]
    lf = ctx["leg_flags"]
    bear_up = ctx["zones"][0]
    bull_lo = ctx["zones"][3]

    if kind == "bearish":
        boundary = _fmt_price(bear_up)
        if is_flat:
            edge = _fmt_price(flat_edge) if flat_edge is not None else boundary
            pnl_txt = _fmt_pnl(flat_pnl)
            if flat_pnl is not None and flat_pnl >= 0:
                return f"At any price below {edge}, gains are locked in at {pnl_txt}."
            if lf["long_puts"]:
                return f"At any price below {edge}, the put limits losses to {pnl_txt}."
            return f"At any price below {edge}, losses are capped at {pnl_txt}."
        if abs(slope) > 0.9:
            base = f"Below {boundary}, the position declines with the stock."
            if has_stock and opt_at is not None and opt_at > 0:
                return (
                    f"Below {boundary}, the position declines with the stock, "
                    f"but the {_fmt_pnl(opt_at, bold=False)} from the options "
                    f"cushions the move."
                )
            return base
        if abs(slope) > 0.01:
            return f"Below {boundary}, the position loses value as the stock falls."
        return f"Below {boundary}, results are largely unchanged."

    if kind == "bullish":
        boundary = _fmt_price(bull_lo)
        if is_flat:
            edge = _fmt_price(flat_edge) if flat_edge is not None else boundary
            pnl_txt = _fmt_pnl(flat_pnl)
            if flat_pnl is not None and flat_pnl <= 0:
                return f"At any price above {edge}, losses are capped at {pnl_txt}."
            if lf["short_calls"] and has_stock:
                return (
                    f"At any price above {edge}, gains are capped at {pnl_txt} "
                    f"\u2014 the short call limits further upside."
                )
            return f"At any price above {edge}, gains are capped at {pnl_txt}."
        if abs(slope) > 0.9:
            return f"Above {boundary}, the position rises with the stock."
        if abs(slope) > 0.01:
            if has_stock:
                return f"Above {boundary}, gains increase as the stock rises."
            return f"Above {boundary}, the position gains value as the stock rises."
        return f"Above {boundary}, results are largely unchanged."

    # stagnant
    stag_lo, stag_hi = ctx["zones"][1], ctx["zones"][2]
    if abs(stag_lo - stag_hi) < 0.01:
        zone_desc = f"Near {_fmt_price(stag_lo)}"
    else:
        zone_desc = f"Between {_fmt_price(stag_lo)} and {_fmt_price(stag_hi)}"

    if is_flat:
        pnl_txt = _fmt_pnl(flat_pnl)
        if flat_pnl is not None and flat_pnl >= 0:
            return f"{zone_desc}, the position captures its maximum gain of {pnl_txt}."
        return f"{zone_desc}, losses are stable at {pnl_txt}."

    if has_stock:
        return f"{zone_desc}, results track the stock with the options overlay in place."
    return f"{zone_desc}, results shift as the stock moves within this range."


def _numbers(ctx: dict) -> Optional[str]:
    """Sentence 2: P&L at anchor price.  Skipped when flat (merged)."""
    if ctx["is_flat"]:
        return None
    anchor = ctx["anchor"]
    cmb = ctx["cmb_at_anchor"]
    has_stock = ctx["has_stock"]
    opt_at = ctx["opt_at_anchor"]
    stk_at = ctx["stk_at_anchor"]

    if has_stock:
        parts = [f"At {_fmt_price(anchor)}, the combined position is {_fmt_pnl(cmb)}"]
        details = []
        if stk_at is not None:
            word = "gain" if stk_at >= 0 else "lose"
            details.append(f"the shares {word} {_fmt_pnl(stk_at, bold=False)}")
        if opt_at is not None:
            word = "add" if opt_at >= 0 else "cost"
            details.append(f"the options {word} {_fmt_pnl(opt_at, bold=False)}")
        if details:
            parts.append(" \u2014 " + " and ".join(details))
        return "".join(parts) + "."

    return f"At {_fmt_price(anchor)}, the position is {_fmt_pnl(cmb)}."


def _floor_ceiling(ctx: dict) -> Optional[str]:
    """Sentence 3: breakeven, max profit, max loss."""
    kind = ctx["kind"]
    is_flat = ctx["is_flat"]
    spot = ctx["spot"]
    breakevens = ctx["zone_breakevens"]
    mp_str = ctx["mp_str"]
    ml_str = ctx["ml_str"]
    mp_unlimited = ctx["mp_unlimited"]
    ml_unlimited = ctx["ml_unlimited"]
    mp_val = ctx["mp_val"]
    ml_val = ctx["ml_val"]

    parts: list[str] = []

    # Breakeven
    for be in breakevens:
        dist = (be - spot) / spot * 100 if spot else 0
        direction = "above" if dist >= 0 else "below"
        parts.append(
            f"Breakeven is {_fmt_price(be)} "
            f"({_fmt_pct(abs(dist))} {direction} current price)."
        )

    # Max profit / max loss depending on zone
    if kind == "bullish":
        if mp_unlimited:
            parts.append("There is no cap on upside gains.")
        elif mp_val is not None and not is_flat:
            parts.append(f"Maximum gain is {_fmt_pnl(mp_val)}.")
    if kind == "bearish":
        if ml_unlimited:
            parts.append("There is no cap on downside risk.")
        elif ml_val is not None and not is_flat:
            parts.append(f"Maximum loss is {_fmt_pnl(ml_val)}.")
    if kind == "stagnant":
        if mp_val is not None and not is_flat:
            parts.append(f"Maximum gain is {_fmt_pnl(mp_val)}.")

    return " ".join(parts) if parts else None


def _tradeoff(ctx: dict) -> Optional[str]:
    """Sentence 4: comparison vs naked stock (only when meaningful)."""
    kind = ctx["kind"]
    has_stock = ctx["has_stock"]
    if not has_stock:
        return None

    avg_cost = ctx["avg_cost"]
    shares = ctx["shares"]
    anchor = ctx["anchor"]
    cmb = ctx["cmb_at_anchor"]
    is_flat = ctx["is_flat"]
    flat_pnl = ctx["flat_pnl"]
    lf = ctx["leg_flags"]
    net_prem = ctx["net_prem"]

    if avg_cost is None or shares == 0:
        return None

    naked = shares * (anchor - avg_cost)
    overlay_impact = cmb - naked

    if kind == "bearish":
        # Flat positive = bought below put floor
        effective = flat_pnl if is_flat else cmb
        if effective is not None and effective >= 0 and is_flat:
            return (
                "The client bought the stock below the protection floor, "
                "so even in a severe decline, the position is profitable."
            )
        if overlay_impact > 1.0:
            return (
                f"Without the options, the loss would be "
                f"{_fmt_pnl(naked, bold=False)}."
            )

    if kind == "bullish" and is_flat and overlay_impact < -1.0:
        premium_abs = abs(net_prem)
        if lf["short_calls"] and lf["long_puts"]:
            what = f"protection below the put strike"
        elif lf["short_calls"]:
            what = f"{_fmt_price(premium_abs)} in collected premium"
        elif lf["long_puts"]:
            what = "downside protection"
        else:
            what = "the options overlay"
        cap_strike = None
        for l in lf["short_calls"]:
            s = l.get("strike")
            if s is not None:
                cap_strike = float(s)
                break
        above_txt = f" above {_fmt_price(cap_strike)}" if cap_strike else ""
        return f"The trade-off: {what} in exchange for giving up gains{above_txt}."

    return None


# ── Scenario builder ────────────────────────────────────────────────────


def _zone_breakevens(
    breakevens: list[float], kind: str, zones: tuple,
) -> list[float]:
    bear_up, stag_lo, stag_hi, bull_lo = zones
    out = []
    for be in breakevens:
        if kind == "bearish" and be <= bear_up:
            out.append(be)
        elif kind == "stagnant" and stag_lo <= be <= stag_hi:
            out.append(be)
        elif kind == "bullish" and be >= bull_lo:
            out.append(be)
    return out


def _build_scenario(kind: str, zones: tuple, d: dict) -> dict:
    """Build one scenario dict (bearish / stagnant / bullish)."""
    bear_up, stag_lo, stag_hi, bull_lo = zones
    grid = d["grid"]
    cmb_pnl = d["cmb_pnl"]
    spot = d["spot"]

    anchor = _pick_anchor(kind, zones, spot, d["strikes"], grid, cmb_pnl)
    cmb_at = float(np.interp(anchor, grid, cmb_pnl))
    opt_at = float(np.interp(anchor, grid, d["opt_pnl"]))
    stk_at = float(np.interp(anchor, grid, d["stk_pnl"]))

    # Flat & slope
    if kind == "bearish":
        fp, fv = _find_flat_region(grid, cmb_pnl, "left")
        zone_lo, zone_hi = float(grid[0]) if len(grid) else 0.0, bear_up
    elif kind == "bullish":
        fp, fv = _find_flat_region(grid, cmb_pnl, "right")
        zone_lo, zone_hi = bull_lo, float(grid[-1]) if len(grid) else spot * 3
    else:
        fp, fv = None, None
        zone_lo, zone_hi = stag_lo, stag_hi

    # Also check if the zone itself is flat (e.g. condor base zone)
    zf, zfv = _zone_is_flat(grid, cmb_pnl, zone_lo, zone_hi)
    is_flat = (fp is not None) or zf
    flat_pnl = fv if fp is not None else zfv
    flat_edge = fp if fp is not None else None

    slope = _compute_slope(grid, cmb_pnl, zone_lo, zone_hi)
    lf = _leg_flags(d["legs"])
    zbe = _zone_breakevens(d["breakevens"], kind, zones)

    ctx = dict(
        kind=kind, zones=zones, anchor=anchor, spot=spot,
        cmb_at_anchor=cmb_at, opt_at_anchor=opt_at, stk_at_anchor=stk_at,
        slope=slope, is_flat=is_flat, flat_pnl=flat_pnl, flat_edge=flat_edge,
        has_stock=d["has_stock"], avg_cost=d["avg_cost"], shares=d["shares"],
        leg_flags=lf, zone_breakevens=zbe, net_prem=d["net_prem"],
        mp_str=d["mp_str"], ml_str=d["ml_str"],
        mp_unlimited=d["mp_unlimited"], ml_unlimited=d["ml_unlimited"],
        mp_val=d["mp_val"], ml_val=d["ml_val"],
    )

    sentences = [_mechanics(ctx)]
    s2 = _numbers(ctx)
    if s2:
        sentences.append(s2)
    s3 = _floor_ceiling(ctx)
    if s3:
        sentences.append(s3)
    s4 = _tradeoff(ctx)
    if s4:
        sentences.append(s4)

    body = " ".join(sentences)

    # Condition string
    ticker = d["ticker"]
    if kind == "bearish":
        condition = f"If {ticker} falls below {_fmt_price(bear_up)}"
    elif kind == "bullish":
        condition = f"If {ticker} rises above {_fmt_price(bull_lo)}"
    else:
        if abs(stag_lo - stag_hi) < 0.01:
            condition = f"If {ticker} stays near {_fmt_price(stag_lo)}"
        else:
            condition = (
                f"If {ticker} stays between "
                f"{_fmt_price(stag_lo)} and {_fmt_price(stag_hi)}"
            )

    return {"kind": kind, "condition": condition, "body": body}


# ── Commentary blocks ───────────────────────────────────────────────────


def _block_at_price(
    label: str, price: float, d: dict,
) -> dict:
    grid = d["grid"]
    cmb_pnl = d["cmb_pnl"]
    if len(grid) == 0:
        return {"level": label, "text": "--"}
    pnl = float(np.interp(price, grid, cmb_pnl))
    if abs(pnl) < 0.01:
        desc = "the position is near breakeven"
    elif pnl > 0:
        desc = f"the position gains {_fmt_pnl(pnl, bold=False)}"
    else:
        desc = f"the position loses {_fmt_pnl(pnl, bold=False)}"
    return {"level": label, "text": f"At {_fmt_price(price)}, {desc}."}


def _build_commentary_blocks(d: dict) -> list[dict]:
    blocks = []
    spot = d["spot"]
    strikes = d["strikes"]
    breakevens = d["breakevens"]
    grid = d["grid"]
    cmb_pnl = d["cmb_pnl"]

    # Spot
    blocks.append(_block_at_price("Spot", spot, d))

    # Strikes
    strike_texts = []
    for s in strikes:
        pnl = float(np.interp(s, grid, cmb_pnl)) if len(grid) else 0
        strike_texts.append(
            f"At strike {_fmt_price(s)}, P&L is {_fmt_pnl(pnl, bold=False)}."
        )
    blocks.append({
        "level": "Strikes",
        "text": " ".join(strike_texts) if strike_texts else "--",
    })

    # Breakevens
    be_texts = []
    for be in breakevens:
        dist = (be - spot) / spot * 100 if spot else 0
        direction = "above" if dist >= 0 else "below"
        be_texts.append(
            f"Breakeven at {_fmt_price(be)} "
            f"({_fmt_pct(abs(dist))} {direction} spot)."
        )
    blocks.append({
        "level": "Breakevens",
        "text": " ".join(be_texts) if be_texts else "--",
    })

    # Low
    if len(grid) > 1:
        low_price = float(grid[1])  # skip exact 0
        low_pnl = float(np.interp(low_price, grid, cmb_pnl))
        fp, fv = _find_flat_region(grid, cmb_pnl, "left")
        if fp is not None:
            blocks.append({
                "level": "Low",
                "text": (
                    f"Below {_fmt_price(fp)}, losses are capped at "
                    f"{_fmt_pnl(fv, bold=False)}."
                ),
            })
        else:
            blocks.append({
                "level": "Low",
                "text": (
                    f"As the stock falls toward zero, P&L reaches "
                    f"{_fmt_pnl(low_pnl, bold=False)}."
                ),
            })
    else:
        blocks.append({"level": "Low", "text": "--"})

    # High
    if len(grid) > 1:
        high_price = float(grid[-2])
        high_pnl = float(np.interp(high_price, grid, cmb_pnl))
        fp, fv = _find_flat_region(grid, cmb_pnl, "right")
        if fp is not None:
            blocks.append({
                "level": "High",
                "text": (
                    f"Above {_fmt_price(fp)}, gains are capped at "
                    f"{_fmt_pnl(fv, bold=False)}."
                ),
            })
        else:
            blocks.append({
                "level": "High",
                "text": (
                    f"As the stock rises, P&L reaches "
                    f"{_fmt_pnl(high_pnl, bold=False)} at "
                    f"{_fmt_price(high_price)}."
                ),
            })
    else:
        blocks.append({"level": "High", "text": "--"})

    return blocks


# ── Main entry point ────────────────────────────────────────────────────


def build_commentary_v2(pack: dict) -> dict:
    """Build payoff-driven commentary from an analysis pack.

    Returns dict with ``narrative_scenarios`` (list of 3 dicts) and
    ``commentary_blocks`` (list of dicts, same structure as v1).
    """
    d = _extract(pack)
    zones = _determine_zones(d["strikes"], d["spot"])

    scenarios = [
        _build_scenario(kind, zones, d)
        for kind in ("bearish", "stagnant", "bullish")
    ]
    blocks = _build_commentary_blocks(d)

    return {
        "narrative_scenarios": scenarios,
        "commentary_blocks": blocks,
    }
