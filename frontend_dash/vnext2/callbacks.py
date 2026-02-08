"""v2 DMC callbacks — ported from vnext/callbacks.py for the /v2 dashboard.

All callbacks use v2-prefixed IDs from frontend_dash.vnext2.ids.
"""

from __future__ import annotations

from datetime import datetime, timezone
import traceback
import json
import math
import re

import dash_mantine_components as dmc
import plotly.graph_objects as go
from dash import Input, Output, State, dcc, no_update, ctx, html, dash_table
from dash.exceptions import PreventUpdate

from core.analysis_pack import build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.strategy_map import get_strategy, list_strategies
from frontend_dash.analysis_adapter import (
    analysis_pack_to_store,
    refresh_leg_premiums,
    to_jsonable,
)
from frontend_dash.smart_strikes import compute_default_strike, is_number_like
from frontend_dash.vnext2 import ids as ID


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
    stamp = None
    if isinstance(pack, dict):
        stamp = pack.get("as_of") or pack.get("asof")
    if not stamp and isinstance(key_payload, dict):
        stamp = key_payload.get("key")
    if stamp:
        safe_stamp = re.sub(r"[^0-9A-Za-z_-]+", "_", str(stamp)).strip("_")
        if safe_stamp:
            return f"alpha_engine_report_{safe_stamp}.pdf"
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
            dmc.TableTr([dmc.TableTd(str(cell) if cell is not None else "--") for cell in row])
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

    # ── #8 Apply legs updates (strategy template or market quotes) ──
    @app.callback(
        Output(ID.LEGS_TABLE, "data"),
        Input(ID.STRATEGY_SELECT, "value"),
        Input(ID.STORE_MARKET, "data"),
        State(ID.STORE_REF, "data"),
        State(ID.PRICING_MODE, "value"),
        State(ID.LEGS_TABLE, "data"),
        State(ID.STORE_UI, "data"),
        prevent_initial_call=True,
    )
    def _v2_apply_legs_updates(
        strategy_id, market_data, ref_data, pricing_mode, legs_data, ui_state
    ):
        trigger_id = ctx.triggered_id if ctx else None
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
        Output(ID.SPOT_STATUS, "children"),
        Input(ID.TICKER_INPUT, "n_submit"),
        Input(ID.TICKER_INPUT, "n_blur"),
        State(ID.TICKER_INPUT, "value"),
        State(ID.STORE_REF, "data"),
        prevent_initial_call=True,
    )
    def _v2_ping_spot(n_submit, n_blur, ticker_value, ref_data):
        raw_ticker = (ticker_value or "").strip()
        if not raw_ticker:
            return no_update, "Enter a ticker"
        trigger = ctx.triggered[0]["prop_id"] if ctx and ctx.triggered else ""
        is_submit = trigger.endswith(".n_submit")
        last_ticker = None
        if isinstance(ref_data, dict):
            last_ticker = ref_data.get("raw_ticker")
        if not is_submit and last_ticker == raw_ticker:
            return no_update, no_update
        if not bloomberg_available or bbg_resolve_security is None or bbg_fetch_spot is None:
            return no_update, "Bloomberg unavailable (offline mode)"
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
            return to_jsonable(store_ref), f"Spot updated ({as_of_text})"
        except Exception as exc:
            store_ref = {
                "raw_ticker": raw_ticker,
                "resolved_ticker": None,
                "spot": None,
                "as_of": _utc_now_str(),
                "status": "error",
                "error": str(exc),
            }
            return to_jsonable(store_ref), f"Spot fetch failed for {raw_ticker}"

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
        ticker = ref_data.get("raw_ticker") or ""
        if spot is None:
            return f"Spot: — ({ticker})"
        try:
            return f"Spot: {float(spot):,.2f} ({ticker})"
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
        return to_jsonable(market_snapshot), status

    # ── #13 Render Bloomberg tab ─────────────────────────────
    # Stubbed — returns placeholder content for all 5 outputs.
    # Full implementation will be wired once the core dashboard flow is stable.
    @app.callback(
        Output(ID.BBG_REQUEST_SUMMARY, "children"),
        Output(ID.BBG_UNDERLYING_SUMMARY, "children"),
        Output(ID.BBG_UNDERLYING_JSON, "children"),
        Output(ID.BBG_LEG_QUOTES, "data"),
        Output(ID.BBG_ERRORS, "children"),
        Input(ID.STORE_MARKET, "data"),
        Input(ID.STORE_INPUTS, "data"),
    )
    def _v2_render_bbg_tab(market_data, inputs_data):
        placeholder = dmc.Text("Bloomberg data will appear here after market refresh.", size="sm", c="dimmed")
        return (
            placeholder,     # BBG_REQUEST_SUMMARY
            placeholder,     # BBG_UNDERLYING_SUMMARY
            "--",            # BBG_UNDERLYING_JSON
            [],              # BBG_LEG_QUOTES (empty DataTable rows)
            placeholder,     # BBG_ERRORS
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
        Input(ID.BTN_PDF, "n_clicks"),
        State(ID.STORE_UI, "data"),
        State(ID.STORE_INPUTS, "data"),
        State(ID.STORE_MARKET, "data"),
        State(ID.STORE_ANALYSIS_KEY, "data"),
        prevent_initial_call=True,
    )
    def _v2_download_report_pdf(
        n_clicks_report, ui_state, inputs_state, market_data, key_payload
    ):
        if not n_clicks_report:
            return no_update, no_update
        if not isinstance(key_payload, dict) or key_payload.get("error"):
            return no_update, "Run Analysis first to generate a report."
        key = key_payload.get("key")
        pack = cache_get(key) if key else None
        if not pack:
            return no_update, "Run Analysis first to generate a report."
        try:
            from reporting.report_model import build_report_model
            from reporting.report_pdf import build_client_report_pdf

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
            }

            report_model = build_report_model(state)
            filename = _report_filename(key_payload, pack)

            try:
                payload = build_client_report_pdf(report_model, prefer_html=True)
            except Exception as exc:
                traceback.print_exc()
                return no_update, f"PDF export error: {type(exc).__name__}: {exc}"

            return (
                dcc.send_bytes(payload, filename=filename),
                "PDF generated.",
            )
        except Exception as exc:
            traceback.print_exc()
            return no_update, f"PDF export error: {type(exc).__name__}: {exc}"

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
            "vol_mode": "atm",
            "atm_iv": 0.2,
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

        # Fetch risk-free rate from Bloomberg treasury indices
        rfr = 0.0
        if expiry_value:
            try:
                from adapters.bloomberg import fetch_risk_free_rate as _fetch_rfr
                from datetime import date as _date
                exp_date = _date.fromisoformat(str(expiry_value)[:10])
                dte = (exp_date - _date.today()).days
                if dte > 0:
                    rfr = _fetch_rfr(dte)
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
                vol_mode="atm",
                atm_iv=0.2,
                underlying_profile=underlying_profile,
                bbg_leg_snapshots=bbg_leg_snapshots,
                scenario_mode=scenario_mode_backend,
                downside_tgt=downside_factor,
                upside_tgt=upside_factor,
                risk_free_rate=rfr,
            )
        except Exception as exc:
            return {"key": None, "as_of": _utc_now_str(), "error": str(exc)}, to_jsonable(
                inputs_snapshot
            )

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
    )
    def _v2_render_chart(key_payload, tab_value):
        if tab_value != "dashboard":
            raise PreventUpdate
        fig = go.Figure()
        # v2 defaults: show all series (no toggle controls)
        show_options = True
        show_stock = True
        show_combined = True
        show_strikes = True
        show_breakevens = True

        if not isinstance(key_payload, dict) or key_payload.get("error"):
            if isinstance(key_payload, dict) and key_payload.get("error"):
                fig.update_layout(
                    template="plotly_dark",
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(20,24,37,0.5)",
                    title=f"Analysis error: {key_payload['error']}",
                )
            else:
                fig.update_layout(
                    template="plotly_dark",
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(20,24,37,0.5)",
                )
                fig.add_annotation(
                    text="Run analysis to see payoff diagram",
                    xref="paper", yref="paper", x=0.5, y=0.5,
                    showarrow=False, font={"size": 14, "color": "#6C7589"},
                )
            return fig
        pack = cache_get(key_payload.get("key"))
        if not pack:
            fig.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(20,24,37,0.5)",
                title="Analysis expired; rerun",
            )
            return fig
        pack_store = analysis_pack_to_store(pack)
        payoff = pack_store.get("payoff") if isinstance(pack_store, dict) else None
        if not isinstance(payoff, dict):
            fig.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(20,24,37,0.5)",
                title="No payoff data in analysis_pack",
            )
            return fig
        x = payoff.get("price_grid") or []
        options = payoff.get("options_pnl") or []
        stock = payoff.get("stock_pnl") or []
        combined = payoff.get("combined_pnl") or []
        if not x:
            fig.update_layout(
                template="plotly_dark",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(20,24,37,0.5)",
                title="No payoff data in analysis_pack",
            )
            return fig
        if show_options and len(options) == len(x):
            fig.add_trace(go.Scatter(
                x=x, y=options, name="Options PnL",
                line={"color": "#2563EB"},
            ))
        if show_stock and len(stock) == len(x):
            fig.add_trace(go.Scatter(
                x=x, y=stock, name="Stock PnL",
                line={"color": "#D1D5DB"},
            ))
        if show_combined and len(combined) == len(x):
            fig.add_trace(go.Scatter(
                x=x, y=combined, name="Combined PnL",
                line={"color": "#7C3AED"},
            ))

        def _numeric_list(values):
            items = []
            for value in values or []:
                num = _coerce_float(value)
                if num is not None:
                    items.append(num)
            return sorted(set(items))

        if show_strikes:
            for strike in _numeric_list(payoff.get("strikes")):
                fig.add_vline(x=strike, line_dash="dot", line_color="#EF4444")
                fig.add_annotation(x=strike, y=1.02, yref="paper", text=f"K={strike:g}")
        if show_breakevens:
            for be in _numeric_list(payoff.get("breakevens")):
                fig.add_vline(x=be, line_dash="dash", line_color="#22D3EE")
                fig.add_annotation(x=be, y=1.08, yref="paper", text=f"BE={be:g}")

        x_vals = [_coerce_float(v) for v in x]
        x_pairs = [v for v in x_vals if v is not None]
        if x_pairs:
            x_min_data = min(x_pairs)
            x_max_data = max(x_pairs)
            anchors = []
            strikes = payoff.get("strikes") or []
            breakevens = payoff.get("breakevens") or []
            for item in strikes + breakevens:
                num = _coerce_float(item)
                if num is not None:
                    anchors.append(num)
            underlying = pack_store.get("underlying") if isinstance(pack_store, dict) else {}
            spot = None
            if isinstance(underlying, dict):
                spot = _coerce_float(underlying.get("spot"))
            if spot is not None:
                anchors.append(spot)
            if anchors:
                anchor_min = min(anchors)
                anchor_max = max(anchors)
                pad = 0.25 * spot if spot else 0.25 * (anchor_max - anchor_min or 1.0)
                x_min_req = anchor_min - pad
                x_max_req = anchor_max + pad
            else:
                x_min_req = 0.0
                x_max_req = x_max_data
            x_min_req = max(x_min_req, x_min_data)
            x_max_req = min(x_max_req, x_max_data)
            x_step = _nice_step(x_min_req, x_max_req)
            x_min, x_max = _snap_range(x_min_req, x_max_req, x_step)

            y_vals = []

            def _add_visible(series):
                if not isinstance(series, list):
                    return
                for xv, yv in zip(x_vals, series):
                    if xv is None:
                        continue
                    if xv < x_min or xv > x_max:
                        continue
                    y_num = _coerce_float(yv)
                    if y_num is not None:
                        y_vals.append(y_num)

            if show_options:
                _add_visible(options)
            if show_stock:
                _add_visible(stock)
            if show_combined:
                _add_visible(combined)

            if y_vals:
                y_min_req = min(y_vals)
                y_max_req = max(y_vals)
                span = y_max_req - y_min_req
                if span == 0:
                    span = abs(y_max_req) * 0.1
                if span == 0:
                    span = 100.0
                y_min_req -= 0.10 * span
                y_max_req += 0.10 * span
                y_step = _nice_step(y_min_req, y_max_req)
                y_min, y_max = _snap_range(y_min_req, y_max_req, y_step)
                fig.update_layout(
                    xaxis={"range": [x_min, x_max], "dtick": x_step},
                    yaxis={"range": [y_min, y_max], "dtick": y_step},
                )

        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(20,24,37,0.5)",
            font={"color": "#C1C7D6"},
            xaxis_title="Stock Price at Expiry",
            yaxis_title="Profit / Loss ($)",
            xaxis_gridcolor="#1E2433",
            yaxis_gridcolor="#1E2433",
            yaxis_zeroline=True,
            yaxis_zerolinecolor="#3D4559",
            margin={"l": 50, "r": 20, "t": 30, "b": 60},
            height=400,
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

    # ── #20 Render metrics/margin/dividend panels ────────────
    @app.callback(
        Output(ID.METRICS_TABLE, "children"),
        Output(ID.MARGIN_CARD, "children"),
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
            return text

        if not isinstance(key_payload, dict) or key_payload.get("error"):
            msg = dmc.Text("Run Analysis to view results.", size="sm", c="dimmed")
            return (
                [_section_title("PAYOFF & METRICS"), msg],
                [_section_title("MARGIN & CAPITAL"), msg],
                [_section_title("DIVIDEND"), msg],
            )

        pack = cache_get(key_payload.get("key"))
        if not pack:
            msg = dmc.Text("Analysis expired; rerun.", size="sm", c="dimmed")
            return (
                [_section_title("PAYOFF & METRICS"), msg],
                [_section_title("MARGIN & CAPITAL"), msg],
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

        for row in summary_rows or []:
            if not isinstance(row, dict):
                continue
            metric = row.get("metric") or row.get("label") or row.get("Metric") or ""
            options_raw = _pick_value(row, ["options", "Options"])
            combined_raw = _pick_value(row, ["combined", "Combined", "net"])
            metrics_rows.append(
                [
                    metric,
                    _format_summary_value(metric, options_raw),
                    _format_summary_value(metric, combined_raw),
                ]
            )

        metrics_children = [_section_title("PAYOFF & METRICS")]
        if metrics_rows:
            metrics_children.append(_dmc_table(["Metric", "Options", "Combined"], metrics_rows))
        else:
            metrics_children.append(dmc.Text("--", size="sm", c="dimmed"))

        # Margin table
        margin = store_pack.get("margin", {}) if isinstance(store_pack, dict) else {}
        margin_rows = [
            ["Classification", margin.get("classification", "--")],
            ["Margin Proxy", margin.get("margin_proxy", "--")],
        ]
        margin_children = [
            _section_title("MARGIN & CAPITAL"),
            _dmc_table_simple(["Field", "Value"], margin_rows),
        ]

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

        return metrics_children, margin_children, dividend_children

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
