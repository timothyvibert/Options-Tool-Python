from datetime import date, datetime
import tempfile
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
from core.eligibility import (
    determine_strategy_code,
    get_account_eligibility,
    load_account_map,
)
from adapters.bloomberg import (
    build_leg_price_updates,
    chain_strikes,
    fetch_option_snapshot,
    fetch_spot,
    fetch_option_chain,
    resolve_security,
    select_chain_ticker,
)
from reporting.report_pdf import build_report_pdf
from core.payoff import _compute_pnl_for_price, compute_payoff
from core.roi import capital_basis, combined_capital_basis
from core.margin import compute_margin_proxy
from core.probability import (
    build_probability_details,
    effective_sigma,
    strategy_pop,
)
from core.pricing import DEALABLE, MID
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
    spot = st.number_input(
        "Spot price", min_value=0.01, value=100.0, step=1.0, key="spot"
    )
    underlying_input = st.text_input(
        "Underlying ticker", key="underlying_ticker"
    )
    resolve_underlying = st.button("Resolve Ticker", key="resolve_ticker")
    if resolve_underlying:
        if underlying_input.strip():
            try:
                resolved = resolve_security(underlying_input.strip())
                st.session_state["resolved_underlying"] = resolved
            except Exception as exc:
                st.error(f"Resolve failed: {exc}")
        else:
            st.warning("Enter an underlying ticker to resolve.")
    resolved_underlying = st.session_state.get("resolved_underlying", "")
    st.text_input(
        "Resolved Underlying",
        value=resolved_underlying,
        disabled=True,
    )
    refresh_spot = st.button("Bloomberg: Refresh Spot", key="refresh_spot")
    if refresh_spot:
        base_ticker = resolved_underlying or underlying_input.strip()
        if base_ticker:
            try:
                new_spot = fetch_spot(base_ticker)
                if pd.isna(new_spot):
                    st.warning("Spot refresh failed; no price returned.")
                else:
                    st.session_state["spot"] = float(new_spot)
            except Exception as exc:
                st.error(f"Spot refresh failed: {exc}")
        else:
            st.warning("Enter an underlying ticker before refreshing.")
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

st.subheader("Option chain")
chain_expiry = st.date_input(
    "Expiry",
    value=st.session_state.get("chain_expiry", date.today()),
    key="chain_expiry",
)
chain_window = st.slider(
    "Chain window (+/- % spot)",
    min_value=0.01,
    max_value=0.5,
    value=st.session_state.get("chain_window", 0.10),
    step=0.01,
    key="chain_window",
)
fetch_chain = st.button("Fetch Option Chain", key="fetch_chain")
if fetch_chain:
    base_ticker = resolved_underlying or underlying_input.strip()
    if not base_ticker:
        st.warning("Enter an underlying ticker before fetching the chain.")
    else:
        try:
            resolved = resolve_security(base_ticker)
            st.session_state["resolved_underlying"] = resolved
            new_spot = fetch_spot(resolved)
            if pd.isna(new_spot):
                st.warning("Spot refresh failed; using current spot value.")
                spot_value = float(st.session_state.get("spot", spot))
            else:
                st.session_state["spot"] = float(new_spot)
                spot_value = float(new_spot)
            chain_df = fetch_option_chain(
                resolved,
                chain_expiry.isoformat(),
                spot_value,
                chain_window,
            )
            st.session_state["option_chain_df"] = chain_df
            st.success(f"Loaded {len(chain_df)} option(s).")
        except Exception as exc:
            st.error(f"Option chain fetch failed: {exc}")

if template_kind == "STOCK_ONLY":
    st.info("Stock-only template; use Stock Position inputs")
else:
    st.subheader("Option legs (up to 4)")
legs = []
chain_df = st.session_state.get("option_chain_df")
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
            put_call = "CALL" if kind == "Call" else "PUT"
            available_strikes = (
                chain_strikes(chain_df, put_call) if chain_df is not None else []
            )
            if available_strikes:
                current_strike = st.session_state.get(
                    f"strike_{idx}", available_strikes[0]
                )
                if current_strike not in available_strikes:
                    current_strike = available_strikes[0]
                strike_index = available_strikes.index(current_strike)
                strike = st.selectbox(
                    "Strike",
                    options=available_strikes,
                    index=strike_index,
                    key=f"strike_{idx}",
                )
                selected_ticker = select_chain_ticker(
                    chain_df, put_call, strike
                )
                if selected_ticker:
                    if st.session_state.get(f"chain_strike_{idx}") != strike:
                        st.session_state[f"bbg_ticker_{idx}"] = selected_ticker
                        st.session_state[f"chain_strike_{idx}"] = strike
            else:
                strike = st.number_input(
                    "Strike",
                    min_value=0.01,
                    value=spot,
                    step=1.0,
                    key=f"strike_{idx}",
                )
                st.session_state[f"chain_strike_{idx}"] = None
            option_ticker = st.text_input(
                "Option ticker (Bloomberg)",
                key=f"bbg_ticker_{idx}",
            )
            manual_override = st.checkbox(
                "Manual override price",
                key=f"manual_prem_{idx}",
            )
            premium = st.number_input(
                "Premium (positive)",
                min_value=0.0,
                value=1.0,
                step=0.1,
                key=f"prem_{idx}",
                help=(
                    "Manual override enabled; this value will be used."
                    if manual_override
                    else "Market data can overwrite this value when available."
                ),
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
pricing_mode = st.radio(
    "Pricing Mode: MID vs BID/ASK (dealable)",
    options=[MID, DEALABLE],
    key="pricing_mode",
    format_func=lambda value: "MID" if value == MID else "BID/ASK (dealable)",
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

st.subheader("Probability")
vol_mode = st.selectbox(
    "Volatility mode",
    options=["ATM", "VEGA_WEIGHTED"],
    key="vol_mode",
)
atm_iv = st.number_input(
    "ATM IV",
    min_value=0.0001,
    value=0.2,
    step=0.01,
    key="atm_iv",
)
show_prob_details = st.checkbox(
    "Show probability details",
    key="show_prob_details",
)

st.subheader("Bloomberg pricing")
fill_leg_prices = st.button("Bloomberg: Fill Leg Prices", key="fill_leg_prices")
if fill_leg_prices:
    leg_requests = []
    tickers = []
    for idx in range(4):
        if not st.session_state.get(f"include_{idx}", False):
            continue
        ticker = st.session_state.get(f"bbg_ticker_{idx}", "").strip()
        if not ticker:
            continue
        manual_override = st.session_state.get(f"manual_prem_{idx}", False)
        position_label = st.session_state.get(f"pos_{idx}", "Long")
        ratio = st.session_state.get(f"ratio_{idx}", 1)
        position = float(ratio) if position_label == "Long" else -float(ratio)
        leg_requests.append(
            {
                "index": idx,
                "ticker": ticker,
                "position": position,
                "manual_override": manual_override,
            }
        )
        if not manual_override:
            tickers.append(ticker)
    unique_tickers = sorted(set(tickers))
    if not unique_tickers:
        st.info("No eligible leg tickers to refresh.")
    else:
        try:
            snapshot = fetch_option_snapshot(unique_tickers)
            updates = build_leg_price_updates(
                leg_requests,
                snapshot,
                pricing_mode,
            )
            for idx, premium in updates.items():
                st.session_state[f"prem_{idx}"] = premium
            if updates:
                st.success(f"Updated {len(updates)} leg price(s).")
            else:
                st.info("No prices updated from Bloomberg data.")
        except Exception as exc:
            st.error(f"Price refresh failed: {exc}")

st.subheader("Account eligibility")
account_map = load_account_map()
if account_map.empty:
    st.warning("No account eligibility data available.")
    account_type = None
    eligibility_table = pd.DataFrame()
    strategy_code = ""
else:
    account_types = sorted(
        account_map["account_type"].dropna().unique().tolist()
    )
    if st.session_state.get("account_type") not in account_types:
        st.session_state["account_type"] = account_types[0]
    account_type = st.selectbox(
        "Account Type",
        options=account_types,
        key="account_type",
    )
    eligibility_input = StrategyInput(
        spot=spot,
        stock_position=stock_position,
        avg_cost=avg_cost,
        legs=legs,
    )
    strategy_code = determine_strategy_code(eligibility_input, roi_policy)
    eligibility_table = get_account_eligibility(strategy_code)

    code_col, eligibility_col = st.columns(2)
    code_col.metric("Strategy Code", strategy_code)
    selected_row = eligibility_table[
        eligibility_table["account_type"] == account_type
    ]
    if selected_row.empty:
        eligibility_value = "Unavailable"
    else:
        eligibility_value = selected_row["eligibility"].iloc[0]
    eligibility_col.metric("Eligibility", eligibility_value)

    with st.expander("Show eligibility table"):
        st.dataframe(eligibility_table, use_container_width=True)

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

    per_leg_iv = [None for _ in legs]
    expiry = st.session_state.get("chain_expiry")
    if isinstance(expiry, date):
        days = (expiry - date.today()).days
        t = max(days / 365.0, 1e-6)
    else:
        t = 1.0
    pop = strategy_pop(
        strategy,
        _compute_pnl_for_price,
        S0=spot,
        r=0.0,
        q=0.0,
        sigma_mode=vol_mode,
        atm_iv=atm_iv,
        per_leg_iv=per_leg_iv,
        t=t,
    )
    st.metric("Strategy PoP", f"{pop * 100:.1f}%")

    if show_prob_details:
        sigma = effective_sigma(
            strategy,
            per_leg_iv=per_leg_iv,
            mode=vol_mode,
            r=0.0,
            q=0.0,
            t=t,
            atm_iv=atm_iv,
        )
        details = build_probability_details(
            S0=spot,
            r=0.0,
            q=0.0,
            sigma=sigma,
            t=t,
            breakevens=results.get("breakevens", []),
        )
        st.dataframe(details, use_container_width=True)

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

    st.subheader("Report")
    generate_pdf = st.button("Generate PDF Report", key="generate_pdf")
    if generate_pdf:
        legs_payload = []
        for idx in range(4):
            if not st.session_state.get(f"include_{idx}", False):
                continue
            ratio = st.session_state.get(f"ratio_{idx}", 1)
            side = st.session_state.get(f"pos_{idx}", "Long")
            qty = ratio if side == "Long" else -ratio
            legs_payload.append(
                {
                    "type": st.session_state.get(f"kind_{idx}", ""),
                    "side": side,
                    "qty": qty,
                    "strike": st.session_state.get(f"strike_{idx}"),
                    "premium": st.session_state.get(f"prem_{idx}"),
                }
            )
        option_basis = capital_basis(strategy, results, roi_policy)
        total_basis = combined_capital_basis(strategy, option_basis)
        margin_proxy = (
            float(scenario_table["margin_requirement"].iloc[0])
            if not scenario_table.empty
            else compute_margin_proxy(strategy, results)
        )
        inputs_payload = {
            "ticker": underlying_input.strip(),
            "resolved_ticker": resolved_underlying,
            "strategy_name": (
                selected_strategy_row["strategy_name"]
                if selected_strategy_row is not None
                else ""
            ),
            "expiry": (
                chain_expiry.isoformat()
                if isinstance(chain_expiry, date)
                else ""
            ),
            "pricing_mode": pricing_mode,
            "spot": spot,
            "stock_position": stock_position,
            "avg_cost": avg_cost,
            "roi_policy": roi_policy,
            "legs": legs_payload,
        }
        summary_payload = {
            "min_pnl": min(results["pnl"]) if results.get("pnl") else None,
            "max_pnl": max(results["pnl"]) if results.get("pnl") else None,
            "breakevens": results.get("breakevens", []),
            "pop": f"{pop * 100:.1f}%",
            "margin_proxy": margin_proxy,
            "capital_basis": total_basis,
        }
        notes = [
            "Expiry-only payoff; interim PnL is not modeled.",
            "Probability of profit is model-based and uses a lognormal distribution.",
            "Margin is a proxy and does not reflect broker-specific rules.",
            "This report is for informational purposes only and is not investment advice.",
        ]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            build_report_pdf(
                tmp.name,
                title="Options Strategy Report",
                as_of=timestamp,
                inputs=inputs_payload,
                summary=summary_payload,
                scenario_df=scenario_table,
                notes=notes,
            )
            tmp_path = tmp.name
        with open(tmp_path, "rb") as handle:
            st.session_state["pdf_bytes"] = handle.read()
        st.session_state["pdf_filename"] = (
            f"strategy_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        )
        st.success("PDF report generated.")
    if st.session_state.get("pdf_bytes"):
        st.download_button(
            "Download PDF Report",
            data=st.session_state["pdf_bytes"],
            file_name=st.session_state.get("pdf_filename", "strategy_report.pdf"),
            mime="application/pdf",
        )
