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
    fetch_option_snapshot,
    fetch_spot,
    resolve_security,
    resolve_option_ticker_from_strike,
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
from ui_state import reset_leg_state_on_context_change


st.set_page_config(page_title="Options Strategy Builder", layout="wide")

def render_dashboard():
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

    selected_strategy_row = None

    if "spot_value" not in st.session_state and "spot_input" not in st.session_state:
        st.session_state["spot_value"] = 100.0
        st.session_state["spot_input"] = 100.0
    elif "spot_value" not in st.session_state:
        st.session_state["spot_value"] = float(
            st.session_state.get("spot_input", 100.0)
        )
    elif "spot_input" not in st.session_state:
        st.session_state["spot_input"] = float(
            st.session_state.get("spot_value", 100.0)
        )

    def _set_spot_state(value: float) -> None:
        st.session_state["spot_value"] = float(value)
        st.session_state["spot_input"] = float(value)

    def _add_notice(key: str, level: str, message: str) -> None:
        notices = st.session_state.get(key)
        if not isinstance(notices, list):
            notices = []
        notices.append((level, message))
        st.session_state[key] = notices

    def _current_underlying() -> str:
        value = (
            st.session_state.get("resolved_underlying")
            or st.session_state.get("underlying_ticker", "")
        )
        return value.strip() if isinstance(value, str) else ""

    def _current_expiry() -> str:
        expiry = st.session_state.get("chain_expiry", date.today())
        if isinstance(expiry, date):
            return expiry.isoformat()
        return str(expiry)

    def _queue_refresh_spot() -> None:
        st.session_state["pending_refresh_spot"] = True

    def _process_refresh_spot() -> None:
        base_ticker = (
            st.session_state.get("resolved_underlying")
            or st.session_state.get("underlying_ticker", "")
        )
        base_ticker = base_ticker.strip() if isinstance(base_ticker, str) else ""
        if not base_ticker:
            _add_notice(
                "spot_notice",
                "warning",
                "Enter an underlying ticker before refreshing.",
            )
            return
        try:
            new_spot = fetch_spot(base_ticker)
        except Exception as exc:
            _add_notice("spot_notice", "error", f"Spot refresh failed: {exc}")
            return
        if pd.isna(new_spot):
            _add_notice(
                "spot_notice",
                "warning",
                "Spot refresh failed; no price returned.",
            )
            return
        _set_spot_state(new_spot)
        st.session_state.pop("spot_notice", None)

    if st.session_state.pop("pending_refresh_spot", False):
        _process_refresh_spot()

    with st.container():
        market_col, strategy_col, chain_col, pricing_col, action_col = st.columns(
            [2.0, 2.6, 2.0, 2.4, 1.6]
        )
        with market_col:
            st.caption("Market")
            spot_input = st.number_input(
                "Spot", min_value=0.01, value=100.0, step=1.0, key="spot_input"
            )
            st.session_state["spot_value"] = float(spot_input)
            spot = float(st.session_state["spot_value"])
            underlying_input = st.text_input("Underlying", key="underlying_ticker")
            resolve_underlying = st.button("Resolve", key="resolve_ticker")
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
                "Resolved",
                value=resolved_underlying,
                disabled=True,
            )
            st.button(
                "Bloomberg: Refresh Spot",
                key="refresh_spot",
                on_click=_queue_refresh_spot,
            )
            for level, message in st.session_state.pop("spot_notice", []):
                if level == "success":
                    st.success(message)
                elif level == "error":
                    st.error(message)
                else:
                    st.warning(message)

        with strategy_col:
            st.caption("Strategy")
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
                    subgroup = st.selectbox(
                        "Subgroup", options=subgroups, key="strategy_subgroup"
                    )
                else:
                    subgroup = None
                    st.info("No subgroups available for this group.")

                strategies_df = (
                    list_strategies(group, subgroup)
                    if subgroup is not None
                    else pd.DataFrame()
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
                        selected_strategy.iloc[0]
                        if not selected_strategy.empty
                        else None
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

        with chain_col:
            st.caption("Expiry")
            chain_expiry = st.date_input(
                "Expiry",
                value=st.session_state.get("chain_expiry", date.today()),
                key="chain_expiry",
            )

        with pricing_col:
            st.caption("Pricing & ROI")
            pricing_mode = st.radio(
                "Pricing",
                options=[MID, DEALABLE],
                key="pricing_mode",
                format_func=lambda value: "MID" if value == MID else "BID/ASK",
                horizontal=True,
            )
            roi_policy = st.selectbox(
                "ROI policy",
                options=[NET_PREMIUM, RISK_MAX_LOSS, CASH_SECURED, MARGIN_PROXY],
                key="roi_policy",
            )
            vol_mode = st.selectbox(
                "Vol mode",
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

        with action_col:
            st.caption("Scenario & actions")
            scenario_mode = st.selectbox(
                "Scenario",
                options=["STANDARD", "INFINITY"],
                key="scenario_mode",
            )
            if scenario_mode == "STANDARD":
                target_cols = st.columns(2)
                downside_tgt = target_cols[0].number_input(
                    "Down x",
                    min_value=0.0,
                    value=0.8,
                    step=0.05,
                    key="downside_tgt",
                )
                upside_tgt = target_cols[1].number_input(
                    "Up x",
                    min_value=0.0,
                    value=1.2,
                    step=0.05,
                    key="upside_tgt",
                )
            else:
                downside_tgt = 0.8
                upside_tgt = 1.2
            fill_leg_prices = st.button(
                "Bloomberg: Fill Leg Prices", key="fill_leg_prices"
            )
            run = st.button("Run Analysis", type="primary")

    reset_leg_state_on_context_change(
        st.session_state,
        st.session_state.get("underlying_ticker", ""),
        st.session_state.get("resolved_underlying", ""),
        _current_expiry(),
        leg_count=4,
    )

    template_kind = (
        str(selected_strategy_row["template_kind"]).strip().upper()
        if selected_strategy_row is not None
        else None
    )

    if fill_leg_prices:
        base_underlying = _current_underlying()
        expiry_value = _current_expiry()
        leg_requests = []
        tickers = []
        for idx in range(4):
            if not st.session_state.get(f"include_{idx}", False):
                continue
            ticker = st.session_state.get(f"bbg_ticker_{idx}", "").strip()
            if not ticker:
                if not base_underlying:
                    _add_notice(
                        "ticker_notice",
                        "warning",
                        f"Leg {idx + 1}: enter an underlying to resolve ticker.",
                    )
                    continue
                kind = st.session_state.get(f"kind_{idx}", "Call")
                put_call = "CALL" if kind == "Call" else "PUT"
                strike = st.session_state.get(f"strike_{idx}", spot)
                try:
                    resolved = resolve_option_ticker_from_strike(
                        base_underlying,
                        expiry_value,
                        put_call,
                        strike,
                    )
                except Exception as exc:
                    _add_notice(
                        "ticker_notice",
                        "error",
                        f"Leg {idx + 1}: ticker resolve failed ({exc}).",
                    )
                    continue
                if resolved:
                    st.session_state[f"bbg_ticker_{idx}"] = resolved
                    ticker = resolved
                else:
                    _add_notice(
                        "ticker_notice",
                        "warning",
                        f"Leg {idx + 1}: no ticker match for {put_call} {strike}.",
                    )
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

    legs = []
    scenario_table = None
    results = None
    pop = None

    left_col, right_col = st.columns([1.25, 1])
    with left_col:
        st.caption("Stock overlay")
        stock_cols = st.columns(2)
        stock_position = stock_cols[0].number_input(
            "Stock position (shares)", value=0.0, step=1.0
        )
        avg_cost = stock_cols[1].number_input(
            "Stock average cost", min_value=0.0, value=spot, step=1.0
        )

        if template_kind == "STOCK_ONLY":
            st.info("Stock-only template; use Stock Position inputs")
        else:
            st.caption("Option legs")
            header_cols = st.columns(
                [0.6, 1.0, 1.0, 0.8, 1.0, 1.0, 1.6, 0.9, 1.0, 0.9]
            )
            header_cols[0].caption("Leg")
            header_cols[1].caption("Type")
            header_cols[2].caption("Side")
            header_cols[3].caption("Ratio")
            header_cols[4].caption("Tag")
            header_cols[5].caption("Strike")
            header_cols[6].caption("Ticker")
            header_cols[7].caption("Manual")
            header_cols[8].caption("Premium")
            header_cols[9].caption("Resolve")

            base_underlying = _current_underlying()
            for idx in range(4):
                row_cols = st.columns(
                    [0.6, 1.0, 1.0, 0.8, 1.0, 1.0, 1.6, 0.9, 1.0, 0.9]
                )
                include = row_cols[0].checkbox(
                    f"Leg {idx + 1}",
                    key=f"include_{idx}",
                    label_visibility="collapsed",
                )
                disabled = not include
                kind = row_cols[1].selectbox(
                    "Type",
                    options=["Call", "Put"],
                    key=f"kind_{idx}",
                    label_visibility="collapsed",
                    disabled=disabled,
                )
                position_label = row_cols[2].selectbox(
                    "Side",
                    options=["Long", "Short"],
                    key=f"pos_{idx}",
                    label_visibility="collapsed",
                    disabled=disabled,
                )
                ratio = row_cols[3].number_input(
                    "Ratio",
                    min_value=1,
                    step=1,
                    value=1,
                    key=f"ratio_{idx}",
                    label_visibility="collapsed",
                    disabled=disabled,
                )
                strike_tag = row_cols[4].text_input(
                    "Tag",
                    key=f"strike_tag_{idx}",
                    label_visibility="collapsed",
                    disabled=disabled,
                )
                strike = row_cols[5].number_input(
                    "Strike",
                    min_value=0.01,
                    value=spot,
                    step=1.0,
                    key=f"strike_{idx}",
                    label_visibility="collapsed",
                    disabled=disabled,
                )
                option_ticker = row_cols[6].text_input(
                    "Option ticker",
                    key=f"bbg_ticker_{idx}",
                    label_visibility="collapsed",
                    disabled=disabled,
                )
                manual_override = row_cols[7].checkbox(
                    "Manual",
                    key=f"manual_prem_{idx}",
                    label_visibility="collapsed",
                    disabled=disabled,
                )
                premium = row_cols[8].number_input(
                    "Premium",
                    min_value=0.0,
                    value=1.0,
                    step=0.1,
                    key=f"prem_{idx}",
                    label_visibility="collapsed",
                    disabled=disabled,
                    help=(
                        "Manual override enabled; this value will be used."
                        if manual_override
                        else "Market data can overwrite this value when available."
                    ),
                )
                resolve_disabled = disabled or not base_underlying
                resolve_clicked = row_cols[9].button(
                    "Resolve",
                    key=f"resolve_leg_{idx}",
                    disabled=resolve_disabled,
                )
                if resolve_clicked:
                    expiry_value = _current_expiry()
                    put_call = "CALL" if kind == "Call" else "PUT"
                    try:
                        resolved = resolve_option_ticker_from_strike(
                            base_underlying,
                            expiry_value,
                            put_call,
                            strike,
                        )
                    except Exception as exc:
                        _add_notice(
                            "ticker_notice",
                            "error",
                            f"Leg {idx + 1}: ticker resolve failed ({exc}).",
                        )
                    else:
                        if resolved:
                            st.session_state[f"bbg_ticker_{idx}"] = resolved
                            _add_notice(
                                "ticker_notice",
                                "success",
                                f"Leg {idx + 1} ticker set to {resolved}.",
                            )
                        else:
                            _add_notice(
                                "ticker_notice",
                                "warning",
                                f"Leg {idx + 1}: no matching ticker.",
                            )
                if include:
                    position = float(ratio) if position_label == "Long" else -float(ratio)
                    legs.append(
                        OptionLeg(
                            kind=kind.lower(),
                            position=position,
                            strike=strike,
                            premium=premium,
                        )
                    )

        for level, message in st.session_state.pop("ticker_notice", []):
            if level == "success":
                st.success(message)
            elif level == "error":
                st.error(message)
            else:
                st.warning(message)

        st.caption("Account eligibility")
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
            eligibility_input = StrategyInput(
                spot=spot,
                stock_position=stock_position,
                avg_cost=avg_cost,
                legs=legs,
            )
            strategy_code = determine_strategy_code(eligibility_input, roi_policy)
            eligibility_table = get_account_eligibility(strategy_code)

            info_cols = st.columns([1.4, 1.0, 1.0])
            account_type = info_cols[0].selectbox(
                "Account Type",
                options=account_types,
                key="account_type",
            )
            info_cols[1].metric("Strategy Code", strategy_code)
            selected_row = eligibility_table[
                eligibility_table["account_type"] == account_type
            ]
            if selected_row.empty:
                eligibility_value = "Unavailable"
            else:
                eligibility_value = selected_row["eligibility"].iloc[0]
            info_cols[2].metric("Eligibility", eligibility_value)

            with st.expander("Eligibility table"):
                st.dataframe(
                    eligibility_table, use_container_width=True, height=220
                )

    with right_col:
        st.caption("Payoff & metrics")
        if run:
            strategy = StrategyInput(
                spot=spot,
                stock_position=stock_position,
                avg_cost=avg_cost,
                legs=legs,
            )
            results = compute_payoff(strategy)

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

            option_basis = capital_basis(strategy, results, roi_policy)
            total_basis = combined_capital_basis(strategy, option_basis)
            if scenario_table is not None and not scenario_table.empty:
                margin_proxy = float(scenario_table["margin_requirement"].iloc[0])
            else:
                margin_proxy = compute_margin_proxy(strategy, results)

            metric_cols = st.columns(3)
            metric_cols[0].metric("Strategy PoP", f"{pop * 100:.1f}%")
            metric_cols[1].metric("Margin Proxy", f"{margin_proxy:.2f}")
            metric_cols[2].metric("Capital Basis", f"{total_basis:.2f}")

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
                height=400,
            )
            st.plotly_chart(fig, use_container_width=True)

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
                st.dataframe(details, use_container_width=True, height=220)

            st.caption("Report")
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
                    file_name=st.session_state.get(
                        "pdf_filename", "strategy_report.pdf"
                    ),
                    mime="application/pdf",
                )
        else:
            st.info("Run Analysis to view payoff and scenarios.")

    st.caption("Scenario table")
    if scenario_table is None or scenario_table.empty:
        st.info("Run Analysis to view scenario results.")
    else:
        st.dataframe(
            scenario_table.head(10),
            use_container_width=True,
            height=260,
        )
        with st.expander("Show full scenario table"):
            st.dataframe(
                scenario_table,
                use_container_width=True,
                height=420,
            )

def render_bloomberg_data():
    st.info("Bloomberg data view coming next")

def render_client_report():
    st.info("Client report preview coming next")


tabs = st.tabs(["Dashboard", "Bloomberg Data", "Client Report"])
with tabs[0]:
    render_dashboard()
with tabs[1]:
    render_bloomberg_data()
with tabs[2]:
    render_client_report()
