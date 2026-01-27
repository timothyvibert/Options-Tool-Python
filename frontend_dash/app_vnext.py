"""Minimal Dash vNext for Options Tool.

Run:
  python -m frontend_dash.app_vnext
"""

from __future__ import annotations

from time import time
import math
import uuid

from core.strategy_map import list_groups, list_strategies, list_subgroups
from frontend_dash.smart_strikes import compute_default_strike
from frontend_dash.vnext import ids as ID

try:
    from adapters.bloomberg import resolve_security as _bbg_resolve_security
    from adapters.bloomberg import fetch_spot as _bbg_fetch_spot
    BLOOMBERG_AVAILABLE = True
except Exception:
    _bbg_resolve_security = None
    _bbg_fetch_spot = None
    BLOOMBERG_AVAILABLE = False

try:
    from dash import Dash, dcc, html, dash_table
    DASH_AVAILABLE = True
except ModuleNotFoundError:
    DASH_AVAILABLE = False
    Dash = None
    dcc = html = dash_table = None


class _DashStub:
    def __init__(self) -> None:
        self.layout = None

    def callback(self, *args, **kwargs):
        def _wrapper(func):
            return func

        return _wrapper

    def run_server(self, *args, **kwargs) -> None:
        raise RuntimeError("Dash is not installed. Install 'dash' to run the app.")


app = Dash(__name__) if DASH_AVAILABLE else _DashStub()

if DASH_AVAILABLE:
    import plotly.graph_objects as go
    from frontend_dash.vnext.layout import (
        get_validation_layout,
        layout_bloomberg as vnext_layout_bloomberg,
        layout_dashboard as vnext_layout_dashboard,
        layout_report as vnext_layout_report,
    )
    from frontend_dash.vnext.callbacks import register_callbacks
else:
    get_validation_layout = None
    vnext_layout_bloomberg = None
    vnext_layout_dashboard = None
    vnext_layout_report = None

    def layout_dashboard():
        return None

    def layout_bloomberg(*args, **kwargs):
        return None

    def layout_report():
        return None


_ANALYSIS_CACHE: dict[str, dict] = {}
_ANALYSIS_CACHE_TS: dict[str, float] = {}
MAX_CACHE_ENTRIES = 20
CACHE_TTL_SECONDS = 1800


def _cache_prune() -> None:
    now = time()
    expired = [
        key
        for key, ts in _ANALYSIS_CACHE_TS.items()
        if now - ts > CACHE_TTL_SECONDS
    ]
    for key in expired:
        _ANALYSIS_CACHE.pop(key, None)
        _ANALYSIS_CACHE_TS.pop(key, None)
    if len(_ANALYSIS_CACHE_TS) > MAX_CACHE_ENTRIES:
        ordered = sorted(_ANALYSIS_CACHE_TS.items(), key=lambda item: item[1])
        for key, _ in ordered[: len(ordered) - MAX_CACHE_ENTRIES]:
            _ANALYSIS_CACHE.pop(key, None)
            _ANALYSIS_CACHE_TS.pop(key, None)


def _cache_put(pack: dict) -> str:
    _cache_prune()
    key = uuid.uuid4().hex
    _ANALYSIS_CACHE[key] = pack
    _ANALYSIS_CACHE_TS[key] = time()
    _cache_prune()
    return key


def _cache_get(key: str | None) -> dict | None:
    if not key:
        return None
    _cache_prune()
    return _ANALYSIS_CACHE.get(key)


CARD_STYLE = {
    "border": "1px solid #1f2937",
    "padding": "8px",
    "borderRadius": "4px",
    "backgroundColor": "#0f172a",
}
CARD_TITLE_STYLE = {"fontWeight": "600", "marginBottom": "6px"}


def _safe_list_groups() -> list[str]:
    try:
        return list_groups()
    except Exception:
        return []


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


def _default_blank_legs(spot: float) -> list[dict]:
    strike = compute_default_strike(spot, "ATM")
    return [
        {
            "kind": "call",
            "side": "Long",
            "qty": 1,
            "strike": float(strike),
            "premium": 0.0,
            "multiplier": 100,
            "override": False,
            "option_ticker": "",
        }
        for _ in range(4)
    ]


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


def _coerce_float(value: object) -> float | None:
    try:
        numeric = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(numeric):
        return None
    return numeric


def _quote_value(quote: dict, keys: list[str]) -> float | None:
    for key in keys:
        if key in quote and quote[key] is not None:
            value = _coerce_float(quote[key])
            if value is not None:
                return value
    return None


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


_groups = _safe_list_groups()
_default_group = _groups[0] if _groups else None
_default_subgroups = _safe_list_subgroups(_default_group)
_default_subgroup = _default_subgroups[0] if _default_subgroups else None
_default_strategy_df = _safe_list_strategies(_default_group, _default_subgroup)
if _default_strategy_df is not None and not _default_strategy_df.empty:
    _default_strategy_id = int(_default_strategy_df.iloc[0]["strategy_id"])
else:
    _default_strategy_id = None


_layout_dashboard = (
    html.Div(
        children=[
            html.Div(
                id="page-dashboard",
                children=[
                    html.H2("Options Strategy Builder (vNext)"),
                    html.Div(id="risk-events-banner"),
                    html.Div(
                        children=[
                            dcc.Graph(
                                id="payoff-chart",
                                figure=go.Figure(),
                                style={"height": "420px"},
                            ),
                            html.Div(
                                style={
                                    "display": "grid",
                                    "gridTemplateColumns": "1fr 1fr",
                                    "gap": "8px",
                                    "marginTop": "8px",
                                },
                                children=[
                                    dcc.Checklist(
                                        id="pnl-toggles",
                                        options=[
                                            {"label": "Options", "value": "options"},
                                            {"label": "Stock", "value": "stock"},
                                            {"label": "Combined", "value": "combined"},
                                        ],
                                        value=["options", "combined"],
                                        style={"fontSize": "12px"},
                                    ),
                                    dcc.Checklist(
                                        id="annotate-toggles",
                                        options=[
                                            {"label": "Strikes", "value": "strikes"},
                                            {"label": "Breakevens", "value": "breakevens"},
                                        ],
                                        value=["strikes", "breakevens"],
                                        style={"fontSize": "12px"},
                                    ),
                                ],
                            ),
                            html.H4("Payoff & Metrics"),
                            html.Div(id="panel-payoff-metrics"),
                            html.H4("Margin & Capital"),
                            html.Div(id="panel-margin-capital"),
                            html.H4("Dividend"),
                            html.Div(id="panel-dividend"),
                            html.H4("Account Eligibility"),
                            html.Div(id="panel-eligibility"),
                        ],
                    ),
                ],
            ),
            html.H3("Scenario Commentary"),
            html.Div(id="scenario-cards"),
            html.H3("Key Levels"),
            html.Div(id="panel-key-levels"),
        ],
    )
    if DASH_AVAILABLE
    else None
)

def layout_dashboard():
    if not DASH_AVAILABLE or vnext_layout_dashboard is None:
        return None
    return vnext_layout_dashboard()

def layout_bloomberg(bloomberg_available: bool | None = None):
    if not DASH_AVAILABLE or vnext_layout_bloomberg is None:
        return None
    if bloomberg_available is None:
        bloomberg_available = BLOOMBERG_AVAILABLE
    return vnext_layout_bloomberg(bloomberg_available)


def layout_report():
    if not DASH_AVAILABLE or vnext_layout_report is None:
        return None
    return vnext_layout_report()


if DASH_AVAILABLE:
    _base_layout = html.Div(
        children=[
            dcc.Tabs(
                id="vnext-tabs",
                value="dashboard",
                children=[
                    dcc.Tab(label="Dashboard", value="dashboard"),
                    dcc.Tab(label="Bloomberg Data", value="bloomberg"),
                    dcc.Tab(label="Client Report", value="report"),
                ],
            ),
            html.Div(
                id="control-plane",
                style={"display": "none"},
                children=[
                    dcc.Store(id="store-ref"),
                    dcc.Store(id="store-market"),
                    dcc.Store(id="store-analysis-key"),
                    dcc.Store(id="store-inputs"),
                    dcc.Store(
                        id="store-ui",
                        data={
                            "show_options": True,
                            "show_stock": False,
                            "show_combined": True,
                            "show_strikes": True,
                            "show_breakevens": True,
                        },
                    ),
                ],
            ),
            html.Div(id="vnext-page"),
        ]
    )
    app.layout = _base_layout
    app.validation_layout = get_validation_layout(_base_layout, BLOOMBERG_AVAILABLE)
    register_callbacks(
        app,
        _cache_get,
        _cache_put,
        BLOOMBERG_AVAILABLE,
        _bbg_resolve_security,
        _bbg_fetch_spot,
    )
else:
    app.layout = None


def _route_tabs(tab):
    if tab == "bloomberg":
        return layout_bloomberg()
    if tab == "report":
        return layout_report()
    return layout_dashboard()


def _toggle_debug(value):
    if isinstance(value, list):
        enabled = "on" in value or len(value) > 0
    else:
        enabled = bool(value)
    return {"display": "block"} if enabled else {"display": "none"}


def _toggle_control_plane(tab):
    if tab == "dashboard":
        return {"display": "block"}
    return {"display": "none"}


def _update_subgroups(group_value):
    subgroups = _safe_list_subgroups(group_value)
    options = [{"label": sg, "value": sg} for sg in subgroups]
    value = subgroups[0] if subgroups else None
    return options, value


def _update_strategies(group_value, subgroup_value):
    df = _safe_list_strategies(group_value, subgroup_value)
    if df is None or df.empty:
        return [], None
    options = [
        {"label": row["strategy_name"], "value": int(row["strategy_id"])}
        for _, row in df.iterrows()
    ]
    return options, int(df.iloc[0]["strategy_id"])


def _apply_legs_updates(
    strategy_id, market_data, spot_value, pricing_mode, legs_data
):
    trigger_id = ctx.triggered_id if ctx else None
    if trigger_id == "store-market":
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
            premium = _select_premium_from_quote(quote, position, pricing_mode or "mid")
            updated = dict(row)
            updated["premium"] = abs(float(premium))
            if idx < len(leg_tickers):
                updated["option_ticker"] = leg_tickers[idx]
            updated_rows.append(updated)
        return updated_rows
    if trigger_id == "strategy-id" or trigger_id is None:
        if not strategy_id:
            return no_update
        spot = _coerce_float(spot_value) or 100.0
        strategy_df = get_strategy(strategy_id)
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


def _ping_spot(n_submit, n_blur, ticker_value, ref_data):
    raw_ticker = (ticker_value or "").strip()
    if not raw_ticker:
        return no_update, no_update, "Enter a ticker"
    trigger = ctx.triggered[0]["prop_id"] if ctx and ctx.triggered else ""
    is_submit = trigger.endswith(".n_submit")
    last_ticker = None
    if isinstance(ref_data, dict):
        last_ticker = ref_data.get("raw_ticker")
    if not is_submit and last_ticker == raw_ticker:
        return no_update, no_update, no_update
    if not BLOOMBERG_AVAILABLE or _bbg_resolve_security is None or _bbg_fetch_spot is None:
        return no_update, no_update, "Bloomberg unavailable (offline mode)"
    try:
        resolved = _bbg_resolve_security(raw_ticker)
        spot_result = _bbg_fetch_spot(resolved)
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
        return to_jsonable(store_ref), spot_value, f"Spot updated ({as_of_text})"
    except Exception as exc:
        store_ref = {
            "raw_ticker": raw_ticker,
            "resolved_ticker": None,
            "spot": None,
            "as_of": _utc_now_str(),
            "status": "error",
            "error": str(exc),
        }
        return to_jsonable(store_ref), no_update, f"Spot fetch failed for {raw_ticker}"


def _refresh_market(n_clicks, ref_data, ticker_value, expiry, pricing_mode, legs_data):
    raw_ticker = ""
    resolved = None
    if isinstance(ref_data, dict):
        raw_ticker = ref_data.get("raw_ticker") or ""
        resolved = ref_data.get("resolved_ticker")
    if not raw_ticker:
        raw_ticker = (ticker_value or "").strip()
    expiry_value = (expiry or "").strip()
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


def _render_debug(ref_data, market_data, expiry):
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
    if isinstance(market_data, dict):
        errors = market_data.get("errors") or []
        refreshed_at = market_data.get("refreshed_at")
        leg_quotes = market_data.get("leg_quotes") or []
        market_view = json.dumps(
            {
                "refreshed_at": refreshed_at,
                "resolved_underlying": market_data.get("resolved_underlying"),
                "market_spot": market_data.get("market_spot"),
                "leg_quotes_count": len(leg_quotes) if isinstance(leg_quotes, list) else 0,
                "errors": errors,
            },
            indent=2,
            sort_keys=True,
        )
    expiry_value = (expiry or "").strip()
    if not expiry_value:
        refresh_msg = "Refresh blocked: expiry required (YYYY-MM-DD)"
    elif errors:
        first_error = errors[0] if errors else "--"
        refresh_msg = f"Refresh completed with {len(errors)} errors: {first_error}"
    elif refreshed_at:
        refresh_msg = f"Refresh OK at {refreshed_at}"
    else:
        refresh_msg = "No market snapshot yet"
    return ref_view, market_view, refresh_msg


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
    expiry_value = (expiry or "").strip()
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
    scenario_mode_backend = "INFINITY" if scenario_mode_ui == "infinity" else "targets"

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
    if roi_policy_ui == "premium" and abs(net_premium_per_share) < 1e-9:
        error = (
            "Net premium is 0 under ROI policy Premium. Enter premiums (or Refresh Bloomberg) "
            "or choose a different ROI policy."
        )
        return {"key": None, "as_of": _utc_now_str(), "error": error}, to_jsonable(
            inputs_snapshot
        )

    roi_map = {
        "premium": "NET_PREMIUM",
        "max_loss": "RISK_MAX_LOSS",
        "cash_secured": "CASH_SECURED",
        "margin": "MARGIN_PROXY",
    }
    roi_backend = roi_map.get(roi_policy_ui, "NET_PREMIUM")
    inputs_snapshot["roi_policy_ui"] = roi_policy_ui
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

    key = _cache_put(pack)
    return {"key": key, "as_of": _utc_now_str(), "error": None}, to_jsonable(
        inputs_snapshot
    )


def _render_chart(key_payload, ui_state):
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
    pack = _cache_get(key_payload.get("key"))
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
    fig.update_layout(title="Payoff at Expiry", height=420, template="plotly_dark")
    return fig


def _sync_ui(pnl_values, annotate_values, current):
    pnl_values = pnl_values or []
    annotate_values = annotate_values or []
    state = dict(current) if isinstance(current, dict) else {}
    state.update(
        {
            "show_options": "options" in pnl_values,
            "show_stock": "stock" in pnl_values,
            "show_combined": "combined" in pnl_values,
            "show_strikes": "strikes" in annotate_values,
            "show_breakevens": "breakevens" in annotate_values,
        }
    )
    return state


def _render_panels(key_payload):
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
    pack = _cache_get(key_payload.get("key"))
    if not pack:
        msg = "Analysis expired; rerun."
        return html.Div(msg), html.Div(msg), html.Div(msg)
    store_pack = analysis_pack_to_store(pack)

    summary = store_pack.get("summary", {}) if isinstance(store_pack, dict) else {}
    summary_rows = summary.get("rows") if isinstance(summary, dict) else []
    metrics_rows = []
    for row in summary_rows or []:
        if not isinstance(row, dict):
            continue
        metric = row.get("metric") or row.get("label") or row.get("Metric") or ""
        metrics_rows.append(
            [
                metric,
                row.get("options") or row.get("Options") or "--",
                row.get("combined") or row.get("Combined") or row.get("net") or "--",
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
    underlying = store_pack.get("underlying", {}) if isinstance(store_pack, dict) else {}
    if isinstance(underlying, dict):
        dividend = underlying.get("dividend_risk", {}) or {}
    div_rows = [
        ["Ex-div Date", dividend.get("ex_div_date", "--")],
        ["Days to Dividend", dividend.get("days_to_dividend", "--")],
        ["Before Expiry", dividend.get("before_expiry", "--")],
    ]
    dividend_table = _table(["Field", "Value"], div_rows)

    return metrics_table, margin_table, dividend_table


def _render_risk_banner(key_payload):
    if not isinstance(key_payload, dict) or key_payload.get("error"):
        return html.Div()
    pack = _cache_get(key_payload.get("key"))
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
                html.Div(f"⚠️ Earnings in {days} days (before expiry)")
            )
        else:
            messages.append(html.Div("⚠️ Earnings before expiry"))
    if isinstance(dividend_risk, dict) and dividend_risk.get("before_expiry") is True:
        days = dividend_risk.get("days_to_dividend")
        if days is not None:
            messages.append(
                html.Div(f"⚠️ Ex-dividend in {days} days (before expiry)")
            )
        else:
            messages.append(html.Div("⚠️ Ex-dividend date before expiry"))
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


def _render_scenario_cards(key_payload):
    if not isinstance(key_payload, dict) or key_payload.get("error"):
        return html.Div("Run Analysis to view scenario commentary.")
    pack = _cache_get(key_payload.get("key"))
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


def _render_key_levels(key_payload):
    if not isinstance(key_payload, dict) or key_payload.get("error"):
        return html.Div("Run Analysis to view key levels.")
    pack = _cache_get(key_payload.get("key"))
    if not pack or not isinstance(pack, dict):
        return html.Div("Run Analysis to view key levels.")
    key_levels = pack.get("key_levels", {})
    levels = key_levels.get("levels") if isinstance(key_levels, dict) else None
    if not isinstance(levels, list) or not levels:
        return html.Div("--")
    def _fmt(value, suffix=""):
        num = _coerce_float(value)
        if num is None:
            return "--"
        text = f"{num:.2f}"
        return f"{text}{suffix}" if suffix else text
    sorted_levels = _sort_key_levels(levels)
    rows = []
    for level in sorted_levels:
        if not isinstance(level, dict):
            continue
        rows.append(
            [
                level.get("label", "--"),
                _fmt(level.get("price")),
                _fmt(level.get("move_pct"), "%"),
                _fmt(level.get("stock_pnl")),
                _fmt(level.get("option_pnl")),
                _fmt(level.get("net_pnl")),
                _fmt(level.get("net_roi")),
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
    return html.Div(
        table, style={"maxHeight": "260px", "overflowY": "auto"}
    )


def _render_eligibility(key_payload):
    if not isinstance(key_payload, dict) or key_payload.get("error"):
        return html.Div("Run Analysis to view eligibility.")
    pack = _cache_get(key_payload.get("key"))
    if not pack or not isinstance(pack, dict):
        return html.Div("Run Analysis to view eligibility.")
    store_pack = analysis_pack_to_store(pack)
    eligibility = store_pack.get("eligibility", {}) if isinstance(store_pack, dict) else {}
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
            [rec.get("account_type", "--"), _format_eligibility(rec.get("eligibility"))]
        )
    return html.Table(
        [
            html.Thead(html.Tr([html.Th("Account Type"), html.Th("Eligible")])),
            html.Tbody([html.Tr([html.Td(cell) for cell in row]) for row in rows]),
        ],
        style={"width": "100%", "fontSize": "12px"},
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
    pack = _cache_get(key)
    if not pack:
        return key_json, "--", "Analysis missing/expired; rerun"
    summary = {
        "as_of": pack.get("as_of"),
        "underlying": (
            {
                "ticker": (pack.get("underlying") or {}).get("ticker"),
                "resolved": (pack.get("underlying") or {}).get("resolved_underlying"),
                "spot": (pack.get("underlying") or {}).get("spot"),
            }
            if isinstance(pack.get("underlying"), dict)
            else {}
        ),
        "payoff_keys": list((pack.get("payoff") or {}).keys())
        if isinstance(pack.get("payoff"), dict)
        else [],
        "scenario_df": bool(
            isinstance(pack.get("scenario"), dict)
            and pack.get("scenario", {}).get("df") is not None
        ),
    }
    return key_json, json.dumps(summary, indent=2, sort_keys=True), "Analysis loaded"


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
