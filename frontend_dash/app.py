"""Dash frontend scaffold for Options Tool.

Run:
  python -m frontend_dash.app
  python frontend_dash/app.py

This is a minimal, backend-first shell. Run Analysis builds a real analysis_pack.
"""

from datetime import datetime, timezone
import math
from functools import lru_cache
from time import time
import uuid

import plotly.graph_objects as go

from core.analysis_pack import build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.strategy_map import (
    get_strategy,
    list_groups,
    list_strategies,
    list_subgroups,
)
from frontend_dash.analysis_adapter import (
    analysis_pack_to_store,
    refresh_leg_premiums,
    to_jsonable,
)
from frontend_dash.smart_strikes import compute_default_strike, is_number_like

try:
    from adapters.bloomberg import resolve_security as _bbg_resolve_security
    from adapters.bloomberg import fetch_spot as _bbg_fetch_spot
    BLOOMBERG_AVAILABLE = True
except Exception:
    _bbg_resolve_security = None
    _bbg_fetch_spot = None
    BLOOMBERG_AVAILABLE = False

try:
    from dash import Dash, Input, Output, State, dcc, html, dash_table, no_update, ctx
    DASH_AVAILABLE = True
except ModuleNotFoundError:
    DASH_AVAILABLE = False
    Dash = None
    Input = Output = State = None
    dcc = html = dash_table = None
    no_update = None
    ctx = None


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


def _utc_now_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


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


def _safe_list_groups() -> list[str]:
    try:
        return list_groups()
    except Exception:
        return []


@lru_cache(maxsize=64)
def _cached_subgroups(group: str) -> tuple[str, ...]:
    try:
        return tuple(list_subgroups(group))
    except Exception:
        return tuple()


@lru_cache(maxsize=128)
def _cached_strategies(group: str, subgroup: str):
    try:
        return list_strategies(group, subgroup)
    except Exception:
        return None


@lru_cache(maxsize=256)
def _cached_strategy_row(strategy_id: int) -> dict | None:
    try:
        strategy_df = get_strategy(strategy_id)
    except Exception:
        return None
    if strategy_df is None or strategy_df.empty:
        return None
    return to_jsonable(strategy_df.iloc[0].to_dict())


def _safe_list_subgroups(group: str | None) -> list[str]:
    if not group:
        return []
    return list(_cached_subgroups(group))


def _safe_list_strategies(group: str | None, subgroup: str | None):
    if not group or not subgroup:
        return None
    return _cached_strategies(group, subgroup)


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


def _coerce_float(value: object) -> float | None:
    try:
        numeric = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(numeric):
        return None
    return numeric


AE_TABLE_STYLE = {"height": "240px", "overflowY": "auto", "overflowX": "auto"}
AE_TABLE_STYLE_TALL = {"height": "320px", "overflowY": "auto", "overflowX": "auto"}
AE_TABLE_HEADER = {
    "backgroundColor": "#111827",
    "color": "#e5e7eb",
    "fontWeight": "600",
    "border": "1px solid #1f2937",
}
AE_TABLE_CELL = {
    "backgroundColor": "#0f172a",
    "color": "#e5e7eb",
    "fontSize": "12px",
    "padding": "6px",
    "border": "1px solid #1f2937",
}
AE_TABLE_DATA_COND = [
    {"if": {"state": "selected"}, "backgroundColor": "#1f2937"},
    {"if": {"state": "active"}, "backgroundColor": "#111827"},
]


def _df_dict_to_table(
    df_dict: dict, table_id: str, page_size: int = 10, table_style=None
):
    if not isinstance(df_dict, dict) or df_dict.get("__type__") != "DataFrame":
        return html.Div("No data", style={"fontSize": "12px", "color": "#6B7280"})
    columns = df_dict.get("columns") or []
    records = df_dict.get("records") or []
    if not isinstance(columns, list) or not isinstance(records, list):
        return html.Div("No data", style={"fontSize": "12px", "color": "#6B7280"})
    style_table = table_style or AE_TABLE_STYLE_TALL
    return dash_table.DataTable(
        id=table_id,
        columns=[{"name": col, "id": col} for col in columns],
        data=records,
        page_size=page_size,
        style_table=style_table,
        style_header=AE_TABLE_HEADER,
        style_cell=AE_TABLE_CELL,
        style_data_conditional=AE_TABLE_DATA_COND,
        fixed_rows={"headers": True},
    )


def _extract_pop_text(pack: dict) -> str:
    summary = pack.get("summary", {}) if isinstance(pack, dict) else {}
    rows = summary.get("rows", []) if isinstance(summary, dict) else []
    for row in rows:
        if not isinstance(row, dict):
            continue
        metric = str(row.get("metric", "")).lower()
        if "prob" in metric or "pop" in metric:
            value = row.get("combined")
            if value is None:
                value = row.get("options")
            if value is None:
                value = row.get("value")
            if value is not None:
                return str(value)
    if not isinstance(pack, dict):
        return "--"
    probability = pack.get("probability", {})
    for key in ("pop", "pop_text"):
        value = pack.get(key)
        if value is not None:
            return str(value)
    if isinstance(probability, dict):
        for key in ("pop", "pop_text"):
            value = probability.get(key)
            if value is not None:
                return str(value)
    return "--"


def _is_blank(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, float) and math.isnan(value):
        return True
    if isinstance(value, str) and not value.strip():
        return True
    return False


def _blank_leg_rows(count: int) -> list[dict]:
    return [
        {
            "kind": "",
            "position": "",
            "strike": "",
            "premium": "",
            "multiplier": 100,
        }
        for _ in range(count)
    ]


def _select_premium_from_quote(quote: dict, position: float, mode: str) -> float:
    def _get(keys: list[str]) -> float | None:
        for key in keys:
            if key in quote and quote[key] is not None:
                try:
                    return float(quote[key])
                except (TypeError, ValueError):
                    continue
        return None

    bid = _get(["bid", "BID", "PX_BID"])
    ask = _get(["ask", "ASK", "PX_ASK"])
    mid = _get(["mid", "MID", "PX_MID"])
    last = _get(["last", "PX_LAST"])
    avg = (bid + ask) / 2.0 if bid is not None and ask is not None else None
    mode_key = (mode or "").strip().lower()
    if mode_key == "mid":
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


def extract_template_legs_from_row(strategy_row: dict, spot: float) -> list[dict]:
    if not isinstance(strategy_row, dict):
        return []
    legs: list[dict] = []
    for leg_index in range(1, 5):
        leg_type = strategy_row.get(f"leg_{leg_index}_type")
        if _is_blank(leg_type):
            continue
        leg_type_upper = str(leg_type).strip().upper()
        if leg_type_upper in {"STOCK", "SHARES"}:
            continue
        if leg_type_upper not in {"CALL", "PUT", "C", "P"}:
            continue
        kind = "call" if leg_type_upper.startswith("C") else "put"

        side_value = strategy_row.get(f"leg_{leg_index}_side")
        side_upper = str(side_value).strip().upper() if not _is_blank(side_value) else ""
        ratio_value = strategy_row.get(f"leg_{leg_index}_ratio")
        ratio = _coerce_float(ratio_value)
        if ratio is None:
            ratio = 1.0
        position = -ratio if side_upper == "SHORT" else ratio

        strike_field = strategy_row.get(f"leg_{leg_index}_strike")
        if _is_blank(strike_field):
            continue
        strike_tag = None
        if is_number_like(strike_field):
            strike_value = float(strike_field)
        else:
            strike_tag = str(strike_field).strip() or "ATM"
            strike_value = compute_default_strike(spot, strike_tag)

        legs.append(
            {
                "kind": kind,
                "position": float(position),
                "strike": float(strike_value),
                "strike_tag": strike_tag,
                "premium": 0.0,
                "multiplier": 100,
            }
        )
    return legs


def _build_dummy_analysis_pack(ticker: str, spot: float) -> dict:
    spot_value = float(spot) if spot is not None else 0.0
    max_price = max(spot_value * 3.0, 0.0)
    price_grid = [max_price * idx / 120 for idx in range(121)]
    premium = 2.0
    options_pnl = [max(price - spot_value, 0.0) * 100 - premium * 100 for price in price_grid]
    stock_pnl = [0.0 for _ in price_grid]
    combined_pnl = [opt + stk for opt, stk in zip(options_pnl, stock_pnl)]
    return {
        "as_of": _utc_now_str(),
        "underlying": {"ticker": ticker, "spot": spot_value},
        "payoff": {
            "price_grid": price_grid,
            "options_pnl": options_pnl,
            "stock_pnl": stock_pnl,
            "combined_pnl": combined_pnl,
            "strikes": [spot_value],
            "breakevens": [spot_value + premium],
        },
    }


if DASH_AVAILABLE:
    _groups = _safe_list_groups()
    _group_options = [{"label": group, "value": group} for group in _groups]
    _group_value = _groups[0] if _groups else None
    _subgroups = _safe_list_subgroups(_group_value)
    _subgroup_options = [
        {"label": subgroup, "value": subgroup} for subgroup in _subgroups
    ]
    _subgroup_value = _subgroups[0] if _subgroups else None
    _strategies_df = _safe_list_strategies(_group_value, _subgroup_value)
    if _strategies_df is not None and not _strategies_df.empty:
        _strategies_df = _strategies_df.sort_values("strategy_id")
        _strategy_options = [
            {
                "label": f"{int(row['strategy_id'])} - {row['strategy_name']}",
                "value": int(row["strategy_id"]),
            }
            for _, row in _strategies_df.iterrows()
        ]
    else:
        _strategy_options = []
    _strategy_value = _strategy_options[0]["value"] if _strategy_options else None

    builder_layout = html.Div(
        [
            html.H2("Options Strategy Builder (Dash)", className="ae-page-title"),
            html.Div(
                [
                    html.Div(
                        [
                            html.H4("Inputs", className="ae-card-title"),
                            html.Label("Ticker", className="ae-label"),
                            dcc.Input(
                                id="ticker-input",
                                type="text",
                                value="",
                                placeholder="e.g. AAPL US",
                                debounce=True,
                                className="ae-input",
                                style={"width": "100%"},
                            ),
                            html.Label("Group", className="ae-label"),
                            dcc.Dropdown(
                                id="strategy-group",
                                options=_group_options,
                                value=_group_value,
                                clearable=False,
                                className="ae-dropdown",
                            ),
                            html.Label("Subgroup", className="ae-label"),
                            dcc.Dropdown(
                                id="strategy-subgroup",
                                options=_subgroup_options,
                                value=_subgroup_value,
                                clearable=False,
                                className="ae-dropdown",
                            ),
                            html.Label("Strategy", className="ae-label"),
                            dcc.Dropdown(
                                id="strategy-id",
                                options=_strategy_options,
                                value=_strategy_value,
                                clearable=False,
                                className="ae-dropdown",
                            ),
                            html.Label("Expiry", className="ae-label"),
                            dcc.Input(
                                id="expiry-input",
                                type="text",
                                value="",
                                placeholder="YYYY-MM-DD",
                                className="ae-input",
                                style={"width": "100%"},
                            ),
                            html.Label("Spot", className="ae-label"),
                            dcc.Input(
                                id="spot-input",
                                type="number",
                                value=100.0,
                                min=0,
                                step=1.0,
                                className="ae-input",
                                style={"width": "100%"},
                            ),
                            html.Div(
                                id="spot-status",
                                style={"fontSize": "12px", "marginTop": "4px"},
                            ),
                            html.Label("Stock position", className="ae-label"),
                            dcc.Input(
                                id="stock-position-input",
                                type="number",
                                value=0.0,
                                step=1.0,
                                className="ae-input",
                                style={"width": "100%"},
                            ),
                            html.Label("Avg cost", className="ae-label"),
                            dcc.Input(
                                id="avg-cost-input",
                                type="number",
                                value=0.0,
                                step=1.0,
                                className="ae-input",
                                style={"width": "100%"},
                            ),
                            html.Label("Option legs", className="ae-label"),
                            dash_table.DataTable(
                                id="legs-table",
                                columns=[
                                    {
                                        "name": "Kind",
                                        "id": "kind",
                                        "presentation": "dropdown",
                                    },
                                    {"name": "Position", "id": "position"},
                                    {"name": "Strike", "id": "strike"},
                                    {"name": "Premium", "id": "premium"},
                                    {"name": "Multiplier", "id": "multiplier"},
                                ],
                                data=[
                                    {
                                        "kind": "call",
                                        "position": 1.0,
                                        "strike": 100.0,
                                        "premium": 2.0,
                                        "multiplier": 100,
                                    }
                                ],
                                dropdown={
                                    "kind": {
                                        "options": [
                                            {"label": "call", "value": "call"},
                                            {"label": "put", "value": "put"},
                                        ]
                                    }
                                },
                                editable=True,
                                style_table=AE_TABLE_STYLE,
                                style_header=AE_TABLE_HEADER,
                                style_cell=AE_TABLE_CELL,
                                style_data_conditional=AE_TABLE_DATA_COND,
                                fixed_rows={"headers": True},
                            ),
                            html.Label("Pricing mode", className="ae-label"),
                            dcc.Dropdown(
                                id="pricing-mode-input",
                                options=[
                                    {"label": "Mid", "value": "mid"},
                                    {"label": "Bid/Ask", "value": "bid_ask"},
                                ],
                                value="mid",
                                clearable=False,
                                className="ae-dropdown",
                            ),
                            html.Label("ROI policy", className="ae-label"),
                            dcc.Dropdown(
                                id="roi-policy-input",
                                options=[
                                    {"label": "premium", "value": "premium"},
                                    {"label": "capital", "value": "capital"},
                                    {"label": "net", "value": "net"},
                                ],
                                value="premium",
                                clearable=False,
                                className="ae-dropdown",
                            ),
                            html.Label("Vol mode", className="ae-label"),
                            dcc.Dropdown(
                                id="vol-mode-input",
                                options=[
                                    {"label": "atm", "value": "atm"},
                                    {"label": "per_leg", "value": "per_leg"},
                                ],
                                value="atm",
                                clearable=False,
                                className="ae-dropdown",
                            ),
                            html.Label("Scenario mode", className="ae-label"),
                            dcc.Dropdown(
                                id="scenario-mode-input",
                                options=[
                                    {"label": "targets", "value": "targets"},
                                    {"label": "strikes", "value": "strikes"},
                                    {"label": "breakevens", "value": "breakevens"},
                                ],
                                value="targets",
                                clearable=False,
                                className="ae-dropdown",
                            ),
                            html.Label("ATM IV", className="ae-label"),
                            dcc.Input(
                                id="atm-iv-input",
                                type="number",
                                value=0.20,
                                min=0,
                                step=0.01,
                                className="ae-input",
                                style={"width": "100%"},
                            ),
                            html.Label("Downside target (%)", className="ae-label"),
                            dcc.Input(
                                id="downside-tgt-input",
                                type="number",
                                value=-10.0,
                                step=1.0,
                                className="ae-input",
                                style={"width": "100%"},
                            ),
                            html.Label("Upside target (%)", className="ae-label"),
                            dcc.Input(
                                id="upside-tgt-input",
                                type="number",
                                value=10.0,
                                step=1.0,
                                className="ae-input",
                                style={"width": "100%"},
                            ),
                            html.Div(style={"height": "12px"}),
                            html.Button(
                                "Refresh Bloomberg Data",
                                id="refresh-button",
                                n_clicks=0,
                                className="ae-btn ae-btn-secondary",
                                style={"width": "100%"},
                            ),
                            html.Div(id="refresh-status", style={"marginTop": "8px"}),
                            html.Button(
                                "Run Analysis",
                                id="run-analysis-button",
                                n_clicks=0,
                                className="ae-btn ae-btn-primary",
                                style={"width": "100%", "marginTop": "8px"},
                            ),
                        ],
                        className="ae-card",
                        style={"flex": "1"},
                    ),
                    html.Div(
                        [
                            html.H4("Payoff", className="ae-card-title"),
                            dcc.Graph(
                                id="payoff-chart",
                                figure=go.Figure(),
                                style={"height": "460px"},
                            ),
                        ],
                        className="ae-card",
                        style={"flex": "2.2"},
                    ),
                    html.Div(
                        [
                            html.H4("View", className="ae-card-title"),
                            dcc.Checklist(
                                id="pnl-toggles",
                                options=[
                                    {"label": "Show Options PnL", "value": "options"},
                                    {"label": "Show Stock PnL", "value": "stock"},
                                    {"label": "Show Combined PnL", "value": "combined"},
                                ],
                                value=["options", "combined"],
                                labelStyle={"display": "block"},
                            ),
                            html.Div(style={"height": "12px"}),
                            html.Div(id="as-of-display", children="As of: --"),
                            html.H4("Results", className="ae-card-title", style={"marginTop": "12px"}),
                            dcc.Tabs(
                                id="results-tabs",
                                value="summary",
                                className="ae-tabs",
                                children=[
                                    dcc.Tab(
                                        label="Summary",
                                        value="summary",
                                        className="ae-tab",
                                        selected_className="ae-tab ae-tab--selected",
                                    ),
                                    dcc.Tab(
                                        label="Scenario",
                                        value="scenario",
                                        className="ae-tab",
                                        selected_className="ae-tab ae-tab--selected",
                                    ),
                                    dcc.Tab(
                                        label="Key Levels",
                                        value="key_levels",
                                        className="ae-tab",
                                        selected_className="ae-tab ae-tab--selected",
                                    ),
                                    dcc.Tab(
                                        label="Margin / POP",
                                        value="margin_pop",
                                        className="ae-tab",
                                        selected_className="ae-tab ae-tab--selected",
                                    ),
                                ],
                            ),
                            html.Div(id="results-content", style={"marginTop": "8px"}),
                        ],
                        className="ae-card",
                        style={"flex": "1"},
                    ),
                ],
                style={"display": "flex", "gap": "12px"},
            ),
        ],
        style={"padding": "16px", "fontFamily": "Arial, sans-serif"},
    )

    app.layout = html.Div(
        className="alpha-engine ae-shell",
        children=[
            dcc.Store(
                id="store-inputs",
                data={
                    "ticker": "",
                    "spot": 100.0,
                    "expiry": "",
                    "stock_position": 0.0,
                    "avg_cost": 0.0,
                    "legs": [
                        {
                            "kind": "call",
                            "position": 1.0,
                            "strike": 100.0,
                            "premium": 2.0,
                            "multiplier": 100,
                        }
                    ],
                    "pricing_mode": "mid",
                    "roi_policy": "premium",
                    "vol_mode": "atm",
                    "atm_iv": 0.20,
                    "scenario_mode": "targets",
                    "downside_tgt": -10.0,
                    "upside_tgt": 10.0,
                },
            ),
            dcc.Store(id="store-ref"),
            dcc.Store(id="store-market"),
            dcc.Store(id="store-analysis-key"),
            dcc.Store(id="store-analysis-pack"),
            dcc.Store(
                id="store-ui",
                data={"show_options": True, "show_stock": False, "show_combined": True},
            ),
            dcc.Store(
                id="store-shell",
                data={
                    "sidebar_collapsed": False,
                    "active_module": "structuring",
                    "active_structuring_tab": "builder",
                },
            ),
            html.Div(
                id="ae-sidebar",
                className="ae-sidebar",
                children=[
                    html.Div(
                        [
                            html.Div("ALPHA ENGINE", className="ae-brand"),
                            html.Button(
                                "≡",
                                id="btn-sidebar-toggle",
                                className="ae-collapse-btn",
                            ),
                        ],
                        className="ae-sidebar-header",
                    ),
                    html.Div(
                        [
                            html.Button(
                                "Overview Map",
                                id="btn-module-overview",
                                className="ae-nav-btn",
                            ),
                            html.Button(
                                "Structuring Lab",
                                id="btn-module-structuring",
                                className="ae-nav-btn",
                            ),
                            html.Button(
                                "Client Intelligence",
                                id="btn-module-client",
                                className="ae-nav-btn",
                            ),
                            html.Button(
                                "Content Factory",
                                id="btn-module-content",
                                className="ae-nav-btn",
                            ),
                            html.Button(
                                "Lifecycle Mgmt",
                                id="btn-module-lifecycle",
                                className="ae-nav-btn",
                            ),
                        ],
                        className="ae-nav",
                    ),
                ],
            ),
            html.Div(
                className="ae-main",
                children=[
                    html.Div(
                        className="ae-header",
                        children=[
                            html.Div(id="breadcrumbs", className="ae-breadcrumbs"),
                            html.Div(id="market-status-chip", className="ae-chip"),
                        ],
                    ),
                    html.Div(
                        className="ae-canvas",
                        children=[
                            html.Div(
                                id="module-overview",
                                children=[
                                    html.H3("Overview Map"),
                                    html.P("Module coming next."),
                                ],
                                style={},
                            ),
                            html.Div(
                                id="module-structuring",
                                children=[
                                    dcc.Tabs(
                                        id="structuring-tabs",
                                        value="builder",
                                        className="ae-tabs",
                                        children=[
                                            dcc.Tab(
                                                label="Strategy Builder",
                                                value="builder",
                                                className="ae-tab",
                                                selected_className="ae-tab ae-tab--selected",
                                            ),
                                            dcc.Tab(
                                                label="Market Data",
                                                value="data",
                                                className="ae-tab",
                                                selected_className="ae-tab ae-tab--selected",
                                            ),
                                            dcc.Tab(
                                                label="Client Report",
                                                value="report",
                                                className="ae-tab",
                                                selected_className="ae-tab ae-tab--selected",
                                            ),
                                        ],
                                    ),
                                    html.Div(
                                        id="structuring-builder-container",
                                        children=[builder_layout],
                                    ),
                                    html.Div(
                                        id="structuring-data-container",
                                        children=[
                                            html.H3("Market Data"),
                                            html.Div(id="structuring-data-summary"),
                                        ],
                                    ),
                                    html.Div(
                                        id="structuring-report-container",
                                        children=[
                                            html.H3("Client Report"),
                                            html.P(
                                                "Generate PDF Report (coming next step)."
                                            ),
                                            html.Div(id="structuring-report-summary"),
                                        ],
                                    ),
                                ],
                                style={},
                            ),
                            html.Div(
                                id="module-client",
                                children=[
                                    html.H3("Client Intelligence"),
                                    html.P("Module coming next."),
                                ],
                                style={},
                            ),
                            html.Div(
                                id="module-content",
                                children=[
                                    html.H3("Content Factory"),
                                    html.P("Module coming next."),
                                ],
                                style={},
                            ),
                            html.Div(
                                id="module-lifecycle",
                                children=[
                                    html.H3("Lifecycle Management"),
                                    html.P("Module coming next."),
                                ],
                                style={},
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )
    app.validation_layout = app.layout


if DASH_AVAILABLE:
    def _default_shell_state(state: dict | None) -> dict:
        base = {
            "sidebar_collapsed": False,
            "active_module": "structuring",
            "active_structuring_tab": "builder",
        }
        if isinstance(state, dict):
            base.update({k: v for k, v in state.items() if k in base})
        return base

    @app.callback(
        Output("store-shell", "data"),
        Input("btn-sidebar-toggle", "n_clicks"),
        Input("btn-module-overview", "n_clicks"),
        Input("btn-module-structuring", "n_clicks"),
        Input("btn-module-client", "n_clicks"),
        Input("btn-module-content", "n_clicks"),
        Input("btn-module-lifecycle", "n_clicks"),
        Input("structuring-tabs", "value"),
        State("store-shell", "data"),
        prevent_initial_call=True,
    )
    def _update_shell_state(
        toggle_clicks: int,
        overview_clicks: int,
        structuring_clicks: int,
        client_clicks: int,
        content_clicks: int,
        lifecycle_clicks: int,
        structuring_tab: str,
        shell_state: dict,
    ) -> dict:
        state = _default_shell_state(shell_state)
        trigger_id = ctx.triggered_id if ctx else None
        if trigger_id == "btn-sidebar-toggle":
            state["sidebar_collapsed"] = not state.get("sidebar_collapsed", False)
        elif trigger_id == "btn-module-overview":
            state["active_module"] = "overview"
        elif trigger_id == "btn-module-structuring":
            state["active_module"] = "structuring"
        elif trigger_id == "btn-module-client":
            state["active_module"] = "client"
        elif trigger_id == "btn-module-content":
            state["active_module"] = "content"
        elif trigger_id == "btn-module-lifecycle":
            state["active_module"] = "lifecycle"
        elif trigger_id == "structuring-tabs":
            state["active_structuring_tab"] = structuring_tab or "builder"
        return to_jsonable(state)

    @app.callback(
        Output("module-overview", "style"),
        Output("module-structuring", "style"),
        Output("module-client", "style"),
        Output("module-content", "style"),
        Output("module-lifecycle", "style"),
        Output("structuring-builder-container", "style"),
        Output("structuring-data-container", "style"),
        Output("structuring-report-container", "style"),
        Output("breadcrumbs", "children"),
        Output("market-status-chip", "children"),
        Output("ae-sidebar", "className"),
        Input("store-shell", "data"),
        Input("store-market", "data"),
    )
    def _render_shell(
        shell_state: dict,
        market_data: dict,
    ) -> tuple[dict, dict, dict, dict, dict, dict, dict, dict, str, str, str]:
        state = _default_shell_state(shell_state)
        active_module = state.get("active_module", "structuring")
        active_tab = state.get("active_structuring_tab", "builder")

        def _module_style(name: str) -> dict:
            return {"display": "block"} if active_module == name else {"display": "none"}

        def _tab_style(name: str) -> dict:
            return {"display": "block"} if active_tab == name else {"display": "none"}

        module_overview = _module_style("overview")
        module_structuring = _module_style("structuring")
        module_client = _module_style("client")
        module_content = _module_style("content")
        module_lifecycle = _module_style("lifecycle")

        builder_style = _tab_style("builder")
        data_style = _tab_style("data")
        report_style = _tab_style("report")

        module_label = {
            "overview": "Overview Map",
            "structuring": "Structuring Lab",
            "client": "Client Intelligence",
            "content": "Content Factory",
            "lifecycle": "Lifecycle Mgmt",
        }.get(active_module, "Structuring Lab")
        tab_label = {
            "builder": "Strategy Builder",
            "data": "Market Data",
            "report": "Client Report",
        }.get(active_tab, "")
        breadcrumbs = (
            f"Dashboard / {module_label} / {tab_label}"
            if active_module == "structuring"
            else f"Dashboard / {module_label}"
        )

        refreshed_at = None
        if isinstance(market_data, dict):
            refreshed_at = market_data.get("refreshed_at")
        market_chip = "MARKET LIVE"
        if refreshed_at:
            market_chip = f"MARKET LIVE • {refreshed_at}"

        sidebar_class = "ae-sidebar"
        if state.get("sidebar_collapsed"):
            sidebar_class = "ae-sidebar collapsed"

        return (
            module_overview,
            module_structuring,
            module_client,
            module_content,
            module_lifecycle,
            builder_style,
            data_style,
            report_style,
            breadcrumbs,
            market_chip,
            sidebar_class,
        )

    @app.callback(
        Output("structuring-data-summary", "children"),
        Input("store-market", "data"),
    )
    def _render_market_summary(market_data: dict):
        if not isinstance(market_data, dict):
            return html.P("No snapshot data available.")
        refreshed_at = market_data.get("refreshed_at") or "--"
        resolved = market_data.get("resolved_underlying") or "--"
        spot = market_data.get("market_spot")
        spot_text = spot if spot is not None else "--"
        leg_quotes = market_data.get("leg_quotes") or []
        quote_count = len([q for q in leg_quotes if isinstance(q, dict) and q])
        errors = market_data.get("errors") or []
        items = [
            html.Li(f"Refreshed at: {refreshed_at}"),
            html.Li(f"Resolved underlying: {resolved}"),
            html.Li(f"Snapshot spot: {spot_text}"),
            html.Li(f"Leg quotes populated: {quote_count}"),
        ]
        if errors:
            items.append(html.Li(f"Errors: {len(errors)}"))
        return html.Ul(items)

    @app.callback(
        Output("structuring-report-summary", "children"),
        Input("store-analysis-key", "data"),
    )
    def _render_report_summary(analysis_key: dict):
        if not isinstance(analysis_key, dict):
            return html.P("Run Analysis to view report context.")
        if analysis_key.get("error"):
            return html.P(f"Analysis error: {analysis_key.get('error')}")
        key = analysis_key.get("key")
        pack = _cache_get(key)
        if not isinstance(pack, dict):
            return html.P("Analysis expired; rerun.")
        as_of = pack.get("as_of") or "--"
        underlying = pack.get("underlying") or {}
        ticker = underlying.get("ticker") or underlying.get("resolved_underlying") or "--"
        return html.Ul([html.Li(f"As of: {as_of}"), html.Li(f"Ticker: {ticker}")])

    @app.callback(
        Output("strategy-subgroup", "options"),
        Output("strategy-subgroup", "value"),
        Input("strategy-group", "value"),
        State("strategy-subgroup", "value"),
    )
    def _update_subgroup_options(group: str, current_value: str):
        subgroups = _safe_list_subgroups(group)
        options = [{"label": subgroup, "value": subgroup} for subgroup in subgroups]
        value = current_value if current_value in subgroups else None
        if value is None and subgroups:
            value = subgroups[0]
        return options, value

    @app.callback(
        Output("strategy-id", "options"),
        Output("strategy-id", "value"),
        Input("strategy-group", "value"),
        Input("strategy-subgroup", "value"),
        State("strategy-id", "value"),
    )
    def _update_strategy_options(
        group: str, subgroup: str, current_value: int
    ):
        strategies_df = _safe_list_strategies(group, subgroup)
        options = []
        if strategies_df is not None and not strategies_df.empty:
            strategies_df = strategies_df.sort_values("strategy_id")
            options = [
                {
                    "label": f"{int(row['strategy_id'])} - {row['strategy_name']}",
                    "value": int(row["strategy_id"]),
                }
                for _, row in strategies_df.iterrows()
            ]
        option_values = [opt["value"] for opt in options]
        value = current_value if current_value in option_values else None
        if value is None and option_values:
            value = option_values[0]
        return options, value

    @app.callback(
        Output("store-ref", "data"),
        Output("spot-input", "value"),
        Output("spot-status", "children"),
        Input("ticker-input", "n_submit"),
        Input("ticker-input", "n_blur"),
        State("ticker-input", "value"),
        State("store-ref", "data"),
        prevent_initial_call=True,
    )
    def _ping_spot(n_submit: int, n_blur: int, ticker_value: str, ref_data: dict):
        raw_ticker = (ticker_value or "").strip()
        if not raw_ticker:
            return no_update, no_update, "Enter a ticker"
        if len(raw_ticker) < 2:
            return no_update, no_update, "Ticker incomplete"
        prop_id = ctx.triggered[0]["prop_id"] if ctx and ctx.triggered else ""
        is_submit = prop_id.endswith(".n_submit")
        last_raw = ""
        if isinstance(ref_data, dict):
            last_raw = str(ref_data.get("raw_ticker", "")).strip()
        if not is_submit and last_raw and last_raw == raw_ticker:
            return no_update, no_update, no_update
        if not BLOOMBERG_AVAILABLE or _bbg_resolve_security is None:
            return no_update, no_update, "Bloomberg unavailable (offline mode)"
        try:
            resolved = _bbg_resolve_security(raw_ticker)
            spot_result = _bbg_fetch_spot(resolved)
            spot_value, as_of = _normalize_spot_result(spot_result)
            if spot_value is None:
                raise ValueError("Spot not available")
            as_of_text = as_of or _utc_now_str()
            return (
                to_jsonable(
                    {
                        "raw_ticker": raw_ticker,
                        "resolved_ticker": resolved,
                        "spot": spot_value,
                        "as_of": as_of_text,
                        "status": "ok",
                        "error": None,
                    }
                ),
                spot_value,
                f"Spot updated ({as_of_text})",
            )
        except Exception as exc:
            return (
                to_jsonable(
                    {
                        "raw_ticker": raw_ticker,
                        "resolved_ticker": None,
                        "spot": None,
                        "as_of": _utc_now_str(),
                        "status": "error",
                        "error": str(exc),
                    }
                ),
                no_update,
                f"Spot fetch failed for {raw_ticker}",
            )

    @app.callback(
        Output("legs-table", "data"),
        Input("strategy-id", "value"),
        Input("store-market", "data"),
        State("spot-input", "value"),
        State("pricing-mode-input", "value"),
        State("legs-table", "data"),
        prevent_initial_call=True,
    )
    def _update_legs_table(
        strategy_id: int,
        market_data: dict,
        spot: float,
        pricing_mode: str,
        legs_data: list[dict],
    ) -> list[dict]:
        trigger_id = ctx.triggered_id if ctx else None
        if trigger_id == "strategy-id":
            if strategy_id is None:
                return no_update
            spot_for_defaults = _coerce_float(spot) or 100.0
            strategy_row = _cached_strategy_row(strategy_id)
            if not strategy_row:
                return no_update
            template_kind = str(strategy_row.get("template_kind", "")).strip().upper()
            template_legs = extract_template_legs_from_row(
                strategy_row, spot_for_defaults
            )
            if template_kind == "STOCK_ONLY" or not template_legs:
                return _blank_leg_rows(4)
            return template_legs
        if trigger_id != "store-market":
            return no_update
        if not isinstance(market_data, dict):
            return no_update
        leg_quotes = market_data.get("leg_quotes")
        if not isinstance(leg_quotes, list) or not leg_quotes:
            return no_update
        if not isinstance(legs_data, list):
            return no_update
        mode = str(pricing_mode or "mid").strip().lower()
        updated_rows = []
        for idx, row in enumerate(legs_data):
            if not isinstance(row, dict):
                updated_rows.append(row)
                continue
            quote = (
                leg_quotes[idx]
                if idx < len(leg_quotes) and isinstance(leg_quotes[idx], dict)
                else {}
            )
            try:
                position = float(row.get("position") or 0.0)
            except (TypeError, ValueError):
                position = 0.0
            premium = _select_premium_from_quote(quote, position, mode)
            updated_row = dict(row)
            updated_row["premium"] = abs(float(premium))
            updated_rows.append(updated_row)
        return updated_rows

    @app.callback(
        Output("store-market", "data"),
        Output("refresh-status", "children"),
        Input("refresh-button", "n_clicks"),
        State("store-ref", "data"),
        State("ticker-input", "value"),
        State("expiry-input", "value"),
        State("pricing-mode-input", "value"),
        State("legs-table", "data"),
        prevent_initial_call=True,
    )
    def _refresh_market(
        n_clicks: int,
        ref_data: dict,
        ticker_value: str,
        expiry: str,
        pricing_mode: str,
        legs_data: list[dict],
    ) -> tuple[dict, str]:
        raw_ticker = str(ticker_value or "").strip()
        resolved_ticker = None
        if isinstance(ref_data, dict):
            ref_raw = str(ref_data.get("raw_ticker") or "").strip()
            if ref_raw:
                raw_ticker = ref_raw
            ref_resolved = ref_data.get("resolved_ticker")
            if ref_resolved:
                resolved_ticker = ref_resolved
        expiry = expiry or None
        pricing_mode = str(pricing_mode or "mid").strip().lower()
        source_legs = legs_data if isinstance(legs_data, list) else []
        if not expiry:
            return no_update, "Refresh failed: expiry required"
        _, market_snapshot, status = refresh_leg_premiums(
            raw_underlying=raw_ticker,
            resolved_underlying=resolved_ticker,
            expiry=expiry,
            legs_rows=source_legs,
            pricing_mode=pricing_mode,
        )
        store_market = {
            "resolved_underlying": market_snapshot.get("resolved_underlying"),
            "market_spot": market_snapshot.get("market_spot"),
            "underlying_profile": market_snapshot.get("underlying_profile"),
            "per_leg_iv": market_snapshot.get("per_leg_iv"),
            "leg_quotes": market_snapshot.get("leg_quotes"),
            "refreshed_at": market_snapshot.get("refreshed_at"),
            "errors": market_snapshot.get("errors"),
        }
        return to_jsonable(store_market), status

    @app.callback(
        Output("store-analysis-pack", "data"),
        Output("store-inputs", "data"),
        Input("run-analysis-button", "n_clicks"),
        State("store-ref", "data"),
        State("ticker-input", "value"),
        State("spot-input", "value"),
        State("expiry-input", "value"),
        State("stock-position-input", "value"),
        State("avg-cost-input", "value"),
        State("legs-table", "data"),
        State("pricing-mode-input", "value"),
        State("roi-policy-input", "value"),
        State("vol-mode-input", "value"),
        State("atm-iv-input", "value"),
        State("scenario-mode-input", "value"),
        State("downside-tgt-input", "value"),
        State("upside-tgt-input", "value"),
        State("strategy-group", "value"),
        State("strategy-subgroup", "value"),
        State("strategy-id", "value"),
        State("store-market", "data"),
        prevent_initial_call=True,
    )
    def _run_analysis(
        n_clicks: int,
        ref_data: dict,
        ticker_value: str,
        spot: float,
        expiry: str,
        stock_position: float,
        avg_cost: float,
        legs_table_data: list[dict],
        pricing_mode: str,
        roi_policy: str,
        vol_mode: str,
        atm_iv: float,
        scenario_mode: str,
        downside_tgt: float,
        upside_tgt: float,
        strategy_group: str,
        strategy_subgroup: str,
        strategy_id: int,
        market_data: dict,
    ) -> tuple[dict, dict]:
        raw_ticker = str(ticker_value or "").strip()
        resolved_ticker = None
        if isinstance(ref_data, dict):
            ref_raw = str(ref_data.get("raw_ticker") or "").strip()
            if ref_raw:
                raw_ticker = ref_raw
            ref_resolved = ref_data.get("resolved_ticker")
            if ref_resolved:
                resolved_ticker = ref_resolved
        if not resolved_ticker:
            resolved_ticker = raw_ticker

        spot_value = _coerce_float(spot)
        if spot_value is None:
            spot_value = 0.0
        stock_position_value = _coerce_float(stock_position) or 0.0
        avg_cost_value = _coerce_float(avg_cost) or 0.0
        expiry_value = str(expiry or "")
        pricing_mode_value = str(pricing_mode or "mid")
        roi_policy_value = str(roi_policy or "premium")
        vol_mode_value = str(vol_mode or "atm")
        atm_iv_value = _coerce_float(atm_iv) or 0.0
        scenario_mode_value = str(scenario_mode or "targets")
        downside_pct = _coerce_float(downside_tgt) or 0.0
        upside_pct = _coerce_float(upside_tgt) or 0.0
        downside_factor = max(1e-6, 1.0 + (downside_pct / 100.0))
        upside_factor = max(1e-6, 1.0 + (upside_pct / 100.0))

        strategy_row = _cached_strategy_row(strategy_id) if strategy_id else None
        strategy_name = ""
        template_kind = None
        if isinstance(strategy_row, dict):
            strategy_name = str(strategy_row.get("strategy_name", "")).strip()
            template_kind = str(strategy_row.get("template_kind", "")).strip().upper()
        strategy_row = to_jsonable(strategy_row) if isinstance(strategy_row, dict) else None

        legs_data = legs_table_data if isinstance(legs_table_data, list) else []
        legs = []
        sanitized_legs = []
        net_premium_per_share = 0.0
        for row in legs_data:
            if not isinstance(row, dict):
                continue
            kind = str(row.get("kind", "")).strip().lower()
            if kind not in {"call", "put"}:
                continue
            try:
                position = float(row.get("position"))
                strike = float(row.get("strike"))
                premium = float(row.get("premium"))
            except (TypeError, ValueError):
                continue
            try:
                multiplier = int(row.get("multiplier", 100) or 100)
            except (TypeError, ValueError):
                multiplier = 100
            strike_tag = row.get("strike_tag")
            sanitized_legs.append(
                {
                    "kind": kind,
                    "position": position,
                    "strike": strike,
                    "strike_tag": strike_tag,
                    "premium": premium,
                    "multiplier": multiplier,
                }
            )
            net_premium_per_share -= position * premium
            legs.append(
                OptionLeg(
                    kind=kind,
                    position=position,
                    strike=strike,
                    premium=premium,
                    multiplier=multiplier,
                )
            )

        inputs_snapshot = to_jsonable(
            {
                "ticker": raw_ticker,
                "raw_ticker": raw_ticker,
                "resolved_ticker": resolved_ticker or raw_ticker,
                "spot": spot_value,
                "expiry": expiry_value,
                "stock_position": stock_position_value,
                "avg_cost": avg_cost_value,
                "legs": sanitized_legs,
                "pricing_mode": pricing_mode_value,
                "roi_policy": roi_policy_value,
                "vol_mode": vol_mode_value,
                "atm_iv": atm_iv_value,
                "scenario_mode": scenario_mode_value,
                "downside_tgt": downside_pct,
                "upside_tgt": upside_pct,
                "strategy_group": strategy_group,
                "strategy_subgroup": strategy_subgroup,
                "strategy_id": strategy_id,
                "strategy_name": strategy_name,
                "template_kind": template_kind,
                "strategy_row": strategy_row,
            }
        )

        roi_policy_key = roi_policy_value.strip().lower()
        if roi_policy_key == "premium" and abs(net_premium_per_share) < 1e-9:
            return (
                {
                    "error": (
                        "Net premium is 0 under ROI policy Premium. Enter premiums "
                        "(or Fetch Bloomberg Data) or choose a different ROI policy."
                    ),
                    "as_of": _utc_now_str(),
                },
                inputs_snapshot,
            )

        strategy_input = StrategyInput(
            spot=spot_value,
            stock_position=stock_position_value,
            avg_cost=avg_cost_value,
            legs=legs,
        )
        strategy_meta = {
            "as_of": _utc_now_str(),
            "expiry": expiry_value,
            "underlying_ticker": raw_ticker,
            "resolved_underlying": resolved_ticker,
            "strategy_name": strategy_name,
            "strategy_id": strategy_id,
            "group": strategy_group,
            "subgroup": strategy_subgroup,
            "strategy_row": strategy_row,
        }
        underlying_profile = {}
        bbg_leg_snapshots = None
        if isinstance(market_data, dict):
            underlying_profile = market_data.get("underlying_profile", {})
            per_leg_iv = market_data.get("per_leg_iv")
            leg_quotes = market_data.get("leg_quotes")
            if per_leg_iv is not None or leg_quotes is not None:
                bbg_leg_snapshots = {
                    "per_leg_iv": per_leg_iv,
                    "leg_quotes": leg_quotes,
                }
        pricing_map = {"mid": "MID", "bid_ask": "DEALABLE"}
        roi_map = {
            "premium": "NET_PREMIUM",
            "capital": "RISK_MAX_LOSS",
            "net": "MARGIN_PROXY",
        }
        vol_map = {"atm": "ATM", "per_leg": "VEGA_WEIGHTED"}
        try:
            pack = build_analysis_pack(
                strategy_input=strategy_input,
                strategy_meta=strategy_meta,
                pricing_mode=pricing_map.get(pricing_mode_value, pricing_mode_value),
                roi_policy=roi_map.get(roi_policy_value, roi_policy_value),
                vol_mode=vol_map.get(vol_mode_value, vol_mode_value),
                atm_iv=atm_iv_value,
                underlying_profile=underlying_profile,
                bbg_leg_snapshots=bbg_leg_snapshots,
                scenario_mode=scenario_mode_value,
                downside_tgt=downside_factor,
                upside_tgt=upside_factor,
            )
            return analysis_pack_to_store(pack), inputs_snapshot
        except Exception as exc:
            return {"error": str(exc)}, inputs_snapshot

    @app.callback(
        Output("store-ui", "data"),
        Input("pnl-toggles", "value"),
    )
    def _update_ui_toggles(values: list[str]) -> dict:
        selected = set(values or [])
        return to_jsonable(
            {
                "show_options": "options" in selected,
                "show_stock": "stock" in selected,
                "show_combined": "combined" in selected,
            }
        )

    @app.callback(
        Output("payoff-chart", "figure"),
        Input("store-analysis-key", "data"),
        Input("store-ui", "data"),
    )
    def _render_chart(analysis_key: dict, ui_state: dict) -> go.Figure:
        fig = go.Figure()
        if not isinstance(analysis_key, dict):
            fig.update_layout(title="Run Analysis to view payoff")
            return fig
        if analysis_key.get("error"):
            fig.update_layout(title=f"Analysis error: {analysis_key['error']}")
            return fig
        key = analysis_key.get("key")
        pack = _cache_get(key)
        if not isinstance(pack, dict):
            fig.update_layout(title="Analysis expired; rerun")
            return fig
        payoff = pack.get("payoff")
        if not isinstance(payoff, dict):
            fig.update_layout(title="Run Analysis to view payoff")
            return fig
        price_grid = to_jsonable(payoff.get("price_grid") or [])
        options_pnl = to_jsonable(payoff.get("options_pnl") or [])
        stock_pnl = to_jsonable(payoff.get("stock_pnl") or [])
        combined_pnl = to_jsonable(payoff.get("combined_pnl") or [])
        if not isinstance(price_grid, list) or not price_grid:
            fig.update_layout(title="Run Analysis to view payoff")
            return fig
        show_options = bool((ui_state or {}).get("show_options", True))
        show_stock = bool((ui_state or {}).get("show_stock", False))
        show_combined = bool((ui_state or {}).get("show_combined", True))
        if show_options:
            fig.add_trace(
                go.Scatter(
                    x=price_grid,
                    y=options_pnl,
                    mode="lines",
                    name="Options PnL",
                )
            )
        if show_stock:
            fig.add_trace(
                go.Scatter(
                    x=price_grid,
                    y=stock_pnl,
                    mode="lines",
                    name="Stock PnL",
                )
            )
        if show_combined:
            fig.add_trace(
                go.Scatter(
                    x=price_grid,
                    y=combined_pnl,
                    mode="lines",
                    name="Combined PnL",
                )
            )
        fig.update_layout(
            xaxis_title="Underlying Price at Expiry",
            yaxis_title="PnL",
            height=460,
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={"color": "#e5e7eb"},
            margin={"l": 40, "r": 20, "t": 30, "b": 40},
        )
        return fig

    @app.callback(
        Output("as-of-display", "children"),
        Input("store-analysis-key", "data"),
    )
    def _render_as_of(analysis_key: dict) -> str:
        if isinstance(analysis_key, dict):
            if analysis_key.get("error"):
                return "As of: --"
            key = analysis_key.get("key")
            pack = _cache_get(key)
            if isinstance(pack, dict):
                as_of = pack.get("as_of")
                if as_of:
                    return f"As of: {as_of}"
        return "As of: --"

    @app.callback(
        Output("results-content", "children"),
        Input("store-analysis-key", "data"),
        Input("results-tabs", "value"),
    )
    def _render_results(analysis_key: dict, tab: str):
        if not isinstance(analysis_key, dict):
            return html.Div("Run Analysis to view results", style={"fontSize": "12px"})
        if analysis_key.get("error"):
            return html.Div(
                f"Analysis error: {analysis_key['error']}",
                style={"fontSize": "12px"},
            )
        key = analysis_key.get("key")
        pack = _cache_get(key)
        if not isinstance(pack, dict):
            return html.Div("Analysis expired; rerun", style={"fontSize": "12px"})
        pack_json = analysis_pack_to_store(pack)
        if tab == "summary":
            summary = pack_json.get("summary", {}) if isinstance(pack_json, dict) else {}
            rows = summary.get("rows", []) if isinstance(summary, dict) else []
            table = dash_table.DataTable(
                columns=[
                    {"name": "Metric", "id": "metric"},
                    {"name": "Options", "id": "options"},
                    {"name": "Combined", "id": "combined"},
                ],
                data=rows if isinstance(rows, list) else [],
                style_table=AE_TABLE_STYLE,
                style_header=AE_TABLE_HEADER,
                style_cell=AE_TABLE_CELL,
                style_data_conditional=AE_TABLE_DATA_COND,
                fixed_rows={"headers": True},
                page_size=10,
            )
            net_total = summary.get("net_premium_total")
            net_per_share = summary.get("net_premium_per_share")
            return html.Div(
                [
                    table,
                    html.Div(
                        f"Net premium total: {net_total}",
                        style={"fontSize": "12px", "marginTop": "6px"},
                    ),
                    html.Div(
                        f"Net premium per share: {net_per_share}",
                        style={"fontSize": "12px"},
                    ),
                ]
            )
        if tab == "scenario":
            scenario = pack_json.get("scenario", {}) if isinstance(pack_json, dict) else {}
            df_dict = None
            if isinstance(scenario, dict):
                df_dict = scenario.get("top10") or scenario.get("df")
            if isinstance(df_dict, dict) and df_dict.get("__type__") == "DataFrame":
                columns = df_dict.get("columns") or []
                filtered_columns = [
                    col for col in columns if str(col).lower() != "commentary"
                ]
                records = df_dict.get("records") or []
                if filtered_columns:
                    records = [
                        {key: row.get(key) for key in filtered_columns}
                        for row in records
                        if isinstance(row, dict)
                    ]
                if isinstance(records, list) and len(records) > 10:
                    records = records[:10]
                df_dict = {
                    "__type__": "DataFrame",
                    "columns": filtered_columns or columns,
                    "records": records,
                }
            return _df_dict_to_table(
                df_dict, "scenario-table", page_size=10, table_style=AE_TABLE_STYLE_TALL
            )
        if tab == "key_levels":
            levels = []
            key_levels = pack_json.get("key_levels", {}) if isinstance(pack_json, dict) else {}
            if isinstance(key_levels, dict):
                levels = key_levels.get("levels") or []
            rows = []
            if isinstance(levels, list):
                for row in levels:
                    if not isinstance(row, dict):
                        continue
                    rows.append(
                        {
                            "label": row.get("label") or row.get("scenario"),
                            "price": row.get("price"),
                            "move_pct": row.get("move_pct"),
                            "net_pnl": row.get("net_pnl"),
                            "net_roi": row.get("net_roi"),
                            "source": row.get("source"),
                        }
                    )
            return dash_table.DataTable(
                columns=[
                    {"name": "Label", "id": "label"},
                    {"name": "Price", "id": "price"},
                    {"name": "Move %", "id": "move_pct"},
                    {"name": "Net PnL", "id": "net_pnl"},
                    {"name": "Net ROI", "id": "net_roi"},
                    {"name": "Source", "id": "source"},
                ],
                data=rows,
                style_table=AE_TABLE_STYLE_TALL,
                style_header=AE_TABLE_HEADER,
                style_cell=AE_TABLE_CELL,
                style_data_conditional=AE_TABLE_DATA_COND,
                fixed_rows={"headers": True},
                page_size=10,
            )
        if tab == "margin_pop":
            margin = pack.get("margin", {}) if isinstance(pack, dict) else {}
            classification = (
                margin.get("classification", "--") if isinstance(margin, dict) else "--"
            )
            margin_proxy = (
                margin.get("margin_proxy", "--") if isinstance(margin, dict) else "--"
            )
            pop_text = _extract_pop_text(pack)
            return html.Div(
                [
                    html.Div(f"Classification: {classification}", style={"fontSize": "12px"}),
                    html.Div(f"Margin proxy: {margin_proxy}", style={"fontSize": "12px"}),
                    html.Div(f"PoP: {pop_text}", style={"fontSize": "12px"}),
                ]
            )
        return html.Div("No data", style={"fontSize": "12px", "color": "#6B7280"})


if __name__ == "__main__":
    if not DASH_AVAILABLE:
        raise SystemExit("Dash is not installed. Install 'dash' to run the app.")
    app.run_server(debug=True, port=8050)
