"""vNext layouts (no callbacks)."""

from __future__ import annotations

import plotly.graph_objects as go
from dash import dcc, html, dash_table

from frontend_dash.vnext import ids as ID

try:
    from core.strategy_map import list_groups, list_strategies, list_subgroups
except Exception:
    list_groups = None
    list_strategies = None
    list_subgroups = None


def layout_control_plane_stores():
    groups = []
    if list_groups is not None:
        try:
            groups = list_groups() or []
        except Exception:
            groups = []
    default_group = groups[0] if groups else None
    subgroups = []
    if list_subgroups is not None and default_group:
        try:
            subgroups = list_subgroups(default_group) or []
        except Exception:
            subgroups = []
    default_subgroup = subgroups[0] if subgroups else None
    default_strategy_id = None
    if list_strategies is not None and default_group and default_subgroup:
        try:
            df = list_strategies(default_group, default_subgroup)
        except Exception:
            df = None
        if df is not None and not df.empty:
            default_strategy_id = int(df.iloc[0]["strategy_id"])
    default_legs = [
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
    return html.Div(
        id=ID.CONTROL_PLANE,
        style={"display": "none"},
        children=[
            dcc.Store(id=ID.STORE_REF),
            dcc.Store(id=ID.STORE_MARKET),
            dcc.Store(id=ID.STORE_ANALYSIS_KEY, storage_type="session"),
            dcc.Store(id=ID.STORE_INPUTS, storage_type="session"),
            dcc.Store(
                id="store-shell",
                storage_type="session",
                data={"sidebar_collapsed": False},
            ),
            dcc.Store(
                id=ID.STORE_UI,
                storage_type="session",
                data={
                    "ticker": "",
                    "spot": 100.0,
                    "expiry": None,
                    "strategy_group": default_group,
                    "strategy_subgroup": default_subgroup,
                    "strategy_id": default_strategy_id,
                    "stock_position": 0.0,
                    "avg_cost": 0.0,
                    "pricing_mode": "mid",
                    "roi_policy": "premium",
                    "vol_mode": "atm",
                    "atm_iv": 0.2,
                    "scenario_mode": "targets",
                    "downside_pct": -10.0,
                    "upside_pct": 10.0,
                    "legs": default_legs,
                    "show_options": True,
                    "show_stock": False,
                    "show_combined": True,
                    "show_strikes": True,
                    "show_breakevens": True,
                },
            ),
        ],
    )


def layout_shell(page_container=None, bloomberg_available: bool = False):
    if page_container is None:
        page_container = html.Div(
            id=ID.PAGE,
            children=[
                layout_dashboard(),
                layout_bloomberg(bloomberg_available),
                layout_report(),
            ],
        )
    return html.Div(
        className="ae-shell",
        children=[
            html.Aside(
                id="ae-sidebar",
                className="ae-sidebar",
                children=[
                    html.Div(
                        className="ae-brand-row",
                        children=[
                            html.Div(
                                className="ae-brand-left",
                                children=[
                                    html.Div("AE", className="ae-brand-badge"),
                                    html.Div(
                                        className="ae-brand-block",
                                        children=[
                                            html.Div(
                                                "ALPHA ENGINE", className="ae-brand"
                                            ),
                                            html.Div(
                                                "INSTITUTIONAL SALES",
                                                className="ae-sub",
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            html.Div("AE", className="ae-brand-mark"),
                            html.Button(
                                "≡",
                                id="btn-sidebar-toggle",
                                className="ae-sidebar-toggle",
                                type="button",
                            ),
                        ],
                    ),
                    html.Div(
                        className="ae-sidebar-nav",
                        children=[
                            html.Div("Core Workflow", className="ae-nav-h"),
                            html.Button(
                                "Options Builder",
                                className="ae-item active",
                                type="button",
                            ),
                            html.Button(
                                "Idea Generator",
                                className="ae-item disabled",
                                type="button",
                            ),
                            html.Button(
                                "Structuring Lab",
                                className="ae-item disabled",
                                type="button",
                            ),
                            html.Div("Client & Book", className="ae-nav-h"),
                            html.Button(
                                "Sales Triggers",
                                className="ae-item disabled",
                                type="button",
                            ),
                            html.Button(
                                "Resonance Matrix",
                                className="ae-item disabled",
                                type="button",
                            ),
                            html.Button(
                                "Content Factory",
                                className="ae-item disabled",
                                type="button",
                            ),
                        ],
                    ),
                ],
            ),
            html.Div(
                className="ae-main",
                children=[
                    html.Div(
                        className="ae-topbar-stack",
                        children=[
                            html.Div(
                                className="ae-ticker-tape",
                                children=[
                                    html.Div(
                                        className="ae-ticker-tape__track",
                                        children=[
                                            html.Span(
                                                "SPX 4,856.12 +0.8%",
                                                className="ae-ticker-item",
                                            ),
                                            html.Span(
                                                "NDX 17,942.44 +1.1%",
                                                className="ae-ticker-item",
                                            ),
                                            html.Span(
                                                "VIX 14.2 -1.1%",
                                                className="ae-ticker-item",
                                            ),
                                            html.Span(
                                                "US10Y 4.08% +2bp",
                                                className="ae-ticker-item",
                                            ),
                                            html.Span(
                                                "EURUSD 1.09 +0.2%",
                                                className="ae-ticker-item",
                                            ),
                                            html.Span(
                                                "SPX 4,856.12 +0.8%",
                                                className="ae-ticker-item",
                                            ),
                                            html.Span(
                                                "NDX 17,942.44 +1.1%",
                                                className="ae-ticker-item",
                                            ),
                                            html.Span(
                                                "VIX 14.2 -1.1%",
                                                className="ae-ticker-item",
                                            ),
                                        ],
                                    )
                                ],
                            ),
                            html.Header(
                                className="ae-topbar",
                                children=[
                                    html.Div(
                                        "Options Builder",
                                        className="ae-title",
                                    ),
                                    dcc.Input(
                                        className="ae-commandbar",
                                        type="text",
                                        placeholder="CMD: Ticker / Client / Command...",
                                    ),
                                    html.Div(
                                        className="ae-status",
                                        children=[
                                            html.Div(
                                                "Live Data",
                                                className="ae-pill",
                                            ),
                                            html.Div(
                                                "09:41 ET",
                                                className="ae-pill",
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        className="ae-content",
                        children=[
                            html.Div(
                                className="ae-tabs",
                                children=[
                                    dcc.Tabs(
                                        id=ID.TABS,
                                        value="dashboard",
                                        children=[
                                            dcc.Tab(
                                                label="Dashboard", value="dashboard"
                                            ),
                                            dcc.Tab(
                                                label="Bloomberg Data",
                                                value="bloomberg",
                                            ),
                                            dcc.Tab(
                                                label="Client Report",
                                                value="report",
                                            ),
                                        ],
                                    )
                                ],
                            ),
                            page_container,
                        ],
                    ),
                ],
            ),
        ],
    )


def _safe_list_groups() -> list[str]:
    if list_groups is None:
        return []
    try:
        return list_groups()
    except Exception:
        return []


def _safe_list_subgroups(group: str | None) -> list[str]:
    if not group or list_subgroups is None:
        return []
    try:
        return list_subgroups(group)
    except Exception:
        return []


def _safe_list_strategies(group: str | None, subgroup: str | None):
    if not group or not subgroup or list_strategies is None:
        return None
    try:
        return list_strategies(group, subgroup)
    except Exception:
        return None


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


_groups = _safe_list_groups()
_group_options = [{"label": g, "value": g} for g in _groups]
_default_group = _groups[0] if _groups else None
_default_subgroups = _safe_list_subgroups(_default_group)
_subgroup_options = [{"label": sg, "value": sg} for sg in _default_subgroups]
_default_subgroup = _default_subgroups[0] if _default_subgroups else None
_default_strategy_df = _safe_list_strategies(_default_group, _default_subgroup)
if _default_strategy_df is not None and not _default_strategy_df.empty:
    _strategy_options = [
        {"label": row["strategy_name"], "value": int(row["strategy_id"])}
        for _, row in _default_strategy_df.iterrows()
    ]
    _default_strategy_id = int(_default_strategy_df.iloc[0]["strategy_id"])
else:
    _strategy_options = []
    _default_strategy_id = None

_panel_market = html.Div(
    className="ae-card",
    children=[
        html.Div(
            className="ae-card__header",
            children=[html.Div("Market", className="ae-card__title")],
        ),
        html.Label("Ticker"),
        dcc.Input(
            id=ID.TICKER_INPUT,
            type="text",
            debounce=True,
            persistence=True,
            persistence_type="session",
            style={"width": "100%"},
        ),
        html.Div(
            id=ID.SPOT_STATUS,
            className="vnext-muted",
        ),
        html.Label("Spot"),
        dcc.Input(
            id=ID.SPOT_INPUT,
            type="number",
            step=0.01,
            persistence=True,
            persistence_type="session",
            style={"width": "100%"},
        ),
        html.Div(
            className="ae-expiry-wrap",
            children=[
                html.Label("Select Expiration"),
                dcc.DatePickerSingle(
                    id=ID.EXPIRY_INPUT,
                    display_format="YYYY-MM-DD",
                    placeholder="YYYY-MM-DD",
                    persistence=True,
                    persistence_type="session",
                    className="ae-date",
                ),
            ],
        ),
        html.Div(
            className="ae-btn-row",
            children=[
                html.Button(
                    "REFRESH DATA",
                    id=ID.BTN_REFRESH,
                    className="ae-btn ae-btn-primary ae-btn-pill",
                ),
                html.Button(
                    "Run Analysis",
                    id=ID.BTN_RUN,
                    className="ae-btn ae-btn-primary ae-btn-pill",
                ),
            ],
        ),
        html.Div(
            id=ID.REFRESH_STATUS,
            className="vnext-muted",
        ),
    ],
)

_panel_strategy = html.Div(
    className="ae-card",
    children=[
        html.Div(
            className="ae-card__header",
            children=[html.Div("Strategy", className="ae-card__title")],
        ),
        html.Label("Strategy Group"),
        dcc.Dropdown(
            id=ID.STRATEGY_GROUP,
            options=_group_options,
            clearable=False,
            persistence=True,
            persistence_type="session",
        ),
        html.Label("Strategy Subgroup"),
        dcc.Dropdown(
            id=ID.STRATEGY_SUBGROUP,
            options=_subgroup_options,
            clearable=False,
            persistence=True,
            persistence_type="session",
        ),
        html.Label("Strategy"),
        dcc.Dropdown(
            id=ID.STRATEGY_ID,
            options=_strategy_options,
            clearable=True,
            persistence=True,
            persistence_type="session",
        ),
    ],
)

_panel_stock_overlay = html.Div(
    className="ae-card",
    children=[
        html.Div(
            className="ae-card__header",
            children=[html.Div("Stock Overlay", className="ae-card__title")],
        ),
        html.Label("Stock Position (shares)"),
        dcc.Input(
            id=ID.STOCK_POSITION,
            type="number",
            step=1.0,
            persistence=True,
            persistence_type="session",
            style={"width": "100%"},
        ),
        html.Label("Avg Cost"),
        dcc.Input(
            id=ID.AVG_COST,
            type="number",
            step=0.01,
            persistence=True,
            persistence_type="session",
            style={"width": "100%"},
        ),
    ],
)

_panel_option_legs = html.Div(
    className="ae-card",
    children=[
        html.Div(
            className="ae-card__header",
            children=[html.Div("Option Legs", className="ae-card__title")],
        ),
        dash_table.DataTable(
            id=ID.LEGS_TABLE,
            columns=[
                {
                    "name": "Type",
                    "id": "kind",
                    "presentation": "dropdown",
                },
                {
                    "name": "Side",
                    "id": "side",
                    "presentation": "dropdown",
                },
                {"name": "Qty", "id": "qty"},
                {"name": "Strike", "id": "strike"},
                {"name": "Premium", "id": "premium"},
                {
                    "name": "Override",
                    "id": "override",
                    "presentation": "dropdown",
                },
                {
                    "name": "Option Ticker",
                    "id": "option_ticker",
                },
            ],
            data=_empty_leg_rows(),
            editable=True,
            persistence=True,
            persistence_type="session",
            persisted_props=["data"],
            dropdown={
                "kind": {
                    "options": [
                        {"label": "Call", "value": "call"},
                        {"label": "Put", "value": "put"},
                    ]
                },
                "side": {
                    "options": [
                        {"label": "Long", "value": "Long"},
                        {"label": "Short", "value": "Short"},
                    ]
                },
                "override": {
                    "options": [
                        {"label": "No", "value": False},
                        {"label": "Yes", "value": True},
                    ]
                },
            },
            style_table={
                "overflowX": "auto",
                "maxHeight": "220px",
                "overflowY": "auto",
            },
        ),
    ],
)

_panel_pricing_roi = html.Div(
    className="ae-card",
    children=[
        html.Div(
            className="ae-card__header",
            children=[html.Div("Pricing & ROI", className="ae-card__title")],
        ),
        html.Label("Pricing Mode"),
        dcc.Dropdown(
            id=ID.PRICING_MODE,
            options=[
                {"label": "Mid", "value": "mid"},
                {"label": "Bid/Ask", "value": "bid_ask"},
            ],
            clearable=False,
            persistence=True,
            persistence_type="session",
        ),
        html.Label("ROI Policy"),
        dcc.Dropdown(
            id=ID.ROI_POLICY,
            options=[
                {
                    "label": "Premium (Net Premium)",
                    "value": "premium",
                },
                {
                    "label": "Max Loss (Risk Max Loss)",
                    "value": "max_loss",
                },
                {
                    "label": "Cash Secured",
                    "value": "cash_secured",
                },
                {
                    "label": "Margin Proxy",
                    "value": "margin",
                },
            ],
            clearable=False,
            persistence=True,
            persistence_type="session",
        ),
        html.Label("Vol Mode"),
        dcc.Dropdown(
            id=ID.VOL_MODE,
            options=[
                {"label": "ATM", "value": "atm"},
                {"label": "Per Leg", "value": "per_leg"},
            ],
            clearable=False,
            persistence=True,
            persistence_type="session",
        ),
        html.Label("ATM IV"),
        dcc.Input(
            id=ID.ATM_IV,
            type="number",
            step=0.01,
            persistence=True,
            persistence_type="session",
            style={"width": "100%"},
        ),
    ],
)

_panel_scenario_actions = html.Div(
    className="ae-card",
    children=[
        html.Div(
            className="ae-card__header",
            children=[html.Div("Scenario & Actions", className="ae-card__title")],
        ),
        html.Label("Scenario Mode"),
        dcc.Dropdown(
            id=ID.SCENARIO_MODE,
            options=[
                {"label": "Targets", "value": "targets"},
                {"label": "Infinity", "value": "infinity"},
            ],
            clearable=False,
            persistence=True,
            persistence_type="session",
        ),
        html.Label("Downside Target (%)"),
        dcc.Input(
            id=ID.DOWNSIDE_TGT,
            type="number",
            step=1.0,
            persistence=True,
            persistence_type="session",
            style={"width": "100%"},
        ),
        html.Label("Upside Target (%)"),
        dcc.Input(
            id=ID.UPSIDE_TGT,
            type="number",
            step=1.0,
            persistence=True,
            persistence_type="session",
            style={"width": "100%"},
        ),
        html.Div(
            "Run Analysis is available in Market.",
            className="ae-muted",
        ),
    ],
)

def layout_page_frame(
    main_children, page_id: str | None = None, include_left_rail: bool = True
):
    if not isinstance(main_children, (list, tuple)):
        main_children = [main_children]
    columns = []
    if include_left_rail:
        columns.append(
            html.Div(
                className="vnext-left-rail ae-left-rail stack gap-md",
                children=_left_rail_children,
            )
        )
    columns.append(
        html.Div(
            className="vnext-main ae-main-col stack gap-md",
            children=list(main_children),
        )
    )
    shell_kwargs = {
        "className": "vnext-shell ae-page-shell stack gap-md",
        "children": [
            html.Div(
                className="vnext-header-row ae-page-header",
                children=[
                    html.Div("Options Strategy Builder", className="vnext-title"),
                    html.Div(
                        className="vnext-header-actions",
                        children=[],
                    ),
                ],
            ),
            html.Div(
                className="vnext-dashboard ae-dashboard row gap-lg pad-lg",
                children=columns,
            ),
        ],
    }
    if page_id is not None:
        shell_kwargs["id"] = page_id
    return html.Div(
        className="vnext-app",
        children=[html.Div(**shell_kwargs)],
    )


_hero_fig = go.Figure()
_hero_fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font={"color": "#e5e7eb"},
)

_panel_hero = html.Div(
    className="ae-card ae-card--hero",
    children=[
        html.Div(className="ae-card__body", children=[
            html.Div(id=ID.RISK_BANNER),
            dcc.Graph(
                id=ID.PAYOFF_CHART,
                figure=_hero_fig,
                className="vnext-hero-chart",
            ),
            html.Div(
                className="ae-chart-toggles",
                children=[
                    dcc.Checklist(
                        id=ID.PNL_TOGGLES,
                        options=[
                            {
                                "label": "Options",
                                "value": "options",
                            },
                            {"label": "Stock", "value": "stock"},
                            {
                                "label": "Combined",
                                "value": "combined",
                            },
                        ],
                        className="vnext-checklist",
                    ),
                    dcc.Checklist(
                        id=ID.ANNOTATE_TOGGLES,
                        options=[
                            {
                                "label": "Strikes",
                                "value": "strikes",
                            },
                            {
                                "label": "Breakevens",
                                "value": "breakevens",
                            },
                        ],
                        className="vnext-checklist",
                    ),
                ],
            ),
        ]),
    ],
)

_panel_payoff_metrics = html.Div(
    className="ae-card",
    children=[
        html.Div(
            className="ae-card__header",
            children=[html.Div("Payoff & Metrics", className="ae-card__title")],
        ),
        html.Div(
            id=ID.PANEL_PAYOFF_METRICS, className="ae-card__body ae-fixed-table"
        ),
    ],
)

_panel_scenario_commentary = html.Div(
    className="ae-card",
    children=[
        html.Div(
            className="ae-card__header",
            children=[html.Div("Scenario Commentary", className="ae-card__title")],
        ),
        html.Div(id=ID.SCENARIO_CARDS, className="ae-card__body"),
    ],
)

_panel_key_levels = html.Div(
    className="ae-card",
    children=[
        html.Div(
            className="ae-card__header",
            children=[html.Div("Key Levels", className="ae-card__title")],
        ),
        html.Div(id=ID.PANEL_KEY_LEVELS, className="ae-card__body ae-fixed-table"),
    ],
)

_panel_margin_capital = html.Div(
    className="ae-card",
    children=[
        html.Div(
            className="ae-card__header",
            children=[html.Div("Margin & Capital", className="ae-card__title")],
        ),
        html.Div(id=ID.PANEL_MARGIN_CAPITAL, className="ae-card__body"),
    ],
)

_panel_dividend = html.Div(
    className="ae-card",
    children=[
        html.Div(
            className="ae-card__header",
            children=[html.Div("Dividend", className="ae-card__title")],
        ),
        html.Div(id=ID.PANEL_DIVIDEND, className="ae-card__body"),
    ],
)

_panel_eligibility = html.Div(
    className="ae-card",
    children=[
        html.Div(
            className="ae-card__header",
            children=[html.Div("Account Eligibility", className="ae-card__title")],
        ),
        html.Div(id=ID.PANEL_ELIGIBILITY, className="ae-card__body"),
    ],
)

_left_rail_children = [
    _panel_market,
    _panel_strategy,
    _panel_stock_overlay,
    _panel_option_legs,
    _panel_payoff_metrics,
]

_dashboard_main_children = [
    html.Div(
        className="ae-main-grid",
        children=[
            _panel_hero,
            html.Div(className="ae-spacer-md"),
            _panel_scenario_commentary,
            _panel_key_levels,
            html.Div(
                className="ae-bottom-grid",
                children=[
                    _panel_margin_capital,
                    _panel_dividend,
                    _panel_eligibility,
                ],
            ),
            html.Div(
                className="ae-duo-grid",
                children=[
                    _panel_pricing_roi,
                    _panel_scenario_actions,
                ],
            ),
        ],
    )
]

_layout_dashboard = layout_page_frame(
    _dashboard_main_children,
    page_id=ID.PAGE_DASHBOARD,
)


def layout_dashboard():
    return _layout_dashboard


def get_validation_layout(base_layout=None, bloomberg_available: bool = False):
    if base_layout is None:
        base_layout = html.Div(
            [
                layout_control_plane_stores(),
                layout_shell(bloomberg_available=bloomberg_available),
            ]
        )
    return base_layout


def layout_bloomberg(bloomberg_available: bool = False):
    main_children = [
        html.Div("Bloomberg Data", className="vnext-section-title ae-section-title"),
        dcc.Checklist(
            id=ID.DEBUG_TOGGLE,
            options=[{"label": "Debug Mode", "value": "on"}],
            value=[],
            className="vnext-checklist",
        ),
        html.Div(
            id=ID.DEBUG_CONTAINER,
            style={"display": "none"},
            children=[
                html.Div("Market Debug", className="vnext-section-title ae-section-title"),
                html.Div(
                    children=[
                        html.Div(
                            id=ID.BBG_MODE,
                            children=(
                                "Bloomberg: "
                                f"{'AVAILABLE' if bloomberg_available else 'OFFLINE'}"
                            ),
                        ),
                        html.Pre(
                            id=ID.REF_DEBUG,
                            className="vnext-pre",
                        ),
                        html.Pre(
                            id=ID.MARKET_DEBUG,
                            className="vnext-pre",
                        ),
                        html.Div(
                            id=ID.REFRESH_DEBUG,
                            className="vnext-muted",
                        ),
                    ],
                    className="ae-card",
                ),
                html.Div("Analysis Debug", className="vnext-section-title ae-section-title"),
                html.Div(
                    children=[
                        html.Pre(
                            id=ID.ANALYSIS_KEY_DEBUG,
                            className="vnext-pre",
                        ),
                        html.Pre(
                            id=ID.ANALYSIS_PACK_DEBUG,
                            className="vnext-pre",
                        ),
                        html.Div(
                            id=ID.ANALYSIS_RENDER_DEBUG,
                            className="vnext-muted",
                        ),
                    ],
                    className="ae-card",
                ),
            ],
        ),
        html.Div("Snapshot transparency coming next.", className="vnext-muted"),
    ]
    return layout_page_frame(
        main_children,
        page_id=ID.PAGE_BLOOMBERG,
        include_left_rail=False,
    )


def layout_report():
    main_children = [
        html.Div("Client Report", className="vnext-section-title ae-section-title"),
        html.Div("Coming next."),
        html.Div(
            "PDF export is disabled (reportlab not installed).",
            className="vnext-muted",
        ),
    ]
    return layout_page_frame(
        main_children,
        page_id=ID.PAGE_REPORT,
        include_left_rail=False,
    )
