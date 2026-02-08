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
        ],
        style={"display": "none"},
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
                    dmc.TabsTab("CLIENT REPORT", value="report"),
                ],
                mb="md",
            ),
            dmc.TabsPanel(value="dashboard", children=[_dashboard_tab()]),
            dmc.TabsPanel(value="bloomberg", children=[_bloomberg_tab()]),
            dmc.TabsPanel(value="report", children=[_report_tab()]),
        ],
    )


# ═══════════════════════════════════════════════════════════
# DASHBOARD TAB
# ═══════════════════════════════════════════════════════════

def _dashboard_tab():
    return dmc.Stack(
        gap="md",
        mt="md",
        children=[
            # ROW 1 — Input Controls (3 cards)
            dmc.Grid(
                gutter="md",
                children=[
                    dmc.GridCol(
                        span={"base": 12, "md": 4},
                        children=[_card_market()],
                    ),
                    dmc.GridCol(
                        span={"base": 12, "md": 4},
                        children=[_card_strategy()],
                    ),
                    dmc.GridCol(
                        span={"base": 12, "md": 4},
                        children=[_card_actions()],
                    ),
                ],
            ),
            # ROW 2 — Legs + Settings
            dmc.Grid(
                gutter="md",
                children=[
                    dmc.GridCol(
                        span={"base": 12, "md": 7},
                        children=[_card_legs()],
                    ),
                    dmc.GridCol(
                        span={"base": 12, "md": 5},
                        children=[
                            dmc.Stack(
                                gap="md",
                                children=[_card_pricing(), _card_scenario()],
                            ),
                        ],
                    ),
                ],
            ),
            # ROW 3 — Risk Banner
            _risk_banner(),
            # ROW 4 — Payoff + Metrics
            dmc.Grid(
                gutter="md",
                children=[
                    dmc.GridCol(
                        span={"base": 12, "md": 7},
                        children=[_card_payoff()],
                    ),
                    dmc.GridCol(
                        span={"base": 12, "md": 5},
                        children=[_card_metrics()],
                    ),
                ],
            ),
            # ROW 5 — Commentary + Dividend
            dmc.Grid(
                gutter="md",
                children=[
                    dmc.GridCol(
                        span={"base": 12, "md": 8},
                        children=[_card_commentary()],
                    ),
                    dmc.GridCol(
                        span={"base": 12, "md": 4},
                        children=[_card_dividend()],
                    ),
                ],
            ),
            # ROW 6 — Key Levels + Margin
            dmc.Grid(
                gutter="md",
                children=[
                    dmc.GridCol(
                        span={"base": 12, "md": 8},
                        children=[_card_key_levels()],
                    ),
                    dmc.GridCol(
                        span={"base": 12, "md": 4},
                        children=[_card_margin()],
                    ),
                ],
            ),
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
        withBorder=True,
        children=[
            _section_title("MARKET"),
            dmc.TextInput(
                id=ID.TICKER_INPUT,
                label="Ticker",
                placeholder="e.g. AAPL US Equity",
                size="sm",
                mb="sm",
            ),
            dmc.Text(
                id=ID.SPOT_DISPLAY,
                children="Spot: — (enter ticker and refresh)",
                size="sm",
                c="dimmed",
                mb="xs",
            ),
            dmc.Text(
                id=ID.SPOT_STATUS,
                size="xs",
                c="dimmed",
                mb="sm",
            ),
            dmc.DatePickerInput(
                id=ID.EXPIRY_SELECT,
                label="Expiration",
                placeholder="Select expiry",
                valueFormat="YYYY-MM-DD",
                clearable=True,
                w="100%",
                size="sm",
            ),
        ],
    )


def _card_strategy():
    return dmc.Card(
        withBorder=True,
        children=[
            _section_title("STRATEGY"),
            dmc.Select(
                id=ID.GROUP_SELECT,
                label="Strategy Group",
                placeholder="Select group",
                data=list_groups(),
                size="sm",
                mb="sm",
            ),
            dmc.Group(
                gap="xs",
                align="end",
                children=[
                    dmc.Select(
                        id=ID.STRATEGY_SELECT,
                        label="Strategy",
                        placeholder="Select strategy",
                        data=["Collar", "Bull Call Spread", "Iron Condor"],
                        clearable=True,
                        searchable=True,
                        size="sm",
                        style={"flex": 1},
                    ),
                    dmc.ActionIcon(
                        dmc.Text("X", size="xs"),
                        id=ID.STRATEGY_CLEAR,
                        variant="subtle",
                        color="gray",
                        size="lg",
                    ),
                ],
            ),
        ],
    )


def _card_actions():
    return dmc.Card(
        withBorder=True,
        children=[
            _section_title("STOCK OVERLAY & ACTIONS"),
            dmc.NumberInput(
                id=ID.SHARES_INPUT,
                label="Shares",
                placeholder="0",
                size="sm",
                mb="sm",
            ),
            dmc.NumberInput(
                id=ID.AVG_COST_INPUT,
                label="Avg Cost",
                placeholder="0.00",
                decimalScale=2,
                size="sm",
                mb="md",
            ),
            dmc.Divider(mb="md"),
            dmc.Group(
                grow=True,
                mb="sm",
                children=[
                    dmc.Button(
                        "REFRESH DATA",
                        id=ID.BTN_REFRESH,
                        variant="outline",
                        color="cyan",
                        size="sm",
                    ),
                    dmc.Button(
                        "RUN ANALYSIS",
                        id=ID.BTN_ANALYZE,
                        variant="filled",
                        color="cyan",
                        size="sm",
                    ),
                ],
            ),
            dmc.Button(
                "GENERATE PDF REPORT",
                id=ID.BTN_PDF,
                variant="light",
                color="green",
                fullWidth=True,
                size="sm",
                mb="xs",
            ),
            dmc.Text(
                id=ID.REFRESH_STATUS,
                children="Market refreshed at —",
                size="xs",
                c="dimmed",
                mt="xs",
            ),
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


def _card_pricing():
    return dmc.Card(
        withBorder=True,
        children=[
            _section_title("PRICING & ROI"),
            dmc.Select(
                id=ID.PRICING_MODE,
                label="Pricing Mode",
                data=[
                    {"value": "mid", "label": "Mid"},
                    {"value": "bid_ask", "label": "Bid/Ask"},
                ],
                value="mid",
                size="sm",
                mb="sm",
            ),
            dmc.Select(
                id=ID.PREMIUM_MODE,
                label="Capital Basis",
                data=[
                    {"value": "premium", "label": "Premium"},
                    {"value": "max_loss", "label": "Max Loss"},
                    {"value": "cash_secured", "label": "Cash Secured"},
                    {"value": "margin", "label": "Margin Proxy"},
                ],
                value="premium",
                size="sm",
            ),
        ],
    )


def _card_scenario():
    return dmc.Card(
        withBorder=True,
        children=[
            _section_title("SCENARIO & ACTIONS"),
            dmc.Select(
                id=ID.SCENARIO_MODE,
                label="Scenario Mode",
                data=[
                    {"value": "targets", "label": "Targets"},
                    {"value": "infinity", "label": "Infinity"},
                ],
                value="targets",
                size="sm",
                mb="sm",
            ),
            dmc.Select(
                id=ID.SCENARIO_SELECT,
                label="Scenario",
                placeholder="Select scenario",
                data=["Custom", "Bearish", "Base", "Bullish"],
                size="sm",
                mb="sm",
            ),
            dmc.NumberInput(
                id=ID.DOWNSIDE_TARGET,
                label="Downside Target (%)",
                value=-10.0,
                step=1,
                size="sm",
                mb="sm",
            ),
            dmc.NumberInput(
                id=ID.UPSIDE_TARGET,
                label="Upside Target (%)",
                value=10.0,
                step=1,
                size="sm",
            ),
        ],
    )


# ───────────────────────────────────────────────────────────
# ROW 3 — Risk Banner
# ───────────────────────────────────────────────────────────

def _risk_banner():
    return dmc.Alert(
        id=ID.RISK_BANNER,
        title="Risk Events",
        children="No active risk events. Run analysis to check for ex-dividend dates and earnings.",
        color="yellow",
        variant="light",
        radius="md",
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
        height=400,
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
            _section_title("PAYOFF AT EXPIRY"),
            dcc.Graph(
                id=ID.PAYOFF_CHART,
                figure=fig,
                config={"displayModeBar": False},
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


def _card_metrics():
    return dmc.Card(
        withBorder=True,
        id=ID.METRICS_TABLE,
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

def _scenario_card(title, subtitle, color):
    return dmc.Card(
        withBorder=True,
        padding="md",
        children=[
            dmc.Group(
                gap="xs",
                mb="xs",
                children=[
                    dmc.Badge(
                        title.split()[0],
                        color=color,
                        size="sm",
                        variant="light",
                    ),
                    dmc.Text(title, fw=600, size="sm"),
                ],
            ),
            dmc.Text(subtitle, size="xs", c="dimmed", mb="sm"),
            dmc.Divider(mb="sm"),
            dmc.Text(
                "Run analysis to see scenario commentary.",
                size="sm",
                c="dimmed",
            ),
        ],
    )


def _card_commentary():
    return dmc.Card(
        withBorder=True,
        id=ID.SCENARIO_CARDS,
        children=[
            _section_title("SCENARIO COMMENTARY"),
            dmc.SimpleGrid(
                cols={"base": 1, "sm": 3},
                spacing="md",
                children=[
                    _scenario_card(
                        "Bearish Case",
                        "Stock drops significantly",
                        "red",
                    ),
                    _scenario_card(
                        "Stagnant Case",
                        "Stock stays near current levels",
                        "gray",
                    ),
                    _scenario_card(
                        "Bullish Case",
                        "Stock rises significantly",
                        "green",
                    ),
                ],
            ),
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
            _section_title("MARGIN & CAPITAL"),
            dmc.Table(
                data={
                    "head": ["Field", "Value"],
                    "body": [
                        ["Classification", "\u2014"],
                        ["Margin Proxy", "\u2014"],
                    ],
                },
                withTableBorder=True,
                highlightOnHover=True,
                verticalSpacing="xs",
            ),
            dmc.Divider(my="md"),
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
    return dmc.Stack(
        gap="md",
        mt="md",
        children=[
            dmc.Switch(id=ID.BBG_DEBUG_TOGGLE, label="Debug Mode", size="sm"),
            dmc.Card(
                withBorder=True,
                children=[
                    _section_title("REQUEST SUMMARY"),
                    html.Div(
                        id=ID.BBG_REQUEST_SUMMARY,
                        children=dmc.Text(
                            "Run analysis to see request data.",
                            size="sm",
                            c="dimmed",
                        ),
                    ),
                ],
            ),
            dmc.Card(
                withBorder=True,
                children=[
                    _section_title("UNDERLYING SNAPSHOT"),
                    html.Div(
                        id=ID.BBG_UNDERLYING_SUMMARY,
                        children=dmc.Text(
                            "Run analysis to see underlying data.",
                            size="sm",
                            c="dimmed",
                        ),
                    ),
                    dmc.Divider(my="sm"),
                    _section_title("RAW JSON"),
                    html.Pre(
                        id=ID.BBG_UNDERLYING_JSON,
                        children="--",
                        style={"fontSize": "11px", "maxHeight": "200px", "overflow": "auto"},
                    ),
                ],
            ),
            dmc.Card(
                withBorder=True,
                children=[
                    _section_title("LEG QUOTES"),
                    dash_table.DataTable(
                        id=ID.BBG_LEG_QUOTES,
                        columns=[
                            {"name": "Leg", "id": "leg"},
                            {"name": "Ticker", "id": "option_ticker"},
                            {"name": "Bid", "id": "bid"},
                            {"name": "Ask", "id": "ask"},
                            {"name": "Mid", "id": "mid"},
                            {"name": "Last", "id": "last"},
                            {"name": "IV", "id": "iv"},
                        ],
                        data=[],
                        style_table={"overflowX": "auto"},
                        style_header=_LEGS_DARK_HEADER,
                        style_cell=_LEGS_DARK_CELL,
                    ),
                ],
            ),
            dmc.Card(
                withBorder=True,
                children=[
                    _section_title("ERRORS"),
                    html.Div(
                        id=ID.BBG_ERRORS,
                        children=dmc.Text("No errors.", size="sm", c="dimmed"),
                    ),
                ],
            ),
        ],
    )


# ═══════════════════════════════════════════════════════════
# CLIENT REPORT TAB
# ═══════════════════════════════════════════════════════════

def _report_tab():
    return dmc.Stack(
        gap="md",
        mt="md",
        children=[
            dmc.Card(
                withBorder=True,
                children=[
                    _section_title("CLIENT REPORT"),
                    dmc.TextInput(
                        id=ID.CIO_RATING_INPUT,
                        label="CIO Rating",
                        placeholder="e.g. Buy, Neutral, Sell",
                        size="sm",
                        mb="md",
                    ),
                    dmc.Text(
                        id=ID.REPORT_STATUS,
                        size="sm",
                        c="dimmed",
                        mb="md",
                    ),
                    html.Div(
                        id=ID.REPORT_PREVIEW,
                        children=dmc.Paper(
                            withBorder=True,
                            p="xl",
                            h=400,
                            children=[
                                dmc.Center(
                                    h="100%",
                                    children=[
                                        dmc.Text(
                                            "PDF preview will appear here after generation.",
                                            c="dimmed",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        ],
    )
