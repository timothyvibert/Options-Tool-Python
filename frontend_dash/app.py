"""Dash frontend scaffold for Options Tool.

Run:
  python -m frontend_dash.app
  python frontend_dash/app.py

This is a minimal, backend-first shell. Run Analysis builds a real analysis_pack.
"""

from datetime import datetime, timezone
import math
from functools import lru_cache

import plotly.graph_objects as go

from core.analysis_pack import build_analysis_pack
from core.models import OptionLeg, StrategyInput
from core.strategy_map import (
    get_strategy,
    list_groups,
    list_strategies,
    list_subgroups,
)
from frontend_dash.analysis_adapter import analysis_pack_to_store
from frontend_dash.smart_strikes import compute_default_strike, is_number_like

try:
    from adapters.bloomberg import resolve_security, fetch_spot
except Exception as exc:
    raise RuntimeError(
        "Missing dependency: resolve_security/fetch_spot could not be imported."
    ) from exc

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
    return strategy_df.iloc[0].to_dict()


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


def _df_dict_to_table(df_dict: dict, table_id: str, page_size: int = 10):
    if not isinstance(df_dict, dict) or df_dict.get("__type__") != "DataFrame":
        return html.Div("No data", style={"fontSize": "12px", "color": "#6B7280"})
    columns = df_dict.get("columns") or []
    records = df_dict.get("records") or []
    if not isinstance(columns, list) or not isinstance(records, list):
        return html.Div("No data", style={"fontSize": "12px", "color": "#6B7280"})
    return dash_table.DataTable(
        id=table_id,
        columns=[{"name": col, "id": col} for col in columns],
        data=records,
        page_size=page_size,
        style_table={"overflowX": "auto"},
        style_cell={"fontSize": "12px", "padding": "4px"},
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

    app.layout = html.Div(
        [
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
            dcc.Store(id="store-analysis-pack"),
            dcc.Store(
                id="store-ui",
                data={"show_options": True, "show_stock": False, "show_combined": True},
            ),
            html.H2("Options Strategy Builder (Dash)"),
            html.Div(
                [
                    html.Div(
                        [
                            html.H4("Inputs"),
                            html.Label("Ticker"),
                            dcc.Input(
                                id="ticker-input",
                                type="text",
                                value="",
                                placeholder="e.g. AAPL US",
                                debounce=True,
                                style={"width": "100%"},
                            ),
                            html.Label("Group"),
                            dcc.Dropdown(
                                id="strategy-group",
                                options=_group_options,
                                value=_group_value,
                                clearable=False,
                            ),
                            html.Label("Subgroup"),
                            dcc.Dropdown(
                                id="strategy-subgroup",
                                options=_subgroup_options,
                                value=_subgroup_value,
                                clearable=False,
                            ),
                            html.Label("Strategy"),
                            dcc.Dropdown(
                                id="strategy-id",
                                options=_strategy_options,
                                value=_strategy_value,
                                clearable=False,
                            ),
                            html.Label("Expiry"),
                            dcc.Input(
                                id="expiry-input",
                                type="text",
                                value="",
                                placeholder="YYYY-MM-DD",
                                style={"width": "100%"},
                            ),
                            html.Label("Spot"),
                            dcc.Input(
                                id="spot-input",
                                type="number",
                                value=100.0,
                                min=0,
                                step=1.0,
                                style={"width": "100%"},
                            ),
                            html.Div(
                                id="spot-status",
                                style={"fontSize": "12px", "marginTop": "4px"},
                            ),
                            html.Label("Stock position"),
                            dcc.Input(
                                id="stock-position-input",
                                type="number",
                                value=0.0,
                                step=1.0,
                                style={"width": "100%"},
                            ),
                            html.Label("Avg cost"),
                            dcc.Input(
                                id="avg-cost-input",
                                type="number",
                                value=0.0,
                                step=1.0,
                                style={"width": "100%"},
                            ),
                            html.Label("Option legs"),
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
                                style_table={"overflowX": "auto"},
                            ),
                            html.Label("Pricing mode"),
                            dcc.Dropdown(
                                id="pricing-mode-input",
                                options=[
                                    {"label": "Mid", "value": "mid"},
                                    {"label": "Bid/Ask", "value": "dealable"},
                                ],
                                value="mid",
                                clearable=False,
                            ),
                            html.Label("ROI policy"),
                            dcc.Dropdown(
                                id="roi-policy-input",
                                options=[
                                    {"label": "premium", "value": "premium"},
                                    {"label": "capital", "value": "capital"},
                                    {"label": "net", "value": "net"},
                                ],
                                value="premium",
                                clearable=False,
                            ),
                            html.Label("Vol mode"),
                            dcc.Dropdown(
                                id="vol-mode-input",
                                options=[
                                    {"label": "atm", "value": "atm"},
                                    {"label": "per_leg", "value": "per_leg"},
                                ],
                                value="atm",
                                clearable=False,
                            ),
                            html.Label("Scenario mode"),
                            dcc.Dropdown(
                                id="scenario-mode-input",
                                options=[
                                    {"label": "targets", "value": "targets"},
                                    {"label": "strikes", "value": "strikes"},
                                    {"label": "breakevens", "value": "breakevens"},
                                ],
                                value="targets",
                                clearable=False,
                            ),
                            html.Label("ATM IV"),
                            dcc.Input(
                                id="atm-iv-input",
                                type="number",
                                value=0.20,
                                min=0,
                                step=0.01,
                                style={"width": "100%"},
                            ),
                            html.Label("Downside target (%)"),
                            dcc.Input(
                                id="downside-tgt-input",
                                type="number",
                                value=-10.0,
                                step=1.0,
                                style={"width": "100%"},
                            ),
                            html.Label("Upside target (%)"),
                            dcc.Input(
                                id="upside-tgt-input",
                                type="number",
                                value=10.0,
                                step=1.0,
                                style={"width": "100%"},
                            ),
                            html.Div(style={"height": "12px"}),
                            html.Button(
                                "Refresh Bloomberg Data",
                                id="refresh-button",
                                n_clicks=0,
                                style={"width": "100%"},
                            ),
                            html.Div(id="refresh-status", style={"marginTop": "8px"}),
                            html.Button(
                                "Run Analysis",
                                id="run-analysis-button",
                                n_clicks=0,
                                style={"width": "100%", "marginTop": "8px"},
                            ),
                        ],
                        style={
                            "flex": "1",
                            "padding": "12px",
                            "border": "1px solid #E5E7EB",
                            "borderRadius": "6px",
                        },
                    ),
                    html.Div(
                        [
                            html.H4("Payoff"),
                            dcc.Graph(id="payoff-chart", figure=go.Figure()),
                        ],
                        style={
                            "flex": "2.2",
                            "padding": "12px",
                            "border": "1px solid #E5E7EB",
                            "borderRadius": "6px",
                        },
                    ),
                    html.Div(
                        [
                            html.H4("View"),
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
                            html.H4("Results", style={"marginTop": "12px"}),
                            dcc.Tabs(
                                id="results-tabs",
                                value="summary",
                                children=[
                                    dcc.Tab(label="Summary", value="summary"),
                                    dcc.Tab(label="Scenario", value="scenario"),
                                    dcc.Tab(label="Key Levels", value="key_levels"),
                                    dcc.Tab(label="Margin / POP", value="margin_pop"),
                                ],
                            ),
                            html.Div(id="results-content", style={"marginTop": "8px"}),
                        ],
                        style={
                            "flex": "1",
                            "padding": "12px",
                            "border": "1px solid #E5E7EB",
                            "borderRadius": "6px",
                        },
                    ),
                ],
                style={"display": "flex", "gap": "12px"},
            ),
        ],
        style={"padding": "16px", "fontFamily": "Arial, sans-serif"},
    )


if DASH_AVAILABLE:
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
        Input("ticker-input", "value"),
        State("spot-input", "value"),
        State("store-ref", "data"),
    )
    def _ping_spot(ticker: str, current_spot: float, ref_data: dict):
        raw_ticker = (ticker or "").strip()
        if not raw_ticker:
            spot_value = current_spot if current_spot is not None else 100.0
            spot_out = spot_value if current_spot is None else no_update
            return (
                {
                    "raw_ticker": "",
                    "resolved_ticker": None,
                    "spot": None,
                    "as_of": None,
                    "status": "empty",
                    "error": None,
                },
                spot_out,
                "",
            )
        if isinstance(ref_data, dict):
            cached_raw = str(ref_data.get("raw_ticker", "")).strip()
            if cached_raw and cached_raw == raw_ticker:
                return no_update, no_update, no_update
        try:
            resolved = resolve_security(raw_ticker)
            spot_result = fetch_spot(resolved)
            spot_value, as_of = _normalize_spot_result(spot_result)
            if spot_value is None:
                raise ValueError("Spot not available")
            as_of_text = as_of or _utc_now_str()
            return (
                {
                    "raw_ticker": raw_ticker,
                    "resolved_ticker": resolved,
                    "spot": spot_value,
                    "as_of": as_of_text,
                    "status": "ok",
                    "error": None,
                },
                spot_value,
                f"Spot updated ({as_of_text})",
            )
        except Exception as exc:
            return (
                {
                    "raw_ticker": raw_ticker,
                    "resolved_ticker": None,
                    "spot": None,
                    "as_of": None,
                    "status": "error",
                    "error": str(exc),
                },
                no_update,
                f"Spot update failed: {exc}",
            )

    @app.callback(
        Output("store-inputs", "data"),
        Output("legs-table", "data"),
        Input("ticker-input", "value"),
        Input("spot-input", "value"),
        Input("expiry-input", "value"),
        Input("stock-position-input", "value"),
        Input("avg-cost-input", "value"),
        Input("legs-table", "data"),
        Input("pricing-mode-input", "value"),
        Input("roi-policy-input", "value"),
        Input("vol-mode-input", "value"),
        Input("scenario-mode-input", "value"),
        Input("atm-iv-input", "value"),
        Input("downside-tgt-input", "value"),
        Input("upside-tgt-input", "value"),
        Input("strategy-group", "value"),
        Input("strategy-subgroup", "value"),
        Input("strategy-id", "value"),
        State("store-ref", "data"),
        State("store-inputs", "data"),
    )
    def _sync_inputs_and_defaults(
        ticker: str,
        spot: float,
        expiry: str,
        stock_position: float,
        avg_cost: float,
        legs_data: list[dict],
        pricing_mode: str,
        roi_policy: str,
        vol_mode: str,
        scenario_mode: str,
        atm_iv: float,
        downside_tgt: float,
        upside_tgt: float,
        strategy_group: str,
        strategy_subgroup: str,
        strategy_id: int,
        ref_data: dict,
        previous_state: dict,
    ) -> tuple[dict, list[dict]]:
        prev_spot = 100.0
        if isinstance(previous_state, dict) and is_number_like(previous_state.get("spot")):
            prev_spot = float(previous_state.get("spot"))
        spot_value = _coerce_float(spot)
        if spot_value is None:
            spot_value = prev_spot
        if spot_value < 0:
            spot_value = 0.0
        stock_position_value = _coerce_float(stock_position)
        if stock_position_value is None:
            stock_position_value = 0.0
        avg_cost_value = _coerce_float(avg_cost)
        if avg_cost_value is None:
            avg_cost_value = 0.0

        ref_spot = None
        resolved_ticker = None
        raw_ticker = (ticker or "").strip()
        if isinstance(ref_data, dict) and ref_data.get("status") == "ok":
            ref_spot = _coerce_float(ref_data.get("spot"))
            resolved_ticker = ref_data.get("resolved_ticker")
            if ref_data.get("raw_ticker"):
                raw_ticker = str(ref_data.get("raw_ticker"))
        spot_for_defaults = ref_spot if ref_spot is not None else spot_value

        prev_strategy_id = None
        if isinstance(previous_state, dict):
            prev_strategy_id = previous_state.get("strategy_id")
        use_defaults = strategy_id is not None and strategy_id != prev_strategy_id

        sanitized_legs = []
        strategy_row = None
        strategy_name = ""
        template_kind = None
        force_default = False

        if use_defaults and strategy_id is not None:
            strategy_row = _cached_strategy_row(strategy_id)
            if strategy_row:
                strategy_name = str(strategy_row.get("strategy_name", "")).strip()
                template_kind = str(strategy_row.get("template_kind", "")).strip().upper()
                template_legs = extract_template_legs_from_row(
                    strategy_row, spot_for_defaults
                )
                if template_kind == "STOCK_ONLY" or not template_legs:
                    template_legs = []
                    force_default = True
                for leg in template_legs:
                    sanitized_legs.append(
                        {
                            "kind": leg.get("kind"),
                            "position": float(leg.get("position", 0.0)),
                            "strike": float(leg.get("strike")),
                            "strike_tag": leg.get("strike_tag"),
                            "premium": 0.0,
                            "multiplier": int(leg.get("multiplier", 100) or 100),
                        }
                    )
        if not sanitized_legs and not force_default:
            if isinstance(legs_data, list):
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
        if not sanitized_legs:
            sanitized_legs = [
                {
                    "kind": "call",
                    "position": 1.0,
                    "strike": float(spot_for_defaults),
                    "strike_tag": "ATM",
                    "premium": 0.0,
                    "multiplier": 100,
                }
            ]

        if isinstance(previous_state, dict):
            if not strategy_name:
                strategy_name = str(previous_state.get("strategy_name", "") or "")
            if template_kind is None:
                template_kind = previous_state.get("template_kind")
            if strategy_row is None:
                strategy_row = previous_state.get("strategy_row")

        store_inputs = {
            "ticker": raw_ticker,
            "raw_ticker": raw_ticker,
            "resolved_ticker": resolved_ticker or raw_ticker,
            "spot": spot_value,
            "expiry": (expiry or "").strip(),
            "stock_position": stock_position_value,
            "avg_cost": avg_cost_value,
            "legs": sanitized_legs,
            "pricing_mode": pricing_mode or "mid",
            "roi_policy": roi_policy or "premium",
            "vol_mode": vol_mode or "atm",
            "atm_iv": float(atm_iv or 0.0),
            "scenario_mode": scenario_mode or "targets",
            "downside_tgt": float(downside_tgt or 0.0),
            "upside_tgt": float(upside_tgt or 0.0),
            "strategy_group": strategy_group,
            "strategy_subgroup": strategy_subgroup,
            "strategy_id": strategy_id,
            "strategy_name": strategy_name,
            "template_kind": template_kind,
            "strategy_row": strategy_row,
        }
        return store_inputs, sanitized_legs

    @app.callback(
        Output("store-market", "data"),
        Output("refresh-status", "children"),
        Input("refresh-button", "n_clicks"),
        State("store-inputs", "data"),
        prevent_initial_call=True,
    )
    def _refresh_market(n_clicks: int, inputs: dict) -> tuple[dict, str]:
        spot = 0.0
        if isinstance(inputs, dict):
            spot = float(inputs.get("spot", 0.0) or 0.0)
        timestamp = _utc_now_str()
        data = {"market_refreshed_at": timestamp, "spot": spot}
        return data, f"Market refreshed at {timestamp}"

    @app.callback(
        Output("store-analysis-pack", "data"),
        Input("run-analysis-button", "n_clicks"),
        State("store-inputs", "data"),
        State("store-market", "data"),
        prevent_initial_call=True,
    )
    def _run_analysis(n_clicks: int, inputs: dict, market_data: dict) -> dict:
        if not isinstance(inputs, dict):
            return {"error": "invalid inputs"}
        ticker = str(inputs.get("ticker", "") or "")
        resolved_ticker = str(inputs.get("resolved_ticker") or ticker)
        spot = float(inputs.get("spot", 0.0) or 0.0)
        stock_position = float(inputs.get("stock_position", 0.0) or 0.0)
        avg_cost = float(inputs.get("avg_cost", 0.0) or 0.0)
        expiry = str(inputs.get("expiry", "") or "")
        pricing_mode = str(inputs.get("pricing_mode", "mid") or "mid")
        roi_policy = str(inputs.get("roi_policy", "premium") or "premium")
        vol_mode = str(inputs.get("vol_mode", "atm") or "atm")
        atm_iv = float(inputs.get("atm_iv", 0.0) or 0.0)
        scenario_mode = str(inputs.get("scenario_mode", "targets") or "targets")
        downside_pct = float(inputs.get("downside_tgt", 0.0) or 0.0)
        upside_pct = float(inputs.get("upside_tgt", 0.0) or 0.0)
        downside_tgt = max(1e-6, 1.0 + (downside_pct / 100.0))
        upside_tgt = max(1e-6, 1.0 + (upside_pct / 100.0))
        legs_data = inputs.get("legs") or []
        legs = []
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
        roi_policy_key = roi_policy.strip().lower()
        if roi_policy_key == "premium" and abs(net_premium_per_share) < 1e-9:
            return {
                "error": (
                    "Net premium is 0 under ROI policy Premium. Enter premiums "
                    "(or Fetch Bloomberg Data) or choose a different ROI policy."
                ),
                "as_of": _utc_now_str(),
            }
        strategy_input = StrategyInput(
            spot=spot,
            stock_position=stock_position,
            avg_cost=avg_cost,
            legs=legs,
        )
        strategy_meta = {
            "as_of": _utc_now_str(),
            "expiry": expiry,
            "underlying_ticker": ticker,
            "resolved_underlying": resolved_ticker,
            "strategy_name": inputs.get("strategy_name") or "",
            "strategy_id": inputs.get("strategy_id"),
            "group": inputs.get("strategy_group"),
            "subgroup": inputs.get("strategy_subgroup"),
            "strategy_row": inputs.get("strategy_row"),
        }
        underlying_profile = {}
        bbg_leg_snapshots = None
        if isinstance(market_data, dict):
            underlying_profile = market_data.get("underlying_profile", {})
            bbg_leg_snapshots = market_data.get("bbg_leg_snapshots")
        pricing_map = {"mid": "MID", "dealable": "DEALABLE"}
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
                pricing_mode=pricing_map.get(pricing_mode, pricing_mode),
                roi_policy=roi_map.get(roi_policy, roi_policy),
                vol_mode=vol_map.get(vol_mode, vol_mode),
                atm_iv=atm_iv,
                underlying_profile=underlying_profile,
                bbg_leg_snapshots=bbg_leg_snapshots,
                scenario_mode=scenario_mode,
                downside_tgt=downside_tgt,
                upside_tgt=upside_tgt,
            )
            return analysis_pack_to_store(pack)
        except Exception as exc:
            return {"error": str(exc)}

    @app.callback(
        Output("store-ui", "data"),
        Input("pnl-toggles", "value"),
    )
    def _update_ui_toggles(values: list[str]) -> dict:
        selected = set(values or [])
        return {
            "show_options": "options" in selected,
            "show_stock": "stock" in selected,
            "show_combined": "combined" in selected,
        }

    @app.callback(
        Output("payoff-chart", "figure"),
        Input("store-analysis-pack", "data"),
        Input("store-ui", "data"),
    )
    def _render_chart(analysis_pack: dict, ui_state: dict) -> go.Figure:
        fig = go.Figure()
        if not isinstance(analysis_pack, dict):
            fig.update_layout(title="Run Analysis to view payoff")
            return fig
        if analysis_pack.get("error"):
            fig.update_layout(title=f"Analysis error: {analysis_pack['error']}")
            return fig
        payoff = analysis_pack.get("payoff")
        if not isinstance(payoff, dict):
            fig.update_layout(title="Run Analysis to view payoff")
            return fig
        price_grid = payoff.get("price_grid") or []
        options_pnl = payoff.get("options_pnl") or []
        stock_pnl = payoff.get("stock_pnl") or []
        combined_pnl = payoff.get("combined_pnl") or []
        if not price_grid:
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
            height=420,
        )
        return fig

    @app.callback(
        Output("as-of-display", "children"),
        Input("store-analysis-pack", "data"),
    )
    def _render_as_of(analysis_pack: dict) -> str:
        if isinstance(analysis_pack, dict):
            as_of = analysis_pack.get("as_of")
            if as_of:
                return f"As of: {as_of}"
        return "As of: --"

    @app.callback(
        Output("results-content", "children"),
        Input("store-analysis-pack", "data"),
        Input("results-tabs", "value"),
    )
    def _render_results(pack: dict, tab: str):
        if not isinstance(pack, dict):
            return html.Div("Run Analysis to view results", style={"fontSize": "12px"})
        if pack.get("error"):
            return html.Div(
                f"Analysis error: {pack['error']}", style={"fontSize": "12px"}
            )
        if tab == "summary":
            summary = pack.get("summary", {}) if isinstance(pack, dict) else {}
            rows = summary.get("rows", []) if isinstance(summary, dict) else []
            table = dash_table.DataTable(
                columns=[
                    {"name": "Metric", "id": "metric"},
                    {"name": "Options", "id": "options"},
                    {"name": "Combined", "id": "combined"},
                ],
                data=rows if isinstance(rows, list) else [],
                style_table={"overflowX": "auto"},
                style_cell={"fontSize": "12px", "padding": "4px"},
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
            scenario = pack.get("scenario", {}) if isinstance(pack, dict) else {}
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
            return _df_dict_to_table(df_dict, "scenario-table", page_size=10)
        if tab == "key_levels":
            levels = []
            key_levels = pack.get("key_levels", {}) if isinstance(pack, dict) else {}
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
                style_table={"overflowX": "auto"},
                style_cell={"fontSize": "12px", "padding": "4px"},
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
