"""v2 DMC callbacks — ported from vnext/callbacks.py for the /v2 dashboard.

All callbacks use v2-prefixed IDs from frontend_dash.vnext2.ids.
"""

from __future__ import annotations

from datetime import datetime, timezone
import traceback
import json
import math
import re

import pandas as pd
import dash_mantine_components as dmc
import plotly.graph_objects as go
from dash import Input, Output, State, dcc, no_update, ctx, html, dash_table
from dash.exceptions import PreventUpdate

from core.analysis_pack import build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.payoff import _detect_breakevens
from core.strategy_map import get_strategy, list_strategies
from frontend_dash.analysis_adapter import (
    analysis_pack_to_store,
    refresh_leg_premiums,
    to_jsonable,
)
from frontend_dash.smart_strikes import compute_default_strike, is_number_like
from frontend_dash.vnext2 import ids as ID
from frontend_dash.vnext2.activity_log import append_entry, read_all, clear_log, get_csv_path


# ═══════════════════════════════════════════════════════════
# HELPERS (ported from vnext/callbacks.py)
# ═══════════════════════════════════════════════════════════

def _utc_now_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def _coerce_float(value: object) -> float | None:
    try:
        numeric = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(numeric):
        return None
    return numeric


def _coerce_bool(value: object) -> bool:
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    if isinstance(value, (int, float)):
        return value != 0
    text = str(value).strip().lower()
    if text in {"true", "yes", "1", "y", "t"}:
        return True
    return False


def _safe_json_dumps(payload: object) -> str:
    try:
        return json.dumps(to_jsonable(payload), sort_keys=True, indent=2)
    except Exception:
        try:
            return json.dumps(str(payload), sort_keys=True, indent=2)
        except Exception:
            return str(payload)


def _report_filename(key_payload: object, pack: object) -> str:
    """Build PDF filename: '2026-02-09_MSFT US Equity_Covered Call.pdf'."""
    as_of = ""
    ticker = ""
    strategy_name = ""

    if isinstance(pack, dict):
        as_of = pack.get("as_of") or pack.get("asof") or ""
        pack_strategy = pack.get("strategy") or {}
        if isinstance(pack_strategy, dict):
            strategy_name = pack_strategy.get("name") or pack_strategy.get("strategy_name") or ""

    if isinstance(key_payload, dict):
        if not as_of:
            as_of = key_payload.get("key") or ""
        ticker = key_payload.get("ticker") or ""

    parts = [p for p in [as_of, ticker, strategy_name] if p]
    if parts:
        name = "_".join(parts)
        name = re.sub(r'[<>:"/\\|?*]+', "", name)
        return f"{name}.pdf"
    return "alpha_engine_report.pdf"


_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _normalize_iso_date(value: object) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    if text == "":
        return None
    if _DATE_RE.match(text):
        return text
    head = text[:10]
    if _DATE_RE.match(head):
        return head
    return None


def _normalize_expiry(value: object) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        value = value.strip()
        if not value:
            return None
        return value
    if hasattr(value, "strftime"):
        try:
            return value.strftime("%Y-%m-%d")
        except Exception:
            return None
    return None


def _fmt_money(value: object) -> str:
    num = _coerce_float(value)
    if num is None:
        return "--"
    return f"{num:,.2f}"


def _fmt_money_signed(value: object) -> str:
    num = _coerce_float(value)
    if num is None:
        return "--"
    return f"{num:,.2f}"


def _fmt_percent_ratio(value: object, decimals: int = 1) -> str:
    num = _coerce_float(value)
    if num is None:
        return "--"
    return f"{num * 100.0:.{decimals}f}%"


def _fmt_percent_point(value: object, decimals: int = 1) -> str:
    num = _coerce_float(value)
    if num is None:
        return "--"
    return f"{num:.{decimals}f}%"


def _nice_step(min_val: float, max_val: float) -> float:
    span = abs(max_val - min_val)
    if span <= 0:
        return 1.0
    raw = span / 7.0
    mag = 10 ** math.floor(math.log10(raw)) if raw > 0 else 1.0
    norm = raw / mag
    if norm <= 1.5:
        nice = 1.0
    elif norm <= 3.0:
        nice = 2.5
    elif norm <= 7.0:
        nice = 5.0
    else:
        nice = 10.0
    return nice * mag


def _snap_range(req_min: float, req_max: float, step: float) -> tuple[float, float]:
    if step <= 0:
        return req_min, req_max
    snap_min = math.floor(req_min / step) * step
    snap_max = math.ceil(req_max / step) * step
    if snap_min == snap_max:
        snap_max = snap_min + step
    return snap_min, snap_max


def _normalize_spot_result(result: object) -> tuple[float | None, str | None]:
    if isinstance(result, dict):
        spot_value = result.get("spot")
        if spot_value is None:
            spot_value = result.get("px_last")
        if spot_value is None:
            spot_value = result.get("PX_LAST")
        as_of = result.get("as_of") or result.get("ts")
        return _coerce_float(spot_value), str(as_of) if as_of else None
    return _coerce_float(result), None


def _safe_list_strategies(group: str | None, subgroup: str | None = None):
    if not group:
        return None
    try:
        return list_strategies(group, subgroup)
    except Exception:
        return None


def _extract_template_legs(row: dict | None, spot: float) -> list[dict]:
    legs: list[dict] = []
    if not isinstance(row, dict):
        return legs
    for idx in range(1, 5):
        leg_type = row.get(f"leg_{idx}_type")
        leg_side = row.get(f"leg_{idx}_side")
        leg_ratio = row.get(f"leg_{idx}_ratio")
        leg_strike = row.get(f"leg_{idx}_strike")
        if leg_type is None or str(leg_type).strip() == "":
            continue
        leg_type_norm = str(leg_type).strip().upper()
        if leg_type_norm == "STOCK":
            continue
        if leg_type_norm not in {"CALL", "PUT"}:
            continue
        if leg_side is None or str(leg_side).strip() == "":
            continue
        side_norm = str(leg_side).strip().upper()
        sign = 1.0 if side_norm == "LONG" else -1.0
        try:
            ratio = float(leg_ratio)
        except (TypeError, ValueError):
            ratio = 1.0
        kind = "call" if leg_type_norm == "CALL" else "put"
        strike_value = None
        strike_tag = None
        if is_number_like(leg_strike):
            try:
                strike_value = float(leg_strike)
            except (TypeError, ValueError):
                strike_value = None
        else:
            strike_tag = str(leg_strike).strip() if leg_strike is not None else None
        if strike_value is None:
            strike_value = compute_default_strike(spot, strike_tag or "ATM")
        legs.append(
            {
                "kind": kind,
                "side": "Long" if sign > 0 else "Short",
                "qty": abs(ratio),
                "strike": float(strike_value),
                "premium": 0.0,
                "multiplier": 100,
                "override": False,
                "option_ticker": "",
            }
        )
    return legs


def _empty_leg_rows_v1() -> list[dict]:
    """Empty rows in v1 column schema (kind/option_ticker)."""
    return [
        {
            "kind": "",
            "side": "",
            "qty": "",
            "strike": "",
            "premium": "",
            "multiplier": 100,
            "override": False,
            "option_ticker": "",
        }
        for _ in range(4)
    ]


def _empty_leg_rows_v2() -> list[dict]:
    """Empty rows in v2 column schema (type/bbg_ticker)."""
    return [
        {
            "type": "",
            "side": "",
            "qty": "",
            "strike": "",
            "premium": "",
            "override": "",
            "bbg_ticker": "",
        }
        for _ in range(4)
    ]


def _quote_value(quote: dict, keys: list[str]) -> float | None:
    for key in keys:
        if key in quote and quote[key] is not None:
            value = _coerce_float(quote[key])
            if value is not None:
                return value
    return None


def _quote_has_values(quote: dict) -> bool:
    if not isinstance(quote, dict):
        return False
    return (
        _quote_value(
            quote,
            [
                "bid", "BID", "PX_BID",
                "ask", "ASK", "PX_ASK",
                "mid", "MID", "PX_MID",
                "last", "PX_LAST",
            ],
        )
        is not None
    )


def _select_premium_from_quote(quote: dict, position: float, pricing_mode: str) -> float:
    bid = _quote_value(quote, ["bid", "BID", "PX_BID"])
    ask = _quote_value(quote, ["ask", "ASK", "PX_ASK"])
    mid = _quote_value(quote, ["mid", "MID", "PX_MID"])
    last = _quote_value(quote, ["last", "PX_LAST"])
    avg = None
    if bid is not None and ask is not None:
        avg = (bid + ask) / 2.0
    mode = (pricing_mode or "").strip().lower()
    if mode == "mid":
        for value in (mid, avg, bid, ask, last):
            if value is not None:
                return float(value)
        return 0.0
    if position > 0:
        for value in (ask, mid, avg, bid, last):
            if value is not None:
                return float(value)
        return 0.0
    if position < 0:
        for value in (bid, mid, avg, ask, last):
            if value is not None:
                return float(value)
        return 0.0
    for value in (mid, avg, bid, ask, last):
        if value is not None:
            return float(value)
    return 0.0


def _row_position(row: dict) -> float:
    qty = _coerce_float(row.get("qty")) or 0.0
    side = str(row.get("side", "")).strip().lower()
    if side == "short":
        return -qty
    return qty


def _legs_have_content(rows: object) -> bool:
    if not isinstance(rows, list):
        return False
    for row in rows:
        if not isinstance(row, dict):
            continue
        kind = str(row.get("kind", "") or row.get("type", "")).strip().lower()
        strike = row.get("strike")
        opt_ticker = str(row.get("option_ticker", "") or row.get("bbg_ticker", "") or "").strip()
        prem = _coerce_float(row.get("premium"))
        if kind in {"call", "put"} and strike not in (None, ""):
            return True
        if opt_ticker:
            return True
        if prem is not None:
            return True
    return False


def _sort_key_levels(levels: list[dict]) -> list[dict]:
    priority = {
        "spot": 0,
        "strike": 1,
        "breakeven": 2,
        "downside": 3,
        "upside": 4,
        "sentinel": 5,
    }

    def _sort_key(level: dict):
        if not isinstance(level, dict):
            return (0, float("inf"), 6)
        price = _coerce_float(level.get("price"))
        price_key = price if price is not None else float("inf")
        source = str(level.get("source", "")).strip().lower()
        label = str(level.get("label", "")).lower()
        level_id = str(level.get("id", "")).lower()
        is_infinity = level_id == "infinity" or "infinity" in label
        rank = priority.get(source, 6)
        return (1 if is_infinity else 0, price_key, rank)

    return sorted(levels, key=_sort_key)


# ═══════════════════════════════════════════════════════════
# LEG COLUMN ADAPTERS (v1 ↔ v2)
# ═══════════════════════════════════════════════════════════
# v1 schema: kind, side, qty, strike, premium, multiplier, override (bool), option_ticker
# v2 schema: type, side, qty, strike, premium, override ("yes"/"no"), bbg_ticker

def _v1_legs_to_v2(rows: list[dict]) -> list[dict]:
    """Convert v1-schema leg rows to v2-schema for the DataTable."""
    out = []
    for row in rows or []:
        if not isinstance(row, dict):
            out.append(row)
            continue
        v2 = dict(row)
        # kind → type
        if "kind" in v2:
            v2["type"] = v2.pop("kind")
        # option_ticker → bbg_ticker
        if "option_ticker" in v2:
            v2["bbg_ticker"] = v2.pop("option_ticker")
        # override bool → string
        override_val = v2.get("override")
        if isinstance(override_val, bool):
            v2["override"] = "yes" if override_val else "no"
        # remove multiplier (not a v2 column)
        v2.pop("multiplier", None)
        out.append(v2)
    return out


def _v2_legs_to_v1(rows: list[dict]) -> list[dict]:
    """Convert v2-schema leg rows to v1-schema for the analysis engine."""
    out = []
    for row in rows or []:
        if not isinstance(row, dict):
            out.append(row)
            continue
        v1 = dict(row)
        # type → kind
        if "type" in v1 and "kind" not in v1:
            v1["kind"] = v1.pop("type")
        # bbg_ticker → option_ticker
        if "bbg_ticker" in v1 and "option_ticker" not in v1:
            v1["option_ticker"] = v1.pop("bbg_ticker")
        # override string → bool
        override_val = v1.get("override")
        if isinstance(override_val, str):
            v1["override"] = override_val.strip().lower() in {"yes", "y", "true", "1"}
        # add multiplier default
        if "multiplier" not in v1:
            v1["multiplier"] = 100
        out.append(v1)
    return out


# ═══════════════════════════════════════════════════════════
# DMC TABLE HELPER
# ═══════════════════════════════════════════════════════════

def _dmc_table(headers: list[str], rows: list[list]) -> dmc.Table:
    """Build a dmc.Table with TableThead/TableTbody/TableTr/TableTh/TableTd."""
    thead = dmc.TableThead(
        dmc.TableTr([dmc.TableTh(h) for h in headers])
    )
    tbody_rows = []
    for row in rows:
        tbody_rows.append(
            dmc.TableTr([dmc.TableTd(cell if cell is not None else "--") for cell in row])
        )
    tbody = dmc.TableTbody(tbody_rows)
    return dmc.Table(
        [thead, tbody],
        striped=True,
        highlightOnHover=True,
        withTableBorder=True,
        withColumnBorders=True,
        verticalSpacing="xs",
        horizontalSpacing="sm",
    )


def _dmc_table_simple(headers: list[str], rows: list[list]) -> dmc.Table:
    """Build a simpler dmc.Table without column borders."""
    thead = dmc.TableThead(
        dmc.TableTr([dmc.TableTh(h) for h in headers])
    )
    tbody_rows = []
    for row in rows:
        tbody_rows.append(
            dmc.TableTr([dmc.TableTd(str(cell) if cell is not None else "--") for cell in row])
        )
    tbody = dmc.TableTbody(tbody_rows)
    return dmc.Table(
        [thead, tbody],
        withTableBorder=True,
        highlightOnHover=True,
        verticalSpacing="xs",
    )


# ═══════════════════════════════════════════════════════════
# CALLBACK REGISTRATION
# ═══════════════════════════════════════════════════════════

def register_v2_callbacks(
    app,
    cache_get,
    cache_put,
    bloomberg_available: bool,
    bbg_resolve_security=None,
    bbg_fetch_spot=None,
) -> None:
    """Register all v2 dashboard callbacks."""

    # ── #0 Theme toggle ──────────────────────────────────────
    @app.callback(
        Output(ID.MANTINE_PROVIDER, "forceColorScheme"),
        Input(ID.THEME_TOGGLE, "checked"),
        prevent_initial_call=True,
    )
    def _v2_toggle_theme(checked):
        return "light" if checked else "dark"

    # ── #7 Update strategies from group ─────────────────────
    @app.callback(
        Output(ID.STRATEGY_SELECT, "data"),
        Output(ID.STRATEGY_SELECT, "value"),
        Input(ID.GROUP_SELECT, "value"),
        State(ID.STORE_UI, "data"),
    )
    def _v2_update_strategies(group_value, ui_state):
        df = _safe_list_strategies(group_value, None)
        if df is None or df.empty:
            return [], None
        options = [
            {"label": row["strategy_name"], "value": str(int(row["strategy_id"]))}
            for _, row in df.iterrows()
        ]
        stored_group = None
        stored_value = None
        if isinstance(ui_state, dict):
            stored_group = ui_state.get("strategy_group")
            stored_value = ui_state.get("strategy_id")
        # Normalize stored value to string for comparison with dmc.Select string values
        stored_value = str(stored_value) if stored_value is not None else None
        option_values = {opt["value"] for opt in options}
        if stored_group == group_value and stored_value in option_values:
            return options, stored_value
        return options, str(int(df.iloc[0]["strategy_id"]))

    # ── #8 Apply legs updates (strategy template, market quotes, or clear) ──
    @app.callback(
        Output(ID.LEGS_TABLE, "data"),
        Input(ID.STRATEGY_SELECT, "value"),
        Input(ID.STORE_MARKET, "data"),
        Input(ID.BTN_CLEAR, "n_clicks"),
        State(ID.STORE_REF, "data"),
        State(ID.PRICING_MODE, "value"),
        State(ID.LEGS_TABLE, "data"),
        State(ID.STORE_UI, "data"),
        prevent_initial_call=True,
    )
    def _v2_apply_legs_updates(
        strategy_id, market_data, clear_clicks, ref_data, pricing_mode, legs_data, ui_state
    ):
        trigger_id = ctx.triggered_id if ctx else None
        if trigger_id == ID.BTN_CLEAR:
            return [
                {"type": "", "side": "", "qty": "", "strike": "",
                 "premium": "", "override": "", "bbg_ticker": ""}
                for _ in range(3)
            ]
        stored_strategy_id = None
        if isinstance(ui_state, dict):
            stored_strategy_id = ui_state.get("strategy_id")
            try:
                stored_strategy_id = (
                    int(stored_strategy_id) if stored_strategy_id is not None else None
                )
            except (TypeError, ValueError):
                stored_strategy_id = None

        if trigger_id == ID.STORE_MARKET:
            # Market refresh — inject premiums and tickers into existing legs
            if not isinstance(market_data, dict):
                return no_update
            quotes = market_data.get("leg_quotes")
            if not isinstance(quotes, list):
                return no_update
            leg_tickers = market_data.get("leg_tickers")
            if not isinstance(leg_tickers, list):
                leg_tickers = []
            rows = legs_data if isinstance(legs_data, list) else []
            updated_rows = []
            for idx, row in enumerate(rows):
                if not isinstance(row, dict):
                    updated_rows.append(row)
                    continue
                quote = {}
                if idx < len(quotes) and isinstance(quotes[idx], dict):
                    quote = quotes[idx]
                # v2 uses "type" not "kind" — adapt for position calc
                v1_row = _v2_legs_to_v1([row])[0] if isinstance(row, dict) else row
                position = _row_position(v1_row)
                has_quote = _quote_has_values(quote)
                override = _coerce_bool(row.get("override"))
                updated = dict(row)
                if not override and has_quote:
                    premium = _select_premium_from_quote(
                        quote, position, pricing_mode or "mid"
                    )
                    updated["premium"] = abs(float(premium))
                if idx < len(leg_tickers):
                    ticker_value = leg_tickers[idx]
                    if isinstance(ticker_value, str) and ticker_value.strip():
                        updated["bbg_ticker"] = ticker_value
                updated_rows.append(updated)
            return updated_rows

        if trigger_id == ID.STRATEGY_SELECT or trigger_id is None:
            # Strategy change — load template legs
            incoming_strategy_id = None
            try:
                incoming_strategy_id = (
                    int(strategy_id) if strategy_id is not None else None
                )
            except (TypeError, ValueError):
                incoming_strategy_id = None
            rows = legs_data if isinstance(legs_data, list) else None
            if _legs_have_content(rows):
                if (
                    incoming_strategy_id is not None
                    and stored_strategy_id == incoming_strategy_id
                ):
                    return no_update
                if trigger_id is None:
                    return no_update
            if not incoming_strategy_id:
                return no_update
            # Get spot from STORE_REF (not from a spot input — v2 has no editable spot)
            spot = 100.0
            if isinstance(ref_data, dict):
                spot = _coerce_float(ref_data.get("spot")) or 100.0
            strategy_df = get_strategy(incoming_strategy_id)
            row = strategy_df.iloc[0].to_dict() if not strategy_df.empty else None
            template_kind = ""
            if isinstance(row, dict):
                template_kind = str(row.get("template_kind") or "").strip().upper()
            legs = _extract_template_legs(row, spot)
            if template_kind == "STOCK_ONLY" or not legs:
                return _empty_leg_rows_v2()
            if len(legs) < 4:
                legs.extend(_empty_leg_rows_v1()[len(legs):])
            # Convert v1-schema template legs to v2-schema
            return _v1_legs_to_v2(legs[:4])

        return no_update

    # ── #9 Ping spot on ticker commit ────────────────────────
    @app.callback(
        Output(ID.STORE_REF, "data"),
        Input(ID.TICKER_INPUT, "n_submit"),
        Input(ID.TICKER_INPUT, "n_blur"),
        State(ID.TICKER_INPUT, "value"),
        State(ID.STORE_REF, "data"),
        prevent_initial_call=True,
    )
    def _v2_ping_spot(n_submit, n_blur, ticker_value, ref_data):
        raw_ticker = (ticker_value or "").strip()
        if not raw_ticker:
            return no_update
        trigger = ctx.triggered[0]["prop_id"] if ctx and ctx.triggered else ""
        is_submit = trigger.endswith(".n_submit")
        last_ticker = None
        if isinstance(ref_data, dict):
            last_ticker = ref_data.get("raw_ticker")
        if not is_submit and last_ticker == raw_ticker:
            return no_update
        if not bloomberg_available or bbg_resolve_security is None or bbg_fetch_spot is None:
            return no_update
        try:
            resolved = bbg_resolve_security(raw_ticker)
            spot_result = bbg_fetch_spot(resolved)
            spot_value, as_of = _normalize_spot_result(spot_result)
            as_of_text = as_of or _utc_now_str()
            store_ref = {
                "raw_ticker": raw_ticker,
                "resolved_ticker": resolved,
                "spot": spot_value,
                "as_of": as_of_text,
                "status": "ok",
                "error": None,
            }
            return to_jsonable(store_ref)
        except Exception as exc:
            store_ref = {
                "raw_ticker": raw_ticker,
                "resolved_ticker": None,
                "spot": None,
                "as_of": _utc_now_str(),
                "status": "error",
                "error": str(exc),
            }
            return to_jsonable(store_ref)

    # ── #10 Display spot from STORE_REF ──────────────────────
    @app.callback(
        Output(ID.SPOT_DISPLAY, "children"),
        Input(ID.STORE_REF, "data"),
        prevent_initial_call=True,
    )
    def _v2_display_spot(ref_data):
        if not isinstance(ref_data, dict):
            return no_update
        spot = ref_data.get("spot")
        if spot is None:
            return "Spot: —"
        try:
            return f"Spot: {float(spot):,.2f}"
        except (TypeError, ValueError):
            return no_update

    # ── #11 Refresh market data ──────────────────────────────
    @app.callback(
        Output(ID.STORE_MARKET, "data"),
        Output(ID.REFRESH_STATUS, "children"),
        Input(ID.BTN_REFRESH, "n_clicks"),
        State(ID.STORE_REF, "data"),
        State(ID.TICKER_INPUT, "value"),
        State(ID.EXPIRY_SELECT, "value"),
        State(ID.PRICING_MODE, "value"),
        State(ID.LEGS_TABLE, "data"),
        prevent_initial_call=True,
    )
    def _v2_refresh_market(n_clicks, ref_data, ticker_value, expiry, pricing_mode, legs_data):
        raw_ticker = ""
        resolved = None
        if isinstance(ref_data, dict):
            raw_ticker = ref_data.get("raw_ticker") or ""
            resolved = ref_data.get("resolved_ticker")
        if not raw_ticker:
            raw_ticker = (ticker_value or "").strip()
        expiry_value = _normalize_expiry(expiry)
        if not expiry_value:
            status = "Refresh failed: expiry required (YYYY-MM-DD)"
            return no_update, status
        # Convert v2 legs to v1 schema for refresh_leg_premiums
        v1_rows = _v2_legs_to_v1(legs_data if isinstance(legs_data, list) else [])
        _, market_snapshot, status = refresh_leg_premiums(
            raw_underlying=raw_ticker,
            resolved_underlying=resolved,
            expiry=expiry_value,
            legs_rows=v1_rows,
            pricing_mode=pricing_mode or "mid",
        )
        # Fetch vol surface during REFRESH DATA
        if isinstance(market_snapshot, dict):
            try:
                from adapters.bloomberg import fetch_vol_surface
                _resolved = resolved or raw_ticker
                if _resolved:
                    _vol_surface = fetch_vol_surface(_resolved)
                    if _vol_surface is not None:
                        # Store as list of dicts for JSON serialization
                        market_snapshot["_vol_surface_records"] = _vol_surface.to_dict(orient="records")
                        market_snapshot["_vol_surface_expiries"] = sorted(
                            _vol_surface["expiry"].dropna().unique().astype(str).tolist()
                        )
                    else:
                        market_snapshot["_vol_surface_records"] = None
            except Exception as e:
                print(f"[VOL_SURFACE] Error in refresh: {e}")
                market_snapshot["_vol_surface_records"] = None
        return to_jsonable(market_snapshot), status

    # ── #13 Render Bloomberg tab ─────────────────────────────
    @app.callback(
        Output(ID.BBG_REQUEST_SUMMARY, "children"),
        Output(ID.BBG_UNDERLYING_SUMMARY, "children"),
        Output(ID.BBG_UNDERLYING_JSON, "children"),
        Output(ID.BBG_LEG_QUOTES, "data"),
        Output(ID.BBG_ERRORS, "children"),
        Input(ID.STORE_MARKET, "data"),
        Input(ID.STORE_INPUTS, "data"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
        prevent_initial_call=True,
    )
    def _v2_render_bbg_tab(market_data, inputs_data, analysis_key):
        market = market_data if isinstance(market_data, dict) else {}
        inputs = inputs_data if isinstance(inputs_data, dict) else {}

        if not market and not inputs:
            placeholder = dmc.Text(
                "Click REFRESH DATA on the Dashboard tab to load Bloomberg data.",
                size="sm", c="dimmed",
            )
            return placeholder, placeholder, "No data yet", [], placeholder

        # ── REQUEST SUMMARY ──────────────────────────────────
        def _kv_row(label, value):
            """Return a pair of Text elements for a key-value row."""
            display = str(value) if value not in (None, "", "--") else "--"
            return [
                dmc.Text(label, fw=600, size="sm", style={"minWidth": "140px"}),
                dmc.Text(display, size="sm"),
            ]

        ticker_val = inputs.get("resolved_ticker") or inputs.get("ticker") or market.get("resolved_underlying")
        expiry_val = inputs.get("expiry")
        strategy_val = inputs.get("strategy_name")
        pricing_val = inputs.get("pricing_mode")
        refresh_ts = market.get("refreshed_at")
        analysis_ts = inputs.get("timestamp")

        summary_children = dmc.SimpleGrid(
            cols=2, spacing="xs", verticalSpacing=4,
            children=(
                _kv_row("Ticker", ticker_val)
                + _kv_row("Expiry", expiry_val)
                + _kv_row("Strategy", strategy_val)
                + _kv_row("Pricing Mode", pricing_val)
                + _kv_row("Market Refresh", refresh_ts)
                + _kv_row("Analysis Run", analysis_ts)
            ),
        )

        # ── UNDERLYING DATA ──────────────────────────────────
        underlying_profile = market.get("underlying_profile")
        if not isinstance(underlying_profile, dict):
            underlying_profile = {}

        # Normalize keys to uppercase for consistent lookup
        norm = {str(k).upper(): v for k, v in underlying_profile.items()}

        def _pick(keys):
            for k in keys:
                val = underlying_profile.get(k)
                if val not in (None, ""):
                    return val
                upper = k.upper()
                if upper in norm and norm[upper] not in (None, ""):
                    return norm[upper]
            return None

        spot_val = market.get("market_spot") or inputs.get("spot")

        underlying_fields = [
            ("Spot Price", spot_val),
            ("Name", _pick(["name", "NAME", "SECURITY_NAME", "SECURITY_DES"])),
            ("Sector", _pick(["sector", "SECTOR", "GICS_SECTOR_NAME"])),
            ("Dividend Yield", _pick(["DIVIDEND_YIELD", "DVD_YLD", "dividend_yield"])),
            ("Ex-Div Date", _pick(["DVD_EX_DT", "EX_DVD_DT", "ex_div_date"])),
            ("52W High", _pick(["HIGH_52WEEK", "WEEK_52_HIGH", "PX_52W_HIGH"])),
            ("52W Low", _pick(["LOW_52WEEK", "WEEK_52_LOW", "PX_52W_LOW"])),
            ("1D Change %", _pick(["chg_pct_1d", "CHG_PCT_1D"])),
            ("1D Change $", _pick(["chg_net_1d", "CHG_NET_1D"])),
            ("6M ATM IV", _pick(["impvol_6m_atm", "6MTH_IMPVOL_100.0%MNY_DF"])),
            ("UBS Rating", _pick(["ubs_rating", "BEST_ANALYST_REC", "UBS_RATING"])),
            ("UBS Target", _pick(["ubs_target", "BEST_TARGET_PRICE", "UBS_TARGET"])),
            ("200D MA", _pick(["mov_avg_200d", "MOV_AVG_200D"])),
            ("Risk-Free Rate", _pick(["risk_free_rate", "RISK_FREE_RATE"])),
        ]

        # Append dividend schedule info from analysis pack if available
        ak = analysis_key if isinstance(analysis_key, dict) else {}
        ak_key = ak.get("key")
        if ak_key:
            ak_pack = cache_get(ak_key)
            if isinstance(ak_pack, dict):
                div_sched = ak_pack.get("dividend_schedule")
                if isinstance(div_sched, dict):
                    underlying_fields.append(
                        ("Dividends to Expiry", div_sched.get("dividend_sum"))
                    )
                    underlying_fields.append(
                        ("# Div Payments", div_sched.get("dividend_count"))
                    )

        # Build as a dmc.Table with two columns
        underlying_rows = []
        for label, value in underlying_fields:
            display = str(value) if value not in (None, "", "--") else "--"
            underlying_rows.append(
                dmc.TableTr([
                    dmc.TableTd(dmc.Text(label, fw=600, size="sm")),
                    dmc.TableTd(dmc.Text(display, size="sm")),
                ])
            )
        if underlying_rows:
            underlying_output = dmc.Table(
                [dmc.TableTbody(underlying_rows)],
                striped=True, highlightOnHover=True,
                style={"maxWidth": "400px"},
            )
        else:
            underlying_output = dmc.Text("No underlying data.", size="sm", c="dimmed")

        # ── LEG QUOTES ───────────────────────────────────────
        leg_quotes = market.get("leg_quotes")
        if not isinstance(leg_quotes, list):
            leg_quotes = []
        leg_tickers = market.get("leg_tickers")
        if not isinstance(leg_tickers, list):
            leg_tickers = []
        input_legs = inputs.get("legs")
        if not isinstance(input_legs, list):
            input_legs = []

        def _fmt_num(val, decimals=2):
            if val is None:
                return "--"
            try:
                return f"{float(val):.{decimals}f}"
            except (TypeError, ValueError):
                return str(val)

        def _fmt_pct(val):
            if val is None:
                return "--"
            try:
                return f"{float(val):.1f}%"
            except (TypeError, ValueError):
                return str(val)

        def _quote_field(quote, keys):
            for k in keys:
                if k in quote and quote[k] is not None:
                    return quote[k]
            return None

        row_count = max(len(leg_quotes), len(leg_tickers), len(input_legs))
        quote_rows = []
        for idx in range(row_count):
            quote = leg_quotes[idx] if idx < len(leg_quotes) and isinstance(leg_quotes[idx], dict) else {}
            ticker = leg_tickers[idx] if idx < len(leg_tickers) else None
            input_leg = input_legs[idx] if idx < len(input_legs) and isinstance(input_legs[idx], dict) else {}

            # Get type and strike from input legs
            leg_type = input_leg.get("type") or input_leg.get("kind") or "--"
            strike = input_leg.get("strike")

            # Compute OTM% if we have spot and strike
            otm_pct = None
            if strike is not None and spot_val is not None:
                try:
                    s = float(spot_val)
                    k = float(strike)
                    if s > 0:
                        otm_pct = abs(k - s) / s * 100
                except (TypeError, ValueError):
                    pass

            row = {
                "leg": f"Leg {idx + 1}",
                "type": str(leg_type).capitalize() if leg_type != "--" else "--",
                "strike": _fmt_num(strike),
                "bid": _fmt_num(_quote_field(quote, ["bid", "BID", "PX_BID"])),
                "ask": _fmt_num(_quote_field(quote, ["ask", "ASK", "PX_ASK"])),
                "mid": _fmt_num(_quote_field(quote, ["mid", "MID", "PX_MID"])),
                "iv": _fmt_pct(_quote_field(quote, ["iv", "IVOL_MID", "IV_MID", "iv_mid"])),
                "delta": _fmt_num(_quote_field(quote, ["delta", "DELTA_MID_RT", "delta_mid"]), 4),
                "otm_pct": _fmt_pct(otm_pct),
                "bbg_ticker": ticker or "--",
            }
            quote_rows.append(row)

        # ── ERRORS ───────────────────────────────────────────
        errors = market.get("errors")
        if not isinstance(errors, list):
            errors = []
        if errors:
            error_items = [dmc.ListItem(dmc.Text(str(e), size="sm")) for e in errors]
            errors_output = dmc.List(error_items, type="unordered", size="sm",
                                     styles={"item": {"color": "var(--mantine-color-red-6)"}})
        else:
            errors_output = dmc.Text("No errors", c="green", size="sm")

        # ── RAW JSON ─────────────────────────────────────────
        raw = {
            "market_data": market,
            "inputs_snapshot": inputs,
        }
        raw_json_text = json.dumps(raw, indent=2, default=str)

        return (
            summary_children,      # BBG_REQUEST_SUMMARY
            underlying_output,     # BBG_UNDERLYING_SUMMARY
            raw_json_text,         # BBG_UNDERLYING_JSON
            quote_rows,            # BBG_LEG_QUOTES
            errors_output,         # BBG_ERRORS
        )

    # ── #14 Download market JSON ─────────────────────────────
    # (no export button in v2 bloomberg tab yet — wire to a future button)
    # For now, skip this callback; the DL_MARKET_JSON component exists but
    # has no trigger. We can add a button later if needed.

    # ── #15 Download PDF report ──────────────────────────────
    # Single trigger: dashboard GENERATE PDF REPORT button.
    @app.callback(
        Output(ID.DL_REPORT_PDF, "data"),
        Output(ID.REPORT_STATUS, "children"),
        Output(ID.LOG_STORE, "data"),
        Input(ID.BTN_PDF, "n_clicks"),
        State(ID.STORE_UI, "data"),
        State(ID.STORE_INPUTS, "data"),
        State(ID.STORE_MARKET, "data"),
        State(ID.STORE_ANALYSIS_KEY, "data"),
        State(ID.FA_NAME_INPUT, "value"),
        State(ID.ACCT_NUMBER_INPUT, "value"),
        State(ID.FA_ID_INPUT, "value"),
        prevent_initial_call=True,
    )
    def _v2_download_report_pdf(
        n_clicks_report, ui_state, inputs_state, market_data, key_payload,
        fa_name_val, acct_number_val, fa_id_val,
    ):
        if not n_clicks_report:
            return no_update, no_update, no_update
        if not isinstance(key_payload, dict) or key_payload.get("error"):
            return no_update, "Run Analysis first to generate a report.", no_update
        key = key_payload.get("key")
        pack = cache_get(key) if key else None
        if not pack:
            return no_update, "Run Analysis first to generate a report.", no_update
        try:
            from reporting.report_model import build_report_model
            from reporting.html_v2.renderer import build_report_pdf_html

            inputs_store = inputs_state if isinstance(inputs_state, dict) else {}
            ui_store = ui_state if isinstance(ui_state, dict) else {}
            market = market_data if isinstance(market_data, dict) else {}

            state = {
                "underlying_snapshot": market.get("underlying_profile") or {},
                "analysis_pack": pack,
                "resolved_underlying": market.get("resolved_underlying")
                or inputs_store.get("resolved_ticker"),
                "underlying_ticker": inputs_store.get("resolved_ticker")
                or inputs_store.get("ticker")
                or ui_store.get("ticker"),
                "spot": inputs_store.get("spot") or ui_store.get("spot"),
                "stock_position": inputs_store.get("stock_position")
                or ui_store.get("stock_position"),
                "avg_cost": inputs_store.get("avg_cost") or ui_store.get("avg_cost"),
                "pricing_mode": inputs_store.get("pricing_mode")
                or ui_store.get("pricing_mode"),
                "roi_policy": inputs_store.get("roi_policy") or ui_store.get("roi_policy"),
                "vol_mode": inputs_store.get("vol_mode") or ui_store.get("vol_mode"),
                "expiry": inputs_store.get("expiry") or ui_store.get("expiry"),
                "legs": inputs_store.get("legs") or [],
                "cio_rating": inputs_store.get("cio_rating") or ui_store.get("cio_rating"),
            }

            report_model = build_report_model(state)
            _payload_with_ticker = dict(key_payload) if isinstance(key_payload, dict) else {}
            _payload_with_ticker["ticker"] = (
                inputs_store.get("resolved_ticker")
                or inputs_store.get("ticker")
                or ui_store.get("ticker")
                or ""
            )
            # Add "Equity" if needed
            _t = _payload_with_ticker["ticker"]
            if _t and "equity" not in _t.lower():
                _payload_with_ticker["ticker"] = f"{_t} Equity"
            filename = _report_filename(_payload_with_ticker, pack)

            try:
                payload = build_report_pdf_html(report_model)
            except Exception as exc:
                traceback.print_exc()
                return no_update, f"PDF export error: {type(exc).__name__}: {exc}", no_update

            # Log activity entry
            try:
                _log_summary = pack.get("summary") or {}
                _log_rows = _log_summary.get("rows") or []
                _max_profit = _log_rows[0].get("options", "--") if len(_log_rows) > 0 else "--"
                _max_loss = _log_rows[1].get("options", "--") if len(_log_rows) > 1 else "--"
                _net_premium = _log_summary.get("net_premium_total", "--")

                _log_legs = inputs_store.get("legs") or []
                _contracts = sum(
                    abs(float(lg.get("position", 0))) for lg in _log_legs if isinstance(lg, dict)
                )

                _strategy_name = ""
                _pack_strategy = pack.get("strategy") or {}
                if isinstance(_pack_strategy, dict):
                    _strategy_name = _pack_strategy.get("name") or _pack_strategy.get("strategy_name") or ""
                if not _strategy_name:
                    _strategy_name = inputs_store.get("strategy_id") or ""

                append_entry({
                    "fa_name": fa_name_val or "",
                    "acct_number": acct_number_val or "",
                    "fa_id": fa_id_val or "",
                    "ticker": inputs_store.get("resolved_ticker") or inputs_store.get("ticker") or "",
                    "strategy": _strategy_name,
                    "expiry": inputs_store.get("expiry") or "",
                    "contracts": str(int(_contracts)) if _contracts else "",
                    "net_premium": str(_net_premium),
                    "max_profit": str(_max_profit),
                    "max_loss": str(_max_loss),
                })
            except Exception:
                pass  # never fail PDF delivery due to logging

            _log_trigger = {"ts": _utc_now_str()}
            return (
                dcc.send_bytes(payload, filename=filename),
                "PDF generated.",
                _log_trigger,
            )
        except Exception as exc:
            traceback.print_exc()
            return no_update, f"PDF export error: {type(exc).__name__}: {exc}", no_update

    # ── #15b Auto-select Excel template from strategy ────────
    @app.callback(
        Output(ID.EXCEL_TEMPLATE_SELECT, "value"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
        State(ID.STORE_INPUTS, "data"),
        prevent_initial_call=True,
    )
    def _v2_auto_select_excel_template(key_payload, inputs_state):
        """When analysis completes, auto-select the matching Excel template."""
        if not isinstance(inputs_state, dict):
            return no_update
        strategy_id = inputs_state.get("strategy_id")
        if not strategy_id:
            return no_update
        try:
            from reporting.excel_templates.registry import get_template_for_strategy
            config = get_template_for_strategy(str(strategy_id))
            if config:
                return config["template_key"]
        except Exception:
            pass
        return no_update

    # ── #15c Generate Excel PDF ──────────────────────────────
    def _build_option_ticker(underlying, expiry, kind, strike):
        """Build Bloomberg-format option ticker: 'MSFT US 03/20/26 C420 Equity'."""
        if not all([underlying, expiry, kind, strike]):
            return ""
        try:
            from datetime import date as _date
            d = _date.fromisoformat(str(expiry)[:10])
            date_str = d.strftime("%m/%d/%y")
        except (ValueError, TypeError):
            date_str = str(expiry)
        kind_letter = "C" if str(kind).upper().startswith("C") else "P"
        try:
            s = float(strike)
            strike_str = str(int(s)) if s == int(s) else f"{s:.2f}"
        except (ValueError, TypeError):
            strike_str = str(strike)
        base = str(underlying).replace(" Equity", "").replace(" equity", "")
        return f"{base} {date_str} {kind_letter}{strike_str} Equity"

    @app.callback(
        Output(ID.DL_EXCEL_PDF, "data"),
        Output(ID.EXCEL_STATUS, "children"),
        Input(ID.BTN_EXCEL_PDF, "n_clicks"),
        State(ID.EXCEL_TEMPLATE_SELECT, "value"),
        State(ID.STORE_ANALYSIS_KEY, "data"),
        State(ID.STORE_INPUTS, "data"),
        State(ID.STORE_MARKET, "data"),
        State(ID.STORE_UI, "data"),
        prevent_initial_call=True,
    )
    def _v2_generate_excel_pdf(
        n_clicks, template_key, key_payload, inputs_state, market_data, ui_state,
    ):
        import os

        if not n_clicks:
            return no_update, no_update

        # ── Validate prerequisites ──
        if not template_key:
            return no_update, "Select an Excel template first."

        if not isinstance(key_payload, dict) or key_payload.get("error"):
            return no_update, "Run Analysis first."

        key = key_payload.get("key")
        pack = cache_get(key) if key else None
        if not pack:
            return no_update, "Run Analysis first."

        inputs_store = inputs_state if isinstance(inputs_state, dict) else {}
        ui_store = ui_state if isinstance(ui_state, dict) else {}

        # ── Build meta dict (bridges dashboard inputs → template cells) ──
        legs = inputs_store.get("legs") or []
        meta = {
            "underlying_ticker": (
                inputs_store.get("resolved_ticker")
                or inputs_store.get("ticker")
                or ui_store.get("ticker")
                or ""
            ),
            "option_ticker_leg1": "",
            "option_ticker_leg2": "",
            "contracts_leg1": 0,
            "shares": inputs_store.get("stock_position") or ui_store.get("stock_position") or 0,
            "cio_rating": inputs_store.get("cio_rating") or ui_store.get("cio_rating") or "",
        }

        # Extract leg tickers and contracts from legs array
        if len(legs) > 0 and isinstance(legs[0], dict):
            meta["option_ticker_leg1"] = (
                legs[0].get("bbg_ticker") or legs[0].get("option_ticker") or ""
            )
            try:
                meta["contracts_leg1"] = abs(int(float(legs[0].get("position") or legs[0].get("qty") or 0)))
            except (ValueError, TypeError):
                pass
        if len(legs) > 1 and isinstance(legs[1], dict):
            meta["option_ticker_leg2"] = (
                legs[1].get("bbg_ticker") or legs[1].get("option_ticker") or ""
            )

        # Construct option tickers from components if not available from BBG
        expiry_val = inputs_store.get("expiry") or ui_store.get("expiry") or ""
        if not meta["option_ticker_leg1"] and len(legs) > 0 and isinstance(legs[0], dict):
            meta["option_ticker_leg1"] = _build_option_ticker(
                meta["underlying_ticker"], expiry_val,
                legs[0].get("type") or legs[0].get("kind") or "",
                legs[0].get("strike") or 0,
            )
        if not meta["option_ticker_leg2"] and len(legs) > 1 and isinstance(legs[1], dict):
            meta["option_ticker_leg2"] = _build_option_ticker(
                meta["underlying_ticker"], expiry_val,
                legs[1].get("type") or legs[1].get("kind") or "",
                legs[1].get("strike") or 0,
            )

        try:
            # ── Step 1: Fill template ──
            from reporting.excel_templates.filler import fill_template
            filled_path = fill_template(template_key, pack, meta)
            if not filled_path:
                return no_update, "Template fill failed — check template file exists."

            # ── Step 2: Export PDF via Excel ──
            from reporting.excel_templates.pdf_exporter import export_pdf
            from reporting.excel_templates.registry import get_template_config
            config = get_template_config(template_key)
            output_sheet = config.get("output_sheet") if config else None

            pdf_path = export_pdf(
                filled_path,
                output_sheet=output_sheet,
                visible=False,
                timeout_seconds=45,
            )

            if not pdf_path or not os.path.isfile(pdf_path):
                return no_update, "PDF export failed — is Excel installed?"

            # ── Step 3: Return as download ──
            # Build filename: "2026-02-09_MSFT US Equity_Covered Call.pdf"
            as_of = pack.get("as_of", "report")
            ticker_raw = meta["underlying_ticker"]  # e.g. "MSFT US"
            # Add "Equity" suffix if not present
            if ticker_raw and "equity" not in ticker_raw.lower():
                ticker_display = f"{ticker_raw} Equity"
            else:
                ticker_display = ticker_raw

            # Get strategy display name from the pack
            strategy_name = ""
            pack_strategy = pack.get("strategy") or {}
            if isinstance(pack_strategy, dict):
                strategy_name = pack_strategy.get("name") or pack_strategy.get("strategy_name") or ""
            if not strategy_name:
                # Fall back to template key cleaned up
                strategy_name = template_key.replace("template_", "").replace("_", " ").title()

            filename = f"{as_of}_{ticker_display}_{strategy_name}.pdf"
            # Clean any chars that aren't safe for filenames
            filename = re.sub(r'[<>:"/\\|?*]+', "", filename)

            with open(pdf_path, "rb") as f:
                pdf_bytes = f.read()

            # Clean up temp files
            try:
                os.remove(filled_path)
                os.remove(pdf_path)
            except OSError:
                pass

            return dcc.send_bytes(pdf_bytes, filename=filename), f"Excel PDF generated: {filename}"

        except ImportError as exc:
            return no_update, f"Missing dependency: {exc} (requires Windows + Excel)"
        except FileNotFoundError as exc:
            return no_update, f"Template not found: {exc}"
        except Exception as exc:
            traceback.print_exc()
            return no_update, f"Excel PDF error: {type(exc).__name__}: {exc}"

    # ── #16 Run analysis ─────────────────────────────────────
    @app.callback(
        Output(ID.STORE_ANALYSIS_KEY, "data"),
        Output(ID.STORE_INPUTS, "data"),
        Input(ID.BTN_ANALYZE, "n_clicks"),
        State(ID.STORE_REF, "data"),
        State(ID.TICKER_INPUT, "value"),
        State(ID.EXPIRY_SELECT, "value"),
        State(ID.SHARES_INPUT, "value"),
        State(ID.AVG_COST_INPUT, "value"),
        State(ID.LEGS_TABLE, "data"),
        State(ID.PRICING_MODE, "value"),
        State(ID.PREMIUM_MODE, "value"),
        State(ID.SCENARIO_MODE, "value"),
        State(ID.DOWNSIDE_TARGET, "value"),
        State(ID.UPSIDE_TARGET, "value"),
        State(ID.GROUP_SELECT, "value"),
        State(ID.STRATEGY_SELECT, "value"),
        State(ID.STORE_MARKET, "data"),
        State(ID.CIO_RATING_INPUT, "value"),
        prevent_initial_call=True,
    )
    def _v2_run_analysis(
        n_clicks,
        ref_data,
        ticker_value,
        expiry,
        stock_position,
        avg_cost,
        legs_table,
        pricing_mode,
        roi_policy,
        scenario_mode,
        downside_pct,
        upside_pct,
        group_value,
        strategy_id,
        market_data,
        cio_rating,
    ):
        raw_ticker = (ticker_value or "").strip()
        resolved_ticker = raw_ticker
        if isinstance(ref_data, dict):
            raw_ticker = ref_data.get("raw_ticker") or raw_ticker
            resolved_ticker = ref_data.get("resolved_ticker") or resolved_ticker

        # Spot from STORE_REF (v2 has no editable spot input)
        spot = 0.0
        if isinstance(ref_data, dict):
            spot = _coerce_float(ref_data.get("spot")) or 0.0

        expiry_value = _normalize_expiry(expiry)
        stock_pos = _coerce_float(stock_position) or 0.0
        avg_cost_val = _coerce_float(avg_cost) or 0.0

        # Convert v2 legs to v1 schema for the engine
        v2_rows = legs_table if isinstance(legs_table, list) else []
        v1_rows = _v2_legs_to_v1(v2_rows)

        legs: list[OptionLeg] = []
        for row in v1_rows:
            if not isinstance(row, dict):
                continue
            kind = str(row.get("kind", "")).strip().lower()
            if kind not in {"call", "put"}:
                continue
            strike = _coerce_float(row.get("strike"))
            premium = _coerce_float(row.get("premium"))
            position = _row_position(row)
            multiplier = _coerce_float(row.get("multiplier")) or 100.0
            if strike is None or premium is None or position == 0.0:
                continue
            legs.append(
                OptionLeg(
                    kind=kind,
                    position=float(position),
                    strike=float(strike),
                    premium=abs(float(premium)),
                    multiplier=int(multiplier),
                )
            )

        scenario_mode_ui = (scenario_mode or "targets").strip().lower()
        scenario_mode_backend = (
            "INFINITY" if scenario_mode_ui == "infinity" else "targets"
        )

        inputs_snapshot = {
            "ticker": raw_ticker,
            "raw_ticker": raw_ticker,
            "resolved_ticker": resolved_ticker,
            "spot": spot,
            "expiry": expiry_value,
            "stock_position": stock_pos,
            "avg_cost": avg_cost_val,
            "legs": [to_jsonable(row) for row in v1_rows],
            "pricing_mode": pricing_mode,
            "roi_policy": roi_policy,
            "vol_mode": "atm",  # updated below after vol surface extraction
            "atm_iv": 0.2,  # updated below after vol surface extraction
            "scenario_mode": scenario_mode_ui,
            "scenario_mode_backend": scenario_mode_backend,
            "downside_pct": downside_pct,
            "upside_pct": upside_pct,
            "strategy_group": group_value,
            "strategy_subgroup": None,
            "strategy_id": strategy_id,
            "cio_rating": cio_rating,
        }

        net_premium = 0.0
        for leg in legs:
            net_premium += leg.position * leg.premium
        net_premium_per_share = -net_premium
        roi_policy_ui = (roi_policy or "premium").strip().lower()
        roi_policy_effective = roi_policy_ui
        warning_msg = None
        if roi_policy_ui == "premium" and abs(net_premium_per_share) < 1e-9:
            roi_policy_effective = "max_loss"
            warning_msg = (
                "Premium ROI selected but net premium is 0; computing ROI using Max Loss."
            )

        roi_map = {
            "premium": "NET_PREMIUM",
            "max_loss": "RISK_MAX_LOSS",
            "cash_secured": "CASH_SECURED",
            "margin": "MARGIN_PROXY",
        }
        roi_backend = roi_map.get(roi_policy_effective, "NET_PREMIUM")
        inputs_snapshot["roi_policy_ui"] = roi_policy_ui
        inputs_snapshot["roi_policy_effective"] = roi_policy_effective
        inputs_snapshot["roi_policy_backend"] = roi_backend

        downside_factor = 1.0 + ((downside_pct or 0.0) / 100.0)
        upside_factor = 1.0 + ((upside_pct or 0.0) / 100.0)
        downside_factor = max(downside_factor, 1e-6)
        upside_factor = max(upside_factor, 1e-6)

        strategy_meta = {
            "as_of": _utc_now_str(),
            "expiry": expiry_value,
            "underlying_ticker": raw_ticker,
            "resolved_underlying": resolved_ticker,
            "strategy_name": "",
            "strategy_id": strategy_id,
            "group": group_value,
            "subgroup": None,
        }
        if strategy_id:
            row = get_strategy(strategy_id)
            if row is not None and not row.empty:
                strategy_meta["strategy_name"] = str(row.iloc[0]["strategy_name"])
                strategy_meta["strategy_id"] = int(row.iloc[0]["strategy_id"])

        underlying_profile = {}
        bbg_leg_snapshots = None
        if isinstance(market_data, dict):
            underlying_profile = market_data.get("underlying_profile") or {}
            per_leg_iv = market_data.get("per_leg_iv")
            leg_quotes = market_data.get("leg_quotes")
            if per_leg_iv is not None or leg_quotes is not None:
                bbg_leg_snapshots = {"per_leg_iv": per_leg_iv, "leg_quotes": leg_quotes}

        # Extract tenor-matched ATM IV from vol surface (if available from REFRESH)
        _atm_iv_from_surface = None
        if isinstance(market_data, dict) and market_data.get("_vol_surface_records"):
            try:
                from adapters.bloomberg import extract_atm_iv_for_expiry
                _vol_surface_df = pd.DataFrame(market_data["_vol_surface_records"])
                _vol_surface_df["expiry"] = pd.to_datetime(_vol_surface_df["expiry"], errors="coerce")
                if expiry_value and spot > 0:
                    _atm_iv_from_surface = extract_atm_iv_for_expiry(
                        _vol_surface_df, expiry_value, spot
                    )
            except Exception as e:
                print(f"[VOL_SURFACE] ATM IV extraction failed: {e}")

        # Use surface ATM IV if available, otherwise fall back to BDP 3M ATM IV
        if _atm_iv_from_surface is not None:
            _effective_atm_iv = _atm_iv_from_surface / 100.0  # convert pct to decimal
            _effective_vol_mode = "surface_atm"
        else:
            # Fallback to 3M ATM IV from underlying profile
            _3m_iv = None
            if isinstance(underlying_profile, dict):
                for k in ["impvol_3m_atm", "3MTH_IMPVOL_100.0%MNY_DF", "IMPVOL_3M_ATM"]:
                    v = underlying_profile.get(k)
                    if v is not None:
                        try:
                            _3m_iv = float(v)
                            break
                        except (TypeError, ValueError):
                            pass
            _effective_atm_iv = (_3m_iv / 100.0) if _3m_iv else 0.2
            _effective_vol_mode = "atm"

        # Update inputs snapshot with resolved vol values
        inputs_snapshot["vol_mode"] = _effective_vol_mode
        inputs_snapshot["atm_iv"] = _effective_atm_iv
        inputs_snapshot["atm_iv_from_surface_pct"] = _atm_iv_from_surface

        # Fetch risk-free rate from Bloomberg treasury indices
        rfr = 0.0
        treasury_label = ""
        if expiry_value:
            try:
                from adapters.bloomberg import fetch_risk_free_rate as _fetch_rfr
                from datetime import date as _date
                exp_date = _date.fromisoformat(str(expiry_value)[:10])
                dte = (exp_date - _date.today()).days
                if dte > 0:
                    rfr_info = _fetch_rfr(dte)
                    rfr = rfr_info["rate"]
                    treasury_label = rfr_info.get("label", "")
            except Exception:
                rfr = 0.0

        try:
            strategy_input = StrategyInput(
                spot=spot,
                stock_position=stock_pos,
                avg_cost=avg_cost_val,
                legs=legs,
            )
            pack = build_analysis_pack(
                strategy_input=strategy_input,
                strategy_meta=strategy_meta,
                pricing_mode=pricing_mode or "mid",
                roi_policy=roi_backend,
                vol_mode=_effective_vol_mode,
                atm_iv=_effective_atm_iv,
                underlying_profile=underlying_profile,
                bbg_leg_snapshots=bbg_leg_snapshots,
                scenario_mode=scenario_mode_backend,
                downside_tgt=downside_factor,
                upside_tgt=upside_factor,
                risk_free_rate=rfr,
                treasury_label=treasury_label,
            )
        except Exception as exc:
            return {"key": None, "as_of": _utc_now_str(), "error": str(exc)}, to_jsonable(
                inputs_snapshot
            )

        # Populate dividend schedule from Bloomberg (needs expiry)
        if expiry_value:
            try:
                from adapters.bloomberg import fetch_dividend_sum_to_expiry
                from datetime import date as _date2
                expiry_parsed = None
                try:
                    expiry_parsed = _date2.fromisoformat(str(expiry_value)[:10])
                except (ValueError, TypeError):
                    pass
                if expiry_parsed:
                    div_ticker = resolved_ticker or raw_ticker
                    div_schedule = fetch_dividend_sum_to_expiry(
                        ticker=div_ticker,
                        expiry_date=expiry_parsed,
                    )
                    pack["dividend_schedule"] = div_schedule
            except Exception as e:
                print(f"[DIV_SCHEDULE] Error: {e}")

        key = cache_put(pack)
        key_payload = {
            "key": key,
            "as_of": _utc_now_str(),
            "error": None,
            "roi_policy_ui": roi_policy_ui,
            "roi_policy_effective": roi_policy_effective,
        }
        if warning_msg:
            key_payload["warning"] = warning_msg
        return key_payload, to_jsonable(inputs_snapshot)

    # ── #17 Render payoff chart ──────────────────────────────
    @app.callback(
        Output(ID.PAYOFF_CHART, "figure"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
        Input(ID.TABS, "value"),
        Input(ID.THEME_TOGGLE, "checked"),
        Input(ID.CHK_OPTIONS, "checked"),
        Input(ID.CHK_STOCK, "checked"),
        Input(ID.CHK_COMBINED, "checked"),
        Input(ID.CHK_BE_OPTIONS, "checked"),
        Input(ID.CHK_BE_COMBINED, "checked"),
    )
    def _v2_render_chart(key_payload, tab_value, checked, chk_options, chk_stock, chk_combined, chk_be_options, chk_be_combined):
        if tab_value != "dashboard":
            raise PreventUpdate
        fig = go.Figure()
        # Trace visibility from checkboxes
        show_options = bool(chk_options)
        show_stock = bool(chk_stock)
        show_combined = bool(chk_combined)
        show_strikes = True

        # Theme-aware chart colors
        is_light = bool(checked)
        if is_light:
            _paper_bg = "rgba(255,255,255,0)"
            _plot_bg = "rgba(246,248,250,0.8)"
            _font_color = "#1F2328"
            _grid_color = "#D0D7DE"
            _zero_line_color = "#656D76"
            _template = "plotly_white"
        else:
            _paper_bg = "#1C2128"
            _plot_bg = "#1C2128"
            _font_color = "#E6EDF3"
            _grid_color = "#21262D"
            _zero_line_color = "#8B949E"
            _template = "plotly_dark"


        def _empty_chart(title=None, annotation=None):
            """Return an empty themed figure for early-return cases."""
            f = go.Figure()
            layout_kw = dict(
                template=_template,
                paper_bgcolor=_paper_bg,
                plot_bgcolor=_plot_bg,
                font={"color": _font_color},
            )
            if title:
                layout_kw["title"] = title
            f.update_layout(**layout_kw)
            if annotation:
                hint_color = "#656D76" if is_light else "#6C7589"
                f.add_annotation(
                    text=annotation,
                    xref="paper", yref="paper", x=0.5, y=0.5,
                    showarrow=False, font={"size": 14, "color": hint_color},
                )
            return f

        if not isinstance(key_payload, dict) or key_payload.get("error"):
            if isinstance(key_payload, dict) and key_payload.get("error"):
                return _empty_chart(title=f"Analysis error: {key_payload['error']}")
            return _empty_chart(annotation="Run analysis to see payoff diagram")
        pack = cache_get(key_payload.get("key"))
        if not pack:
            return _empty_chart(title="Analysis expired; rerun")
        pack_store = analysis_pack_to_store(pack)
        payoff = pack_store.get("payoff") if isinstance(pack_store, dict) else None
        if not isinstance(payoff, dict):
            return _empty_chart(title="No payoff data in analysis_pack")
        x = payoff.get("price_grid") or []
        options = payoff.get("options_pnl") or []
        stock = payoff.get("stock_pnl") or []
        combined = payoff.get("combined_pnl") or []
        if not x:
            return _empty_chart(title="No payoff data in analysis_pack")

        def _numeric_list(values):
            items = []
            for value in values or []:
                num = _coerce_float(value)
                if num is not None:
                    items.append(num)
            return sorted(set(items))

        # ── X-axis scaling: spot + strikes only (not breakevens) ──
        x_vals = [_coerce_float(v) for v in x]
        x_pairs = [v for v in x_vals if v is not None]
        underlying = pack_store.get("underlying") if isinstance(pack_store, dict) else {}
        spot = None
        if isinstance(underlying, dict):
            spot = _coerce_float(underlying.get("spot"))

        strike_vals = _numeric_list(payoff.get("strikes"))
        be_vals = _numeric_list(payoff.get("breakevens"))

        if x_pairs:
            if spot and spot > 0:
                range_prices = [p for p in [spot] + strike_vals if p and p > 0]
                if not range_prices:
                    range_prices = [spot]
                price_min = min(range_prices)
                price_max = max(range_prices)
                price_spread = price_max - price_min

                # Minimum spread: 10% of spot
                min_spread = spot * 0.10
                if price_spread < min_spread:
                    mid = (price_min + price_max) / 2
                    price_min = mid - min_spread / 2
                    price_max = mid + min_spread / 2
                    price_spread = min_spread

                # Padding: 15% each side
                padding = price_spread * 0.15
                x_min_req = max(0, price_min - padding)
                x_max_req = price_max + padding
            else:
                x_min_req = min(x_pairs)
                x_max_req = max(x_pairs)
            x_step = _nice_step(x_min_req, x_max_req)
            x_min, x_max = _snap_range(x_min_req, x_max_req, x_step)
            x_range_span = x_max - x_min if x_max > x_min else 1.0

        # Add traces with full data range (0 to 3×spot) — user can pan/zoom
        if show_stock and len(stock) == len(x):
            fig.add_trace(go.Scatter(
                x=x, y=stock, name="Stock PnL",
                line={"color": "#6E7681", "width": 1.5, "dash": "dash"},
            ))
        if show_options and len(options) == len(x):
            fig.add_trace(go.Scatter(
                x=x, y=options, name="Options PnL",
                line={"color": "#2563EB", "width": 2.5},
            ))
        if show_combined and len(combined) == len(x):
            fig.add_trace(go.Scatter(
                x=x, y=combined, name="Combined PnL",
                line={"color": "#7C3AED", "width": 3},
            ))

        if x_pairs:
            # ── Annotations: strikes below chart, breakevens above ──
            ann_x_positions = []

            def _offset_x(xpos):
                """Nudge annotation if too close to an existing one."""
                for existing in ann_x_positions:
                    if abs(xpos - existing) / x_range_span < 0.05:
                        xpos += 0.03 * x_range_span
                        break
                ann_x_positions.append(xpos)
                return xpos

            if show_strikes:
                for strike in strike_vals:
                    fig.add_vline(
                        x=strike, line_dash="dot",
                        line_color="#EF4444", line_width=1, opacity=0.5,
                    )
                    fig.add_annotation(
                        x=_offset_x(strike), yref="paper", y=-0.03,
                        yanchor="top", text=f"K ${strike:,.0f}",
                        showarrow=False, font={"size": 10, "color": "#EF4444"},
                    )
            # Options-only breakevens (computed from options_pnl)
            if chk_be_options:
                opt_be_vals = _detect_breakevens(
                    [v for v in x if isinstance(v, (int, float))],
                    [v for v in options if isinstance(v, (int, float))],
                ) if len(options) == len(x) else []
                for be in opt_be_vals:
                    fig.add_vline(
                        x=be, line_dash="dash",
                        line_color="#2DD4BF", line_width=1,
                        annotation_text=f"OBE ${be:,.2f}",
                        annotation_position="top",
                        annotation_font_color="#2DD4BF",
                        annotation_font_size=11,
                    )
            # Combined breakevens (from analysis pack)
            if chk_be_combined:
                for be in be_vals:
                    fig.add_vline(
                        x=be, line_dash="dash",
                        line_color="#F0B429", line_width=1,
                        annotation_text=f"BE ${be:,.2f}",
                        annotation_position="top",
                        annotation_font_color="#F0B429",
                        annotation_font_size=11,
                    )

            # ── Y-axis scaling: visible (checked) traces only ──
            vis_mask = [v is not None and x_min <= v <= x_max for v in x_vals]

            def _visible_y(series):
                if not isinstance(series, list) or len(series) != len(x):
                    return []
                return [_coerce_float(yv) for yv, m in zip(series, vis_mask)
                        if m and _coerce_float(yv) is not None]

            y_vals = []
            if show_combined and len(combined) == len(x):
                y_vals.extend(_visible_y(combined))
            if show_options and len(options) == len(x):
                y_vals.extend(_visible_y(options))
            if show_stock and len(stock) == len(x):
                y_vals.extend(_visible_y(stock))

            if not y_vals:
                y_vals = [0]

            y_min_req = min(y_vals)
            y_max_req = max(y_vals)

            # 10% padding
            span = y_max_req - y_min_req
            if span == 0:
                span = abs(y_max_req) * 0.1 if y_max_req != 0 else 100.0
            y_min_req -= span * 0.10
            y_max_req += span * 0.10
            y_step = _nice_step(y_min_req, y_max_req)
            y_min, y_max = _snap_range(y_min_req, y_max_req, y_step)

            fig.update_layout(
                xaxis={"range": [x_min, x_max], "autorange": False, "tickmode": "auto", "nticks": 10},
                yaxis={"range": [y_min, y_max], "autorange": False, "tickmode": "auto", "nticks": 10},
            )

        fig.update_layout(
            template=_template,
            paper_bgcolor=_paper_bg,
            plot_bgcolor=_plot_bg,
            font={"color": _font_color},
            xaxis_title="Stock Price at Expiry",
            yaxis_title="Profit / Loss ($)",
            xaxis_gridcolor=_grid_color,
            xaxis_tickmode="auto",
            xaxis_nticks=10,
            xaxis_fixedrange=False,
            yaxis_gridcolor=_grid_color,
            yaxis_zeroline=True,
            yaxis_zerolinecolor="gray",
            yaxis_zerolinewidth=0.5,
            yaxis_fixedrange=False,
            hovermode="x unified",
            hoverlabel=dict(
                bgcolor="#161B22",
                font_size=12,
                font_color="#E6EDF3",
                bordercolor="#30363D",
            ),
            margin={"l": 50, "r": 20, "t": 50, "b": 80},
            height=520,
            showlegend=False,
        )
        return fig

    # ── #18 Sync UI state to STORE_UI ────────────────────────
    @app.callback(
        Output(ID.STORE_UI, "data"),
        Input(ID.TICKER_INPUT, "n_submit"),
        Input(ID.TICKER_INPUT, "n_blur"),
        Input(ID.EXPIRY_SELECT, "value"),
        Input(ID.GROUP_SELECT, "value"),
        Input(ID.STRATEGY_SELECT, "value"),
        Input(ID.SHARES_INPUT, "value"),
        Input(ID.AVG_COST_INPUT, "value"),
        Input(ID.PRICING_MODE, "value"),
        Input(ID.PREMIUM_MODE, "value"),
        Input(ID.SCENARIO_MODE, "value"),
        Input(ID.DOWNSIDE_TARGET, "value"),
        Input(ID.UPSIDE_TARGET, "value"),
        Input(ID.LEGS_TABLE, "data"),
        Input(ID.STORE_REF, "data"),
        Input(ID.CIO_RATING_INPUT, "value"),
        State(ID.TICKER_INPUT, "value"),
        State(ID.STORE_UI, "data"),
        prevent_initial_call=True,
    )
    def _v2_sync_ui(
        ticker_submit,
        ticker_blur,
        expiry_value,
        strategy_group,
        strategy_id,
        stock_position,
        avg_cost,
        pricing_mode,
        premium_mode,
        scenario_mode,
        downside_pct,
        upside_pct,
        legs_data,
        ref_data,
        cio_rating,
        ticker_value,
        current,
    ):
        triggered = {
            item.get("prop_id", "").split(".", 1)[0]
            for item in (ctx.triggered or [])
        }
        if not triggered:
            return no_update
        state = dict(current) if isinstance(current, dict) else {}

        if ID.STORE_REF in triggered and isinstance(ref_data, dict):
            raw_ticker = ref_data.get("raw_ticker")
            if raw_ticker:
                state["ticker"] = raw_ticker
            spot_from_ref = ref_data.get("spot")
            if spot_from_ref is not None:
                state["spot"] = spot_from_ref

        value_map = {
            ID.TICKER_INPUT: ("ticker", ticker_value),
            ID.EXPIRY_SELECT: ("expiry", _normalize_iso_date(expiry_value)),
            ID.GROUP_SELECT: ("strategy_group", strategy_group),
            ID.STRATEGY_SELECT: ("strategy_id", strategy_id),
            ID.SHARES_INPUT: ("stock_position", stock_position),
            ID.AVG_COST_INPUT: ("avg_cost", avg_cost),
            ID.PRICING_MODE: ("pricing_mode", pricing_mode),
            ID.PREMIUM_MODE: ("roi_policy", premium_mode),
            ID.SCENARIO_MODE: ("scenario_mode", scenario_mode),
            ID.DOWNSIDE_TARGET: ("downside_pct", downside_pct),
            ID.UPSIDE_TARGET: ("upside_pct", upside_pct),
            ID.CIO_RATING_INPUT: ("cio_rating", cio_rating),
        }
        for trig_id in triggered:
            if trig_id not in value_map:
                continue
            key, value = value_map[trig_id]
            if value is not None:
                state[key] = value

        if isinstance(current, dict) and state == current:
            return no_update
        return state

    # ── #19 Hydrate UI from STORE_UI on tab switch ───────────
    # NOTE: STRATEGY_SELECT.value is NOT output here.
    # It is owned by _v2_update_strategies, which already restores from STORE_UI
    # on its initial fire.
    @app.callback(
        Output(ID.TICKER_INPUT, "value"),
        Output(ID.EXPIRY_SELECT, "value"),
        Output(ID.GROUP_SELECT, "value"),
        Output(ID.SHARES_INPUT, "value"),
        Output(ID.AVG_COST_INPUT, "value"),
        Output(ID.PRICING_MODE, "value"),
        Output(ID.PREMIUM_MODE, "value"),
        Output(ID.SCENARIO_MODE, "value"),
        Output(ID.DOWNSIDE_TARGET, "value"),
        Output(ID.UPSIDE_TARGET, "value"),
        Output(ID.CIO_RATING_INPUT, "value"),
        Input(ID.TABS, "value"),
        State(ID.STORE_UI, "data"),
    )
    def _v2_hydrate_ui(tab_value, ui_state):
        hydrate_count = 11
        if tab_value != "dashboard":
            return (no_update,) * hydrate_count
        state = ui_state if isinstance(ui_state, dict) else {}

        def _value(key: str, default):
            if key in state and state[key] is not None:
                return state[key]
            return default

        return (
            _value("ticker", ""),
            _normalize_iso_date(_value("expiry", None)),
            _value("strategy_group", None),
            _value("stock_position", 0),
            _value("avg_cost", 0),
            _value("pricing_mode", "mid"),
            _value("roi_policy", "premium"),
            _value("scenario_mode", "targets"),
            _value("downside_pct", -10.0),
            _value("upside_pct", 10.0),
            _value("cio_rating", ""),
        )

    # ── #20 Render metrics/dividend panels ───────────────────
    @app.callback(
        Output(ID.METRICS_TABLE, "children"),
        Output(ID.DIVIDEND_CARD, "children"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
        Input(ID.TABS, "value"),
    )
    def _v2_render_panels(key_payload, tab_value):
        if tab_value != "dashboard":
            raise PreventUpdate

        def _section_title(text):
            return dmc.Text(
                text, size="xs", fw=700, tt="uppercase", c="dimmed", mb="sm",
                style={"letterSpacing": "0.08em"},
            )

        def _format_summary_value(metric_label: str, raw_value: object) -> str:
            if raw_value is None or raw_value == "":
                return "--"
            text = str(raw_value).strip()
            metric_key = str(metric_label or "").strip().lower()
            if metric_key in {"max profit", "max loss"}:
                return _fmt_money_signed(raw_value) if _coerce_float(raw_value) is not None else text
            if metric_key in {"capital basis", "notional exposure"}:
                return _fmt_money(raw_value) if _coerce_float(raw_value) is not None else text
            if metric_key in {"max roi", "min roi"}:
                return _fmt_percent_ratio(raw_value) if _coerce_float(raw_value) is not None else text
            if metric_key == "net prem % spot":
                if "%" in text:
                    return text
                return _fmt_percent_point(raw_value) if _coerce_float(raw_value) is not None else text
            if metric_key == "cost/credit":
                return text
            if metric_key == "pop":
                if "%" in text:
                    return text
                return _fmt_percent_point(raw_value) if _coerce_float(raw_value) is not None else text
            if metric_key in {"risk/reward", "closest breakeven", "be distance %",
                              "treasury obligation", "treasury interest", "treasury return %"}:
                return text
            return text

        if not isinstance(key_payload, dict) or key_payload.get("error"):
            msg = dmc.Text("Run Analysis to view results.", size="sm", c="dimmed")
            return (
                [_section_title("PAYOFF & METRICS"), msg],
                [_section_title("DIVIDEND"), msg],
            )

        pack = cache_get(key_payload.get("key"))
        if not pack:
            msg = dmc.Text("Analysis expired; rerun.", size="sm", c="dimmed")
            return (
                [_section_title("PAYOFF & METRICS"), msg],
                [_section_title("DIVIDEND"), msg],
            )

        store_pack = analysis_pack_to_store(pack)

        # Metrics table
        summary = store_pack.get("summary", {}) if isinstance(store_pack, dict) else {}
        summary_rows = summary.get("rows") if isinstance(summary, dict) else []
        metrics_rows = []

        def _pick_value(row_dict: dict, keys: list[str]):
            for key in keys:
                if key in row_dict:
                    value = row_dict.get(key)
                    if value is not None:
                        return value
            return None

        def _color_cost_credit(text):
            text_str = str(text)
            if text_str.startswith("Credit"):
                return dmc.Text(text_str, c="green", size="sm", fw=500)
            elif text_str.startswith("Debit"):
                return dmc.Text(text_str, c="red", size="sm", fw=500)
            return text_str

        def _value_color(val_str: str) -> str:
            """Return color for positive/negative values."""
            s = str(val_str).strip()
            if s in ("--", "N/A", "Unlimited", "", "\u2014"):
                return "dimmed"
            if "Credit" in s:
                return "green"
            if "Debit" in s:
                return "red"
            try:
                num_str = s.replace("$", "").replace(",", "").replace("%", "").replace("x", "").replace("+", "")
                num = float(num_str)
                if num > 0:
                    return "green"
                elif num < 0:
                    return "red"
            except (ValueError, TypeError):
                pass
            return "dimmed"

        _no_color_metrics = {"net prem % spot", "be distance %", "pop", "closest breakeven"}

        for row in summary_rows or []:
            if not isinstance(row, dict):
                continue
            metric = row.get("metric") or row.get("label") or row.get("Metric") or ""
            options_raw = _pick_value(row, ["options", "Options"])
            combined_raw = _pick_value(row, ["combined", "Combined", "net"])

            options_formatted = _format_summary_value(metric, options_raw)
            combined_formatted = _format_summary_value(metric, combined_raw)

            _metric_key = str(metric).strip().lower()

            # Color Cost/Credit
            if _metric_key == "cost/credit":
                options_formatted = _color_cost_credit(options_formatted)
                combined_formatted = _color_cost_credit(combined_formatted)
            elif _metric_key not in _no_color_metrics:
                opt_color = _value_color(str(options_formatted))
                comb_color = _value_color(str(combined_formatted))
                if opt_color != "dimmed":
                    options_formatted = dmc.Text(str(options_formatted), c=opt_color, size="sm")
                if comb_color != "dimmed":
                    combined_formatted = dmc.Text(str(combined_formatted), c=comb_color, size="sm")

            metrics_rows.append(
                [
                    metric,
                    options_formatted,
                    combined_formatted,
                ]
            )

        metrics_children = [_section_title("PAYOFF & METRICS")]
        if metrics_rows:
            metrics_children.append(_dmc_table(["Metric", "Options", "Combined"], metrics_rows))
        else:
            metrics_children.append(dmc.Text("--", size="sm", c="dimmed"))

        # Dividend table
        dividend = {}
        underlying = store_pack.get("underlying", {}) if isinstance(store_pack, dict) else {}
        if isinstance(underlying, dict):
            dividend = underlying.get("dividend_risk", {}) or {}
        div_rows = [
            ["Ex-div Date", dividend.get("ex_div_date", "--")],
            ["Days to Dividend", dividend.get("days_to_dividend", "--")],
            ["Before Expiry", dividend.get("before_expiry", "--")],
        ]
        dividend_children = [
            _section_title("DIVIDEND"),
            _dmc_table_simple(["Field", "Value"], div_rows),
        ]

        return metrics_children, dividend_children

    # ── #20a Render probability bar ──────────────────────────
    @app.callback(
        Output(ID.PROB_POP, "children"),
        Output(ID.PROB_ASSIGN, "children"),
        Output(ID.PROB_25, "children"),
        Output(ID.PROB_50, "children"),
        Output(ID.PROB_100, "children"),
        Output(ID.PROB_IV, "children"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
        prevent_initial_call=True,
    )
    def _v2_render_probabilities(analysis_key):
        """Render probability metrics bar."""
        if not isinstance(analysis_key, dict) or analysis_key.get("error"):
            raise PreventUpdate

        pack = cache_get(analysis_key.get("key"))
        if not pack:
            raise PreventUpdate

        probs = pack.get("probabilities", {})
        if not probs:
            return "--", "--", "--", "--", "--", "--"

        def colored_prob(value, pct_str, good_high=True):
            """Return dmc.Text with color based on value."""
            if value is None:
                return dmc.Text("--", size="sm", fw=600, ta="center")
            if good_high:
                color = "green" if value > 0.6 else ("yellow" if value > 0.4 else "red")
            else:
                color = "red" if value > 0.5 else ("yellow" if value > 0.3 else "green")
            return dmc.Text(pct_str, size="sm", fw=600, ta="center", c=color)

        pop = colored_prob(probs.get("pop"), probs.get("pop_pct", "--"), good_high=True)
        assign = colored_prob(probs.get("assignment_prob"), probs.get("assignment_prob_pct", "--"), good_high=False)
        p25 = colored_prob(probs.get("prob_25_profit"), probs.get("prob_25_pct", "--"), good_high=True)
        p50 = colored_prob(probs.get("prob_50_profit"), probs.get("prob_50_pct", "--"), good_high=True)
        p100 = colored_prob(probs.get("prob_100_profit"), probs.get("prob_100_pct", "--"), good_high=True)
        iv_val = probs.get("iv_used_pct", "--")
        iv_text = dmc.Text(iv_val if iv_val != "--" else "--", size="sm", fw=600, ta="center")

        return pop, assign, p25, p50, p100, iv_text

    # ── #20b Render margin panel (CBOE/House toggle) ─────────
    @app.callback(
        Output(ID.MARGIN_FULL_TABLE, "children"),
        Output(ID.MARGIN_CLASSIFICATION, "children"),
        Output(ID.HOUSE_INTRADAY_SECTION, "style"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
        Input(ID.MARGIN_MODE_SELECT, "value"),
        prevent_initial_call=True,
    )
    def _v2_render_margin(key_payload, margin_mode):
        if not isinstance(key_payload, dict) or key_payload.get("error"):
            return (
                dmc.Text("Run Analysis to view margin.", size="sm", c="dimmed"),
                "--",
                {"display": "none"},
            )

        pack = cache_get(key_payload.get("key"))
        if not pack:
            return (
                dmc.Text("No analysis data.", size="sm", c="dimmed"),
                "--",
                {"display": "none"},
            )

        margin_data = pack.get("margin", {}).get("full")
        if not margin_data:
            # Fallback to old format
            margin_old = pack.get("margin", {})
            old_rows = [
                ["Classification", margin_old.get("classification", "--")],
                ["Margin Proxy", _fmt_money(margin_old.get("margin_proxy"))],
            ]
            return (
                _dmc_table_simple(["Field", "Value"], old_rows),
                margin_old.get("classification", "--"),
                {"display": "none"},
            )

        refined_code = margin_data.get("classification_refined", "")

        def _margin_row(rule_set, account, stage, data):
            amount = data.get("amount")
            if amount is not None and data.get("allowed", True):
                amt_str = f"${amount:,.2f}"
            else:
                amt_str = "N/A"
            req_text = data.get("requirement_text") or data.get("notes", "")
            if len(req_text) > 80:
                req_text = req_text[:77] + "..."
            return [rule_set, account, stage, amt_str, req_text]

        if margin_mode == "House":
            rows = [
                _margin_row("CBOE", "Cash", "Initial", margin_data["cboe"]["cash_initial"]),
                _margin_row("House", "Margin", "Initial", margin_data["house"]["margin_initial"]),
                _margin_row("House", "Margin", "Maintenance", margin_data["house"]["margin_maintenance"]),
            ]
            show_house = {"display": "block"}
        else:
            rows = [
                _margin_row("CBOE", "Cash", "Initial", margin_data["cboe"]["cash_initial"]),
                _margin_row("CBOE", "Margin", "Initial", margin_data["cboe"]["margin_initial"]),
                _margin_row("CBOE", "Margin", "Maintenance", margin_data["cboe"]["margin_maintenance"]),
            ]
            show_house = {"display": "none"}

        table = _dmc_table(
            ["Rule Set", "Account", "Stage", "Req ($)", "Requirement"],
            rows,
        )
        return table, refined_code, show_house

    # ── #20c House Intraday Check ─────────────────────────────
    @app.callback(
        Output(ID.HOUSE_INTRADAY_TABLE, "children"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
        Input(ID.HOUSE_HOUSECALL, "value"),
        Input(ID.HOUSE_SMA, "value"),
        Input(ID.HOUSE_TODAYS_CHANGE, "value"),
        Input(ID.HOUSE_NEW_CASH, "value"),
        Input(ID.MARGIN_MODE_SELECT, "value"),
        prevent_initial_call=True,
    )
    def _v2_render_house_intraday(
        analysis_key, housecall, sma, todays_change, new_cash, margin_mode,
    ):
        if margin_mode != "House":
            raise PreventUpdate
        if not isinstance(analysis_key, dict) or analysis_key.get("error"):
            raise PreventUpdate

        pack = cache_get(analysis_key.get("key"))
        if not pack:
            raise PreventUpdate

        margin_data = pack.get("margin", {}).get("full")
        if not margin_data:
            raise PreventUpdate

        house_init = margin_data.get("house", {}).get("margin_initial", {})
        house_req = house_init.get("amount") or 0

        from core.margin import compute_house_intraday

        result = compute_house_intraday(
            house_margin_req=house_req,
            housecall_excess=housecall or 0,
            sma=sma or 0,
            todays_change=todays_change or 0,
            new_intraday_cash=new_cash or 0,
        )

        ok_flag = result["ok_to_trade"]
        flag_color = "green" if ok_flag else ("red" if ok_flag is False else "gray")
        flag_text = "OK" if ok_flag else ("Failed" if ok_flag is False else "N/A")

        rows = [
            dmc.TableTr([
                dmc.TableTd("House Margin Req"),
                dmc.TableTd(
                    f"${result['house_margin_req']:,.2f}" if result["house_margin_req"] else "N/A",
                    style={"textAlign": "right"},
                ),
            ]),
            dmc.TableTr([
                dmc.TableTd("Intraday Available"),
                dmc.TableTd(
                    f"${result['intraday_available']:,.2f}",
                    style={"textAlign": "right"},
                ),
            ]),
            dmc.TableTr([
                dmc.TableTd("OK to Trade"),
                dmc.TableTd(dmc.Badge(flag_text, color=flag_color, size="sm")),
            ]),
        ]

        return dmc.Table(
            children=[dmc.TableTbody(rows)],
            withTableBorder=True,
            style={"fontSize": "13px"},
        )

    # ── #21 Render risk banner (badge inside payoff card) ────
    @app.callback(
        Output(ID.RISK_BANNER, "children"),
        Output(ID.RISK_BANNER, "color"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
    )
    def _v2_render_risk_banner(key_payload):
        if not isinstance(key_payload, dict) or key_payload.get("error"):
            return "No risk events", "green"
        pack = cache_get(key_payload.get("key"))
        if not pack or not isinstance(pack, dict):
            return "No risk events", "green"
        underlying = pack.get("underlying", {})
        if not isinstance(underlying, dict):
            return "No risk events", "green"
        earnings_risk = underlying.get("earnings_risk", {}) or {}
        dividend_risk = underlying.get("dividend_risk", {}) or {}
        messages = []
        if isinstance(earnings_risk, dict) and earnings_risk.get("before_expiry") is True:
            days = earnings_risk.get("days_to_earnings")
            if days is not None:
                messages.append(f"Earnings in {days}d")
            else:
                messages.append("Earnings before expiry")
        if isinstance(dividend_risk, dict) and dividend_risk.get("before_expiry") is True:
            days = dividend_risk.get("days_to_dividend")
            if days is not None:
                messages.append(f"Ex-div in {days}d")
            else:
                messages.append("Ex-div before expiry")
        if not messages:
            return "No risk events", "green"
        return " | ".join(messages), "red"

    # ── #22 Render scenario cards ────────────────────────────
    @app.callback(
        Output(ID.SCENARIO_CARDS, "children"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
        Input(ID.TABS, "value"),
    )
    def _v2_render_scenario_cards(key_payload, tab_value):
        if tab_value != "dashboard":
            raise PreventUpdate

        def _section_title(text):
            return dmc.Text(
                text, size="xs", fw=700, tt="uppercase", c="dimmed", mb="sm",
                style={"letterSpacing": "0.08em"},
            )

        def _default_cards():
            def _placeholder(title, subtitle, color):
                return dmc.Card(
                    withBorder=True, padding="md",
                    children=[
                        dmc.Group(gap="xs", mb="xs", children=[
                            dmc.Badge(title.split()[0], color=color, size="sm", variant="light"),
                            dmc.Text(title, fw=600, size="sm"),
                        ]),
                        dmc.Text(subtitle, size="xs", c="dimmed", mb="sm"),
                        dmc.Divider(mb="sm"),
                        dmc.Text("Run analysis to see scenario commentary.", size="sm", c="dimmed"),
                    ],
                )
            return [
                _section_title("SCENARIO COMMENTARY"),
                dmc.SimpleGrid(cols={"base": 1, "sm": 3}, spacing="md", children=[
                    _placeholder("Bearish Case", "Stock drops significantly", "red"),
                    _placeholder("Stagnant Case", "Stock stays near current levels", "gray"),
                    _placeholder("Bullish Case", "Stock rises significantly", "green"),
                ]),
            ]

        if not isinstance(key_payload, dict) or key_payload.get("error"):
            return _default_cards()
        pack = cache_get(key_payload.get("key"))
        if not pack or not isinstance(pack, dict):
            return _default_cards()
        narrative = pack.get("narrative_scenarios")
        if not isinstance(narrative, dict):
            return _default_cards()

        def _card(label, block, color):
            block = block if isinstance(block, dict) else {}
            title = block.get("title") or label
            condition = block.get("condition") or ""
            body = block.get("body") or "--"
            return dmc.Card(
                withBorder=True, padding="md",
                children=[
                    dmc.Group(gap="xs", mb="xs", children=[
                        dmc.Badge(title.split()[0], color=color, size="sm", variant="light"),
                        dmc.Text(title, fw=600, size="sm"),
                    ]),
                    dmc.Text(condition, size="xs", c="dimmed", mb="sm"),
                    dmc.Divider(mb="sm"),
                    dmc.Text(body, size="sm"),
                ],
            )

        return [
            _section_title("SCENARIO COMMENTARY"),
            dmc.SimpleGrid(cols={"base": 1, "sm": 3}, spacing="md", children=[
                _card("Bearish Case", narrative.get("bear"), "red"),
                _card("Stagnant Case", narrative.get("base"), "gray"),
                _card("Bullish Case", narrative.get("bull"), "green"),
            ]),
        ]

    # ── #23 Render key levels ────────────────────────────────
    @app.callback(
        Output(ID.KEY_LEVELS_TABLE, "children"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
        Input(ID.TABS, "value"),
    )
    def _v2_render_key_levels(key_payload, tab_value):
        if tab_value != "dashboard":
            raise PreventUpdate

        def _section_title(text):
            return dmc.Text(
                text, size="xs", fw=700, tt="uppercase", c="dimmed", mb="sm",
                style={"letterSpacing": "0.08em"},
            )

        default = [
            _section_title("KEY LEVELS"),
            dmc.Text("Run Analysis to view key levels.", size="sm", c="dimmed"),
        ]
        if not isinstance(key_payload, dict) or key_payload.get("error"):
            return default
        pack = cache_get(key_payload.get("key"))
        if not pack or not isinstance(pack, dict):
            return default
        key_levels = pack.get("key_levels", {})
        levels = key_levels.get("levels") if isinstance(key_levels, dict) else None
        if not isinstance(levels, list) or not levels:
            return default

        sorted_levels = _sort_key_levels(levels)
        rows = []
        for level in sorted_levels:
            if not isinstance(level, dict):
                continue
            rows.append(
                [
                    level.get("label", "--"),
                    _fmt_money(level.get("price")),
                    _fmt_percent_point(level.get("move_pct")),
                    _fmt_money_signed(level.get("stock_pnl")),
                    _fmt_money_signed(level.get("option_pnl")),
                    _fmt_money_signed(level.get("net_pnl")),
                    _fmt_percent_ratio(level.get("net_roi")),
                    level.get("source", "--"),
                ]
            )
        headers = ["Label", "Price", "Move %", "Stock PnL", "Option PnL", "Net PnL", "Net ROI", "Source"]
        return [
            _section_title("KEY LEVELS"),
            html.Div(_dmc_table(headers, rows), style={"maxHeight": "300px", "overflowY": "auto"}),
        ]

    # ── #24 Render eligibility ───────────────────────────────
    @app.callback(
        Output(ID.ELIGIBILITY_TABLE, "children"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
        Input(ID.TABS, "value"),
    )
    def _v2_render_eligibility(key_payload, tab_value):
        if tab_value != "dashboard":
            raise PreventUpdate
        if not isinstance(key_payload, dict) or key_payload.get("error"):
            return dmc.Text("Run Analysis to view eligibility.", size="sm", c="dimmed")
        pack = cache_get(key_payload.get("key"))
        if not pack or not isinstance(pack, dict):
            return dmc.Text("Run Analysis to view eligibility.", size="sm", c="dimmed")
        store_pack = analysis_pack_to_store(pack)
        eligibility = (
            store_pack.get("eligibility", {}) if isinstance(store_pack, dict) else {}
        )
        table = eligibility.get("table")
        records = []
        if isinstance(table, dict) and table.get("__type__") == "DataFrame":
            records = table.get("records") or []
        elif isinstance(table, list):
            records = table
        if not records:
            return dmc.Text("Eligibility data unavailable for this strategy.", size="sm", c="dimmed")

        def _format_eligibility(value):
            if value is True:
                return "Allowed"
            if value is False:
                return "Not allowed"
            text = str(value).strip().upper()
            if text in {"ALLOWED", "Y", "YES", "TRUE"}:
                return "Allowed"
            if text in {"RESTRICTED"}:
                return "Restricted"
            if text in {"NOT_ALLOWED", "N", "NO", "FALSE"}:
                return "Not allowed"
            return str(value) if value not in (None, "", "nan") else "--"

        rows = []
        for rec in records:
            if not isinstance(rec, dict):
                continue
            rows.append(
                [
                    rec.get("account_type", "--"),
                    _format_eligibility(rec.get("eligibility")),
                ]
            )
        return _dmc_table_simple(["Account Type", "Eligible"], rows)

    # ── Activity Log callbacks ─────────────────────────────────

    @app.callback(
        Output(ID.LOG_TABLE, "data"),
        Output(ID.LOG_SUMMARY, "children"),
        Input(ID.LOG_STORE, "data"),
        Input(ID.TABS, "value"),
        Input(ID.CLEAR_LOG_YES, "n_clicks"),
        prevent_initial_call=False,
    )
    def _v2_load_activity_log(log_trigger, active_tab, clear_clicks):
        entries = read_all()
        entries = list(reversed(entries))
        summary = f"{len(entries)} illustration{'s' if len(entries) != 1 else ''} logged"
        return entries, summary

    @app.callback(
        Output(ID.DL_ACTIVITY_CSV, "data"),
        Input(ID.BTN_DOWNLOAD_CSV, "n_clicks"),
        prevent_initial_call=True,
    )
    def _v2_download_activity_csv(n_clicks):
        if not n_clicks:
            raise PreventUpdate
        return dcc.send_file(get_csv_path(), filename="activity_log.csv")

    @app.callback(
        Output(ID.CLEAR_LOG_CONFIRM, "opened"),
        Input(ID.BTN_CLEAR_LOG, "n_clicks"),
        Input(ID.CLEAR_LOG_CANCEL, "n_clicks"),
        Input(ID.CLEAR_LOG_YES, "n_clicks"),
        State(ID.CLEAR_LOG_CONFIRM, "opened"),
        prevent_initial_call=True,
    )
    def _v2_clear_log_modal(clear_click, cancel_click, yes_click, is_open):
        trigger_id = ctx.triggered_id
        if trigger_id == ID.BTN_CLEAR_LOG:
            return True
        if trigger_id == ID.CLEAR_LOG_CANCEL:
            return False
        if trigger_id == ID.CLEAR_LOG_YES:
            clear_log()
            return False
        raise PreventUpdate

    # ── #25 Stock info stats row ────────────────────────────────
    @app.callback(
        Output(ID.STAT_YTD, "children"),
        Output(ID.STAT_52WK_LOW, "children"),
        Output(ID.STAT_52WK_HIGH, "children"),
        Output(ID.STAT_3M_IV, "children"),
        Input(ID.STORE_MARKET, "data"),
        prevent_initial_call=True,
    )
    def _v2_render_stock_info(market_data):
        """Populate Market Card stock info stats from market snapshot."""
        if not isinstance(market_data, dict):
            raise PreventUpdate
        underlying = market_data.get("underlying_profile") or {}

        # YTD %
        ytd_raw = underlying.get("chg_pct_ytd")
        if ytd_raw is not None:
            try:
                ytd_val = float(ytd_raw)
                sign = "+" if ytd_val >= 0 else ""
                color = "green" if ytd_val >= 0 else "red"
                ytd_out = dmc.Text(f"{sign}{ytd_val:.1f}%", size="sm", fw=600, c=color)
            except (TypeError, ValueError):
                ytd_out = "--"
        else:
            ytd_out = "--"

        # 52wk Low
        low_raw = underlying.get("low_52week")
        if low_raw is not None:
            try:
                low_out = f"${float(low_raw):,.2f}"
            except (TypeError, ValueError):
                low_out = "--"
        else:
            low_out = "--"

        # 52wk High
        high_raw = underlying.get("high_52week")
        if high_raw is not None:
            try:
                high_out = f"${float(high_raw):,.2f}"
            except (TypeError, ValueError):
                high_out = "--"
        else:
            high_out = "--"

        # 3M IV
        iv_raw = underlying.get("impvol_3m_atm")
        if iv_raw is not None:
            try:
                iv_out = f"{float(iv_raw):.1f}%"
            except (TypeError, ValueError):
                iv_out = "--"
        else:
            iv_out = "--"

        return ytd_out, low_out, high_out, iv_out

    # ── Shutdown callbacks ─────────────────────────────────────

    @app.callback(
        Output(ID.SHUTDOWN_CONFIRM, "opened"),
        Input(ID.BTN_SHUTDOWN, "n_clicks"),
        Input(ID.SHUTDOWN_CANCEL, "n_clicks"),
        State(ID.SHUTDOWN_CONFIRM, "opened"),
        prevent_initial_call=True,
    )
    def _v2_shutdown_modal(shutdown_click, cancel_click, is_open):
        trigger_id = ctx.triggered_id
        if trigger_id == ID.BTN_SHUTDOWN:
            return True
        return False

    @app.callback(
        Output(ID.SHUTDOWN_YES, "disabled"),
        Input(ID.SHUTDOWN_YES, "n_clicks"),
        prevent_initial_call=True,
    )
    def _v2_shutdown_server(n_clicks):
        if not n_clicks:
            raise PreventUpdate
        import threading
        import os
        import signal

        def _kill():
            import time
            time.sleep(0.5)
            os.kill(os.getpid(), signal.SIGTERM)

        threading.Thread(target=_kill, daemon=True).start()
        return True  # disable button to show it was clicked
