import plotly.graph_objects as go
import streamlit as st

from core.models import OptionLeg, StrategyInput
from core.payoff import compute_payoff


st.set_page_config(page_title="Options Strategy Builder", layout="wide")
st.title("Options Strategy Builder")


col1, col2 = st.columns(2)
with col1:
    spot = st.number_input("Spot price", min_value=0.01, value=100.0, step=1.0)
with col2:
    stock_position = st.number_input("Stock position (shares)", value=0.0, step=1.0)
avg_cost = st.number_input("Stock average cost", min_value=0.0, value=spot, step=1.0)

st.subheader("Option legs (up to 4)")
legs = []
for idx in range(4):
    with st.expander(f"Leg {idx + 1}", expanded=idx == 0):
        include = st.checkbox("Include leg", key=f"include_{idx}")
        if not include:
            continue
        kind = st.selectbox(
            "Type",
            options=["Call", "Put"],
            key=f"kind_{idx}",
        )
        position_label = st.selectbox(
            "Position",
            options=["Long", "Short"],
            key=f"pos_{idx}",
        )
        strike = st.number_input(
            "Strike",
            min_value=0.01,
            value=spot,
            step=1.0,
            key=f"strike_{idx}",
        )
        premium = st.number_input(
            "Premium (positive)",
            min_value=0.0,
            value=1.0,
            step=0.1,
            key=f"prem_{idx}",
        )
        position = 1.0 if position_label == "Long" else -1.0
        legs.append(
            OptionLeg(
                kind=kind.lower(),
                position=position,
                strike=strike,
                premium=premium,
            )
        )

run = st.button("Run Analysis", type="primary")
if run:
    strategy = StrategyInput(
        spot=spot,
        stock_position=stock_position,
        avg_cost=avg_cost,
        legs=legs,
    )
    results = compute_payoff(strategy)
    price_grid = results["price_grid"]
    pnl = results["pnl"]

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=price_grid, y=pnl, mode="lines", name="Expiry PnL")
    )
    for breakeven in results["breakevens"]:
        fig.add_vline(x=breakeven, line_dash="dash", line_color="gray")
    fig.update_layout(
        xaxis_title="Underlying Price at Expiry",
        yaxis_title="PnL",
        height=500,
    )
    st.plotly_chart(fig, use_container_width=True)
