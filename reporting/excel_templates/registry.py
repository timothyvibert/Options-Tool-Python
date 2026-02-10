"""Template registry -- maps template names to injection configurations.

Each config is a dict with:
  - "file": original xlsx filename
  - "strategy_match": list of strategy_id strings this template handles
  - "output_sheet": name of the PDF-visible sheet
  - "data_sheet": name of the staging sheet (usually "data")
  - "injections": list of injection dicts, each with:
      - "cell": str like "data!E7" or "output!F10"
      - "source": dotted path into analysis_pack or a special key
      - "transform": optional transform function name
"""
from __future__ import annotations

import math
from datetime import date, datetime
from typing import Any, Optional


# --- Transform functions ---


def _as_date_text_dd_mmmm_yyyy(value: Any) -> Optional[str]:
    """Format date as 'dd mmmm yyyy' for report header."""
    if value is None:
        return None
    if isinstance(value, str):
        try:
            value = date.fromisoformat(value[:10])
        except (ValueError, TypeError):
            return str(value)
    if isinstance(value, (date, datetime)):
        return value.strftime("%d %B %Y")
    return str(value)


def _as_pricing_disclaimer(value: Any) -> Optional[str]:
    """Format as '^ Pricing is HIGHLY indicative on mmmm dd, yyyy'."""
    if value is None:
        d = date.today()
    elif isinstance(value, str):
        try:
            d = date.fromisoformat(value[:10])
        except (ValueError, TypeError):
            d = date.today()
    elif isinstance(value, (date, datetime)):
        d = value if isinstance(value, date) else value.date()
    else:
        d = date.today()
    return f" ^Pricing is HIGHLY indicative on {d.strftime('%B %d, %Y')}"


def _pct_as_decimal(value: Any) -> Optional[float]:
    """Convert percentage (e.g. 12.5) to decimal (0.125)."""
    if value is None:
        return None
    try:
        return float(value) / 100.0
    except (ValueError, TypeError):
        return None


def _div_yield_as_decimal(value: Any) -> Optional[float]:
    """Convert dividend yield percentage to decimal."""
    return _pct_as_decimal(value)


def _vol_as_decimal(value: Any) -> Optional[float]:
    """Convert vol (e.g. 22.5) to decimal (0.225)."""
    return _pct_as_decimal(value)


def _round_premium(value: Any) -> Optional[float]:
    """Round premium to 1 decimal (matches template ROUNDUP pattern)."""
    if value is None:
        return None
    try:
        return round(float(value), 1)
    except (ValueError, TypeError):
        return None


def _now_timestamp(value: Any = None) -> datetime:
    """Return current datetime for NOW() replacement."""
    return datetime.now()


def _negate(value: Any) -> Optional[float]:
    """Negate a value (for short leg delta display)."""
    if value is None:
        return None
    try:
        return -float(value)
    except (ValueError, TypeError):
        return None


def _round_premium_down(value: Any) -> Optional[float]:
    """Round premium DOWN to 1 decimal (matches template ROUNDDOWN pattern)."""
    if value is None:
        return None
    try:
        return math.floor(float(value) * 10) / 10
    except (ValueError, TypeError):
        return None


def _as_pricing_disclaimer_prev_close(value: Any) -> Optional[str]:
    """Format as '*Pricing is HIGHLY indicative on the close mmmm dd yyyy' (yesterday's date)."""
    from datetime import timedelta
    if value is None:
        d = date.today()
    elif isinstance(value, str):
        try:
            d = date.fromisoformat(value[:10])
        except (ValueError, TypeError):
            d = date.today()
    elif isinstance(value, (date, datetime)):
        d = value if isinstance(value, date) else value.date()
    else:
        d = date.today()
    prev = d - timedelta(days=1)
    return f"*Pricing is HIGHLY indicative on the close {prev.strftime('%B %d %Y')}"


def _resolve(pack: dict, path: str) -> Any:
    """Resolve a dotted path like 'underlying.spot' from analysis_pack."""
    parts = path.split(".")
    current: Any = pack
    for part in parts:
        if isinstance(current, dict):
            current = current.get(part)
        else:
            return None
        if current is None:
            return None
    return current


# --- Transform registry ---
TRANSFORMS: dict[str, Any] = {
    "date_dd_mmmm_yyyy": _as_date_text_dd_mmmm_yyyy,
    "pricing_disclaimer": _as_pricing_disclaimer,
    "pricing_disclaimer_prev_close": _as_pricing_disclaimer_prev_close,
    "pct_as_decimal": _pct_as_decimal,
    "div_yield_decimal": _div_yield_as_decimal,
    "vol_as_decimal": _vol_as_decimal,
    "round_premium": _round_premium,
    "round_premium_down": _round_premium_down,
    "negate": _negate,
    "now_timestamp": _now_timestamp,
}


# ============================================================
# TEMPLATE: Covered Call (Single Stock_Covered Call_Overwrite.xlsx)
# ============================================================
#
# INJ_000001: data!E7:E12 -- inputs block
# INJ_000002: data!E4:O4 -- market + leg staging
# INJ_000003: data!T4:U4 -- dividends + trade cost
# INJ_000004: data!X4:Y4 -- company name + sector
# INJ_000005: output!N1 -- as_of date text
# INJ_000006: output!O8:O10 -- div yield, 52W high/low
# INJ_000007: output!F10:F11 -- 1D changes
# INJ_000008: output!H10 -- earnings date
# INJ_000009: output!O33:O34 -- 6m impvol, vol percentile

TEMPLATE_COVERED_CALL: dict[str, Any] = {
    "file": "Single Stock_Covered Call_Overwrite.xlsx",
    "template_key": "template_covered_call",
    "strategy_match": ["8"],
    "output_sheet": "output",
    "data_sheet": "data",
    "injections": [
        # === INJ_000001: Inputs block (data!E7:E12) ===
        {"cell": "data!E7", "source": "meta.underlying_ticker", "label": "ticker"},
        {"cell": "data!E8", "source": "meta.option_ticker_leg1", "label": "option_ticker"},
        {"cell": "data!E9", "source": "meta.shares", "label": "shares"},
        {"cell": "data!E10", "source": "underlying.ubs_rating", "label": "grp_rating"},
        {"cell": "data!E11", "source": "underlying.ubs_target", "label": "target_price"},
        {"cell": "data!E12", "source": "meta.cio_rating", "label": "cio_rating"},

        # === INJ_000002: Market + Leg staging (data!E4:O4) ===
        {"cell": "data!E4", "source": "underlying.spot", "label": "spot_price"},
        {"cell": "data!F4", "source": "meta.option_ticker_leg1", "label": "opt_name_staging"},
        {"cell": "data!G4", "source": "legs.0.strike", "label": "strike"},
        {"cell": "data!H4", "source": "strategy.expiry", "label": "expiry_date"},
        {"cell": "data!I4", "source": "_computed.dte", "label": "days_to_expiry"},
        {"cell": "data!J4", "source": "strategy.expiry", "label": "expiry_display"},
        {"cell": "data!K4", "source": "legs.0.premium", "label": "premium_mid"},
        {"cell": "data!L4", "source": "legs.0.iv_mid", "label": "iv_bid"},
        {"cell": "data!M4", "source": "underlying.impvol_3m_atm", "label": "vol_90d"},
        {"cell": "data!N4", "source": "_computed.bid_ask_spread", "label": "spread"},
        {"cell": "data!O4", "source": "legs.0.delta_mid", "label": "delta"},

        # === INJ_000003: Dividend sum + trade cost (data!T4:U4) ===
        {"cell": "data!T4", "source": "dividend_schedule.dividend_sum", "label": "div_to_expiry", "default": 0},
        {"cell": "data!U4", "source": "_computed.trade_cost", "label": "trade_cost", "default": 0},

        # === INJ_000004: Name + Sector (data!X4:Y4) ===
        {"cell": "data!X4", "source": "underlying.profile.NAME", "label": "company_name"},
        {"cell": "data!Y4", "source": "underlying.profile.GICS_SECTOR_NAME", "label": "gics_sector"},

        # === INJ_000005: Report date (output!N1) ===
        {"cell": "output!N1", "source": "as_of", "transform": "date_dd_mmmm_yyyy", "label": "report_date"},

        # === INJ_000006: Yield + 52W (output!O8:O10) ===
        {"cell": "output!O8", "source": "underlying.profile.EQY_DVD_YLD_IND", "transform": "div_yield_decimal", "label": "div_yield"},
        {"cell": "output!O9", "source": "underlying.high_52week", "label": "high_52w"},
        {"cell": "output!O10", "source": "underlying.low_52week", "label": "low_52w"},

        # === INJ_000007: Day change (output!F10:F11) ===
        {"cell": "output!F10", "source": "underlying.chg_pct_1d", "transform": "pct_as_decimal", "label": "chg_pct_1d"},
        {"cell": "output!F11", "source": "underlying.chg_net_1d", "label": "chg_net_1d"},

        # === INJ_000008: Earnings date (output!H10) ===
        {"cell": "output!H10", "source": "underlying.earnings_date", "label": "earnings_date"},

        # === INJ_000009: Vol stats (output!O33:O34) ===
        {"cell": "output!O33", "source": "underlying.impvol_6m_atm", "transform": "vol_as_decimal", "label": "impvol_6m"},
        {"cell": "output!O34", "source": "underlying.vol_percentile", "transform": "vol_as_decimal", "label": "vol_pctile"},

        # === Additional volatile cells to freeze ===
        {"cell": "output!D52", "source": "as_of", "transform": "pricing_disclaimer", "label": "pricing_footnote"},
        {"cell": "output!J52", "source": "_computed.now", "transform": "now_timestamp", "label": "pricing_timestamp"},
    ],
}


# ============================================================
# TEMPLATE: Long Call (Single Stock_Long Call.xlsx)
# ============================================================
# From "Excel Illustration Templates.txt" — Long Call section
#
# Output sheet: "speculative call" (not "output")
# Data sheet: "data"
# Inputs: data!E7:E11 (5 fields — ticker, option, qty, rating, target — NO CIO rating)
#
# BBG fields on output sheet (all on "speculative call"):
#   F12 = chg_pct_1d /100,  F13 = chg_net_1d
#   G15 = opt expire dt,  G16 = opt strike px
#   G18 = PX MID (premium, rounded up),  G19 = opt delta
#   N10 = high 52week,  N11 = low 52week,  N13 = expected report dt
#
# Data sheet staging:
#   E4 = spot (BDP),  X4 = company name (BDP)

TEMPLATE_LONG_CALL: dict[str, Any] = {
    "file": "Single Stock_Long Call.xlsx",
    "template_key": "template_long_call",
    "strategy_match": ["4"],  # strategy_id for Long Call
    "output_sheet": "speculative call",
    "data_sheet": "data",
    "injections": [
        # === Inputs (data!E7:E11) — note: only 5 fields, no CIO rating ===
        {"cell": "data!E7", "source": "meta.underlying_ticker", "label": "ticker"},
        {"cell": "data!E8", "source": "meta.option_ticker_leg1", "label": "option_ticker"},
        {"cell": "data!E9", "source": "meta.contracts_leg1", "label": "contracts"},
        {"cell": "data!E10", "source": "underlying.ubs_rating", "label": "research_rating"},
        {"cell": "data!E11", "source": "underlying.ubs_target", "label": "target_price"},

        # === Data sheet staging ===
        {"cell": "data!E4", "source": "underlying.spot", "label": "spot_price"},
        {"cell": "data!X4", "source": "underlying.profile.NAME", "label": "company_name"},

        # === Output sheet Bloomberg replacements (speculative call) ===
        # Day change
        {"cell": "speculative call!F12", "source": "underlying.chg_pct_1d", "transform": "pct_as_decimal", "label": "chg_pct_1d"},
        {"cell": "speculative call!F13", "source": "underlying.chg_net_1d", "label": "chg_net_1d"},

        # Option leg data
        {"cell": "speculative call!G15", "source": "strategy.expiry", "label": "opt_expiry"},
        {"cell": "speculative call!G16", "source": "legs.0.strike", "label": "opt_strike"},
        {"cell": "speculative call!G18", "source": "legs.0.premium", "transform": "round_premium", "label": "opt_premium"},
        {"cell": "speculative call!G19", "source": "legs.0.delta_mid", "label": "opt_delta"},

        # Underlying stats
        {"cell": "speculative call!N10", "source": "underlying.high_52week", "label": "high_52w"},
        {"cell": "speculative call!N11", "source": "underlying.low_52week", "label": "low_52w"},
        {"cell": "speculative call!N13", "source": "underlying.earnings_date", "label": "earnings_date"},
    ],
}


# ============================================================
# TEMPLATE: Short Put / Cash-Secured (Single Stock_Short Put.xlsx)
# ============================================================
# From "Excel Illustration Templates.txt" — Cash Secured Put section
#
# Output sheet: "Cash-Secured"
# Data sheet: "data"
# Inputs: data!E7:E12 (6 fields — same as Covered Call)
#
# INJ_000001: data!E7:E12 — inputs block
# INJ_000002: data!E4 — spot price
# INJ_000003: data!X4:Y4 — name + sector
# INJ_000004: Cash-Secured!G16:G20 — [expiry, strike, spot-strike, premium, delta]
# INJ_000005: Cash-Secured!F13 — chg_pct_1d
# INJ_000006: Cash-Secured!I13 — chg_net_1d
# INJ_000007: Cash-Secured!N11:N13 — [div_yield, high_52w, low_52w]
# INJ_000008: Cash-Secured!G22 — expected report dt
# INJ_000009: Cash-Secured!M21 — 200d moving avg
# INJ_000010: Cash-Secured!Q1 — T-bill yield (for accrual calc)
# INJ_000011: Cash-Secured!Q23 — T-bill yield display
# INJ_000012: Cash-Secured!N1 — report date text
# INJ_000013: Cash-Secured!G21 — days to expiry
# INJ_000014: Cash-Secured!I62:K62 — pricing timestamp block

TEMPLATE_SHORT_PUT: dict[str, Any] = {
    "file": "Single Stock_Short Put.xlsx",
    "template_key": "template_short_put",
    "strategy_match": ["7"],  # strategy_id for Short Put
    "output_sheet": "Cash-Secured",
    "data_sheet": "data",
    "injections": [
        # === INJ_000001: Inputs (data!E7:E12) ===
        {"cell": "data!E7", "source": "meta.underlying_ticker", "label": "ticker"},
        {"cell": "data!E8", "source": "meta.option_ticker_leg1", "label": "option_ticker"},
        {"cell": "data!E9", "source": "meta.contracts_leg1", "label": "contracts"},
        {"cell": "data!E10", "source": "underlying.ubs_rating", "label": "ib_rating"},
        {"cell": "data!E11", "source": "underlying.ubs_target", "label": "target_price"},
        {"cell": "data!E12", "source": "meta.cio_rating", "label": "cio_rating"},

        # === INJ_000002: Spot (data!E4) ===
        {"cell": "data!E4", "source": "underlying.spot", "label": "spot_price"},

        # === INJ_000003: Name + Sector (data!X4:Y4) ===
        {"cell": "data!X4", "source": "underlying.profile.NAME", "label": "company_name"},
        {"cell": "data!Y4", "source": "underlying.profile.GICS_SECTOR_NAME", "label": "gics_sector"},

        # === INJ_000004: Option block (Cash-Secured!G16:G20) ===
        # G16=expiry, G17=strike, G18=spot-strike (formula will recalc), G19=premium, G20=delta
        {"cell": "Cash-Secured!G16", "source": "strategy.expiry", "label": "opt_expiry"},
        {"cell": "Cash-Secured!G17", "source": "legs.0.strike", "label": "opt_strike"},
        # G18 is a formula (=spot-strike), but since it references Bloomberg we overwrite it
        {"cell": "Cash-Secured!G18", "source": "_computed.spot_minus_strike", "label": "spot_minus_strike"},
        {"cell": "Cash-Secured!G19", "source": "legs.0.premium", "transform": "round_premium", "label": "opt_premium"},
        {"cell": "Cash-Secured!G20", "source": "legs.0.delta_mid", "label": "opt_delta"},

        # === INJ_000005: Day % change (Cash-Secured!F13) ===
        {"cell": "Cash-Secured!F13", "source": "underlying.chg_pct_1d", "transform": "pct_as_decimal", "label": "chg_pct_1d"},

        # === INJ_000006: Day $ change (Cash-Secured!I13) ===
        {"cell": "Cash-Secured!I13", "source": "underlying.chg_net_1d", "label": "chg_net_1d"},

        # === INJ_000007: Equity stats (Cash-Secured!N11:N13) ===
        {"cell": "Cash-Secured!N11", "source": "underlying.profile.EQY_DVD_YLD_IND", "transform": "div_yield_decimal", "label": "div_yield"},
        {"cell": "Cash-Secured!N12", "source": "underlying.high_52week", "label": "high_52w"},
        {"cell": "Cash-Secured!N13", "source": "underlying.low_52week", "label": "low_52w"},

        # === INJ_000008: Expected report date (Cash-Secured!G22) ===
        {"cell": "Cash-Secured!G22", "source": "underlying.earnings_date", "label": "earnings_date"},

        # === INJ_000009: 200-day moving avg (Cash-Secured!M21) ===
        {"cell": "Cash-Secured!M21", "source": "underlying.mov_avg_200d", "label": "mov_avg_200d"},

        # === INJ_000010: T-bill yield for accrual (Cash-Secured!Q1) ===
        {"cell": "Cash-Secured!Q1", "source": "policies.risk_free_rate", "label": "t_bill_yield"},

        # === INJ_000011: T-bill yield display (Cash-Secured!Q23) ===
        {"cell": "Cash-Secured!Q23", "source": "policies.risk_free_rate", "label": "t_bill_yield_display"},

        # === INJ_000012: Report date text (Cash-Secured!N1) ===
        {"cell": "Cash-Secured!N1", "source": "as_of", "transform": "date_dd_mmmm_yyyy", "label": "report_date"},

        # === INJ_000013: Days to expiry (Cash-Secured!G21) ===
        {"cell": "Cash-Secured!G21", "source": "_computed.dte", "label": "days_to_expiry"},

        # === INJ_000014: Pricing timestamp block (Cash-Secured!I62:K62) ===
        {"cell": "Cash-Secured!I62", "source": "_computed.now", "transform": "now_timestamp", "label": "pricing_now"},
        {"cell": "Cash-Secured!K62", "source": "as_of", "transform": "pricing_disclaimer", "label": "pricing_disclaimer"},
    ],
}


# ============================================================
# TEMPLATE: Bull Call Spread (Single Stock_Bull Call Spread.xlsm)
# ============================================================
# Output sheet: "output"
# Data sheet: "data"
# Also has: Graph sheet (payoff curve), DIV sheet (hidden), calc sheet
#
# Inputs: data!E7:E12 (6 fields: ticker, long_opt, short_opt, contracts, rating, target)
# NOTE: E8 = long call, E9 = short call (2 option tickers)
#
# INJ_000001: data!E7:E12 — inputs
# INJ_000002: data!E4 — spot
# INJ_000003: data!I4 — DTE (volatile)
# INJ_000004: data!X4:Y4 — name + sector
# INJ_000005: output!N7:N9 — [div_yield, high_52w, low_52w]
# INJ_000006: output!F9:F10 — [chg_pct_1d, chg_net_1d]
# INJ_000007: output!E17:I17 — [leg1_delta, (blanks), leg2_delta_negated]
# INJ_000008: output!G20:J21 — 2x4 grid [expiry, strike, premium] per leg
# INJ_000009: output!N1 — report date
# INJ_000010: output!J60 — pricing disclaimer
# INJ_000011: output!O60 — NOW() timestamp

TEMPLATE_BULL_CALL_SPREAD: dict[str, Any] = {
    "file": "Single Stock_Bull Call Spread.xlsm",
    "template_key": "template_bull_call_spread",
    "strategy_match": ["13"],
    "output_sheet": "output",
    "data_sheet": "data",
    "injections": [
        # === INJ_000001: Inputs (data!E7:E12) ===
        {"cell": "data!E7", "source": "meta.underlying_ticker", "label": "ticker"},
        {"cell": "data!E8", "source": "meta.option_ticker_leg1", "label": "long_call_ticker"},
        {"cell": "data!E9", "source": "meta.option_ticker_leg2", "label": "short_call_ticker"},
        {"cell": "data!E10", "source": "meta.contracts_leg1", "label": "contracts"},
        {"cell": "data!E11", "source": "underlying.ubs_rating", "label": "rating"},
        {"cell": "data!E12", "source": "underlying.ubs_target", "label": "target"},

        # === INJ_000002: Spot (data!E4) ===
        {"cell": "data!E4", "source": "underlying.spot", "label": "spot"},

        # === INJ_000003: DTE (data!I4) ===
        {"cell": "data!I4", "source": "_computed.dte", "label": "dte"},

        # === INJ_000004: Name + Sector (data!X4:Y4) ===
        {"cell": "data!X4", "source": "underlying.profile.NAME", "label": "company_name"},
        {"cell": "data!Y4", "source": "underlying.profile.GICS_SECTOR_NAME", "label": "gics_sector"},

        # === INJ_000005: Yield + 52W (output!N7:N9) ===
        {"cell": "output!N7", "source": "underlying.profile.EQY_DVD_YLD_IND", "transform": "div_yield_decimal", "label": "div_yield"},
        {"cell": "output!N8", "source": "underlying.high_52week", "label": "high_52w"},
        {"cell": "output!N9", "source": "underlying.low_52week", "label": "low_52w"},

        # === INJ_000006: Day change (output!F9:F10) ===
        {"cell": "output!F9", "source": "underlying.chg_pct_1d", "transform": "pct_as_decimal", "label": "chg_pct_1d"},
        {"cell": "output!F10", "source": "underlying.chg_net_1d", "label": "chg_net_1d"},

        # === INJ_000007: Option deltas (output!E17 and output!I17) ===
        # E17 = long call delta (raw), I17 = short call delta (negated — template flips sign)
        {"cell": "output!E17", "source": "legs.0.delta_mid", "label": "leg1_delta"},
        {"cell": "output!I17", "source": "legs.1.delta_mid", "transform": "negate", "label": "leg2_delta_neg"},

        # === INJ_000008: Leg term grid (output!G20:J21) ===
        # Row 20 = long leg: G20=expiry, I20=strike, J20=premium (ROUNDUP)
        # Row 21 = short leg: G21=expiry, I21=strike, J21=premium (ROUNDDOWN)
        {"cell": "output!G20", "source": "strategy.expiry", "label": "leg1_expiry"},
        {"cell": "output!I20", "source": "legs.0.strike", "label": "leg1_strike"},
        {"cell": "output!J20", "source": "legs.0.premium", "transform": "round_premium", "label": "leg1_premium"},
        {"cell": "output!G21", "source": "strategy.expiry", "label": "leg2_expiry"},
        {"cell": "output!I21", "source": "legs.1.strike", "label": "leg2_strike"},
        {"cell": "output!J21", "source": "legs.1.premium", "transform": "round_premium_down", "label": "leg2_premium"},

        # === INJ_000009: Report date (output!N1) ===
        {"cell": "output!N1", "source": "as_of", "transform": "date_dd_mmmm_yyyy", "label": "report_date"},

        # === INJ_000010: Pricing disclaimer (output!J60) ===
        {"cell": "output!J60", "source": "as_of", "transform": "pricing_disclaimer", "label": "pricing_note"},

        # === INJ_000011: NOW() timestamp (output!O60) ===
        {"cell": "output!O60", "source": "_computed.now", "transform": "now_timestamp", "label": "timestamp"},
    ],
}


# ============================================================
# TEMPLATE: Bear Put Spread / Put Spread Hedge
# (Single Stock_Put Spread Hedge.xlsx)
# ============================================================
# Output sheet: "BearPutSpread"
# Data sheet: "data"
# Also has: DIV sheet (visible but lookup only)
#
# Inputs: data!E7:E13 (7 fields — includes CIO rating at E13)
# NOTE: E8 = long put, E9 = short put
#
# Data sheet staging:
#   E4 — spot
#   G4 — leg1 expiry staging
#   J4 — expiry date staging (referenced by output)
#   AB4 — leg1 delta staging
#   X4:Y4 — name + sector
#
# Output sheet direct Bloomberg overwrites:
#   N6 = high_52w, N7 = low_52w
#   F9 = chg_pct_1d, F10 = chg_net_1d
#   G12 = leg2 expiry (short put)
#   G13 = leg2 strike (short put)
#   F15 = leg1 premium (ROUNDUP), G15 = leg2 premium (ROUNDDOWN)
#   F16 = leg1 delta, G16 = leg2 delta
#   F18 = DTE long, G18 = DTE short
#   N1 = report date, D56 = pricing disclaimer (prev close), I56 = NOW()

TEMPLATE_BEAR_PUT_SPREAD: dict[str, Any] = {
    "file": "Single Stock_Put Spread Hedge.xlsx",
    "template_key": "template_bear_put_spread",
    "strategy_match": ["14"],
    "output_sheet": "BearPutSpread",
    "data_sheet": "data",
    "injections": [
        # === INJ_000001: Inputs (data!E7:E13) — 7 fields ===
        {"cell": "data!E7", "source": "meta.underlying_ticker", "label": "ticker"},
        {"cell": "data!E8", "source": "meta.option_ticker_leg1", "label": "long_put_ticker"},
        {"cell": "data!E9", "source": "meta.option_ticker_leg2", "label": "short_put_ticker"},
        {"cell": "data!E10", "source": "meta.contracts_leg1", "label": "contracts"},
        {"cell": "data!E11", "source": "underlying.ubs_rating", "label": "rating"},
        {"cell": "data!E12", "source": "underlying.ubs_target", "label": "target"},
        {"cell": "data!E13", "source": "meta.cio_rating", "label": "cio_rating"},

        # === INJ_000002: Spot + staging (data sheet) ===
        {"cell": "data!E4", "source": "underlying.spot", "label": "spot"},
        {"cell": "data!G4", "source": "strategy.expiry", "label": "leg1_expiry_staging"},
        {"cell": "data!J4", "source": "strategy.expiry", "label": "expiry_date_staging"},
        {"cell": "data!AB4", "source": "legs.0.delta_mid", "label": "leg1_delta_staging"},

        # === INJ_000003: Name + Sector (data!X4:Y4) ===
        {"cell": "data!X4", "source": "underlying.profile.NAME", "label": "company_name"},
        {"cell": "data!Y4", "source": "underlying.profile.GICS_SECTOR_NAME", "label": "gics_sector"},

        # === INJ_000004: High 52W (BearPutSpread!N6) ===
        {"cell": "BearPutSpread!N6", "source": "underlying.high_52week", "label": "high_52w"},

        # === INJ_000005: Low 52W (BearPutSpread!N7) ===
        {"cell": "BearPutSpread!N7", "source": "underlying.low_52week", "label": "low_52w"},

        # === INJ_000006: Chg pct 1d (BearPutSpread!F9) ===
        {"cell": "BearPutSpread!F9", "source": "underlying.chg_pct_1d", "transform": "pct_as_decimal", "label": "chg_pct_1d"},

        # === INJ_000007: Chg net 1d (BearPutSpread!F10) ===
        {"cell": "BearPutSpread!F10", "source": "underlying.chg_net_1d", "label": "chg_net_1d"},

        # === INJ_000008: Leg2 (short put) expiry (BearPutSpread!G12) ===
        {"cell": "BearPutSpread!G12", "source": "strategy.expiry", "label": "leg2_expiry"},

        # === INJ_000009: Leg2 (short put) strike (BearPutSpread!G13) ===
        {"cell": "BearPutSpread!G13", "source": "legs.1.strike", "label": "leg2_strike"},

        # === INJ_000010: Leg1 (long put) premium ROUNDUP (BearPutSpread!F15) ===
        {"cell": "BearPutSpread!F15", "source": "legs.0.premium", "transform": "round_premium", "label": "leg1_premium"},

        # === INJ_000011: Leg2 (short put) premium ROUNDDOWN (BearPutSpread!G15) ===
        {"cell": "BearPutSpread!G15", "source": "legs.1.premium", "transform": "round_premium_down", "label": "leg2_premium"},

        # === INJ_000012: Leg1 delta (BearPutSpread!F16) ===
        {"cell": "BearPutSpread!F16", "source": "legs.0.delta_mid", "label": "leg1_delta"},

        # === INJ_000013: Leg2 delta (BearPutSpread!G16) ===
        {"cell": "BearPutSpread!G16", "source": "legs.1.delta_mid", "label": "leg2_delta"},

        # === INJ_000014: DTE long leg (BearPutSpread!F18) ===
        {"cell": "BearPutSpread!F18", "source": "_computed.dte", "label": "dte_long"},

        # === INJ_000015: DTE short leg (BearPutSpread!G18) — same expiry ===
        {"cell": "BearPutSpread!G18", "source": "_computed.dte", "label": "dte_short"},

        # === INJ_000016: Report date (BearPutSpread!N1) ===
        {"cell": "BearPutSpread!N1", "source": "as_of", "transform": "date_dd_mmmm_yyyy", "label": "report_date"},

        # === INJ_000017: Pricing disclaimer prev close (BearPutSpread!D56) ===
        {"cell": "BearPutSpread!D56", "source": "as_of", "transform": "pricing_disclaimer_prev_close", "label": "pricing_disclaimer"},

        # === INJ_000018: NOW() timestamp (BearPutSpread!I56) ===
        {"cell": "BearPutSpread!I56", "source": "_computed.now", "transform": "now_timestamp", "label": "timestamp"},
    ],
}


# ============================================================
# TEMPLATE: Protective Collar (Single Stock_Protective Collar.xlsx)
# ============================================================
# Output sheet: "Protective Collar"
# Data sheet: "data"
# Also has: DIV (hidden, empty), COMMISSION CALC
#
# Inputs: data!E7:E13 (7 fields — includes CIO at E13)
# NOTE: E8 = leg1 option (put), E9 = leg2 option (call)
#
# This template has a 2-ROW staging grid: data!E4:O5
# Row 4 = leg1 (put) data, Row 5 = leg2 (call) data
#
# INJ_000001: data!E7:E13 — inputs (7 fields)
# INJ_000002: data!E4:O5 — 2-row market+leg staging
# INJ_000003: data!T4 — dividends to expiry
# INJ_000004: data!X4:Y4 — name + sector
# INJ_000005: Protective Collar!O4 — earnings date
# INJ_000006: Protective Collar!O7:O9 — [div_yield, high_52w, low_52w]
# INJ_000007: Protective Collar!F9:F10 — [chg_pct_1d, chg_net_1d]
# INJ_000008: Protective Collar!G14:G15 — leg2 [expiry, strike]
# INJ_000009: Protective Collar!F17:G18 — 2x2 grid [premiums; deltas]
# INJ_000010: Protective Collar!N1 — report date
# INJ_000011: Protective Collar!H60 — NOW() timestamp
# INJ_000012: Protective Collar!L60 — pricing indicative line

TEMPLATE_PROTECTIVE_COLLAR: dict[str, Any] = {
    "file": "Single Stock_Protective Collar.xlsx",
    "template_key": "template_protective_collar",
    "strategy_match": ["12"],
    "output_sheet": "Protective Collar",
    "data_sheet": "data",
    "injections": [
        # === INJ_000001: Inputs (data!E7:E13) — 7 fields ===
        {"cell": "data!E7", "source": "meta.underlying_ticker", "label": "ticker"},
        {"cell": "data!E8", "source": "meta.option_ticker_leg1", "label": "put_ticker"},
        {"cell": "data!E9", "source": "meta.option_ticker_leg2", "label": "call_ticker"},
        {"cell": "data!E10", "source": "meta.contracts_leg1", "label": "contracts"},
        {"cell": "data!E11", "source": "underlying.ubs_rating", "label": "rating"},
        {"cell": "data!E12", "source": "underlying.ubs_target", "label": "target"},
        {"cell": "data!E13", "source": "meta.cio_rating", "label": "cio_rating"},

        # === INJ_000002: 2-row staging grid (data!E4:O5) ===
        # Row 4 (leg1 = put): spot, opt_name, strike, expiry, dte, expiry_date, premium, iv, vol90d, spread, delta
        {"cell": "data!E4", "source": "underlying.spot", "label": "spot_r4"},
        {"cell": "data!F4", "source": "meta.option_ticker_leg1", "label": "opt_name_r4"},
        {"cell": "data!G4", "source": "legs.0.strike", "label": "strike_r4"},
        {"cell": "data!H4", "source": "strategy.expiry", "label": "expiry_r4"},
        {"cell": "data!I4", "source": "_computed.dte", "label": "dte_r4"},
        {"cell": "data!J4", "source": "strategy.expiry", "label": "expiry_display_r4"},
        {"cell": "data!K4", "source": "legs.0.premium", "label": "premium_r4"},
        {"cell": "data!L4", "source": "legs.0.iv_mid", "label": "iv_r4"},
        {"cell": "data!O4", "source": "legs.0.delta_mid", "label": "delta_r4"},
        # Row 5 (leg2 = call):
        {"cell": "data!E5", "source": "underlying.spot", "label": "spot_r5"},
        {"cell": "data!F5", "source": "meta.option_ticker_leg2", "label": "opt_name_r5"},
        {"cell": "data!G5", "source": "legs.1.strike", "label": "strike_r5"},
        {"cell": "data!H5", "source": "strategy.expiry", "label": "expiry_r5"},
        {"cell": "data!I5", "source": "_computed.dte", "label": "dte_r5"},
        {"cell": "data!J5", "source": "strategy.expiry", "label": "expiry_display_r5"},
        {"cell": "data!K5", "source": "legs.1.premium", "label": "premium_r5"},
        {"cell": "data!L5", "source": "legs.1.iv_mid", "label": "iv_r5"},
        {"cell": "data!O5", "source": "legs.1.delta_mid", "label": "delta_r5"},

        # === INJ_000003: Dividends to expiry (data!T4) ===
        {"cell": "data!T4", "source": "dividend_schedule.dividend_sum", "label": "div_to_expiry", "default": 0},

        # === INJ_000004: Name + Sector (data!X4:Y4) ===
        {"cell": "data!X4", "source": "underlying.profile.NAME", "label": "company_name"},
        {"cell": "data!Y4", "source": "underlying.profile.GICS_SECTOR_NAME", "label": "gics_sector"},

        # === INJ_000005: Earnings date (Protective Collar!O4) ===
        {"cell": "Protective Collar!O4", "source": "underlying.earnings_date", "label": "earnings_date"},

        # === INJ_000006: Yield + 52W (Protective Collar!O7:O9) ===
        {"cell": "Protective Collar!O7", "source": "underlying.profile.EQY_DVD_YLD_IND", "transform": "div_yield_decimal", "label": "div_yield"},
        {"cell": "Protective Collar!O8", "source": "underlying.high_52week", "label": "high_52w"},
        {"cell": "Protective Collar!O9", "source": "underlying.low_52week", "label": "low_52w"},

        # === INJ_000007: Day change (Protective Collar!F9:F10) ===
        {"cell": "Protective Collar!F9", "source": "underlying.chg_pct_1d", "transform": "pct_as_decimal", "label": "chg_pct_1d"},
        {"cell": "Protective Collar!F10", "source": "underlying.chg_net_1d", "label": "chg_net_1d"},

        # === INJ_000008: Leg2 expiry + strike (Protective Collar!G14:G15) ===
        {"cell": "Protective Collar!G14", "source": "strategy.expiry", "label": "leg2_expiry"},
        {"cell": "Protective Collar!G15", "source": "legs.1.strike", "label": "leg2_strike"},

        # === INJ_000009: Premiums + Deltas grid (Protective Collar!F17:G18) ===
        # F17 = leg1 (put) premium, G17 = leg2 (call) premium
        # F18 = leg1 (put) delta, G18 = leg2 (call) delta
        {"cell": "Protective Collar!F17", "source": "legs.0.premium", "label": "leg1_premium"},
        {"cell": "Protective Collar!G17", "source": "legs.1.premium", "label": "leg2_premium"},
        {"cell": "Protective Collar!F18", "source": "legs.0.delta_mid", "label": "leg1_delta"},
        {"cell": "Protective Collar!G18", "source": "legs.1.delta_mid", "label": "leg2_delta"},

        # === INJ_000010: Report date (Protective Collar!N1) ===
        {"cell": "Protective Collar!N1", "source": "as_of", "transform": "date_dd_mmmm_yyyy", "label": "report_date"},

        # === INJ_000011: NOW() timestamp (Protective Collar!H60) ===
        {"cell": "Protective Collar!H60", "source": "_computed.now", "transform": "now_timestamp", "label": "timestamp"},

        # === INJ_000012: Pricing indicative line (Protective Collar!L60) ===
        {"cell": "Protective Collar!L60", "source": "as_of", "transform": "pricing_disclaimer", "label": "pricing_note"},
    ],
}


# --- Registry ---
TEMPLATE_REGISTRY: dict[str, dict] = {
    "template_covered_call": TEMPLATE_COVERED_CALL,
    "template_long_call": TEMPLATE_LONG_CALL,
    "template_short_put": TEMPLATE_SHORT_PUT,
    "template_bull_call_spread": TEMPLATE_BULL_CALL_SPREAD,
    "template_bear_put_spread": TEMPLATE_BEAR_PUT_SPREAD,
    "template_protective_collar": TEMPLATE_PROTECTIVE_COLLAR,
    # Deferred (needs xlsx inspection):
    # "template_long_put": TEMPLATE_LONG_PUT,
}


def get_template_config(template_key: str) -> Optional[dict]:
    """Get template config by key."""
    return TEMPLATE_REGISTRY.get(template_key)


def get_template_for_strategy(strategy_id: str) -> Optional[dict]:
    """Find the best template config for a given strategy_id."""
    for config in TEMPLATE_REGISTRY.values():
        if strategy_id in config.get("strategy_match", []):
            return config
    return None


def list_templates() -> list[dict]:
    """Return list of available templates with key and display name."""
    result = []
    for key, config in TEMPLATE_REGISTRY.items():
        result.append({
            "key": key,
            "file": config["file"],
            "strategy_match": config.get("strategy_match", []),
        })
    return result
