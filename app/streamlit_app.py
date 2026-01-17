from typing import Optional, Tuple

import pandas as pd
import plotly.graph_objects as go
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


import streamlit as st

from core.models import OptionLeg, StrategyInput
from core.payoff import compute_payoff
from core.roi import CASH_SECURED, MARGIN_PROXY, NET_PREMIUM, RISK_MAX_LOSS
from core.scenarios import build_scenario_points, compute_scenario_table
from core.strategy_map import get_strategy, list_groups, list_strategies, list_subgroups


st.set_page_config(page_title="Options Strategy Builder", layout="wide")
st.title("Options Strategy Builder")


def _parse_leg_type(value: object) -> Optional[str]:
    if pd.isna(value):
        return None
    text = str(value).strip().upper()
    if text in {"CALL", "PUT"}:
        return text
    return None


def _parse_side(value: object) -> str:
    if pd.isna(value):
        return "Long"
    text = str(value).strip().upper()
    return "Short" if text == "SHORT" else "Long"


def _parse_ratio(value: object) -> int:
    if pd.isna(value):
        return 1
    try:
        ratio = int(float(value))
    except (TypeError, ValueError):
        return 1
    return max(ratio, 1)


def _parse_strike(value: object, spot: float) -> Tuple[str, float]:
    if pd.isna(value):
        return "", spot
    if isinstance(value, (int, float)) and not pd.isna(value):
        return "", float(value)
    text = str(value).strip()
    if text == "":
        return "", spot
    try:
        number = float(text)
    except ValueError:
        return text, spot
    return "", number


def _apply_strategy_defaults(strategy_row: pd.Series, spot: float) -> None:
    option_legs = []
    for leg_index in range(1, 5):
        leg_type = _parse_leg_type(strategy_row.get(f"leg_{leg_index}_type"))
        if leg_type not in {"CALL", "PUT"}:
            continue
        side = _parse_side(strategy_row.get(f"leg_{leg_index}_side"))
        ratio = _parse_ratio(strategy_row.get(f"leg_{leg_index}_ratio"))
        strike_tag, strike_value = _parse_strike(
            strategy_row.get(f"leg_{leg_index}_strike"),
            spot,
        )
        option_legs.append(
            {
                "kind": "Call" if leg_type == "CALL" else "Put",
                "side": side,
                "ratio": ratio,
                "strike_tag": strike_tag,
                "strike": strike_value,
            }
        )

    for idx in range(4):
        if idx < len(option_legs):
            leg = option_legs[idx]
            st.session_state[f"include_{idx}"] = True
            st.session_state[f"kind_{idx}"] = leg["kind"]
            st.session_state[f"pos_{idx}"] = leg["side"]
            st.session_state[f"ratio_{idx}"] = leg["ratio"]
            st.session_state[f"strike_tag_{idx}"] = leg["strike_tag"]
            st.session_state[f"strike_{idx}"] = leg["strike"]
        else:
            st.session_state[f"include_{idx}"] = False
            st.session_state[f"kind_{idx}"] = "Call"
            st.session_state[f"pos_{idx}"] = "Long"
            st.session_state[f"ratio_{idx}"] = 1
            st.session_state[f"strike_tag_{idx}"] = ""
            st.session_state[f"strike_{idx}"] = spot


col1, col2 = st.columns(2)
with col1:
    spot = st.number_input("Spot price", min_value=0.01, value=100.0, step=1.0)
with col2:
    stock_position = st.number_input("Stock position (shares)", value=0.0, step=1.0)
avg_cost = st.number_input("Stock average cost", min_value=0.0, value=spot, step=1.0)

st.subheader("Strategy template")
groups = list_groups()
if not groups:
    st.warning("No strategy templates available.")
    selected_strategy_row = None
else:
    if st.session_state.get("strategy_group") not in groups:
        st.session_state["strategy_group"] = groups[0]
    group = st.selectbox("Group", options=groups, key="strategy_group")

    subgroups = list_subgroups(group)
    if subgroups:
        if st.session_state.get("strategy_subgroup") not in subgroups:
            st.session_state["strategy_subgroup"] = subgroups[0]
        subgroup = st.selectbox("Subgroup", options=subgroups, key="strategy_subgroup")
    else:
        subgroup = None
        st.info("No subgroups available for this group.")

    strategies_df = (
        list_strategies(group, subgroup) if subgroup is not None else pd.DataFrame()
    )
    if not strategies_df.empty:
        strategies_df = strategies_df.sort_values("strategy_id")
        strategy_ids = strategies_df["strategy_id"].tolist()
        name_map = dict(
            zip(strategies_df["strategy_id"], strategies_df["strategy_name"])
        )
        if st.session_state.get("strategy_id") not in strategy_ids:
            st.session_state["strategy_id"] = strategy_ids[0]
        strategy_id = st.selectbox(
            "Strategy",
            options=strategy_ids,
            key="strategy_id",
            format_func=lambda value: f"{value} - {name_map.get(value, '')}",
        )
        selected_strategy = get_strategy(strategy_id)
        selected_strategy_row = (
            selected_strategy.iloc[0] if not selected_strategy.empty else None
        )
    else:
        selected_strategy_row = None
        st.info("No strategies available for this group/subgroup.")

    selected_id = (
        int(selected_strategy_row["strategy_id"])
        if selected_strategy_row is not None
        else None
    )
    if selected_id != st.session_state.get("active_strategy_id"):
        st.session_state["active_strategy_id"] = selected_id
        if selected_strategy_row is not None:
            _apply_strategy_defaults(selected_strategy_row, spot)

template_kind = (
    str(selected_strategy_row["template_kind"]).strip().upper()
    if selected_strategy_row is not None
    else None
)

if template_kind == "STOCK_ONLY":
    st.info("Stock-only template; use Stock Position inputs")
else:
    st.subheader("Option legs (up to 4)")
legs = []
if template_kind != "STOCK_ONLY":
    for idx in range(4):
        with st.expander(f"Leg {idx + 1}", expanded=idx == 0):
            include = st.checkbox("Include leg", key=f"include_{idx}")
            if not include:
                continue
            type_col, side_col, ratio_col = st.columns(3)
            kind = type_col.selectbox(
                "Type",
                options=["Call", "Put"],
                key=f"kind_{idx}",
            )
            position_label = side_col.selectbox(
                "Position",
                options=["Long", "Short"],
                key=f"pos_{idx}",
            )
            ratio = ratio_col.number_input(
                "Ratio",
                min_value=1,
                step=1,
                value=1,
                key=f"ratio_{idx}",
            )
            strike_tag = st.text_input(
                "Strike tag",
                key=f"strike_tag_{idx}",
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
            position = float(ratio) if position_label == "Long" else -float(ratio)
            legs.append(
                OptionLeg(
                    kind=kind.lower(),
                    position=position,
                    strike=strike,
                    premium=premium,
                )
            )

st.subheader("Scenario settings")
scenario_mode = st.selectbox(
    "Scenario mode",
    options=["STANDARD", "INFINITY"],
    key="scenario_mode",
)
roi_policy = st.selectbox(
    "ROI policy",
    options=[NET_PREMIUM, RISK_MAX_LOSS, CASH_SECURED, MARGIN_PROXY],
    key="roi_policy",
)
if scenario_mode == "STANDARD":
    downside_tgt = st.number_input(
        "Downside target (x spot)",
        min_value=0.0,
        value=0.8,
        step=0.05,
        key="downside_tgt",
    )
    upside_tgt = st.number_input(
        "Upside target (x spot)",
        min_value=0.0,
        value=1.2,
        step=0.05,
        key="upside_tgt",
    )
else:
    downside_tgt = 0.8
    upside_tgt = 1.2

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

    scenario_points = build_scenario_points(
        strategy,
        results,
        mode=scenario_mode,
        downside_tgt=downside_tgt,
        upside_tgt=upside_tgt,
    )
    scenario_table = compute_scenario_table(
        strategy,
        scenario_points,
        payoff_result=results,
        roi_policy=roi_policy,
        strategy_row=selected_strategy_row,
    )

    st.subheader("Scenario table")
    st.dataframe(scenario_table.head(10), use_container_width=True)
    with st.expander("Show full scenario table"):
        st.dataframe(scenario_table, use_container_width=True)
