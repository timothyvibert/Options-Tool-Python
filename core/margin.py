"""
Margin calculator -- full CBOE + House engines.

Ported from mod_Margin (v2.0) in the Excel VBA workbook.
Supports all MarginMap_CBOE strategy codes.
Both CBOE and House modes computed simultaneously.

Backward-compatible: classify_strategy() and compute_margin_proxy()
retain their original signatures.
"""
from __future__ import annotations

import math
from typing import List

from core.margin_map import lookup_requirement_text
from core.models import OptionLeg, StrategyInput
from core.payoff import _compute_pnl_for_price, compute_payoff


# ===================================================================
# Strategy code constants
# ===================================================================
LNG_LE_9M = "LNG_LE_9M"
LNG_GT_9M = "LNG_GT_9M"
LNG_GT_9M_LISTED = "LNG_GT_9M_LISTED"
LNG_GT_9M_OTC = "LNG_GT_9M_OTC"
SH_OPT = "SH_OPT"
SH_OPT_BROAD = "SH_OPT_BROAD"
SH_OPT_LEV = "SH_OPT_LEV"
SH_OPT_BROAD_LEV = "SH_OPT_BROAD_LEV"
SH_PUT_CALL = "SH_PUT_CALL"
SH_PUT_CALL_FLEX = "SH_PUT_CALL_FLEX"
SH_PUT_CALL_FLEX_IDX = "SH_PUT_CALL_FLEX_IDX"
SPR = "SPR"
SPR_FLEX = "SPR_FLEX"
SPR_FLEX_IDX = "SPR_FLEX_IDX"
BOX_LONG = "BOX_LONG"
BOX_SHORT = "BOX_SHORT"
CCOV = "CCOV"
PPRT = "PPRT"
COL_EQ = "COL_EQ"
CONV = "CONV"
REVCONV = "REVCONV"
SH_PUT_SH_UND = "SH_PUT_SH_UND"
LNG_CALL_SH_UND = "LNG_CALL_SH_UND"
SH_CALL_CONV = "SH_CALL_CONV"
SH_CALL_WAR = "SH_CALL_WAR"
SH_IDX_CALL_LNG_ETF = "SH_IDX_CALL_LNG_ETF"
MPL_COMP = "MPL_COMP"
CASH_EQUIV = "CASH_EQUIV"
ESCROW = "ESCROW"
GENERAL = "GENERAL"

# Groups for routing in the CBOE engine
_LONG_CODES = {LNG_LE_9M, LNG_GT_9M, LNG_GT_9M_LISTED, LNG_GT_9M_OTC}
_SHORT_CODES = {SH_OPT, SH_OPT_BROAD, SH_OPT_LEV, SH_OPT_BROAD_LEV}
_STRADDLE_CODES = {SH_PUT_CALL, SH_PUT_CALL_FLEX, SH_PUT_CALL_FLEX_IDX}
_SPREAD_CODES = {SPR, SPR_FLEX, SPR_FLEX_IDX, BOX_LONG, BOX_SHORT}


# ===================================================================
# 1. BASE CLASSIFICATION  (backward-compatible, 7 codes)
# ===================================================================

def classify_strategy(input: StrategyInput) -> str:
    """Base classification into 7 core codes.  Signature unchanged."""
    legs = [leg for leg in input.legs if leg.kind.lower() in {"call", "put"}]
    has_stock = input.stock_position != 0
    all_long = bool(legs) and all(leg.position > 0 for leg in legs)
    all_short = bool(legs) and all(leg.position < 0 for leg in legs)

    short_calls = [leg for leg in legs if leg.kind.lower() == "call" and leg.position < 0]
    long_calls = [leg for leg in legs if leg.kind.lower() == "call" and leg.position > 0]
    short_puts = [leg for leg in legs if leg.kind.lower() == "put" and leg.position < 0]
    long_puts = [leg for leg in legs if leg.kind.lower() == "put" and leg.position > 0]

    if has_stock and input.stock_position > 0:
        if short_calls and long_puts and not long_calls and not short_puts:
            return COL_EQ
        if short_calls and not long_calls and not short_puts and not long_puts:
            return CCOV
        if long_puts and not long_calls and not short_calls and not short_puts:
            return PPRT

    if not has_stock:
        if all_long:
            return LNG_LE_9M
        if all_short:
            if short_calls and short_puts:
                return SH_PUT_CALL
            return SH_OPT

    payoff = compute_payoff(input)
    bounded = not payoff.get("unlimited_upside", False) and not payoff.get(
        "unlimited_downside", False
    )
    if bounded:
        return SPR
    if all_short or any(leg.position < 0 for leg in legs):
        return SH_OPT
    return LNG_LE_9M


# ===================================================================
# 2. REFINED CLASSIFICATION  (all 30 codes)
# ===================================================================

def classify_strategy_refined(
    input: StrategyInput,
    *,
    is_index: bool = False,
    is_volatility_index: bool = False,
    index_base_type: str = "BROAD",
    leverage_factor: float = 1.0,
    listing_type: str = "LISTED",
    dte: float = 0.0,
    is_flex: bool = False,
    settlement_type: str = "PHYSICAL",
    exercise_type: str = "AMERICAN",
) -> str:
    """Refined classification into all 30 CBOE codes."""
    base = classify_strategy(input)
    legs = [leg for leg in input.legs if leg.kind.lower() in {"call", "put"}]
    has_stock = input.stock_position != 0
    stock_pos = input.stock_position

    short_calls = [l for l in legs if l.kind.lower() == "call" and l.position < 0]
    long_calls = [l for l in legs if l.kind.lower() == "call" and l.position > 0]
    short_puts = [l for l in legs if l.kind.lower() == "put" and l.position < 0]
    long_puts = [l for l in legs if l.kind.lower() == "put" and l.position > 0]

    # ── Detect CONV / REVCONV ─────────────────────────────────
    if has_stock and long_puts and short_calls and not long_calls and not short_puts:
        # Potential conversion: long stock + long put + short call at same strike
        put_strikes = {round(l.strike, 6) for l in long_puts}
        call_strikes = {round(l.strike, 6) for l in short_calls}
        common = put_strikes & call_strikes
        if common and stock_pos > 0:
            return CONV

    if has_stock and long_calls and short_puts and not short_calls and not long_puts:
        # Potential reverse conversion: short stock + long call + short put at same strike
        call_strikes = {round(l.strike, 6) for l in long_calls}
        put_strikes = {round(l.strike, 6) for l in short_puts}
        common = call_strikes & put_strikes
        if common and stock_pos < 0:
            return REVCONV

    # ── Detect SH_PUT_SH_UND / LNG_CALL_SH_UND ──────────────
    if has_stock and stock_pos < 0:
        if short_puts and not short_calls and not long_calls and not long_puts:
            return SH_PUT_SH_UND
        if long_calls and not short_calls and not short_puts and not long_puts:
            return LNG_CALL_SH_UND

    # ── Detect BOX spreads ────────────────────────────────────
    if not has_stock and len(legs) == 4:
        lc = sorted(long_calls, key=lambda l: l.strike)
        sc = sorted(short_calls, key=lambda l: l.strike)
        lp = sorted(long_puts, key=lambda l: l.strike)
        sp = sorted(short_puts, key=lambda l: l.strike)

        if len(lc) == 1 and len(sc) == 1 and len(lp) == 1 and len(sp) == 1:
            lc_k = round(lc[0].strike, 6)
            sc_k = round(sc[0].strike, 6)
            lp_k = round(lp[0].strike, 6)
            sp_k = round(sp[0].strike, 6)
            # BOX_LONG: bull call (long K1, short K2) + bear put (long K2, short K1)
            if lc_k < sc_k and lp_k == sc_k and sp_k == lc_k:
                return BOX_LONG
            # BOX_SHORT: bear call (short K1, long K2) + bull put (short K2, long K1)
            if sc_k < lc_k and sp_k == lc_k and lp_k == sc_k:
                return BOX_SHORT

    # ── Refine LNG codes based on DTE ─────────────────────────
    if base == LNG_LE_9M:
        if dte > 270:
            if listing_type.upper() == "OTC":
                return LNG_GT_9M_OTC
            if listing_type.upper() == "LISTED":
                return LNG_GT_9M_LISTED
            return LNG_GT_9M
        return LNG_LE_9M

    # ── Refine SH_OPT based on index / leverage ──────────────
    if base == SH_OPT:
        if leverage_factor > 1.0:
            if is_index and index_base_type.upper() == "BROAD":
                return SH_OPT_BROAD_LEV
            return SH_OPT_LEV
        if is_index and index_base_type.upper() == "BROAD":
            return SH_OPT_BROAD
        return SH_OPT

    # ── Refine SH_PUT_CALL for FLEX ───────────────────────────
    if base == SH_PUT_CALL:
        if is_flex:
            if is_index:
                return SH_PUT_CALL_FLEX_IDX
            return SH_PUT_CALL_FLEX
        return SH_PUT_CALL

    # ── Refine SPR for FLEX ───────────────────────────────────
    if base == SPR:
        if is_flex:
            if is_index:
                return SPR_FLEX_IDX
            return SPR_FLEX
        return SPR

    # ── CCOV / PPRT / COL_EQ pass through ─────────────────────
    return base


# ===================================================================
# 3. INTERNAL MATH HELPERS
# ===================================================================

def _option_pnl_at_price(legs: List[OptionLeg], price: float) -> float:
    """Compute option-only PnL at a given underlying price."""
    total = 0.0
    for leg in legs:
        if leg.kind.lower() == "call":
            intrinsic = max(price - leg.strike, 0.0)
        else:
            intrinsic = max(leg.strike - price, 0.0)
        total += leg.position * (intrinsic - leg.premium) * leg.multiplier
    return total


def _max_loss_requirement(legs: List[OptionLeg], spot: float) -> float:
    """Max loss from option-only PnL across critical price points."""
    if not legs:
        return 0.0
    strikes = sorted({leg.strike for leg in legs})
    high = max(spot, max(strikes) if strikes else spot) * 3.0
    test_prices = [0.0] + strikes + [spot, high]
    # Add midpoints between strikes for accuracy
    for i in range(len(strikes) - 1):
        test_prices.append((strikes[i] + strikes[i + 1]) / 2.0)
    min_pnl = min(_option_pnl_at_price(legs, p) for p in test_prices)
    return max(-min_pnl, 0.0)


def _sum_long_premium(legs: List[OptionLeg]) -> float:
    """Total premium paid for long option legs."""
    return sum(
        abs(leg.position) * leg.premium * leg.multiplier
        for leg in legs
        if leg.position > 0
    )


def _long_put_premium(legs: List[OptionLeg]) -> float:
    """Total premium paid for long put legs."""
    return sum(
        abs(leg.position) * leg.premium * leg.multiplier
        for leg in legs
        if leg.kind.lower() == "put" and leg.position > 0
    )


def _short_option_requirement(
    leg: OptionLeg,
    spot: float,
    pct: float = 0.20,
    min_pct: float = 0.10,
    leverage_factor: float = 1.0,
) -> float:
    """
    Short option margin for a single leg.

    ShortOptionsRequirement from VBA:
      premium + max(adj_pct * underlying - OTM, adj_min * underlying)

    pct/min_pct are base percentages before leverage adjustment.
    """
    qty = abs(leg.position)
    multiplier = leg.multiplier
    underlying_value = qty * spot * multiplier
    premium_component = qty * leg.premium * multiplier

    if leg.kind.lower() == "call":
        otm = max(leg.strike - spot, 0.0) * qty * multiplier
    else:
        otm = max(spot - leg.strike, 0.0) * qty * multiplier

    adj_pct = pct * leverage_factor
    adj_min = min_pct * leverage_factor

    return premium_component + max(
        adj_pct * underlying_value - otm,
        adj_min * underlying_value,
    )


def _short_straddle_requirement(
    legs: List[OptionLeg],
    spot: float,
    pct: float = 0.20,
    min_pct: float = 0.10,
    leverage_factor: float = 1.0,
) -> float:
    """
    ShortStraddleRequirement from VBA:
      max(put_total, call_total) + other_side_premium
    """
    short_calls = [l for l in legs if l.kind.lower() == "call" and l.position < 0]
    short_puts = [l for l in legs if l.kind.lower() == "put" and l.position < 0]

    call_req = sum(
        _short_option_requirement(l, spot, pct, min_pct, leverage_factor)
        for l in short_calls
    )
    put_req = sum(
        _short_option_requirement(l, spot, pct, min_pct, leverage_factor)
        for l in short_puts
    )
    call_prem = sum(abs(l.position) * l.premium * l.multiplier for l in short_calls)
    put_prem = sum(abs(l.position) * l.premium * l.multiplier for l in short_puts)

    if call_req >= put_req:
        return call_req + put_prem
    else:
        return put_req + call_prem


def _protective_put_maintenance(
    legs: List[OptionLeg], spot: float, stock_pos: float
) -> float:
    """
    ProtectivePutMaintenance from VBA:
      min(10% * putStrikeAgg + putOTM, 25% * underlyingMV)
    """
    long_puts = [l for l in legs if l.kind.lower() == "put" and l.position > 0]
    if not long_puts:
        return 0.25 * abs(stock_pos) * spot

    put_strike_agg = sum(
        abs(l.position) * l.strike * l.multiplier for l in long_puts
    )
    put_otm = sum(
        max(spot - l.strike, 0.0) * abs(l.position) * l.multiplier
        for l in long_puts
    )
    underlying_mv = abs(stock_pos) * spot

    return min(0.10 * put_strike_agg + put_otm, 0.25 * underlying_mv)


def _collar_maintenance(legs: List[OptionLeg], spot: float) -> float:
    """
    CollarMaintenance from VBA:
      min(10% * putStrikeAgg + putOTM, 25% * callStrikeAgg)
    """
    long_puts = [l for l in legs if l.kind.lower() == "put" and l.position > 0]
    short_calls = [l for l in legs if l.kind.lower() == "call" and l.position < 0]

    put_strike_agg = sum(
        abs(l.position) * l.strike * l.multiplier for l in long_puts
    )
    put_otm = sum(
        max(spot - l.strike, 0.0) * abs(l.position) * l.multiplier
        for l in long_puts
    )
    call_strike_agg = sum(
        abs(l.position) * l.strike * l.multiplier for l in short_calls
    )
    if call_strike_agg == 0:
        return 0.0

    return min(0.10 * put_strike_agg + put_otm, 0.25 * call_strike_agg)


def _stock_req_long(
    account: str, stage: str, spot: float, stock_pos: float
) -> float:
    """
    StockReq_Long from VBA: Reg-T baseline for long stock.
      Cash = 100% MV, Margin Init = 50% MV, Margin Maint = 25% MV.
    """
    mv = abs(stock_pos) * spot
    acct = account.upper()
    stg = stage.upper()

    if acct == "CASH":
        return mv  # 100%
    if stg == "INITIAL":
        return 0.50 * mv  # Reg T
    # MAINTENANCE
    return 0.25 * mv


def _stock_req_short(
    account: str, stage: str, spot: float, stock_pos: float
) -> float:
    """Short stock Reg-T: cash not allowed, init=150% MV, maint=130% MV."""
    mv = abs(stock_pos) * spot
    acct = account.upper()
    stg = stage.upper()

    if acct == "CASH":
        return float("inf")  # not allowed
    if stg == "INITIAL":
        return 1.50 * mv
    return 1.30 * mv


def _cash_escrow_for_short_options(
    legs: List[OptionLeg], spot: float
) -> float:
    """
    CashEscrowReq_ForShortOptions from VBA:
      Puts: aggregate strike value (strike * qty * mult)
      Calls: underlying MV (spot * qty * mult)
    """
    total = 0.0
    for leg in legs:
        if leg.position >= 0:
            continue
        qty = abs(leg.position)
        mult = leg.multiplier
        if leg.kind.lower() == "put":
            total += leg.strike * qty * mult
        else:  # call
            total += spot * qty * mult
    return total


# ===================================================================
# 4. CBOE NUMERIC ENGINE
# ===================================================================

def _get_short_pcts(
    code: str,
    is_index: bool = False,
    is_volatility_index: bool = False,
    index_base_type: str = "BROAD",
    leverage_factor: float = 1.0,
) -> tuple[float, float, float]:
    """Return (pct, min_pct, leverage) for short option formulas."""
    if code in {SH_OPT_BROAD, SH_OPT_BROAD_LEV}:
        return 0.15, 0.10, leverage_factor
    if code in {SH_OPT_LEV}:
        return 0.20, 0.10, leverage_factor
    if is_volatility_index:
        return 0.20, 0.10, leverage_factor
    if is_index and index_base_type.upper() == "BROAD":
        return 0.15, 0.10, leverage_factor
    return 0.20, 0.10, leverage_factor


def compute_margin_cboe(
    code: str,
    account: str,
    stage: str,
    input: StrategyInput,
    *,
    leverage_factor: float = 1.0,
    is_index: bool = False,
    is_volatility_index: bool = False,
    index_base_type: str = "BROAD",
    settlement_type: str = "PHYSICAL",
    exercise_type: str = "AMERICAN",
    listing_type: str = "LISTED",
    dte: float = 0.0,
    is_flex: bool = False,
) -> dict:
    """
    CBOE margin requirement for a single (account, stage) combination.

    Returns: {"amount": float|None, "allowed": bool, "notes": str}
    """
    acct = account.upper()
    stg = stage.upper()
    legs = [l for l in input.legs if l.kind.lower() in {"call", "put"}]
    spot = float(input.spot)
    stock_pos = float(input.stock_position)

    # ── LONG OPTIONS ──────────────────────────────────────────
    if code in _LONG_CODES:
        prem_total = _sum_long_premium(legs)
        if acct == "CASH":
            return {"amount": prem_total, "allowed": True,
                    "notes": "100% premium (fully paid)"}
        if stg == "INITIAL":
            if code == LNG_GT_9M_LISTED:
                return {"amount": 0.75 * prem_total, "allowed": True,
                        "notes": "75% premium (listed >9M)"}
            if code == LNG_GT_9M_OTC:
                return {"amount": 0.75 * prem_total, "allowed": True,
                        "notes": "75% premium (OTC >9M approx)"}
            return {"amount": prem_total, "allowed": True,
                    "notes": "100% premium"}
        # MAINTENANCE
        if code in {LNG_GT_9M_LISTED, LNG_GT_9M_OTC, LNG_GT_9M}:
            return {"amount": 0.75 * prem_total, "allowed": True,
                    "notes": "75% market value (>9M)"}
        return {"amount": 0.0, "allowed": True,
                "notes": "No margin requirement (<=9M)"}

    # ── SHORT OPTIONS ─────────────────────────────────────────
    if code in _SHORT_CODES:
        if acct == "CASH":
            escrow = _cash_escrow_for_short_options(legs, spot)
            return {"amount": escrow, "allowed": True,
                    "notes": "Cash escrow (put=strike*qty*mult, call=spot*qty*mult)"}
        pct, min_pct, lev = _get_short_pcts(
            code, is_index, is_volatility_index, index_base_type, leverage_factor,
        )
        total = 0.0
        for leg in legs:
            if leg.position < 0:
                total += _short_option_requirement(leg, spot, pct, min_pct, lev)
        return {"amount": total, "allowed": True,
                "notes": f"Premium + max({pct*100:.0f}%*UndVal-OTM, {min_pct*100:.0f}%*UndVal)"
                         + (f" [lev={lev:.1f}]" if lev > 1.0 else "")}

    # ── SHORT STRADDLE / STRANGLE ─────────────────────────────
    if code in _STRADDLE_CODES:
        if acct == "CASH":
            escrow = _cash_escrow_for_short_options(legs, spot)
            return {"amount": escrow, "allowed": True,
                    "notes": "Cash escrow for each short leg"}
        pct, min_pct, lev = _get_short_pcts(
            code, is_index, is_volatility_index, index_base_type, leverage_factor,
        )
        total = _short_straddle_requirement(legs, spot, pct, min_pct, lev)
        return {"amount": total, "allowed": True,
                "notes": "max(put_req, call_req) + other_leg_premium"}

    # ── SPREADS / BOXES ───────────────────────────────────────
    if code in _SPREAD_CODES:
        ml = _max_loss_requirement(legs, spot)
        if acct == "CASH":
            # Cash spreads: only European cash-settled
            if settlement_type.upper() == "CASH" and exercise_type.upper() == "EUROPEAN":
                return {"amount": ml, "allowed": True,
                        "notes": "Cash spread (European cash-settled): max loss"}
            if is_index and settlement_type.upper() == "CASH":
                return {"amount": ml, "allowed": True,
                        "notes": "Cash spread (cash-settled index): max loss"}
            return {"amount": None, "allowed": False,
                    "notes": "Cash spreads only for European cash-settled options"}
        return {"amount": ml, "allowed": True,
                "notes": "Max potential loss (option-only payoff)"}

    # ── COVERED CALL ──────────────────────────────────────────
    if code == CCOV:
        mv = abs(stock_pos) * spot
        if acct == "CASH":
            return {"amount": mv, "allowed": True,
                    "notes": "Underlying fully paid; short call 0 req"}
        if stg == "INITIAL":
            return {"amount": 0.50 * mv, "allowed": True,
                    "notes": "50% MV (Reg T); short call 0 req"}
        return {"amount": 0.25 * mv, "allowed": True,
                "notes": "25% MV maintenance; short call 0 req"}

    # ── PROTECTIVE PUT ────────────────────────────────────────
    if code == PPRT:
        mv = abs(stock_pos) * spot
        put_prem = _long_put_premium(legs)
        if acct == "CASH":
            return {"amount": mv + put_prem, "allowed": True,
                    "notes": "MV + long put premium (both fully paid)"}
        if stg == "INITIAL":
            return {"amount": 0.50 * mv + put_prem, "allowed": True,
                    "notes": "50% MV + put premium"}
        maint = _protective_put_maintenance(legs, spot, stock_pos)
        return {"amount": maint, "allowed": True,
                "notes": "min(10%*putStrike+putOTM, 25%*MV)"}

    # ── COLLAR ────────────────────────────────────────────────
    if code == COL_EQ:
        mv = abs(stock_pos) * spot
        put_prem = _long_put_premium(legs)
        if acct == "CASH":
            return {"amount": mv + put_prem, "allowed": True,
                    "notes": "MV + put premium; short call 0 req"}
        if stg == "INITIAL":
            return {"amount": 0.50 * mv + put_prem, "allowed": True,
                    "notes": "50% MV + put premium; short call 0 req"}
        maint = _collar_maintenance(legs, spot)
        return {"amount": maint, "allowed": True,
                "notes": "min(10%*putStrike+putOTM, 25%*callStrike)"}

    # ── CONVERSION ────────────────────────────────────────────
    if code == CONV:
        mv = abs(stock_pos) * spot
        put_prem = _long_put_premium(legs)
        # Find common strike
        long_puts = [l for l in legs if l.kind.lower() == "put" and l.position > 0]
        short_calls = [l for l in legs if l.kind.lower() == "call" and l.position < 0]
        strike = long_puts[0].strike if long_puts else 0.0
        mult = long_puts[0].multiplier if long_puts else 100
        qty = abs(long_puts[0].position) if long_puts else 1

        if acct == "CASH":
            return {"amount": mv + put_prem, "allowed": True,
                    "notes": "MV + put premium; short call 0 req"}
        if stg == "INITIAL":
            return {"amount": 0.50 * mv + put_prem, "allowed": True,
                    "notes": "50% MV + put premium; short call 0 req"}
        # Maintenance = 10% * strike * qty * mult
        maint = 0.10 * strike * qty * mult
        return {"amount": maint, "allowed": True,
                "notes": "10% * strike (same strike conversion)"}

    # ── REVERSE CONVERSION ────────────────────────────────────
    if code == REVCONV:
        long_calls = [l for l in legs if l.kind.lower() == "call" and l.position > 0]
        call_prem = sum(abs(l.position) * l.premium * l.multiplier for l in long_calls)
        strike = long_calls[0].strike if long_calls else 0.0
        mult = long_calls[0].multiplier if long_calls else 100
        qty = abs(long_calls[0].position) if long_calls else 1

        if acct == "CASH":
            return {"amount": None, "allowed": False,
                    "notes": "Not permitted in cash accounts"}
        if stg == "INITIAL":
            short_mv = abs(stock_pos) * spot
            return {"amount": 0.50 * short_mv + call_prem, "allowed": True,
                    "notes": "50% short stock MV + call premium; short put 0 req"}
        # Maintenance = 110% * strike
        maint = 1.10 * strike * qty * mult
        return {"amount": maint, "allowed": True,
                "notes": "110% * strike (reverse conversion)"}

    # ── SHORT PUT + SHORT UNDERLYING ──────────────────────────
    if code == SH_PUT_SH_UND:
        if acct == "CASH":
            return {"amount": None, "allowed": False,
                    "notes": "Not permitted in cash accounts"}
        # Short stock is margined normally; short put has 0 additional req
        stock_req = _stock_req_short(acct, stg, spot, stock_pos)
        return {"amount": stock_req, "allowed": True,
                "notes": "Short stock margined normally; short put 0 additional req"}

    # ── LONG CALL + SHORT UNDERLYING ──────────────────────────
    if code == LNG_CALL_SH_UND:
        long_calls = [l for l in legs if l.kind.lower() == "call" and l.position > 0]
        call_prem = sum(abs(l.position) * l.premium * l.multiplier for l in long_calls)
        if acct == "CASH":
            return {"amount": None, "allowed": False,
                    "notes": "Not permitted in cash accounts"}
        stock_req = _stock_req_short(acct, stg, spot, stock_pos)
        return {"amount": stock_req + call_prem, "allowed": True,
                "notes": "Short stock margined + call premium paid"}

    # ── COVERED CALLS WITH CONVERTIBLE / WARRANT / ETF ────────
    if code in {SH_CALL_CONV, SH_CALL_WAR, SH_IDX_CALL_LNG_ETF}:
        # These require special security types; approximate as CCOV
        mv = abs(stock_pos) * spot if stock_pos else spot * 100
        if acct == "CASH":
            return {"amount": mv, "allowed": True,
                    "notes": f"{code}: approx as covered call (cash)"}
        if stg == "INITIAL":
            return {"amount": 0.50 * mv, "allowed": True,
                    "notes": f"{code}: approx as covered call (init)"}
        return {"amount": 0.25 * mv, "allowed": True,
                "notes": f"{code}: approx as covered call (maint)"}

    # ── MPL / GENERAL / FALLBACK ──────────────────────────────
    # For unrecognized codes, compute a conservative estimate
    short_legs = [l for l in legs if l.position < 0]
    long_legs = [l for l in legs if l.position > 0]

    if not legs and stock_pos != 0:
        stock_req = (
            _stock_req_long(acct, stg, spot, stock_pos)
            if stock_pos > 0
            else _stock_req_short(acct, stg, spot, stock_pos)
        )
        return {"amount": stock_req, "allowed": True,
                "notes": "Stock-only position (Reg-T)"}

    if short_legs:
        pct, min_pct, lev = _get_short_pcts(
            code, is_index, is_volatility_index, index_base_type, leverage_factor,
        )
        total = sum(
            _short_option_requirement(l, spot, pct, min_pct, lev)
            for l in short_legs
        )
        return {"amount": total, "allowed": True,
                "notes": f"GENERAL fallback: short option formula"}

    total = _sum_long_premium(legs)
    return {"amount": total, "allowed": True,
            "notes": "GENERAL fallback: long premium paid"}


# ===================================================================
# 5. HOUSE NUMERIC ENGINE
# ===================================================================

def compute_margin_house(
    code: str,
    account: str,
    stage: str,
    input: StrategyInput,
    *,
    leverage_factor: float = 1.0,
    is_index: bool = False,
    is_volatility_index: bool = False,
    index_base_type: str = "BROAD",
) -> dict:
    """
    House margin requirement.

    From VBA ComputeMarginReq_House():
    - If stock_pos != 0: delegate entirely to CBOE (FINRA/4210 combined)
    - Otherwise: same formulas as CBOE for options
    """
    # If stock is involved, delegate to CBOE (combined treatment)
    if input.stock_position != 0:
        return compute_margin_cboe(
            code, account, stage, input,
            leverage_factor=leverage_factor,
            is_index=is_index,
            is_volatility_index=is_volatility_index,
            index_base_type=index_base_type,
        )

    # Pure option strategies: House uses same logic as CBOE for margin account
    return compute_margin_cboe(
        code, account, stage, input,
        leverage_factor=leverage_factor,
        is_index=is_index,
        is_volatility_index=is_volatility_index,
        index_base_type=index_base_type,
    )


# ===================================================================
# 6. HOUSE INTRADAY CHECK
# ===================================================================

def compute_house_intraday(
    house_margin_req: float | None,
    housecall_excess: float,
    sma: float,
    todays_change: float,
    new_intraday_cash: float,
) -> dict:
    """
    House intraday check -- OK to Trade flag.

    From VBA BuildHouseIntradayPanel():
      intraday_available = min(SMA + new_cash, callExcess + new_cash) + todays_change
      ok_to_trade = intraday_available >= house_margin_req
    """
    intraday_available = (
        min(sma + new_intraday_cash, housecall_excess + new_intraday_cash)
        + todays_change
    )

    if house_margin_req is None or not isinstance(house_margin_req, (int, float)):
        ok = None
    else:
        ok = intraday_available >= house_margin_req

    return {
        "house_margin_req": house_margin_req,
        "intraday_available": intraday_available,
        "ok_to_trade": ok,
        "notes": "min(SMA+NewCash, CallExcess+NewCash) + Today's Change",
    }


# ===================================================================
# 7. PUBLIC API -- compute everything at once
# ===================================================================

def compute_margin_full(
    input: StrategyInput,
    payoff_result: dict | None = None,
    *,
    is_index: bool = False,
    is_volatility_index: bool = False,
    index_base_type: str = "BROAD",
    leverage_factor: float = 1.0,
    settlement_type: str = "PHYSICAL",
    exercise_type: str = "AMERICAN",
    listing_type: str = "LISTED",
    dte: float = 0.0,
    is_flex: bool = False,
) -> dict:
    """
    Compute full margin requirements: both CBOE and House, all combos.

    Returns nested dict with classification, cboe, and house sections.
    """
    base_code = classify_strategy(input)
    refined_code = classify_strategy_refined(
        input,
        is_index=is_index,
        is_volatility_index=is_volatility_index,
        index_base_type=index_base_type,
        leverage_factor=leverage_factor,
        listing_type=listing_type,
        dte=dte,
        is_flex=is_flex,
        settlement_type=settlement_type,
        exercise_type=exercise_type,
    )

    cboe_kwargs = dict(
        leverage_factor=leverage_factor,
        is_index=is_index,
        is_volatility_index=is_volatility_index,
        index_base_type=index_base_type,
        settlement_type=settlement_type,
        exercise_type=exercise_type,
        listing_type=listing_type,
        dte=dte,
        is_flex=is_flex,
    )

    cboe_cash_init = compute_margin_cboe(
        refined_code, "CASH", "INITIAL", input, **cboe_kwargs,
    )
    cboe_marg_init = compute_margin_cboe(
        refined_code, "MARGIN", "INITIAL", input, **cboe_kwargs,
    )
    cboe_marg_maint = compute_margin_cboe(
        refined_code, "MARGIN", "MAINTENANCE", input, **cboe_kwargs,
    )

    house_kwargs = dict(
        leverage_factor=leverage_factor,
        is_index=is_index,
        is_volatility_index=is_volatility_index,
        index_base_type=index_base_type,
    )
    house_marg_init = compute_margin_house(
        refined_code, "MARGIN", "INITIAL", input, **house_kwargs,
    )
    house_marg_maint = compute_margin_house(
        refined_code, "MARGIN", "MAINTENANCE", input, **house_kwargs,
    )

    # Add requirement text from CSV lookup
    for acct, stg, result in [
        ("CASH", "INITIAL", cboe_cash_init),
        ("MARGIN", "INITIAL", cboe_marg_init),
        ("MARGIN", "MAINTENANCE", cboe_marg_maint),
    ]:
        result["requirement_text"] = lookup_requirement_text(refined_code, acct, stg)

    return {
        "classification": base_code,
        "classification_refined": refined_code,
        "cboe": {
            "cash_initial": cboe_cash_init,
            "margin_initial": cboe_marg_init,
            "margin_maintenance": cboe_marg_maint,
        },
        "house": {
            "margin_initial": house_marg_init,
            "margin_maintenance": house_marg_maint,
        },
    }


# ===================================================================
# 8. BACKWARD COMPATIBILITY
# ===================================================================

def _option_only_input(input: StrategyInput) -> StrategyInput:
    return StrategyInput(
        spot=input.spot,
        stock_position=0.0,
        avg_cost=0.0,
        legs=input.legs,
    )


def _short_option_margin(leg: OptionLeg, spot: float) -> float:
    """Original short-option formula (kept for compute_margin_proxy compat)."""
    return _short_option_requirement(leg, spot, 0.20, 0.10, 1.0)


def compute_margin_proxy(
    input: StrategyInput, payoff_result: dict, mode: str = "CBOE"
) -> float:
    """Backward-compatible proxy.  Returns CBOE Margin Initial amount."""
    _ = mode
    classification = classify_strategy(input)
    spot = float(input.spot)

    if classification == LNG_LE_9M:
        total = sum(
            leg.position * leg.premium * leg.multiplier
            for leg in input.legs
            if leg.position > 0
        )
        return max(1.0, float(total))

    if classification == SPR:
        option_only = _option_only_input(input)
        price_grid = payoff_result.get("price_grid", [])
        if not price_grid:
            payoff_result = compute_payoff(input)
            price_grid = payoff_result.get("price_grid", [])
        option_pnl = [
            _compute_pnl_for_price(option_only, price) for price in price_grid
        ]
        if not option_pnl:
            return 1.0
        return max(1.0, abs(min(option_pnl)))

    if classification in {SH_OPT, SH_PUT_CALL}:
        total = 0.0
        for leg in input.legs:
            if leg.position < 0:
                total += _short_option_margin(leg, spot)
        return max(1.0, total)

    if classification == CCOV:
        return max(1.0, 0.5 * abs(input.stock_position) * spot)

    if classification in {PPRT, COL_EQ}:
        net_put_premium = sum(
            leg.position * leg.premium * leg.multiplier
            for leg in input.legs
            if leg.kind.lower() == "put"
        )
        total = 0.5 * abs(input.stock_position) * spot + max(
            net_put_premium, 0.0
        )
        return max(1.0, total)

    return 1.0
