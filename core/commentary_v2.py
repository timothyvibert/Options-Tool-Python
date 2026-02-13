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
    # Issue 5: suppress sign on near-zero values
    if abs(v) < 0.005:
        s = "$0.00"
    elif v >= 0:
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

    # Issue 6: parse Capital Basis
    cap_basis_str = _parse_metric(rows, "Capital Basis", prefer)
    cap_basis = _parse_dollar(cap_basis_str) if cap_basis_str else None

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
        cap_basis=cap_basis,
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


def _zone_extremum(
    grid: np.ndarray, pnl: np.ndarray, lo: float, hi: float,
) -> tuple[Optional[float], Optional[float], str]:
    """Find a peak or valley inside a zone.

    Returns (price, pnl_value, 'max'|'min') or (None, None, '').
    Only triggers when the extremum is significantly different from boundaries.
    """
    mask = (grid >= lo) & (grid <= hi)
    zg, zp = grid[mask], pnl[mask]
    if len(zp) < 5:
        return None, None, ""
    max_idx = int(np.argmax(zp))
    min_idx = int(np.argmin(zp))
    max_val = float(zp[max_idx])
    min_val = float(zp[min_idx])
    boundary_max = max(float(zp[0]), float(zp[-1]))
    boundary_min = min(float(zp[0]), float(zp[-1]))
    peak_above = max_val - boundary_max
    valley_below = boundary_min - min_val
    if peak_above > 10.0 and peak_above > valley_below:
        return float(zg[max_idx]), max_val, "max"
    if valley_below > 10.0:
        return float(zg[min_idx]), min_val, "min"
    return None, None, ""


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


def _best_leg_strike(legs: list[dict]) -> Optional[float]:
    """Return the strike of the first leg, or None."""
    for l in legs:
        s = l.get("strike")
        if s is not None:
            return float(s)
    return None


def _leg_strike_near(legs: list[dict], near: float) -> Optional[float]:
    """Return the strike closest to *near* from the given legs."""
    best = None
    best_dist = float("inf")
    for l in legs:
        s = l.get("strike")
        if s is not None:
            d = abs(float(s) - near)
            if d < best_dist:
                best = float(s)
                best_dist = d
    return best


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
    net_prem = ctx["net_prem"]
    ticker = ctx["ticker"]
    spot = ctx["spot"]

    if kind == "bearish":
        boundary = _fmt_price(bear_up)

        if is_flat:
            edge = _fmt_price(flat_edge) if flat_edge is not None else boundary
            pnl_txt = _fmt_pnl(flat_pnl)

            # Issue 4: condor/butterfly — flat edge differs from zone boundary
            cap_price = flat_edge if flat_edge is not None else bear_up
            if flat_edge is not None and abs(cap_price - bear_up) > 1.0:
                parts = [f"Below {boundary}"]
                sp = _leg_strike_near(lf["short_puts"], near=bear_up)
                lp = _leg_strike_near(lf["long_puts"], near=cap_price)
                if sp:
                    parts.append(
                        f", the short {_fmt_price(sp)} put drives losses"
                    )
                if lp:
                    parts.append(
                        f", but the long {_fmt_price(lp)} put provides"
                        " a hard floor"
                    )
                parts.append(
                    f". Maximum loss is {pnl_txt} at any price below {edge}."
                )
                return "".join(parts)

            # Simple flat region
            if flat_pnl is not None and flat_pnl >= 0:
                subj = (
                    "the client's gains are"
                    if has_stock
                    else "gains are"
                )
                return f"At any price below {edge}, {subj} locked in at {pnl_txt}."

            # Floor from long put — reference the leg
            lp_strike = _best_leg_strike(lf["long_puts"])
            floor_ref = (
                f" \u2014 the long {_fmt_price(lp_strike)} put provides"
                " a hard floor"
                if lp_strike
                else ""
            )
            subj = (
                "the client's losses are"
                if has_stock
                else "losses are"
            )
            return (
                f"At any price below {edge},"
                f" {subj} capped at {pnl_txt}{floor_ref}."
            )

        # Not flat — Issue 10: check slope direction
        if slope > 0.9:
            # P&L worsens as stock falls — normal long exposure
            if has_stock:
                if opt_at is not None and opt_at > 0:
                    return (
                        f"Below {boundary}, the client still has full downside"
                        f" exposure, but the"
                        f" {_fmt_pnl(opt_at, bold=False)} from the options"
                        " cushions the move."
                    )
                return (
                    f"Below {boundary}, the client still has full downside"
                    " exposure."
                )
            return f"Below {boundary}, the position declines with the stock."

        if slope < -0.9:
            # P&L improves as stock falls — inverse / short exposure
            if has_stock:
                return (
                    f"Below {boundary}, the client's position gains value"
                    " as the stock falls."
                )
            return (
                f"Below {boundary}, the position gains value"
                " as the stock falls."
            )

        if abs(slope) > 0.01:
            if slope > 0:
                subj = (
                    "the client's position loses"
                    if has_stock
                    else "the position loses"
                )
                return (
                    f"Below {boundary}, {subj} value"
                    " as the stock falls."
                )
            subj = (
                "the client's position gains"
                if has_stock
                else "the position gains"
            )
            return (
                f"Below {boundary}, {subj} value"
                " as the stock falls."
            )

        subj = (
            "the client's position is"
            if has_stock
            else "results are"
        )
        return f"Below {boundary}, {subj} largely unchanged."

    if kind == "bullish":
        boundary = _fmt_price(bull_lo)

        if is_flat:
            edge = _fmt_price(flat_edge) if flat_edge is not None else boundary
            pnl_txt = _fmt_pnl(flat_pnl)

            # Issue 4: condor/butterfly transition
            cap_price = flat_edge if flat_edge is not None else bull_lo
            if flat_edge is not None and abs(cap_price - bull_lo) > 1.0:
                parts = [f"Above {boundary}"]
                sc = _leg_strike_near(lf["short_calls"], near=bull_lo)
                lc = _leg_strike_near(lf["long_calls"], near=cap_price)
                if sc:
                    parts.append(
                        f", the short {_fmt_price(sc)} call drives losses"
                    )
                if lc:
                    parts.append(
                        f", but the long {_fmt_price(lc)} call caps"
                        " the damage"
                    )
                parts.append(
                    f". Maximum loss is {pnl_txt}"
                    f" at any price above {edge}."
                )
                return "".join(parts)

            if flat_pnl is not None and flat_pnl <= 0:
                subj = (
                    "the client's losses are"
                    if has_stock
                    else "losses are"
                )
                return f"At any price above {edge}, {subj} capped at {pnl_txt}."

            # Capped gains — reference short call
            sc_strike = _best_leg_strike(lf["short_calls"])
            cap_ref = (
                " \u2014 the short call limits further upside"
                if sc_strike and has_stock
                else ""
            )
            subj = (
                "the client's gains are"
                if has_stock
                else "gains are"
            )
            return (
                f"At any price above {edge}, {subj} capped"
                f" at {pnl_txt}{cap_ref}."
            )

        # Not flat — Issue 10: directional language
        if slope > 0.9:
            subj = (
                "the client's position rises"
                if has_stock
                else "the position rises"
            )
            return f"Above {boundary}, {subj} with the stock."

        if slope < -0.9:
            if has_stock:
                return (
                    f"Above {boundary}, the client's losses increase"
                    " as the stock rises."
                )
            return (
                f"Above {boundary}, losses increase as the stock rises."
            )

        if abs(slope) > 0.01:
            if slope > 0:
                subj = (
                    "the client's gains increase"
                    if has_stock
                    else "the position gains value"
                )
            else:
                subj = (
                    "the client's position loses value"
                    if has_stock
                    else "the position loses value"
                )
            return f"Above {boundary}, {subj} as the stock rises."

        subj = (
            "the client's position is"
            if has_stock
            else "results are"
        )
        return f"Above {boundary}, {subj} largely unchanged."

    # ── Stagnant ──
    stag_lo, stag_hi = ctx["zones"][1], ctx["zones"][2]
    if abs(stag_lo - stag_hi) < 0.01:
        zone_desc = f"Near {_fmt_price(stag_lo)}"
    else:
        zone_desc = f"Between {_fmt_price(stag_lo)} and {_fmt_price(stag_hi)}"

    if is_flat:
        pnl_txt = _fmt_pnl(flat_pnl)
        # Issue 11: credit strategy target framing
        if (
            flat_pnl is not None
            and flat_pnl >= 0
            and net_prem < -1.0
            and abs(stag_lo - stag_hi) > 0.01
        ):
            prem_abs = _fmt_price(abs(net_prem))
            lo_pct = _fmt_pct(abs((stag_lo - spot) / spot * 100))
            hi_pct = _fmt_pct(abs((stag_hi - spot) / spot * 100))
            lo_dir = "down" if stag_lo < spot else "up"
            hi_dir = "up" if stag_hi > spot else "down"
            return (
                f"This is the target outcome. As long as {ticker} stays"
                f" between {_fmt_price(stag_lo)} and {_fmt_price(stag_hi)}"
                f" \u2014 roughly {lo_pct} {lo_dir} to {hi_pct} {hi_dir}"
                f" from here \u2014 all options expire worthless and the full"
                f" {prem_abs} credit is retained."
            )
        if flat_pnl is not None and flat_pnl >= 0:
            return (
                f"{zone_desc}, the position captures its maximum gain"
                f" of {pnl_txt}."
            )
        return f"{zone_desc}, losses are stable at {pnl_txt}."

    # Not flat — Issue 2: replace filler with context-dependent sentences
    if has_stock:
        if net_prem < -1.0:
            prem_abs = _fmt_price(abs(net_prem))
            credit_value = abs(net_prem)
            opts_at = ctx["opt_at_anchor"]
            if (
                opts_at is not None
                and abs(opts_at - credit_value)
                < max(credit_value * 0.2, 5.0)
            ):
                return (
                    "This is the ideal range \u2014 the options expire"
                    " worthless and the client keeps the full"
                    f" {prem_abs} in premium on top of share movement."
                )
            return (
                f"{zone_desc}, the client's position moves with the stock,"
                f" enhanced by the {prem_abs} net credit received."
            )
        if net_prem > 1.0:
            cost = _fmt_price(net_prem)
            return (
                f"{zone_desc}, the client's position moves with the stock,"
                f" reduced by the {cost} option cost."
            )
        # Near-zero premium
        if lf["short_calls"] and lf["long_puts"]:
            return (
                f"{zone_desc}, the client's position moves with the stock"
                " \u2014 the collar has no net cost in this range."
            )
        return (
            f"{zone_desc}, the client's position moves with the stock."
        )

    # Options-only, not flat
    grid = ctx["grid"]
    cmb_pnl = ctx["cmb_pnl"]
    ext_price, ext_pnl, ext_type = _zone_extremum(
        grid, cmb_pnl, stag_lo, stag_hi,
    )
    if ext_type == "max":
        return (
            f"{zone_desc}, the position reaches its maximum gain of"
            f" {_fmt_pnl(ext_pnl)} at {_fmt_price(ext_price)} and"
            " deteriorates toward the zone boundaries."
        )
    if ext_type == "min":
        return (
            f"{zone_desc}, the position reaches its maximum loss of"
            f" {_fmt_pnl(ext_pnl)} at {_fmt_price(ext_price)} and"
            " improves toward the zone boundaries."
        )
    if slope > 0.01:
        return (
            f"{zone_desc}, the position gains value"
            " as the stock moves higher."
        )
    if slope < -0.01:
        return (
            f"{zone_desc}, the position gains value"
            " as the stock moves lower."
        )
    return f"{zone_desc}, the position is roughly flat."


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
        # Issue 1: "the client's" when with stock
        parts = [
            f"At {_fmt_price(anchor)}, the client's combined position"
            f" is {_fmt_pnl(cmb)}"
        ]
        details = []
        if stk_at is not None:
            word = "gain" if stk_at >= 0 else "lose"
            details.append(
                f"the shares {word} {_fmt_pnl(stk_at, bold=False)}"
            )
        if opt_at is not None:
            word = "add" if opt_at >= 0 else "cost"
            details.append(
                f"the options {word} {_fmt_pnl(opt_at, bold=False)}"
            )
        if details:
            parts.append(" \u2014 " + " and ".join(details))
        return "".join(parts) + "."

    return f"At {_fmt_price(anchor)}, the position is {_fmt_pnl(cmb)}."


def _floor_ceiling(ctx: dict) -> Optional[str]:
    """Sentence 3: breakeven, max profit, max loss."""
    kind = ctx["kind"]
    is_flat = ctx["is_flat"]
    flat_pnl = ctx["flat_pnl"]
    spot = ctx["spot"]
    breakevens = ctx["zone_breakevens"]
    mp_unlimited = ctx["mp_unlimited"]
    ml_unlimited = ctx["ml_unlimited"]
    mp_val = ctx["mp_val"]
    ml_val = ctx["ml_val"]

    parts: list[str] = []

    # Issue 9: combine breakevens into one sentence
    if len(breakevens) == 1:
        be = breakevens[0]
        dist = (be - spot) / spot * 100 if spot else 0
        direction = "above" if dist >= 0 else "below"
        parts.append(
            f"Breakeven is {_fmt_price(be)}"
            f" ({_fmt_pct(abs(dist))} {direction} spot)."
        )
    elif len(breakevens) >= 2:
        be_strs = []
        for be in breakevens:
            dist = (be - spot) / spot * 100 if spot else 0
            direction = "above" if dist >= 0 else "below"
            be_strs.append(
                f"{_fmt_price(be)} ({_fmt_pct(abs(dist))}"
                f" {direction} spot)"
            )
        parts.append(f"Breakevens are {' and '.join(be_strs)}.")

    # Issue 3: check flat region before claiming "no cap"
    if kind == "bullish":
        if mp_unlimited and not is_flat:
            parts.append("There is no cap on upside gains.")
        elif mp_val is not None and not is_flat:
            parts.append(f"Maximum gain is {_fmt_pnl(mp_val)}.")
    if kind == "bearish":
        if ml_unlimited and not is_flat:
            parts.append("There is no cap on downside risk.")
        elif ml_val is not None and not is_flat:
            parts.append(f"Maximum loss is {_fmt_pnl(ml_val)}.")
    if kind == "stagnant":
        if mp_val is not None and not is_flat:
            parts.append(f"Maximum gain is {_fmt_pnl(mp_val)}.")

    return " ".join(parts) if parts else None


def _tradeoff(ctx: dict) -> Optional[str]:
    """Sentence 4: trade-off / comparison vs naked stock."""
    kind = ctx["kind"]
    has_stock = ctx["has_stock"]
    lf = ctx["leg_flags"]
    net_prem = ctx["net_prem"]
    spot = ctx["spot"]

    # ── Options-only: leverage comparison (Issue 8) ──
    if not has_stock:
        if kind in ("bullish", "bearish") and net_prem > 0:
            # Only for pure long strategies (no short legs)
            has_short = lf["short_calls"] or lf["short_puts"]
            long_legs = lf["long_calls"] + lf["long_puts"]
            if long_legs and not has_short:
                total_contracts = sum(
                    abs(l.get("position", 0)) for l in long_legs
                )
                mult = long_legs[0].get("multiplier", 100)
                shares_controlled = int(total_contracts * mult)
                if shares_controlled > 0:
                    shares_cost = shares_controlled * spot
                    prem_fmt = _fmt_price(abs(net_prem))
                    cost_fmt = _fmt_price(shares_cost)
                    direction = (
                        "upside" if kind == "bullish" else "downside"
                    )
                    return (
                        f"The capital outlay is {prem_fmt} vs."
                        f" {cost_fmt} to buy {shares_controlled} shares"
                        f" \u2014 leveraged {direction} exposure"
                        " at a fraction of the cost."
                    )
        return None

    # ── With stock ──
    avg_cost = ctx["avg_cost"]
    shares = ctx["shares"]
    anchor = ctx["anchor"]
    cmb = ctx["cmb_at_anchor"]
    is_flat = ctx["is_flat"]
    flat_pnl = ctx["flat_pnl"]
    opt_at = ctx["opt_at_anchor"]

    if avg_cost is None or shares == 0:
        return None

    naked = shares * (anchor - avg_cost)
    overlay_impact = cmb - naked
    stock_value = abs(shares * spot)
    impact_pct = (
        abs(overlay_impact) / stock_value * 100 if stock_value > 0 else 0
    )

    # ── Bearish ──
    if kind == "bearish":
        effective = flat_pnl if is_flat else cmb
        if effective is not None and effective >= 0 and is_flat:
            return (
                "The client bought the stock below the protection floor,"
                " so even in a severe decline, the position is profitable."
            )
        # Issue 7: compare vs holding stock alone
        if impact_pct > 1.0 and overlay_impact > 1.0:
            if lf["long_puts"]:
                return (
                    f"Without the put, a drop to"
                    f" {_fmt_price(anchor)} would mean a"
                    f" {_fmt_pnl(naked, bold=False)} loss"
                    " on the shares alone."
                )
            return (
                f"Without the options, the loss would be"
                f" {_fmt_pnl(naked, bold=False)}."
            )

    # ── Stagnant ──
    if kind == "stagnant":
        # Issue 7: credit enhancement
        if net_prem < -1.0 and impact_pct > 1.0 and opt_at is not None:
            enhancement_pct = (
                abs(opt_at) / stock_value * 100 if stock_value > 0 else 0
            )
            if enhancement_pct > 0.1:
                return (
                    f"The premium adds a {_fmt_pct(enhancement_pct)}"
                    " enhancement over holding the stock alone."
                )
        # Issue 8: protective put cost framing
        if net_prem > 1.0 and lf["long_puts"]:
            prem_fmt = _fmt_price(net_prem)
            pct = (
                abs(net_prem) / stock_value * 100
                if stock_value > 0
                else 0
            )
            put_strike = _best_leg_strike(lf["long_puts"])
            if put_strike:
                return (
                    f"The cost of protection: {prem_fmt}"
                    f" ({_fmt_pct(pct)} of the position)"
                    f" for a guaranteed loss limit"
                    f" at {_fmt_price(put_strike)}."
                )

    # ── Bullish ──
    if kind == "bullish" and is_flat and lf["short_calls"]:
        # Issue 8: collar
        if lf["short_calls"] and lf["long_puts"]:
            put_strike = _best_leg_strike(lf["long_puts"])
            call_strike = _best_leg_strike(lf["short_calls"])
            put_ref = (
                _fmt_price(put_strike) if put_strike else "the put strike"
            )
            call_ref = (
                _fmt_price(call_strike) if call_strike else "the call strike"
            )
            return (
                f"The trade-off: downside protection below {put_ref}"
                f" in exchange for capping gains above {call_ref}."
            )
        # Issue 8: covered call
        if lf["short_calls"]:
            premium_abs = _fmt_price(abs(net_prem))
            cap_strike = _best_leg_strike(lf["short_calls"])
            above_txt = (
                f" above {_fmt_price(cap_strike)}" if cap_strike else ""
            )
            return (
                f"The trade-off: {premium_abs} in collected premium"
                f" in exchange for giving up gains{above_txt}."
            )

    return None


def _return_context(ctx: dict) -> Optional[str]:
    """Issue 6: return-on-capital sentence when cap basis is known."""
    kind = ctx["kind"]
    if kind not in ("stagnant", "bullish"):
        return None
    mp_val = ctx["mp_val"]
    cap_basis = ctx.get("cap_basis")
    if mp_val is None or mp_val <= 0:
        return None
    if cap_basis is None or cap_basis <= 0:
        return None
    return_pct = mp_val / cap_basis * 100
    return (
        f"That represents a {_fmt_pct(return_pct)} return"
        f" on the {_fmt_price(cap_basis)} capital at risk."
    )


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
        ticker=d["ticker"],
        zone_lo=zone_lo, zone_hi=zone_hi,
        cap_basis=d.get("cap_basis"),
        grid=grid, cmb_pnl=cmb_pnl,
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
    s5 = _return_context(ctx)
    if s5:
        sentences.append(s5)

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
