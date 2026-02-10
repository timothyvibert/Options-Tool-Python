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
    "pct_as_decimal": _pct_as_decimal,
    "div_yield_decimal": _div_yield_as_decimal,
    "vol_as_decimal": _vol_as_decimal,
    "round_premium": _round_premium,
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


# --- Registry ---
TEMPLATE_REGISTRY: dict[str, dict] = {
    "template_covered_call": TEMPLATE_COVERED_CALL,
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
