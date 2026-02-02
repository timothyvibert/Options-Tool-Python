"""vNext callbacks registration."""

from __future__ import annotations

from datetime import datetime, timezone
import os
import tempfile
import traceback
import json
import math
import re
import subprocess

import plotly.graph_objects as go
from dash import Input, Output, State, dcc, no_update, ctx, html
from dash.exceptions import PreventUpdate

from core.analysis_pack import build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.strategy_map import get_strategy, list_strategies, list_subgroups
from frontend_dash.analysis_adapter import (
    analysis_pack_to_store,
    refresh_leg_premiums,
    to_jsonable,
)
from frontend_dash.smart_strikes import compute_default_strike, is_number_like
from frontend_dash.vnext import ids as ID
from frontend_dash.vnext.layout import (
    layout_bloomberg,
    layout_dashboard,
    layout_report,
)
from reporting.report_model import _pick_first_df, build_report_model
from reporting.report_pdf import build_report_pdf, build_report_pdf_v2


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
    if text in {"false", "no", "0", "n", "f", ""}:
        return False
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


def _render_report_pdf_template(report_model: object) -> tuple[bytes | None, str | None]:
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    cli_path = os.path.join(
        repo_root, "Design", "figma_report_v2", "src", "cli", "render_report.mjs"
    )
    if not os.path.exists(cli_path):
        return None, "template renderer not found"
    try:
        with tempfile.TemporaryDirectory() as tmp_dir:
            contract_path = os.path.join(tmp_dir, "report_contract.json")
            output_path = os.path.join(tmp_dir, "report.pdf")
            with open(contract_path, "w", encoding="utf-8") as handle:
                handle.write(_safe_json_dumps(report_model))
            result = subprocess.run(
                ["node", cli_path, contract_path, output_path],
                cwd=repo_root,
                capture_output=True,
                text=True,
                timeout=45,
            )
            if result.returncode != 0:
                if result.stdout:
                    print("Template renderer stdout:", result.stdout)
                if result.stderr:
                    print("Template renderer stderr:", result.stderr)
                return None, "template renderer failed"
            if not os.path.exists(output_path) or os.path.getsize(output_path) <= 0:
                return None, "template renderer produced no output"
            with open(output_path, "rb") as handle:
                return handle.read(), None
    except FileNotFoundError as exc:
        print("Template renderer error:", exc)
        return None, "node not available"
    except Exception as exc:
        print("Template renderer error:", exc)
        return None, f"{type(exc).__name__}: {exc}"


_DATE_RE = re.compile(r"^\\d{4}-\\d{2}-\\d{2}$")


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


def _safe_list_subgroups(group: str | None) -> list[str]:
    if not group:
        return []
    try:
        return list_subgroups(group)
    except Exception:
        return []


def _safe_list_strategies(group: str | None, subgroup: str | None):
    if not group or not subgroup:
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


def _empty_leg_rows() -> list[dict]:
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
                "bid",
                "BID",
                "PX_BID",
                "ask",
                "ASK",
                "PX_ASK",
                "mid",
                "MID",
                "PX_MID",
                "last",
                "PX_LAST",
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
        kind = str(row.get("kind", "")).strip().lower()
        strike = row.get("strike")
        opt_ticker = str(row.get("option_ticker", "") or "").strip()
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


def register_callbacks(
    app,
    cache_get,
    cache_put,
    bloomberg_available: bool,
    bbg_resolve_security=None,
    bbg_fetch_spot=None,
) -> None:
    @app.callback(
        Output(ID.PAGE_DASHBOARD, "style"),
        Output(ID.PAGE_BLOOMBERG, "style"),
        Output(ID.PAGE_REPORT, "style"),
        Input(ID.TABS, "value"),
    )
    def _toggle_pages(tab):
        show = {"display": "block"}
        hide = {"display": "none"}
        if tab == "bloomberg":
            return hide, show, hide
        if tab == "report":
            return hide, hide, show
        return show, hide, hide

    @app.callback(
        Output(ID.DEBUG_CONTAINER, "style"),
        Input(ID.DEBUG_TOGGLE, "value"),
    )
    def _toggle_debug(value):
        if isinstance(value, list):
            enabled = "on" in value or len(value) > 0
        else:
            enabled = bool(value)
        return {"display": "block"} if enabled else {"display": "none"}

    @app.callback(
        Output(ID.CONTROL_PLANE, "style"),
        Input(ID.TABS, "value"),
    )
    def _toggle_control_plane(tab):
        if tab == "dashboard":
            return {"display": "block"}
        return {"display": "none"}

    @app.callback(
        Output("store-shell", "data"),
        Input("btn-sidebar-toggle", "n_clicks"),
        State("store-shell", "data"),
        prevent_initial_call=True,
    )
    def _toggle_sidebar(n_clicks, shell_state):
        state = dict(shell_state) if isinstance(shell_state, dict) else {}
        collapsed = bool(state.get("sidebar_collapsed", False))
        state["sidebar_collapsed"] = not collapsed
        return state

    @app.callback(
        Output("ae-sidebar", "className"),
        Input("store-shell", "data"),
    )
    def _apply_sidebar_class(shell_state):
        collapsed = False
        if isinstance(shell_state, dict):
            collapsed = bool(shell_state.get("sidebar_collapsed"))
        return "ae-sidebar collapsed" if collapsed else "ae-sidebar"

    @app.callback(
        Output(ID.STRATEGY_SUBGROUP, "options"),
        Output(ID.STRATEGY_SUBGROUP, "value"),
        Input(ID.STRATEGY_GROUP, "value"),
        State(ID.STORE_UI, "data"),
    )
    def _update_subgroups(group_value, ui_state):
        subgroups = _safe_list_subgroups(group_value)
        options = [{"label": sg, "value": sg} for sg in subgroups]
        stored_group = None
        stored_value = None
        if isinstance(ui_state, dict):
            stored_group = ui_state.get("strategy_group")
            stored_value = ui_state.get("strategy_subgroup")
        if stored_group == group_value and stored_value in subgroups:
            return options, stored_value
        value = subgroups[0] if subgroups else None
        return options, value

    @app.callback(
        Output(ID.STRATEGY_ID, "options"),
        Output(ID.STRATEGY_ID, "value"),
        Input(ID.STRATEGY_GROUP, "value"),
        Input(ID.STRATEGY_SUBGROUP, "value"),
        State(ID.STORE_UI, "data"),
    )
    def _update_strategies(group_value, subgroup_value, ui_state):
        df = _safe_list_strategies(group_value, subgroup_value)
        if df is None or df.empty:
            return [], None
        options = [
            {"label": row["strategy_name"], "value": int(row["strategy_id"])}
            for _, row in df.iterrows()
        ]
        stored_group = None
        stored_subgroup = None
        stored_value = None
        if isinstance(ui_state, dict):
            stored_group = ui_state.get("strategy_group")
            stored_subgroup = ui_state.get("strategy_subgroup")
            stored_value = ui_state.get("strategy_id")
        try:
            stored_value = int(stored_value) if stored_value is not None else None
        except (TypeError, ValueError):
            stored_value = None
        option_values = {opt["value"] for opt in options}
        if (
            stored_group == group_value
            and stored_subgroup == subgroup_value
            and stored_value in option_values
        ):
            return options, stored_value
        return options, int(df.iloc[0]["strategy_id"])

    @app.callback(
        Output(ID.LEGS_TABLE, "data"),
        Input(ID.STRATEGY_ID, "value"),
        Input(ID.STORE_MARKET, "data"),
        State(ID.SPOT_INPUT, "value"),
        State(ID.PRICING_MODE, "value"),
        State(ID.LEGS_TABLE, "data"),
        State(ID.STORE_UI, "data"),
    )
    def _apply_legs_updates(
        strategy_id, market_data, spot_value, pricing_mode, legs_data, ui_state
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
                position = _row_position(row)
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
                        updated["option_ticker"] = ticker_value
                updated_rows.append(updated)
            return updated_rows
        if trigger_id == ID.STRATEGY_ID or trigger_id is None:
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
            spot = _coerce_float(spot_value) or 100.0
            strategy_df = get_strategy(incoming_strategy_id)
            row = strategy_df.iloc[0].to_dict() if not strategy_df.empty else None
            template_kind = ""
            if isinstance(row, dict):
                template_kind = str(row.get("template_kind") or "").strip().upper()
            legs = _extract_template_legs(row, spot)
            if template_kind == "STOCK_ONLY" or not legs:
                return _empty_leg_rows()
            if len(legs) < 4:
                legs.extend(_empty_leg_rows()[len(legs) :])
            return legs[:4]
        return no_update

    @app.callback(
        Output(ID.STORE_REF, "data"),
        Output(ID.SPOT_STATUS, "children"),
        Input(ID.TICKER_INPUT, "n_submit"),
        Input(ID.TICKER_INPUT, "n_blur"),
        State(ID.TICKER_INPUT, "value"),
        State(ID.STORE_REF, "data"),
        prevent_initial_call=True,
    )
    def _ping_spot(n_submit, n_blur, ticker_value, ref_data):
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

    @app.callback(
        Output(ID.SPOT_INPUT, "value"),
        Input(ID.STORE_REF, "data"),
        prevent_initial_call=True,
    )
    def _display_spot_from_ref(ref_data):
        if not isinstance(ref_data, dict):
            return no_update
        spot = ref_data.get("spot")
        if spot is None:
            return no_update
        try:
            return float(spot)
        except (TypeError, ValueError):
            return no_update

    @app.callback(
        Output(ID.STORE_MARKET, "data"),
        Output(ID.REFRESH_STATUS, "children"),
        Input(ID.BTN_REFRESH, "n_clicks"),
        State(ID.STORE_REF, "data"),
        State(ID.TICKER_INPUT, "value"),
        State(ID.EXPIRY_INPUT, "date"),
        State(ID.PRICING_MODE, "value"),
        State(ID.LEGS_TABLE, "data"),
        prevent_initial_call=True,
    )
    def _refresh_market(n_clicks, ref_data, ticker_value, expiry, pricing_mode, legs_data):
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
        rows = legs_data if isinstance(legs_data, list) else []
        _, market_snapshot, status = refresh_leg_premiums(
            raw_underlying=raw_ticker,
            resolved_underlying=resolved,
            expiry=expiry_value,
            legs_rows=rows,
            pricing_mode=pricing_mode or "mid",
        )
        return to_jsonable(market_snapshot), status

    @app.callback(
        Output(ID.REF_DEBUG, "children"),
        Output(ID.MARKET_DEBUG, "children"),
        Output(ID.REFRESH_DEBUG, "children"),
        Input(ID.STORE_REF, "data"),
        Input(ID.STORE_MARKET, "data"),
    )
    def _render_debug(ref_data, market_data):
        ref_view = "--"
        if isinstance(ref_data, dict):
            ref_view = json.dumps(
                {
                    "raw_ticker": ref_data.get("raw_ticker"),
                    "resolved_ticker": ref_data.get("resolved_ticker"),
                    "status": ref_data.get("status"),
                    "error": ref_data.get("error"),
                    "as_of": ref_data.get("as_of"),
                    "spot": ref_data.get("spot"),
                },
                indent=2,
                sort_keys=True,
            )
        market_view = "--"
        errors = []
        refreshed_at = None
        expiry_value = ""
        if isinstance(market_data, dict):
            expiry_value = str(market_data.get("expiry") or "").strip()
            errors = market_data.get("errors") or []
            refreshed_at = market_data.get("refreshed_at")
            leg_quotes = market_data.get("leg_quotes") or []
            market_view = json.dumps(
                {
                    "refreshed_at": refreshed_at,
                    "resolved_underlying": market_data.get("resolved_underlying"),
                    "market_spot": market_data.get("market_spot"),
                    "leg_quotes_count": len(leg_quotes)
                    if isinstance(leg_quotes, list)
                    else 0,
                    "errors": errors,
                },
                indent=2,
                sort_keys=True,
            )
        expiry_value = _normalize_iso_date(expiry_value)
        if not expiry_value:
            refresh_msg = "Refresh blocked: expiry not available"
        elif errors:
            first_error = errors[0] if errors else "--"
            refresh_msg = f"Refresh completed with {len(errors)} errors: {first_error}"
        elif refreshed_at:
            refresh_msg = f"Refresh OK at {refreshed_at}"
        else:
            refresh_msg = "No market snapshot yet"
        return ref_view, market_view, refresh_msg

    @app.callback(
        Output(ID.BBG_REQUEST_SUMMARY, "children"),
        Output(ID.BBG_UNDERLYING_SUMMARY, "children"),
        Output(ID.BBG_UNDERLYING_JSON, "children"),
        Output(ID.BBG_LEG_QUOTES, "data"),
        Output(ID.BBG_ERRORS, "children"),
        Input(ID.STORE_MARKET, "data"),
        Input(ID.STORE_INPUTS, "data"),
    )
    def _render_market_transparency(market_data, inputs_data):
        market = market_data if isinstance(market_data, dict) else {}
        inputs = inputs_data if isinstance(inputs_data, dict) else {}

        refreshed_at = market.get("refreshed_at")
        raw_ticker = inputs.get("raw_ticker") or inputs.get("ticker")
        resolved = market.get("resolved_underlying") or inputs.get("resolved_ticker")
        expiry_value = inputs.get("expiry")
        errors = market.get("errors") if isinstance(market.get("errors"), list) else []
        errors_count = len(errors)

        leg_tickers = market.get("leg_tickers")
        if not isinstance(leg_tickers, list):
            leg_tickers = []
        if not leg_tickers:
            legs = inputs.get("legs")
            if isinstance(legs, list):
                leg_tickers = [
                    row.get("option_ticker")
                    for row in legs
                    if isinstance(row, dict)
                ]

        tickers_text = ", ".join(
            [t.strip() for t in leg_tickers if isinstance(t, str) and t.strip()]
        )
        if not tickers_text:
            tickers_text = "--"

        leg_quotes = market.get("leg_quotes")
        if not isinstance(leg_quotes, list):
            leg_quotes = []
        quote_count = sum(
            1
            for quote in leg_quotes
            if isinstance(quote, dict) and any(value is not None for value in quote.values())
        )

        def _display(value: object) -> str:
            if value is None or value == "":
                return "--"
            return str(value)

        def _kv(label: str, value: object):
            return html.Div(
                [
                    html.Span(f"{label}: ", className="ae-muted"),
                    html.Span(_display(value)),
                ]
            )

        request_summary = [
            _kv("Refreshed At", refreshed_at),
            _kv("Raw Ticker", raw_ticker),
            _kv("Resolved Underlying", resolved),
            _kv("Expiry", expiry_value),
            _kv("Leg Tickers", tickers_text),
            _kv("Quote Count", quote_count),
            _kv("Errors", errors_count),
        ]

        underlying_profile = market.get("underlying_profile")
        if not isinstance(underlying_profile, dict):
            underlying_profile = {}

        normalized_profile = {
            str(key).upper(): value for key, value in underlying_profile.items()
        }

        def _pick_profile(keys: list[str]) -> object | None:
            for key in keys:
                if key in underlying_profile and underlying_profile[key] not in (None, ""):
                    return underlying_profile[key]
                upper = key.upper()
                if upper in normalized_profile and normalized_profile[upper] not in (None, ""):
                    return normalized_profile[upper]
            return None

        underlying_rows = []
        for label, keys in [
            ("Name", ["name", "NAME", "SECURITY_NAME", "SECURITY_DES"]),
            ("Sector", ["sector", "SECTOR", "GICS_SECTOR_NAME"]),
            ("Industry", ["industry", "INDUSTRY", "GICS_INDUSTRY_NAME"]),
            ("52W High", ["HIGH_52WEEK", "WEEK_52_HIGH", "PX_52W_HIGH"]),
            ("52W Low", ["LOW_52WEEK", "WEEK_52_LOW", "PX_52W_LOW"]),
            ("Dividend Yield", ["DIVIDEND_YIELD", "DVD_YLD"]),
        ]:
            value = _pick_profile(keys)
            if value is not None and value != "":
                underlying_rows.append(_kv(label, value))
        if not underlying_rows:
            underlying_rows = [html.Div("No underlying snapshot.", className="vnext-muted")]

        underlying_json = (
            _safe_json_dumps(underlying_profile) if underlying_profile else "--"
        )

        def _quote_field(quote: dict, keys: list[str]) -> object | None:
            for key in keys:
                if key in quote and quote[key] is not None:
                    return quote[key]
            return None

        quote_rows = []
        row_count = max(len(leg_quotes), len(leg_tickers))
        for idx in range(row_count):
            quote = (
                leg_quotes[idx]
                if idx < len(leg_quotes) and isinstance(leg_quotes[idx], dict)
                else {}
            )
            ticker = leg_tickers[idx] if idx < len(leg_tickers) else None
            row = {
                "leg": idx + 1,
                "option_ticker": ticker or "--",
                "bid": _quote_field(quote, ["bid", "BID", "PX_BID"]),
                "ask": _quote_field(quote, ["ask", "ASK", "PX_ASK"]),
                "mid": _quote_field(quote, ["mid", "MID", "PX_MID"]),
                "last": _quote_field(quote, ["last", "PX_LAST"]),
                "iv": _quote_field(quote, ["iv", "IVOL_MID", "IV_MID", "iv_mid"]),
            }
            for key, value in list(row.items()):
                if value is None:
                    row[key] = "--"
            quote_rows.append(row)

        if errors:
            error_children = html.Ul([html.Li(str(err)) for err in errors])
        else:
            error_children = html.Div("No errors.", className="vnext-muted")

        return request_summary, underlying_rows, underlying_json, quote_rows, error_children

    @app.callback(
        Output(ID.DL_MARKET_JSON, "data"),
        Input(ID.BTN_EXPORT_MARKET_JSON, "n_clicks"),
        State(ID.STORE_INPUTS, "data"),
        State(ID.STORE_MARKET, "data"),
        prevent_initial_call=True,
    )
    def _download_market_snapshot(n_clicks, inputs_data, market_data):
        if not n_clicks:
            return no_update
        exported_at = _utc_now_str()
        bundle = {
            "exported_at": exported_at,
            "inputs": inputs_data if isinstance(inputs_data, dict) else {},
            "market_snapshot": market_data if isinstance(market_data, dict) else {},
        }
        payload = _safe_json_dumps(bundle)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        filename = f"alpha_engine_market_snapshot_{stamp}.json"
        return dcc.send_string(payload, filename=filename)

    @app.callback(
        Output(ID.DL_REPORT_PDF, "data"),
        Output(ID.REPORT_STATUS, "children"),
        Input(ID.BTN_REPORT_PDF, "n_clicks"),
        State(ID.STORE_UI, "data"),
        State(ID.STORE_INPUTS, "data"),
        State(ID.STORE_MARKET, "data"),
        State(ID.STORE_ANALYSIS_KEY, "data"),
        prevent_initial_call=True,
    )
    def _download_report_pdf(
        n_clicks, ui_state, inputs_state, market_data, key_payload
    ):
        if not n_clicks:
            return no_update, no_update
        if not isinstance(key_payload, dict) or key_payload.get("error"):
            return no_update, "Run Analysis first to generate a report."
        key = key_payload.get("key")
        pack = cache_get(key) if key else None
        if not pack:
            return no_update, "Run Analysis first to generate a report."
        try:
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

            template_payload, _ = _render_report_pdf_template(report_model)
            filename = _report_filename(key_payload, pack)
            if template_payload:
                return (
                    dcc.send_bytes(template_payload, filename=filename),
                    "Generated via template renderer.",
                )

            try:
                with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                    tmp_path = tmp.name
                build_report_pdf_v2(tmp_path, report_model=report_model)
                with open(tmp_path, "rb") as handle:
                    payload = handle.read()
            except RuntimeError:
                return (
                    no_update,
                    "PDF export requires reportlab. Install with: pip install reportlab",
                )
            except Exception as exc:
                traceback.print_exc()
                return no_update, f"PDF export error: {type(exc).__name__}: {exc}"
            finally:
                try:
                    if "tmp_path" in locals() and os.path.exists(tmp_path):
                        os.remove(tmp_path)
                except Exception:
                    pass

            return (
                dcc.send_bytes(payload, filename=filename),
                "Template renderer unavailable; using fallback PDF.",
            )
        except Exception as exc:
            traceback.print_exc()
            return no_update, f"PDF export error: {type(exc).__name__}: {exc}"

    @app.callback(
        Output(ID.STORE_ANALYSIS_KEY, "data"),
        Output(ID.STORE_INPUTS, "data"),
        Input(ID.BTN_RUN, "n_clicks"),
        State(ID.STORE_REF, "data"),
        State(ID.TICKER_INPUT, "value"),
        State(ID.SPOT_INPUT, "value"),
        State(ID.EXPIRY_INPUT, "date"),
        State(ID.STOCK_POSITION, "value"),
        State(ID.AVG_COST, "value"),
        State(ID.LEGS_TABLE, "data"),
        State(ID.PRICING_MODE, "value"),
        State(ID.ROI_POLICY, "value"),
        State(ID.VOL_MODE, "value"),
        State(ID.ATM_IV, "value"),
        State(ID.SCENARIO_MODE, "value"),
        State(ID.DOWNSIDE_TGT, "value"),
        State(ID.UPSIDE_TGT, "value"),
        State(ID.STRATEGY_GROUP, "value"),
        State(ID.STRATEGY_SUBGROUP, "value"),
        State(ID.STRATEGY_ID, "value"),
        State(ID.STORE_MARKET, "data"),
        prevent_initial_call=True,
    )
    def _run_analysis(
        n_clicks,
        ref_data,
        ticker_value,
        spot_value,
        expiry,
        stock_position,
        avg_cost,
        legs_table,
        pricing_mode,
        roi_policy,
        vol_mode,
        atm_iv,
        scenario_mode,
        downside_pct,
        upside_pct,
        group_value,
        subgroup_value,
        strategy_id,
        market_data,
    ):
        raw_ticker = (ticker_value or "").strip()
        resolved_ticker = raw_ticker
        if isinstance(ref_data, dict):
            raw_ticker = ref_data.get("raw_ticker") or raw_ticker
            resolved_ticker = ref_data.get("resolved_ticker") or resolved_ticker
        spot = _coerce_float(spot_value) or 0.0
        expiry_value = _normalize_expiry(expiry)
        stock_pos = _coerce_float(stock_position) or 0.0
        avg_cost_val = _coerce_float(avg_cost) or 0.0
        legs_rows = legs_table if isinstance(legs_table, list) else []
        legs: list[OptionLeg] = []
        for row in legs_rows:
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
            "legs": [to_jsonable(row) for row in legs_rows],
            "pricing_mode": pricing_mode,
            "roi_policy": roi_policy,
            "vol_mode": vol_mode,
            "atm_iv": atm_iv,
            "scenario_mode": scenario_mode_ui,
            "scenario_mode_backend": scenario_mode_backend,
            "downside_pct": downside_pct,
            "upside_pct": upside_pct,
            "strategy_group": group_value,
            "strategy_subgroup": subgroup_value,
            "strategy_id": strategy_id,
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
                "Premium ROI selected but net premium is 0; computing ROI using Max Loss until premiums are provided "
                "(enter premiums / Refresh Bloomberg, or choose a different ROI policy)."
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
            "subgroup": subgroup_value,
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
                vol_mode=vol_mode or "atm",
                atm_iv=_coerce_float(atm_iv) or 0.2,
                underlying_profile=underlying_profile,
                bbg_leg_snapshots=bbg_leg_snapshots,
                scenario_mode=scenario_mode_backend,
                downside_tgt=downside_factor,
                upside_tgt=upside_factor,
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

    @app.callback(
        Output(ID.PAYOFF_CHART, "figure"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
        Input(ID.STORE_UI, "data"),
        Input(ID.TABS, "value"),
    )
    def _render_chart(key_payload, ui_state, tab_value):
        if tab_value != "dashboard":
            raise PreventUpdate
        fig = go.Figure()
        ui_state = ui_state if isinstance(ui_state, dict) else {}
        show_options = bool(ui_state.get("show_options", True))
        show_stock = bool(ui_state.get("show_stock", False))
        show_combined = bool(ui_state.get("show_combined", True))
        show_strikes = bool(ui_state.get("show_strikes", True))
        show_breakevens = bool(ui_state.get("show_breakevens", True))
        if not isinstance(key_payload, dict) or key_payload.get("error"):
            if isinstance(key_payload, dict) and key_payload.get("error"):
                fig.update_layout(title=f"Analysis error: {key_payload['error']}")
            else:
                fig.update_layout(title="Run Analysis to view payoff")
            return fig
        pack = cache_get(key_payload.get("key"))
        if not pack:
            fig.update_layout(title="Analysis expired; rerun")
            return fig
        pack_store = analysis_pack_to_store(pack)
        payoff = pack_store.get("payoff") if isinstance(pack_store, dict) else None
        if not isinstance(payoff, dict):
            fig.update_layout(title="No payoff data in analysis_pack")
            return fig
        x = payoff.get("price_grid") or []
        options = payoff.get("options_pnl") or []
        stock = payoff.get("stock_pnl") or []
        combined = payoff.get("combined_pnl") or []
        if not x:
            fig.update_layout(title="No payoff data in analysis_pack")
            return fig
        if show_options and len(options) == len(x):
            fig.add_trace(go.Scatter(x=x, y=options, name="Options PnL"))
        if show_stock and len(stock) == len(x):
            fig.add_trace(go.Scatter(x=x, y=stock, name="Stock PnL"))
        if show_combined and len(combined) == len(x):
            fig.add_trace(go.Scatter(x=x, y=combined, name="Combined PnL"))

        def _numeric_list(values):
            items = []
            for value in values or []:
                num = _coerce_float(value)
                if num is not None:
                    items.append(num)
            return sorted(set(items))

        if show_strikes:
            for strike in _numeric_list(payoff.get("strikes")):
                fig.add_vline(x=strike, line_dash="dot", line_color="#9ca3af")
                fig.add_annotation(x=strike, y=1.02, yref="paper", text=f"K={strike:g}")
        if show_breakevens:
            for be in _numeric_list(payoff.get("breakevens")):
                fig.add_vline(x=be, line_dash="dash", line_color="#f59e0b")
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

        fig.update_layout(title="Payoff at Expiry", height=420, template="plotly_dark")
        return fig

    @app.callback(
        Output(ID.STORE_UI, "data"),
        Input(ID.TICKER_INPUT, "n_submit"),
        Input(ID.TICKER_INPUT, "n_blur"),
        Input(ID.SPOT_INPUT, "value"),
        Input(ID.EXPIRY_INPUT, "date"),
        Input(ID.STRATEGY_GROUP, "value"),
        Input(ID.STRATEGY_SUBGROUP, "value"),
        Input(ID.STRATEGY_ID, "value"),
        Input(ID.STOCK_POSITION, "value"),
        Input(ID.AVG_COST, "value"),
        Input(ID.PRICING_MODE, "value"),
        Input(ID.ROI_POLICY, "value"),
        Input(ID.VOL_MODE, "value"),
        Input(ID.ATM_IV, "value"),
        Input(ID.SCENARIO_MODE, "value"),
        Input(ID.DOWNSIDE_TGT, "value"),
        Input(ID.UPSIDE_TGT, "value"),
        Input(ID.LEGS_TABLE, "data"),
        Input(ID.PNL_TOGGLES, "value"),
        Input(ID.ANNOTATE_TOGGLES, "value"),
        Input(ID.STORE_REF, "data"),
        State(ID.TICKER_INPUT, "value"),
        State(ID.STORE_UI, "data"),
        prevent_initial_call=True,
    )
    def _sync_ui(
        ticker_submit,
        ticker_blur,
        spot_value,
        expiry_value,
        strategy_group,
        strategy_subgroup,
        strategy_id,
        stock_position,
        avg_cost,
        pricing_mode,
        roi_policy,
        vol_mode,
        atm_iv,
        scenario_mode,
        downside_pct,
        upside_pct,
        legs_data,
        pnl_values,
        annotate_values,
        ref_data,
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
            if ID.SPOT_INPUT in triggered:
                spot_from_ref = ref_data.get("spot")
                if spot_from_ref is not None:
                    state["spot"] = spot_from_ref
        value_map = {
            ID.TICKER_INPUT: ("ticker", ticker_value),
        ID.EXPIRY_INPUT: ("expiry", _normalize_iso_date(expiry_value)),
            ID.STRATEGY_GROUP: ("strategy_group", strategy_group),
            ID.STRATEGY_SUBGROUP: ("strategy_subgroup", strategy_subgroup),
            ID.STRATEGY_ID: ("strategy_id", strategy_id),
            ID.STOCK_POSITION: ("stock_position", stock_position),
            ID.AVG_COST: ("avg_cost", avg_cost),
            ID.PRICING_MODE: ("pricing_mode", pricing_mode),
            ID.ROI_POLICY: ("roi_policy", roi_policy),
            ID.VOL_MODE: ("vol_mode", vol_mode),
            ID.ATM_IV: ("atm_iv", atm_iv),
            ID.SCENARIO_MODE: ("scenario_mode", scenario_mode),
            ID.DOWNSIDE_TGT: ("downside_pct", downside_pct),
            ID.UPSIDE_TGT: ("upside_pct", upside_pct),
        }
        for trig_id in triggered:
            if trig_id not in value_map:
                continue
            key, value = value_map[trig_id]
            if value is not None:
                state[key] = value
        pnl_values = pnl_values or []
        annotate_values = annotate_values or []
        if ID.PNL_TOGGLES in triggered or ID.ANNOTATE_TOGGLES in triggered:
            state.update(
                {
                    "show_options": "options" in pnl_values,
                    "show_stock": "stock" in pnl_values,
                    "show_combined": "combined" in pnl_values,
                    "show_strikes": "strikes" in annotate_values,
                    "show_breakevens": "breakevens" in annotate_values,
                }
            )
        if isinstance(current, dict) and state == current:
            return no_update
        return state

    @app.callback(
        Output(ID.TICKER_INPUT, "value"),
        Output(ID.EXPIRY_INPUT, "date"),
        Output(ID.STRATEGY_GROUP, "value"),
        Output(ID.STOCK_POSITION, "value"),
        Output(ID.AVG_COST, "value"),
        Output(ID.PRICING_MODE, "value"),
        Output(ID.ROI_POLICY, "value"),
        Output(ID.VOL_MODE, "value"),
        Output(ID.ATM_IV, "value"),
        Output(ID.SCENARIO_MODE, "value"),
        Output(ID.DOWNSIDE_TGT, "value"),
        Output(ID.UPSIDE_TGT, "value"),
        Output(ID.PNL_TOGGLES, "value"),
        Output(ID.ANNOTATE_TOGGLES, "value"),
        Input(ID.TABS, "value"),
        State(ID.STORE_UI, "data"),
    )
    def _hydrate_ui(tab_value, ui_state):
        hydrate_count = 14
        if tab_value != "dashboard":
            return (no_update,) * hydrate_count
        state = ui_state if isinstance(ui_state, dict) else {}

        def _value(key: str, default):
            if key in state and state[key] is not None:
                return state[key]
            return default

        ticker = _value("ticker", "")
        expiry = _normalize_iso_date(_value("expiry", None))
        strategy_group = _value("strategy_group", None)
        stock_position = _value("stock_position", 0.0)
        avg_cost = _value("avg_cost", 0.0)
        pricing_mode = _value("pricing_mode", "mid")
        roi_policy = _value("roi_policy", "premium")
        vol_mode = _value("vol_mode", "atm")
        atm_iv = _value("atm_iv", 0.2)
        scenario_mode = _value("scenario_mode", "targets")
        downside_pct = _value("downside_pct", -10.0)
        upside_pct = _value("upside_pct", 10.0)

        pnl_values = []
        if _value("show_options", True):
            pnl_values.append("options")
        if _value("show_stock", False):
            pnl_values.append("stock")
        if _value("show_combined", True):
            pnl_values.append("combined")

        annotate_values = []
        if _value("show_strikes", True):
            annotate_values.append("strikes")
        if _value("show_breakevens", True):
            annotate_values.append("breakevens")

        return (
            ticker,
            expiry,
            strategy_group,
            stock_position,
            avg_cost,
            pricing_mode,
            roi_policy,
            vol_mode,
            atm_iv,
            scenario_mode,
            downside_pct,
            upside_pct,
            pnl_values,
            annotate_values,
        )

    @app.callback(
        Output(ID.PANEL_PAYOFF_METRICS, "children"),
        Output(ID.PANEL_MARGIN_CAPITAL, "children"),
        Output(ID.PANEL_DIVIDEND, "children"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
        Input(ID.TABS, "value"),
    )
    def _render_panels(key_payload, tab_value):
        if tab_value != "dashboard":
            raise PreventUpdate
        def _table(headers, rows):
            return html.Table(
                [
                    html.Thead(html.Tr([html.Th(h) for h in headers])),
                    html.Tbody(
                        [html.Tr([html.Td(cell) for cell in row]) for row in rows]
                    ),
                ],
                style={"width": "100%", "fontSize": "12px"},
            )

        if not isinstance(key_payload, dict) or key_payload.get("error"):
            msg = "Run Analysis to view results."
            return html.Div(msg), html.Div(msg), html.Div(msg)
        pack = cache_get(key_payload.get("key"))
        if not pack:
            msg = "Analysis expired; rerun."
            return html.Div(msg), html.Div(msg), html.Div(msg)
        store_pack = analysis_pack_to_store(pack)

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

        def _format_summary_value(metric_label: str, raw_value: object) -> str:
            if raw_value is None or raw_value == "":
                return "--"
            text = str(raw_value).strip()
            metric_key = str(metric_label or "").strip().lower()
            if metric_key in {"max profit", "max loss"}:
                return (
                    _fmt_money_signed(raw_value)
                    if _coerce_float(raw_value) is not None
                    else text
                )
            if metric_key in {"capital basis", "notional exposure"}:
                return (
                    _fmt_money(raw_value)
                    if _coerce_float(raw_value) is not None
                    else text
                )
            if metric_key in {"max roi", "min roi"}:
                return (
                    _fmt_percent_ratio(raw_value)
                    if _coerce_float(raw_value) is not None
                    else text
                )
            if metric_key == "net prem % spot":
                if "%" in text:
                    return text
                return (
                    _fmt_percent_point(raw_value)
                    if _coerce_float(raw_value) is not None
                    else text
                )
            if metric_key == "cost/credit":
                return text
            if metric_key == "pop":
                if "%" in text:
                    return text
                return (
                    _fmt_percent_point(raw_value)
                    if _coerce_float(raw_value) is not None
                    else text
                )
            return text

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
        metrics_table = (
            _table(["Metric", "Options", "Combined"], metrics_rows)
            if metrics_rows
            else html.Div("--")
        )

        margin = store_pack.get("margin", {}) if isinstance(store_pack, dict) else {}
        margin_rows = [
            ["Classification", margin.get("classification", "--")],
            ["Margin Proxy", margin.get("margin_proxy", "--")],
        ]
        margin_table = _table(["Field", "Value"], margin_rows)

        dividend = {}
        underlying = (
            store_pack.get("underlying", {}) if isinstance(store_pack, dict) else {}
        )
        if isinstance(underlying, dict):
            dividend = underlying.get("dividend_risk", {}) or {}
        div_rows = [
            ["Ex-div Date", dividend.get("ex_div_date", "--")],
            ["Days to Dividend", dividend.get("days_to_dividend", "--")],
            ["Before Expiry", dividend.get("before_expiry", "--")],
        ]
        dividend_table = _table(["Field", "Value"], div_rows)

        return metrics_table, margin_table, dividend_table

    @app.callback(
        Output(ID.RISK_BANNER, "children"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
    )
    def _render_risk_banner(key_payload):
        if not isinstance(key_payload, dict) or key_payload.get("error"):
            return html.Div()
        pack = cache_get(key_payload.get("key"))
        if not pack or not isinstance(pack, dict):
            return html.Div()
        underlying = pack.get("underlying", {})
        if not isinstance(underlying, dict):
            return html.Div()
        earnings_risk = underlying.get("earnings_risk", {}) or {}
        dividend_risk = underlying.get("dividend_risk", {}) or {}
        messages = []
        if isinstance(earnings_risk, dict) and earnings_risk.get("before_expiry") is True:
            days = earnings_risk.get("days_to_earnings")
            if days is not None:
                messages.append(
                    html.Div(
                        [
                            html.Span("WARN", className="risk-badge"),
                            html.Span(f"Earnings in {days} days (before expiry)"),
                        ]
                    )
                )
            else:
                messages.append(
                    html.Div(
                        [
                            html.Span("WARN", className="risk-badge"),
                            html.Span("Earnings before expiry"),
                        ]
                    )
                )
        if isinstance(dividend_risk, dict) and dividend_risk.get("before_expiry") is True:
            days = dividend_risk.get("days_to_dividend")
            if days is not None:
                messages.append(
                    html.Div(
                        [
                            html.Span("WARN", className="risk-badge"),
                            html.Span(
                                f"Ex-dividend in {days} days (before expiry)"
                            ),
                        ]
                    )
                )
            else:
                messages.append(
                    html.Div(
                        [
                            html.Span("WARN", className="risk-badge"),
                            html.Span("Ex-dividend date before expiry"),
                        ]
                    )
                )
        if not messages:
            return html.Div()
        return html.Div(
            messages,
            style={
                "padding": "8px",
                "border": "1px solid #f59e0b",
                "borderRadius": "4px",
                "backgroundColor": "#1f2937",
                "marginBottom": "12px",
            },
        )

    @app.callback(
        Output(ID.SCENARIO_CARDS, "children"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
        Input(ID.TABS, "value"),
    )
    def _render_scenario_cards(key_payload, tab_value):
        if tab_value != "dashboard":
            raise PreventUpdate
        if not isinstance(key_payload, dict) or key_payload.get("error"):
            return html.Div("Run Analysis to view scenario commentary.")
        pack = cache_get(key_payload.get("key"))
        if not pack or not isinstance(pack, dict):
            return html.Div("Run Analysis to view scenario commentary.")
        narrative = pack.get("narrative_scenarios")
        if not isinstance(narrative, dict):
            return html.Div("Run Analysis to view scenario commentary.")

        def _card(label, block):
            block = block if isinstance(block, dict) else {}
            title = block.get("title") or label
            condition = block.get("condition") or ""
            body = block.get("body") or "--"
            return html.Div(
                [
                    html.Div(title, style={"fontWeight": "600", "marginBottom": "4px"}),
                    html.Div(condition, style={"fontSize": "12px", "color": "#9ca3af"}),
                    html.Div(body, style={"marginTop": "6px", "fontSize": "12px"}),
                ],
                style={
                    "border": "1px solid #1f2937",
                    "padding": "8px",
                    "borderRadius": "4px",
                    "backgroundColor": "#0f172a",
                },
            )

        return html.Div(
            [
                _card("Bearish Case", narrative.get("bear")),
                _card("Stagnant Case", narrative.get("base")),
                _card("Bullish Case", narrative.get("bull")),
            ],
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(3, 1fr)",
                "gap": "8px",
                "marginBottom": "12px",
            },
        )

    @app.callback(
        Output(ID.PANEL_KEY_LEVELS, "children"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
        Input(ID.TABS, "value"),
    )
    def _render_key_levels(key_payload, tab_value):
        if tab_value != "dashboard":
            raise PreventUpdate
        if not isinstance(key_payload, dict) or key_payload.get("error"):
            return html.Div("Run Analysis to view key levels.")
        pack = cache_get(key_payload.get("key"))
        if not pack or not isinstance(pack, dict):
            return html.Div("Run Analysis to view key levels.")
        key_levels = pack.get("key_levels", {})
        levels = key_levels.get("levels") if isinstance(key_levels, dict) else None
        if not isinstance(levels, list) or not levels:
            return html.Div("--")

        def _fmt_price(value):
            num = _coerce_float(value)
            if num is None:
                return "--"
            return f"{num:.2f}"

        sorted_levels = _sort_key_levels(levels)
        rows = []
        for level in sorted_levels:
            if not isinstance(level, dict):
                continue
            rows.append(
                [
                    level.get("label", "--"),
                    _fmt_price(level.get("price")),
                    _fmt_percent_point(level.get("move_pct")),
                    _fmt_money_signed(level.get("stock_pnl")),
                    _fmt_money_signed(level.get("option_pnl")),
                    _fmt_money_signed(level.get("net_pnl")),
                    _fmt_percent_ratio(level.get("net_roi")),
                    level.get("source", "--"),
                ]
            )
        table = html.Table(
            [
                html.Thead(
                    html.Tr(
                        [
                            html.Th("Label"),
                            html.Th("Price"),
                            html.Th("Move %"),
                            html.Th("Stock PnL"),
                            html.Th("Option PnL"),
                            html.Th("Net PnL"),
                            html.Th("Net ROI"),
                            html.Th("Source"),
                        ]
                    )
                ),
                html.Tbody([html.Tr([html.Td(cell) for cell in row]) for row in rows]),
            ],
            style={"width": "100%", "fontSize": "12px"},
        )
        return html.Div(table, style={"maxHeight": "260px", "overflowY": "auto"})

    @app.callback(
        Output(ID.PANEL_ELIGIBILITY, "children"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
        Input(ID.TABS, "value"),
    )
    def _render_eligibility(key_payload, tab_value):
        if tab_value != "dashboard":
            raise PreventUpdate
        if not isinstance(key_payload, dict) or key_payload.get("error"):
            return html.Div("Run Analysis to view eligibility.")
        pack = cache_get(key_payload.get("key"))
        if not pack or not isinstance(pack, dict):
            return html.Div("Run Analysis to view eligibility.")
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
            return html.Div("Eligibility data unavailable for this strategy.")

        def _format_eligibility(value):
            if value is True:
                return "? Allowed"
            if value is False:
                return "? Not allowed"
            text = str(value).strip().upper()
            if text in {"ALLOWED", "Y", "YES", "TRUE"}:
                return "? Allowed"
            if text in {"RESTRICTED"}:
                return "? Restricted"
            if text in {"NOT_ALLOWED", "N", "NO", "FALSE"}:
                return "? Not allowed"
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
        return html.Table(
            [
                html.Thead(html.Tr([html.Th("Account Type"), html.Th("Eligible")])),
                html.Tbody([html.Tr([html.Td(cell) for cell in row]) for row in rows]),
            ],
            style={"width": "100%", "fontSize": "12px"},
        )

    @app.callback(
        Output(ID.ANALYSIS_KEY_DEBUG, "children"),
        Output(ID.ANALYSIS_PACK_DEBUG, "children"),
        Output(ID.ANALYSIS_RENDER_DEBUG, "children"),
        Input(ID.STORE_ANALYSIS_KEY, "data"),
    )
    def _render_analysis_debug(analysis_key):
        if not isinstance(analysis_key, dict):
            return "--", "--", "No analysis key yet"
        key_json = json.dumps(analysis_key, indent=2, sort_keys=True)
        if analysis_key.get("error"):
            return key_json, "--", f"Analysis error: {analysis_key['error']}"
        key = analysis_key.get("key")
        if not key:
            return key_json, "--", "No analysis key yet"
        pack = cache_get(key)
        if not pack:
            return key_json, "--", "Analysis missing/expired; rerun"
        store_pack = analysis_pack_to_store(pack)

        def _first_last_pairs(x_vals, y_vals, n=5):
            pairs = []
            if isinstance(x_vals, list) and isinstance(y_vals, list):
                for x, y in zip(x_vals, y_vals):
                    pairs.append(
                        {
                            "x": _coerce_float(x),
                            "y": _coerce_float(y),
                        }
                    )
            return {
                "first": pairs[:n],
                "last": pairs[-n:] if len(pairs) > n else pairs,
            }

        payoff = store_pack.get("payoff") if isinstance(store_pack, dict) else {}
        price_grid = payoff.get("price_grid") if isinstance(payoff, dict) else []
        options = payoff.get("options_pnl") if isinstance(payoff, dict) else []
        stock = payoff.get("stock_pnl") if isinstance(payoff, dict) else []
        combined = payoff.get("combined_pnl") if isinstance(payoff, dict) else []
        strikes = payoff.get("strikes") if isinstance(payoff, dict) else []
        breakevens = payoff.get("breakevens") if isinstance(payoff, dict) else []

        scenario_df = {}
        scenario = store_pack.get("scenario") if isinstance(store_pack, dict) else {}
        if isinstance(scenario, dict):
            scenario_df = scenario.get("df") or {}
        scenario_rows = []
        if isinstance(scenario_df, dict) and scenario_df.get("__type__") == "DataFrame":
            scenario_rows = scenario_df.get("records") or []
        if isinstance(scenario_df, list):
            scenario_rows = scenario_df
        scenario_preview = []
        for row in scenario_rows[:8]:
            if not isinstance(row, dict):
                continue
            scenario_preview.append(
                {
                    "price": row.get("price"),
                    "option_pnl": row.get("option_pnl"),
                    "stock_pnl": row.get("stock_pnl"),
                    "combined_pnl": row.get("combined_pnl"),
                    "net_roi": row.get("net_roi"),
                }
            )

        summary_rows = []
        summary = store_pack.get("summary") if isinstance(store_pack, dict) else {}
        if isinstance(summary, dict):
            summary_rows = summary.get("rows") or []

        key_levels_rows = []
        key_levels = store_pack.get("key_levels") if isinstance(store_pack, dict) else {}
        levels = key_levels.get("levels") if isinstance(key_levels, dict) else []
        if isinstance(levels, list):
            for level in levels[:8]:
                if not isinstance(level, dict):
                    continue
                key_levels_rows.append(
                    {
                        "label": level.get("label"),
                        "price": level.get("price"),
                        "net_pnl": level.get("net_pnl"),
                        "net_roi": level.get("net_roi"),
                        "source": level.get("source"),
                    }
                )

        debug_payload = {
            "as_of": pack.get("as_of"),
            "underlying": (
                {
                    "ticker": (pack.get("underlying") or {}).get("ticker"),
                    "resolved": (pack.get("underlying") or {}).get(
                        "resolved_underlying"
                    ),
                    "spot": (pack.get("underlying") or {}).get("spot"),
                }
                if isinstance(pack.get("underlying"), dict)
                else {}
            ),
            "payoff": {
                "len": len(price_grid) if isinstance(price_grid, list) else 0,
                "combined": _first_last_pairs(price_grid, combined),
                "options": _first_last_pairs(price_grid, options),
                "stock": _first_last_pairs(price_grid, stock),
                "strikes": strikes,
                "breakevens": breakevens,
            },
            "summary_rows": summary_rows,
            "key_levels_top": key_levels_rows,
            "scenario_top": scenario_preview,
        }
        return key_json, json.dumps(debug_payload, indent=2, sort_keys=True), "Analysis loaded"
