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
    return html.Div(
        id=ID.CONTROL_PLANE,
        style={"display": "none"},
        children=[
            dcc.Store(id=ID.STORE_REF),
            dcc.Store(id=ID.STORE_MARKET),
            dcc.Store(id=ID.STORE_ANALYSIS_KEY),
            dcc.Store(id=ID.STORE_INPUTS),
            dcc.Store(
                id=ID.STORE_UI,
                data={
                    "show_options": True,
                    "show_stock": False,
                    "show_combined": True,
                    "show_strikes": True,
                    "show_breakevens": True,
                },
            ),
        ],
    )


def layout_shell(page_container=None):
    if page_container is None:
        page_container = html.Div(id=ID.PAGE)
    return html.Div(
        className="ae-shell",
        children=[
            html.Aside(
                className="ae-sidebar",
                children=[
                    html.Div(
                        children=[
                            html.Div("ALPHA ENGINE", className="ae-brand"),
                            html.Div("Institutional Sales", className="ae-sub"),
                        ]
                    ),
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
            html.Div(
                className="ae-main",
                children=[
                    html.Header(
                        className="ae-topbar",
                        children=[
                            html.Div("Options Builder", className="ae-title"),
                            html.Div(
                                className="ae-status",
                                children=[
                                    html.Div("Live Data", className="ae-pill"),
                                    html.Div("09:41 ET", className="ae-pill"),
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        className="ae-content",
                        children=[
                            dcc.Tabs(
                                id=ID.TABS,
                                value="dashboard",
                                children=[
                                    dcc.Tab(
                                        label="Dashboard", value="dashboard"
                                    ),
                                    dcc.Tab(
                                        label="Bloomberg Data", value="bloomberg"
                                    ),
                                    dcc.Tab(
                                        label="Client Report", value="report"
                                    ),
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
    className="vnext-panel panel pad",
    children=[
        html.Div(
            className="panel-header",
            children=[
                html.Div(
                    className="panel-title",
                    children=[
                        html.Div(
                            "Market",
                            className="h2",
                        )
                    ],
                )
            ],
        ),
        html.Label("Ticker"),
        dcc.Input(
            id=ID.TICKER_INPUT,
            type="text",
            debounce=True,
            value="",
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
            value=100.0,
            step=0.01,
            style={"width": "100%"},
        ),
        html.Label("Expiry (YYYY-MM-DD)"),
        dcc.Input(
            id=ID.EXPIRY_INPUT,
            type="text",
            value="",
            style={"width": "100%"},
        ),
        html.Button(
            "Refresh Bloomberg Data",
            id=ID.BTN_REFRESH,
            className="vnext-btn",
        ),
        html.Div(
            id=ID.REFRESH_STATUS,
            className="vnext-muted",
        ),
    ],
)

_panel_strategy = html.Div(
    className="vnext-panel panel pad",
    children=[
        html.Div(
            className="panel-header",
            children=[
                html.Div(
                    className="panel-title",
                    children=[
                        html.Div(
                            "Strategy",
                            className="h2",
                        )
                    ],
                )
            ],
        ),
        html.Label("Strategy Group"),
        dcc.Dropdown(
            id=ID.STRATEGY_GROUP,
            options=_group_options,
            value=_default_group,
            clearable=False,
        ),
        html.Label("Strategy Subgroup"),
        dcc.Dropdown(
            id=ID.STRATEGY_SUBGROUP,
            options=_subgroup_options,
            value=_default_subgroup,
            clearable=False,
        ),
        html.Label("Strategy"),
        dcc.Dropdown(
            id=ID.STRATEGY_ID,
            options=_strategy_options,
            value=_default_strategy_id,
            clearable=True,
        ),
    ],
)

_panel_stock_overlay = html.Div(
    className="vnext-panel panel pad",
    children=[
        html.Div(
            className="panel-header",
            children=[
                html.Div(
                    className="panel-title",
                    children=[
                        html.Div(
                            "Stock Overlay",
                            className="h2",
                        )
                    ],
                )
            ],
        ),
        html.Label("Stock Position (shares)"),
        dcc.Input(
            id=ID.STOCK_POSITION,
            type="number",
            value=0.0,
            step=1.0,
            style={"width": "100%"},
        ),
        html.Label("Avg Cost"),
        dcc.Input(
            id=ID.AVG_COST,
            type="number",
            value=0.0,
            step=0.01,
            style={"width": "100%"},
        ),
    ],
)

_panel_option_legs = html.Div(
    className="vnext-panel panel pad",
    children=[
        html.Div(
            className="panel-header",
            children=[
                html.Div(
                    className="panel-title",
                    children=[
                        html.Div(
                            "Option Legs",
                            className="h2",
                        )
                    ],
                )
            ],
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
    className="vnext-panel panel pad",
    children=[
        html.Div(
            className="panel-header",
            children=[
                html.Div(
                    className="panel-title",
                    children=[
                        html.Div(
                            "Pricing & ROI",
                            className="h2",
                        )
                    ],
                )
            ],
        ),
        html.Label("Pricing Mode"),
        dcc.Dropdown(
            id=ID.PRICING_MODE,
            options=[
                {"label": "Mid", "value": "mid"},
                {"label": "Bid/Ask", "value": "bid_ask"},
            ],
            value="mid",
            clearable=False,
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
            value="premium",
            clearable=False,
        ),
        html.Label("Vol Mode"),
        dcc.Dropdown(
            id=ID.VOL_MODE,
            options=[
                {"label": "ATM", "value": "atm"},
                {"label": "Per Leg", "value": "per_leg"},
            ],
            value="atm",
            clearable=False,
        ),
        html.Label("ATM IV"),
        dcc.Input(
            id=ID.ATM_IV,
            type="number",
            value=0.2,
            step=0.01,
            style={"width": "100%"},
        ),
    ],
)

_panel_scenario_actions = html.Div(
    className="vnext-panel panel pad",
    children=[
        html.Div(
            className="panel-header",
            children=[
                html.Div(
                    className="panel-title",
                    children=[
                        html.Div(
                            "Scenario & Actions",
                            className="h2",
                        )
                    ],
                )
            ],
        ),
        html.Label("Scenario Mode"),
        dcc.Dropdown(
            id=ID.SCENARIO_MODE,
            options=[
                {"label": "Targets", "value": "targets"},
                {"label": "Infinity", "value": "infinity"},
            ],
            value="targets",
            clearable=False,
        ),
        html.Label("Downside Target (%)"),
        dcc.Input(
            id=ID.DOWNSIDE_TGT,
            type="number",
            value=-10.0,
            step=1.0,
            style={"width": "100%"},
        ),
        html.Label("Upside Target (%)"),
        dcc.Input(
            id=ID.UPSIDE_TGT,
            type="number",
            value=10.0,
            step=1.0,
            style={"width": "100%"},
        ),
        html.Button(
            "Run Analysis",
            id=ID.BTN_RUN,
            className="vnext-btn vnext-btn-primary",
        ),
    ],
)

_left_rail_children = [
    _panel_market,
    _panel_strategy,
    _panel_stock_overlay,
    _panel_option_legs,
    _panel_pricing_roi,
    _panel_scenario_actions,
]

def layout_page_frame(
    main_children, page_id: str | None = None, include_left_rail: bool = True
):
    if not isinstance(main_children, (list, tuple)):
        main_children = [main_children]
    columns = []
    if include_left_rail:
        columns.append(
            html.Div(
                className="vnext-left-rail stack gap-md",
                children=_left_rail_children,
            )
        )
    columns.append(
        html.Div(
            className="vnext-main stack gap-md",
            children=list(main_children),
        )
    )
    shell_kwargs = {
        "className": "vnext-shell stack gap-md",
        "children": [
            html.Div(
                className="vnext-header-row",
                        children=[
                            html.Div("Options Strategy Builder", className="vnext-title"),
                            html.Div(
                                className="vnext-header-actions",
                                children=[],
                            ),
                        ],
            ),
            html.Div(
                className="vnext-dashboard row gap-lg pad-lg",
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


_dashboard_main_children = [
    html.Div(
        className="vnext-panel vnext-hero panel pad",
        children=[
            html.Div(id=ID.RISK_BANNER),
            dcc.Graph(
                id=ID.PAYOFF_CHART,
                figure=go.Figure(),
                className="vnext-hero-chart",
            ),
            html.Div(
                className="vnext-row",
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
                        value=["options", "combined"],
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
                        value=["strikes", "breakevens"],
                        className="vnext-checklist",
                    ),
                ],
            ),
        ],
    ),
    html.Div(
        className="vnext-panel panel pad",
        children=[
            html.Div(
                className="panel-header",
                children=[
                    html.Div(
                        className="panel-title",
                        children=[
                            html.Div(
                                "Payoff & Metrics",
                                className="h2",
                            )
                        ],
                    )
                ],
            ),
            html.Div(id=ID.PANEL_PAYOFF_METRICS),
        ],
    ),
    html.Div(
        className="vnext-panel panel pad",
        children=[
            html.Div(
                className="panel-header",
                children=[
                    html.Div(
                        className="panel-title",
                        children=[
                            html.Div(
                                "Scenario Commentary",
                                className="h2",
                            )
                        ],
                    )
                ],
            ),
            html.Div(id=ID.SCENARIO_CARDS),
        ],
    ),
    html.Div(
        className="vnext-panel panel pad",
        children=[
            html.Div(
                className="panel-header",
                children=[
                    html.Div(
                        className="panel-title",
                        children=[
                            html.Div(
                                "Key Levels",
                                className="h2",
                            )
                        ],
                    )
                ],
            ),
            html.Div(id=ID.PANEL_KEY_LEVELS),
        ],
    ),
    html.Div(
        className="vnext-panel panel pad",
        children=[
            html.Div(
                className="panel-header",
                children=[
                    html.Div(
                        className="panel-title",
                        children=[
                            html.Div(
                                "Margin & Capital",
                                className="h2",
                            )
                        ],
                    )
                ],
            ),
            html.Div(id=ID.PANEL_MARGIN_CAPITAL),
        ],
    ),
    html.Div(
        className="vnext-panel panel pad",
        children=[
            html.Div(
                className="panel-header",
                children=[
                    html.Div(
                        className="panel-title",
                        children=[
                            html.Div(
                                "Dividend",
                                className="h2",
                            )
                        ],
                    )
                ],
            ),
            html.Div(id=ID.PANEL_DIVIDEND),
        ],
    ),
    html.Div(
        className="vnext-panel panel pad",
        children=[
            html.Div(
                className="panel-header",
                children=[
                    html.Div(
                        className="panel-title",
                        children=[
                            html.Div(
                                "Account Eligibility",
                                className="h2",
                            )
                        ],
                    )
                ],
            ),
            html.Div(id=ID.PANEL_ELIGIBILITY),
        ],
    ),
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
                layout_shell(),
            ]
        )
    return html.Div(
        [
            base_layout,
            layout_dashboard(),
            layout_bloomberg(bloomberg_available),
            layout_report(),
        ]
    )


def layout_bloomberg(bloomberg_available: bool = False):
    main_children = [
        html.Div("Bloomberg Data", className="vnext-section-title"),
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
                html.Div("Market Debug", className="vnext-section-title"),
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
                    className="vnext-panel",
                ),
                html.Div("Analysis Debug", className="vnext-section-title"),
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
                    className="vnext-panel",
                ),
            ],
        ),
        html.Div("Snapshot transparency coming next.", className="vnext-muted"),
    ]
    return layout_page_frame(main_children, include_left_rail=False)


def layout_report():
    main_children = [
        html.Div("Client Report", className="vnext-section-title"),
        html.Div("Coming next."),
        html.Div(
            "PDF export is disabled (reportlab not installed).",
            className="vnext-muted",
        ),
    ]
    return layout_page_frame(main_children, include_left_rail=False)
