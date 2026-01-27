"""vNext layouts (no callbacks)."""

from __future__ import annotations

import plotly.graph_objects as go
from dash import dcc, html, dash_table

from frontend_dash.vnext import ids as ID


_layout_dashboard = html.Div(
    className="vnext-app",
    children=[
        html.Div(
            id=ID.PAGE_DASHBOARD,
            className="vnext-shell stack gap-md",
            children=[
                html.Div(
                    className="vnext-header-row",
                    children=[
                        html.Div("Options Strategy Builder", className="vnext-title"),
                        html.Div(
                            className="vnext-header-actions",
                            children=[
                                html.Button(
                                    "Refresh Bloomberg Data",
                                    id=ID.BTN_REFRESH,
                                    className="vnext-btn",
                                ),
                                html.Button(
                                    "Run Analysis",
                                    id=ID.BTN_RUN,
                                    className="vnext-btn vnext-btn-primary",
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="vnext-dashboard row gap-lg pad-lg",
                    children=[
                        html.Div(
                            className="vnext-left-rail stack gap-md",
                            children=[
                            ],
                        ),
                        html.Div(
                            className="vnext-main stack gap-md",
                            children=[
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
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)


def layout_dashboard():
    return _layout_dashboard


def get_validation_layout(base_layout, bloomberg_available: bool = False):
    return html.Div(
        [
            base_layout,
            layout_dashboard(),
            layout_bloomberg(bloomberg_available),
            layout_report(),
        ]
    )


def layout_bloomberg(bloomberg_available: bool = False):
    return html.Div(
        className="vnext-app",
        children=[
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
    )


def layout_report():
    return html.Div(
        className="vnext-app",
        children=[
            html.Div("Client Report", className="vnext-section-title"),
            html.Div("Coming next."),
            html.Div(
                "PDF export is disabled (reportlab not installed).",
                className="vnext-muted",
            ),
        ]
    )
