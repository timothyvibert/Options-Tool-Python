"""DMC v2 layout — visual skeleton with placeholder content.

All components use dash-mantine-components (Mantine v8).
No callbacks are registered here; this is layout-only.
"""

from __future__ import annotations

import dash_mantine_components as dmc
from dash import dcc, html, dash_table
import plotly.graph_objects as go

from core.strategy_map import list_groups
from frontend_dash.vnext2 import ids as ID
from frontend_dash.vnext2.theme import THEME


# ═══════════════════════════════════════════════════════════
# PUBLIC ENTRY
# ═══════════════════════════════════════════════════════════

def layout_v2():
    """Return the complete v2 DMC layout wrapped in MantineProvider."""
    return html.Div(className="v2-root", children=[
        dmc.MantineProvider(
            id=ID.MANTINE_PROVIDER,
            forceColorScheme="dark",
            theme=THEME,
            children=[
                _stores(),
                _shutdown_modal(),
                dmc.AppShell(
                    header={"height": 60},
                    padding="md",
                    children=[
                        dmc.AppShellHeader(children=[_header()]),
                        dmc.AppShellMain(children=[_tabs()]),
                    ],
                ),
            ],
        ),
    ])


# ═══════════════════════════════════════════════════════════
# STORES
# ═══════════════════════════════════════════════════════════

def _stores():
    return html.Div(
        children=[
            dcc.Store(id=ID.STORE_REF),
            dcc.Store(id=ID.STORE_MARKET),
            dcc.Store(id=ID.STORE_ANALYSIS_KEY, storage_type="session"),
            dcc.Store(id=ID.STORE_UI, storage_type="session"),
            dcc.Store(id=ID.STORE_INPUTS),
            dcc.Download(id=ID.DL_REPORT_PDF),
            dcc.Download(id=ID.DL_MARKET_JSON),
            dcc.Store(id=ID.LOG_STORE, storage_type="memory"),
            dcc.Download(id=ID.DL_ACTIVITY_CSV),
        ],
        style={"display": "none"},
    )


def _shutdown_modal():
    return dmc.Modal(
        id=ID.SHUTDOWN_CONFIRM,
        title="Shutdown Server",
        centered=True,
        children=[
            dmc.Text("This will stop the Options Builder server. You will need to relaunch to use it again."),
            dmc.Group(
                justify="flex-end",
                mt="md",
                children=[
                    dmc.Button("Cancel", id=ID.SHUTDOWN_CANCEL, variant="outline"),
                    dmc.Button("Shutdown", id=ID.SHUTDOWN_YES, color="red"),
                ],
            ),
        ],
    )


# ═══════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════

def _header():
    return dmc.Group(
        justify="space-between",
        h="100%",
        px="md",
        children=[
            # Left — title
            dmc.Text(
                "OPTIONS BUILDER",
                fw=700,
                size="sm",
                style={"letterSpacing": "0.06em"},
            ),
            # Center — command bar
            dmc.TextInput(
                placeholder="Search ticker, client, command...",
                w=400,
                size="sm",
                variant="filled",
            ),
            # Right — theme toggle, live badge, clock
            dmc.Group(
                gap="md",
                children=[
                    dmc.Switch(
                        id=ID.THEME_TOGGLE,
                        label="Light",
                        size="sm",
                    ),
                    dmc.Badge(
                        "LIVE DATA",
                        color="green",
                        variant="dot",
                        size="sm",
                    ),
                    dmc.Text("09:41 ET", size="sm", c="dimmed"),
                    dmc.Button(
                        "\u23FB", id=ID.BTN_SHUTDOWN,
                        variant="subtle", color="red", size="compact-sm",
                    ),
                ],
            ),
        ],
    )


# ═══════════════════════════════════════════════════════════
# TABS
# ═══════════════════════════════════════════════════════════

def _tabs():
    return dmc.Tabs(
        id=ID.TABS,
        value="dashboard",
        children=[
            dmc.TabsList(
                children=[
                    dmc.TabsTab("DASHBOARD", value="dashboard"),
                    dmc.TabsTab("BLOOMBERG DATA", value="bloomberg"),
                    dmc.TabsTab("ACTIVITY LOG", value="report"),
                ],
                mb="md",
            ),
            dmc.TabsPanel(value="dashboard", children=[_dashboard_tab()], keepMounted=True),
            dmc.TabsPanel(value="bloomberg", children=[_bloomberg_tab()], keepMounted=True),
            dmc.TabsPanel(value="report", children=[_report_tab()], keepMounted=True),
        ],
    )


# ═══════════════════════════════════════════════════════════
# DASHBOARD TAB
# ═══════════════════════════════════════════════════════════

def _dashboard_tab():
    return dmc.Stack(
        gap="md",
        children=[
            # ROW 1 — Four input cards (equal width)
            dmc.SimpleGrid(
                cols={"base": 1, "sm": 2, "md": 4},
                spacing="md",
                children=[
                    _card_market(),
                    _card_strategy(),
                    _card_actions(),
                    _card_tracking(),
                ],
            ),
            # ROW 1b — Collapsible advanced settings
            _settings_panel(),
            # ROW 2 + 3 — Tight group: Legs/Chart then Metrics/Scenarios
            dmc.Stack(
                gap="xs",
                children=[
                    _row2_legs_chart(),
                    _row3a_metrics_scenarios(),
                ],
            ),
            # ROW 4 — Key levels (full width)
            _row4_key_levels(),
            # ROW 5 — Margin (7/12) + Eligibility/Dividend stacked (5/12)
            _row5_margin_sidebar(),
        ],
    )


# ───────────────────────────────────────────────────────────
# Helpers
# ───────────────────────────────────────────────────────────

def _section_title(text):
    """Reusable uppercase card section heading."""
    return dmc.Text(
        text,
        size="xs",
        fw=700,
        tt="uppercase",
        c="dimmed",
        mb="sm",
        style={"letterSpacing": "0.08em"},
    )


def _legend_dot(color, label):
    """Small colored dot + label for chart legend."""
    return dmc.Group(
        gap=4,
        children=[
            html.Span(
                style={
                    "width": 10,
                    "height": 10,
                    "borderRadius": "50%",
                    "backgroundColor": color,
                    "display": "inline-block",
                }
            ),
            dmc.Text(label, size="xs", c="dimmed"),
        ],
    )


def _legend_line(color, label, dashed=False):
    """Small colored line + label for chart legend."""
    border_style = f"2px dashed {color}" if dashed else "none"
    bg = "transparent" if dashed else color
    return dmc.Group(
        gap=4,
        children=[
            html.Span(
                style={
                    "width": 16,
                    "height": 0 if dashed else 3,
                    "backgroundColor": bg,
                    "borderTop": border_style if dashed else "none",
                    "display": "inline-block",
                    "verticalAlign": "middle",
                }
            ),
            dmc.Text(label, size="xs", c="dimmed"),
        ],
    )


# ───────────────────────────────────────────────────────────
# ROW 1 Cards
# ───────────────────────────────────────────────────────────

def _card_market():
    return dmc.Card(
        withBorder=True, shadow="sm",
        children=[
            _section_title("MARKET"),
            dmc.TextInput(id=ID.TICKER_INPUT, label="Ticker", placeholder="e.g. AAPL US Equity", size="sm", mb="xs"),
            dmc.Text(id=ID.SPOT_DISPLAY, children="Spot: —", size="sm", c="dimmed", mb="xs"),
            dmc.Text(id=ID.SPOT_STATUS, size="xs", c="dimmed", mb="xs"),
            dmc.DatePickerInput(id=ID.EXPIRY_SELECT, label="Expiration", placeholder="Select expiry", valueFormat="YYYY-MM-DD", clearable=True, w="100%", size="sm"),
        ],
    )


def _card_strategy():
    return dmc.Card(
        withBorder=True, shadow="sm",
        children=[
            _section_title("STRATEGY"),
            dmc.Select(id=ID.GROUP_SELECT, label="Strategy Group", placeholder="Select group", data=list_groups(), searchable=True, size="sm", mb="xs"),
            dmc.Group(
                gap="xs", align="end",
                children=[
                    dmc.Select(id=ID.STRATEGY_SELECT, label="Strategy", placeholder="Select strategy", data=[], clearable=True, searchable=True, size="sm", style={"flex": 1}),
                    dmc.ActionIcon(dmc.Text("X", size="xs"), id=ID.STRATEGY_CLEAR, variant="subtle", color="gray", size="lg"),
                ],
            ),
        ],
    )


def _card_actions():
    return dmc.Card(
        withBorder=True, shadow="sm",
        children=[
            _section_title("STOCK OVERLAY & ACTIONS"),
            dmc.NumberInput(id=ID.SHARES_INPUT, label="Shares", placeholder="0", size="sm", mb="xs"),
            dmc.NumberInput(id=ID.AVG_COST_INPUT, label="Avg Cost", placeholder="0.00", decimalScale=2, size="sm", mb="sm"),
            dmc.Group(
                grow=True, mb="xs",
                children=[
                    dmc.Button("REFRESH DATA", id=ID.BTN_REFRESH, variant="outline", color="cyan", size="sm"),
                    dmc.Button("RUN ANALYSIS", id=ID.BTN_ANALYZE, variant="filled", color="cyan", size="sm"),
                ],
            ),
            dmc.Text(id=ID.REFRESH_STATUS, children="", size="xs", c="dimmed"),
        ],
    )


def _card_tracking():
    return dmc.Card(
        withBorder=True, shadow="sm",
        children=[
            _section_title("OUTPUT & TRACKING"),
            dmc.TextInput(id=ID.FA_NAME_INPUT, label="FA Name", placeholder="e.g. John Smith", size="sm", mb="xs"),
            dmc.TextInput(id=ID.ACCT_NUMBER_INPUT, label="Account Number", placeholder="e.g. AB-123456", size="sm", mb="sm"),
            dmc.Button("GENERATE PDF REPORT", id=ID.BTN_PDF, variant="light", color="green", fullWidth=True, size="sm", mb="xs"),
            dmc.Text(id=ID.REPORT_STATUS, children="", size="xs", c="dimmed"),
        ],
    )


# ───────────────────────────────────────────────────────────
# ROW 2 Cards
# ───────────────────────────────────────────────────────────

_LEGS_DARK_HEADER = {
    "backgroundColor": "#141825",
    "color": "#A8AFBF",
    "fontWeight": "bold",
    "fontSize": "11px",
    "textTransform": "uppercase",
    "letterSpacing": "0.04em",
    "borderBottom": "1px solid #1E2433",
}
_LEGS_DARK_CELL = {
    "backgroundColor": "#0E1119",
    "color": "#C1C7D6",
    "borderBottom": "1px solid #1E2433",
    "fontSize": "12px",
    "padding": "8px",
}


def _card_legs():
    return dmc.Card(
        withBorder=True,
        children=[
            _section_title("OPTION LEGS"),
            dash_table.DataTable(
                id=ID.LEGS_TABLE,
                columns=[
                    {"name": "Type", "id": "type", "presentation": "dropdown"},
                    {"name": "Side", "id": "side", "presentation": "dropdown"},
                    {"name": "Qty", "id": "qty"},
                    {"name": "Strike", "id": "strike"},
                    {"name": "Premium", "id": "premium"},
                    {"name": "Override", "id": "override", "presentation": "dropdown"},
                    {"name": "BBG Ticker", "id": "bbg_ticker"},
                ],
                data=[
                    {
                        "type": "",
                        "side": "",
                        "qty": "",
                        "strike": "",
                        "premium": "",
                        "override": "",
                        "bbg_ticker": "",
                    }
                    for _ in range(3)
                ],
                editable=True,
                dropdown={
                    "type": {
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
                            {"label": "No", "value": "no"},
                            {"label": "Yes", "value": "yes"},
                        ]
                    },
                },
                style_table={"overflowX": "auto"},
                style_header=_LEGS_DARK_HEADER,
                style_cell=_LEGS_DARK_CELL,
                style_data_conditional=[
                    {
                        "if": {"state": "active"},
                        "backgroundColor": "#1A2030",
                        "border": "1px solid #22d3ee",
                    },
                ],
            ),
        ],
    )


def _settings_panel():
    """Collapsible advanced settings — collapsed by default."""
    return dmc.Accordion(
        children=[
            dmc.AccordionItem(
                value="settings",
                children=[
                    dmc.AccordionControl("Advanced Settings"),
                    dmc.AccordionPanel(
                        dmc.Grid(
                            gutter="md",
                            children=[
                                dmc.GridCol(span=2, children=[
                                    dmc.Select(id=ID.PRICING_MODE, label="Pricing Mode", data=[{"value": "mid", "label": "Mid"}, {"value": "bid_ask", "label": "Bid/Ask"}], value="mid", size="sm"),
                                ]),
                                dmc.GridCol(span=2, children=[
                                    dmc.Select(id=ID.PREMIUM_MODE, label="Capital Basis", data=[{"value": "premium", "label": "Premium"}, {"value": "max_loss", "label": "Max Loss"}, {"value": "cash_secured", "label": "Cash Secured"}, {"value": "margin", "label": "Margin Proxy"}], value="premium", size="sm"),
                                ]),
                                dmc.GridCol(span=2, children=[
                                    dmc.Select(id=ID.SCENARIO_MODE, label="Scenario Mode", data=[{"value": "targets", "label": "Targets"}, {"value": "infinity", "label": "Infinity"}], value="targets", size="sm"),
                                ]),
                                dmc.GridCol(span=2, children=[
                                    dmc.NumberInput(id=ID.DOWNSIDE_TARGET, label="Downside (%)", value=-10.0, step=1, size="sm"),
                                ]),
                                dmc.GridCol(span=2, children=[
                                    dmc.NumberInput(id=ID.UPSIDE_TARGET, label="Upside (%)", value=10.0, step=1, size="sm"),
                                ]),
                                dmc.GridCol(span=2, children=[
                                    dmc.Select(id=ID.CIO_RATING_INPUT, label="CIO Rating", data=["Most Preferred", "Bellwether", "Least Preferred", "Not Covered"], placeholder="Select rating", clearable=True, size="sm"),
                                ]),
                            ],
                        )
                    ),
                ],
            )
        ],
        value=None,
        variant="separated",
    )



# ───────────────────────────────────────────────────────────
# ROW 4 — Payoff + Metrics
# ───────────────────────────────────────────────────────────

def _card_payoff():
    fig = go.Figure()
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(20,24,37,0.5)",
        font={"color": "#C1C7D6"},
        xaxis={
            "title": "Stock Price at Expiry",
            "gridcolor": "#1E2433",
        },
        yaxis={
            "title": "Profit / Loss ($)",
            "gridcolor": "#1E2433",
            "zeroline": True,
            "zerolinecolor": "#3D4559",
        },
        margin={"l": 50, "r": 20, "t": 30, "b": 60},
        height=500,
        showlegend=False,
    )
    fig.add_annotation(
        text="Run analysis to see payoff diagram",
        xref="paper",
        yref="paper",
        x=0.5,
        y=0.5,
        showarrow=False,
        font={"size": 14, "color": "#6C7589"},
    )
    return dmc.Card(
        withBorder=True,
        children=[
            dmc.Group(
                justify="space-between",
                mb="sm",
                children=[
                    _section_title("PAYOFF AT EXPIRY"),
                    dmc.Badge(
                        id=ID.RISK_BANNER,
                        children="No risk events",
                        color="green",
                        variant="light",
                        size="sm",
                    ),
                ],
            ),
            dcc.Graph(
                id=ID.PAYOFF_CHART,
                figure=fig,
                config={"responsive": True, "displayModeBar": False},
            ),
            dmc.Group(
                mt="sm",
                gap="lg",
                children=[
                    _legend_dot("#2563EB", "OPTIONS"),
                    _legend_dot("#D1D5DB", "STOCK"),
                    _legend_dot("#7C3AED", "COMBINED"),
                    _legend_line("#EF4444", "STRIKES"),
                    _legend_line("#22D3EE", "BREAKEVENS", dashed=True),
                ],
            ),
        ],
    )


def _row2_legs_chart():
    """Row 2: Option legs table (left) + payoff chart (right)."""
    return dmc.Grid(
        gutter="md",
        children=[
            dmc.GridCol(span=5, children=[_card_legs()]),
            dmc.GridCol(span=7, children=[_card_payoff()]),
        ],
    )


def _card_metrics():
    return dmc.Card(
        withBorder=True,
        id=ID.METRICS_TABLE,
        style={"height": "100%"},
        children=[
            _section_title("PAYOFF & METRICS"),
            dmc.Table(
                data={
                    "head": ["Metric", "Options", "Combined"],
                    "body": [
                        ["Max Profit", "\u2014", "\u2014"],
                        ["Max Loss", "\u2014", "\u2014"],
                        ["Capital Basis", "\u2014", "\u2014"],
                        ["Max ROI", "\u2014", "\u2014"],
                        ["Min ROI", "\u2014", "\u2014"],
                        ["Cost/Credit", "\u2014", "\u2014"],
                        ["Notional Exposure", "\u2014", "\u2014"],
                        ["Net Prem/Share", "\u2014", "\u2014"],
                        ["Net Prem % Spot", "\u2014", "\u2014"],
                    ],
                },
                striped=True,
                highlightOnHover=True,
                withTableBorder=True,
                withColumnBorders=True,
                verticalSpacing="xs",
                horizontalSpacing="sm",
            ),
        ],
    )


# ───────────────────────────────────────────────────────────
# ROW 5 — Commentary + Dividend
# ───────────────────────────────────────────────────────────

def _card_commentary():
    return dmc.Card(
        withBorder=True,
        id=ID.SCENARIO_CARDS,
        style={"height": "100%"},
        children=[
            _section_title("SCENARIO COMMENTARY"),
            dmc.Text("Run analysis to see scenario commentary.", size="sm", c="dimmed"),
        ],
    )


def _card_dividend():
    return dmc.Card(
        withBorder=True,
        id=ID.DIVIDEND_CARD,
        children=[
            _section_title("DIVIDEND"),
            dmc.Table(
                data={
                    "head": ["Field", "Value"],
                    "body": [
                        ["Ex-div Date", "\u2014"],
                        ["Days to Dividend", "\u2014"],
                        ["Before Expiry", "\u2014"],
                    ],
                },
                withTableBorder=True,
                highlightOnHover=True,
                verticalSpacing="xs",
            ),
        ],
    )


# ───────────────────────────────────────────────────────────
# ROW 6 — Key Levels + Margin
# ───────────────────────────────────────────────────────────

def _card_key_levels():
    return dmc.Card(
        withBorder=True,
        id=ID.KEY_LEVELS_TABLE,
        children=[
            _section_title("KEY LEVELS"),
            dmc.Table(
                data={
                    "head": [
                        "Label",
                        "Price",
                        "Move %",
                        "Stock PnL",
                        "Option PnL",
                        "Net PnL",
                        "Net ROI",
                        "Source",
                    ],
                    "body": [
                        [
                            "Spot",
                            "\u2014",
                            "0.0%",
                            "\u2014",
                            "\u2014",
                            "\u2014",
                            "\u2014",
                            "Market",
                        ],
                        [
                            "Strike 1",
                            "\u2014",
                            "\u2014",
                            "\u2014",
                            "\u2014",
                            "\u2014",
                            "\u2014",
                            "Strategy",
                        ],
                        [
                            "Breakeven",
                            "\u2014",
                            "\u2014",
                            "\u2014",
                            "\u2014",
                            "\u2014",
                            "\u2014",
                            "Computed",
                        ],
                    ],
                },
                striped=True,
                highlightOnHover=True,
                withTableBorder=True,
                withColumnBorders=True,
                verticalSpacing="xs",
                horizontalSpacing="sm",
            ),
        ],
    )


def _card_margin():
    return dmc.Card(
        withBorder=True,
        id=ID.MARGIN_CARD,
        children=[
            dmc.Group([
                _section_title("MARGIN & CAPITAL"),
                dmc.Select(
                    id=ID.MARGIN_MODE_SELECT,
                    data=["CBOE", "House"],
                    value="CBOE",
                    size="xs",
                    w=100,
                ),
            ], justify="space-between"),

            # Classification badge
            dmc.Group([
                dmc.Text("Classification:", size="sm", c="dimmed"),
                dmc.Badge(id=ID.MARGIN_CLASSIFICATION, children="--", variant="light", size="sm"),
            ], gap="xs", mt="xs"),

            # Main requirement table (3 rows)
            html.Div(
                id=ID.MARGIN_FULL_TABLE,
                children=dmc.Text("Run Analysis to view margin.", size="sm", c="dimmed"),
                style={"marginTop": "8px"},
            ),

            # House Intraday Check section (hidden by default)
            html.Div(
                id=ID.HOUSE_INTRADAY_SECTION,
                children=[
                    dmc.Divider(label="House Intraday Check", labelPosition="center", mt="md", mb="sm"),
                    dmc.SimpleGrid(cols=2, spacing="xs", children=[
                        dmc.NumberInput(id=ID.HOUSE_HOUSECALL, label="Housecall/Excess", size="xs", value=0, decimalScale=2, prefix="$", thousandSeparator=","),
                        dmc.NumberInput(id=ID.HOUSE_SMA, label="SMA", size="xs", value=0, decimalScale=2, prefix="$", thousandSeparator=","),
                        dmc.NumberInput(id=ID.HOUSE_TODAYS_CHANGE, label="Today's Change", size="xs", value=0, decimalScale=2, prefix="$", thousandSeparator=","),
                        dmc.NumberInput(id=ID.HOUSE_NEW_CASH, label="New Intraday Cash", size="xs", value=0, decimalScale=2, prefix="$", thousandSeparator=","),
                    ]),
                    html.Div(id=ID.HOUSE_INTRADAY_TABLE, style={"marginTop": "8px"}),
                ],
                style={"display": "none"},
            ),

        ],
    )


# ───────────────────────────────────────────────────────────
# Row 3 Output Panel Helpers
# ───────────────────────────────────────────────────────────

def _row3a_metrics_scenarios():
    """Row 3a: Metrics (left) + Scenario commentary (right)."""
    return dmc.Grid(
        gutter="md",
        children=[
            dmc.GridCol(span=5, children=[_card_metrics()]),
            dmc.GridCol(span=7, children=[_card_commentary()]),
        ],
    )


def _card_eligibility():
    return dmc.Card(
        withBorder=True,
        children=[
            _section_title("ACCOUNT ELIGIBILITY"),
            html.Div(
                id=ID.ELIGIBILITY_TABLE,
                children=dmc.Text(
                    "Run analysis to see account eligibility.",
                    size="sm",
                    c="dimmed",
                ),
            ),
        ],
    )


def _row4_key_levels():
    """Row 4: Key levels full width."""
    return dmc.Grid(
        gutter="md",
        children=[
            dmc.GridCol(span=12, children=[_card_key_levels()]),
        ],
    )


def _row5_margin_sidebar():
    """Row 5: Margin (7/12) + Eligibility/Dividend stacked (5/12)."""
    return dmc.Grid(
        gutter="md",
        children=[
            dmc.GridCol(span=7, children=[_card_margin()]),
            dmc.GridCol(
                span=5,
                children=[
                    dmc.Stack(
                        gap="md",
                        children=[
                            _card_eligibility(),
                            _card_dividend(),
                        ],
                    )
                ],
            ),
        ],
    )


# ═══════════════════════════════════════════════════════════
# BLOOMBERG DATA TAB
# ═══════════════════════════════════════════════════════════

def _placeholder_card(title, text):
    return dmc.Card(
        withBorder=True,
        children=[
            _section_title(title),
            dmc.Text(text, size="sm", c="dimmed"),
        ],
    )


def _bloomberg_tab():
    request_summary_card = dmc.Card(
        withBorder=True, shadow="sm", p="md",
        children=[
            dmc.Text("REQUEST SUMMARY", fw=700, size="sm"),
            html.Div(id=ID.BBG_REQUEST_SUMMARY, children=dmc.Text(
                "Click REFRESH DATA on the Dashboard tab to load Bloomberg data.",
                size="sm", c="dimmed",
            )),
        ],
    )

    underlying_card = dmc.Card(
        withBorder=True, shadow="sm", p="md",
        children=[
            dmc.Text("UNDERLYING DATA", fw=700, size="sm"),
            html.Div(id=ID.BBG_UNDERLYING_SUMMARY, children=dmc.Text(
                "No data yet.", size="sm", c="dimmed",
            )),
        ],
    )

    errors_card = dmc.Card(
        withBorder=True, shadow="sm", p="md",
        children=[
            dmc.Text("ERRORS & WARNINGS", fw=700, size="sm"),
            html.Div(id=ID.BBG_ERRORS, children=dmc.Text(
                "No errors.", size="sm", c="dimmed",
            )),
        ],
    )

    leg_quotes_card = dmc.Card(
        withBorder=True, shadow="sm", p="md",
        children=[
            dmc.Text("LEG QUOTES", fw=700, size="sm"),
            dash_table.DataTable(
                id=ID.BBG_LEG_QUOTES,
                columns=[
                    {"name": "Leg", "id": "leg"},
                    {"name": "Type", "id": "type"},
                    {"name": "Strike", "id": "strike"},
                    {"name": "Bid", "id": "bid"},
                    {"name": "Ask", "id": "ask"},
                    {"name": "Mid", "id": "mid"},
                    {"name": "IV", "id": "iv"},
                    {"name": "Delta", "id": "delta"},
                    {"name": "OTM%", "id": "otm_pct"},
                    {"name": "BBG Ticker", "id": "bbg_ticker"},
                ],
                data=[],
                style_table={"overflowX": "auto"},
                style_header=_LEGS_DARK_HEADER,
                style_cell=_LEGS_DARK_CELL,
            ),
        ],
    )

    raw_data_accordion = dmc.Accordion(
        children=[
            dmc.AccordionItem(
                value="raw-data",
                children=[
                    dmc.AccordionControl("Raw Bloomberg Data (JSON)"),
                    dmc.AccordionPanel(
                        html.Pre(
                            id=ID.BBG_UNDERLYING_JSON,
                            style={
                                "maxHeight": "400px",
                                "overflow": "auto",
                                "fontSize": "12px",
                                "whiteSpace": "pre-wrap",
                            },
                        )
                    ),
                ],
            )
        ],
        value=None,  # collapsed by default
    )

    return dmc.Stack(
        gap="md",
        mt="md",
        children=[
            request_summary_card,
            dmc.Grid([
                dmc.GridCol(underlying_card, span=6),
                dmc.GridCol(errors_card, span=6),
            ], gutter="md"),
            leg_quotes_card,
            raw_data_accordion,
        ],
    )


# ═══════════════════════════════════════════════════════════
# ACTIVITY LOG TAB
# ═══════════════════════════════════════════════════════════

def _report_tab():
    return dmc.Stack(
        gap="md",
        mt="md",
        children=[
            # Header row with title and action buttons
            dmc.Group(
                justify="space-between",
                children=[
                    dmc.Text("ACTIVITY LOG", fw=700, size="lg"),
                    dmc.Group(
                        gap="sm",
                        children=[
                            dmc.Button(
                                "Download CSV",
                                id=ID.BTN_DOWNLOAD_CSV,
                                variant="outline",
                                size="sm",
                            ),
                            dmc.Button(
                                "Clear Log",
                                id=ID.BTN_CLEAR_LOG,
                                color="red",
                                variant="outline",
                                size="sm",
                            ),
                        ],
                    ),
                ],
            ),

            # Summary stats
            dmc.Text(id=ID.LOG_SUMMARY, size="sm", c="dimmed"),

            # The log table
            dash_table.DataTable(
                id=ID.LOG_TABLE,
                columns=[
                    {"name": "Date", "id": "timestamp"},
                    {"name": "FA Name", "id": "fa_name"},
                    {"name": "Account #", "id": "acct_number"},
                    {"name": "Ticker", "id": "ticker"},
                    {"name": "Strategy", "id": "strategy"},
                    {"name": "Expiry", "id": "expiry"},
                    {"name": "Contracts", "id": "contracts"},
                    {"name": "Net Premium", "id": "net_premium"},
                    {"name": "Max Profit", "id": "max_profit"},
                    {"name": "Max Loss", "id": "max_loss"},
                ],
                data=[],
                sort_action="native",
                filter_action="native",
                page_size=20,
                style_table={"overflowX": "auto"},
                style_header={"fontWeight": "bold", "backgroundColor": "transparent"},
                style_cell={"textAlign": "center", "padding": "8px", "backgroundColor": "transparent"},
                style_data={"backgroundColor": "transparent"},
                style_filter={"backgroundColor": "transparent"},
            ),

            # Confirmation modal for clear
            dmc.Modal(
                id=ID.CLEAR_LOG_CONFIRM,
                title="Clear Activity Log",
                centered=True,
                children=[
                    dmc.Text("Are you sure you want to clear all log entries? This cannot be undone."),
                    dmc.Group(
                        justify="flex-end",
                        mt="md",
                        children=[
                            dmc.Button("Cancel", id=ID.CLEAR_LOG_CANCEL, variant="outline"),
                            dmc.Button("Clear All", id=ID.CLEAR_LOG_YES, color="red"),
                        ],
                    ),
                ],
            ),

            # Keep report preview area for PDF output
            html.Div(
                id=ID.REPORT_PREVIEW,
                children=dmc.Paper(
                    withBorder=True, p="xl", h=300,
                    children=dmc.Center(h="100%", children=dmc.Text("PDF preview will appear here after generation.", c="dimmed")),
                ),
            ),
        ],
    )
