"""Dash frontend scaffold for Options Tool.

Run:
  python -m frontend_dash.app
  python frontend_dash/app.py

This is a minimal, backend-first shell that uses a dummy analysis_pack.
"""

from datetime import datetime, timezone

import plotly.graph_objects as go

try:
    from dash import Dash, Input, Output, State, dcc, html
    DASH_AVAILABLE = True
except ModuleNotFoundError:
    DASH_AVAILABLE = False
    Dash = None
    Input = Output = State = None
    dcc = html = None


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
    app.layout = html.Div(
        [
            dcc.Store(id="store-inputs", data={"ticker": "", "spot": 100.0}),
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
        Output("store-inputs", "data"),
        Input("ticker-input", "value"),
        Input("spot-input", "value"),
    )
    def _persist_inputs(ticker: str, spot: float) -> dict:
        try:
            spot_value = float(spot) if spot is not None else 0.0
        except (TypeError, ValueError):
            spot_value = 0.0
        return {"ticker": (ticker or "").strip(), "spot": spot_value}

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
        prevent_initial_call=True,
    )
    def _run_analysis(n_clicks: int, inputs: dict) -> dict:
        ticker = ""
        spot = 0.0
        if isinstance(inputs, dict):
            ticker = str(inputs.get("ticker", "") or "")
            spot = float(inputs.get("spot", 0.0) or 0.0)
        return _build_dummy_analysis_pack(ticker, spot)

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


if __name__ == "__main__":
    if not DASH_AVAILABLE:
        raise SystemExit("Dash is not installed. Install 'dash' to run the app.")
    app.run_server(debug=True, port=8050)
