"""vNext layouts (no callbacks)."""

from __future__ import annotations

import plotly.graph_objects as go
from dash import dcc, html

from frontend_dash.vnext import ids as ID


_layout_dashboard = html.Div(
    children=[
        html.Div(
            id=ID.PAGE_DASHBOARD,
            children=[
                html.H2("Options Strategy Builder (vNext)"),
                html.Div(id=ID.RISK_BANNER),
                html.Div(
                    children=[
                        dcc.Graph(
                            id=ID.PAYOFF_CHART,
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
                                    id=ID.PNL_TOGGLES,
                                    options=[
                                        {"label": "Options", "value": "options"},
                                        {"label": "Stock", "value": "stock"},
                                        {"label": "Combined", "value": "combined"},
                                    ],
                                    value=["options", "combined"],
                                    style={"fontSize": "12px"},
                                ),
                                dcc.Checklist(
                                    id=ID.ANNOTATE_TOGGLES,
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
                        html.Div(id=ID.PANEL_PAYOFF_METRICS),
                        html.H4("Margin & Capital"),
                        html.Div(id=ID.PANEL_MARGIN_CAPITAL),
                        html.H4("Dividend"),
                        html.Div(id=ID.PANEL_DIVIDEND),
                        html.H4("Account Eligibility"),
                        html.Div(id=ID.PANEL_ELIGIBILITY),
                    ],
                ),
            ],
        ),
        html.H3("Scenario Commentary"),
        html.Div(id=ID.SCENARIO_CARDS),
        html.H3("Key Levels"),
        html.Div(id=ID.PANEL_KEY_LEVELS),
    ],
)


def layout_dashboard():
    return _layout_dashboard


def layout_bloomberg(bloomberg_available: bool = False):
    return html.Div(
        children=[
            html.H3("Bloomberg Data"),
            dcc.Checklist(
                id=ID.DEBUG_TOGGLE,
                options=[{"label": "Debug Mode", "value": "on"}],
                value=[],
                style={"fontSize": "12px"},
            ),
            html.Div(
                id=ID.DEBUG_CONTAINER,
                style={"display": "none"},
                children=[
                    html.H3("Market Debug"),
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
                                style={
                                    "backgroundColor": "#111827",
                                    "color": "#e5e7eb",
                                    "padding": "8px",
                                    "fontSize": "12px",
                                    "whiteSpace": "pre-wrap",
                                },
                            ),
                            html.Pre(
                                id=ID.MARKET_DEBUG,
                                style={
                                    "backgroundColor": "#111827",
                                    "color": "#e5e7eb",
                                    "padding": "8px",
                                    "fontSize": "12px",
                                    "whiteSpace": "pre-wrap",
                                },
                            ),
                            html.Div(
                                id=ID.REFRESH_DEBUG,
                                style={"fontSize": "12px", "color": "#e5e7eb"},
                            ),
                        ],
                        style={"marginTop": "8px"},
                    ),
                    html.H3("Analysis Debug"),
                    html.Div(
                        children=[
                            html.Pre(
                                id=ID.ANALYSIS_KEY_DEBUG,
                                style={
                                    "backgroundColor": "#111827",
                                    "color": "#e5e7eb",
                                    "padding": "8px",
                                    "fontSize": "12px",
                                    "whiteSpace": "pre-wrap",
                                },
                            ),
                            html.Pre(
                                id=ID.ANALYSIS_PACK_DEBUG,
                                style={
                                    "backgroundColor": "#111827",
                                    "color": "#e5e7eb",
                                    "padding": "8px",
                                    "fontSize": "12px",
                                    "whiteSpace": "pre-wrap",
                                },
                            ),
                            html.Div(
                                id=ID.ANALYSIS_RENDER_DEBUG,
                                style={"fontSize": "12px", "color": "#e5e7eb"},
                            ),
                        ],
                        style={"marginTop": "12px"},
                    ),
                ],
            ),
            html.Div("Snapshot transparency coming next."),
        ]
    )


def layout_report():
    return html.Div(
        children=[
            html.H3("Client Report"),
            html.Div("Coming next."),
            html.Div(
                "PDF export is disabled (reportlab not installed).",
                style={"fontSize": "12px", "marginTop": "6px"},
            ),
        ]
    )
