from datetime import date, datetime
import math
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
from core.analysis_pack import build_analysis_pack
from adapters.bloomberg import (
    build_leg_price_updates,
    fetch_option_snapshot,
    fetch_spot,
    fetch_underlying_snapshot,
    resolve_security,
    resolve_option_ticker_from_strike,
)
from reporting.report_pdf import build_report_pdf
from core.payoff import _compute_pnl_for_price, compute_payoff
from core.roi import capital_basis, combined_capital_basis
from core.margin import classify_strategy, compute_margin_proxy
from core.probability import (
    build_probability_details,
    effective_sigma,
    strategy_pop,
)
from core.pricing import DEALABLE, MID
from core.roi import (
    CASH_SECURED,
    MARGIN_PROXY,
    NET_PREMIUM,
    RISK_MAX_LOSS,
    compute_net_premium,
)
from core.scenarios import build_scenario_points, compute_scenario_table
from core.strategy_map import get_strategy, list_groups, list_strategies, list_subgroups
from ui_state import reset_leg_state_on_context_change


DEBUG_UI = False

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

    def _contract_identity(idx: int) -> tuple[str, str, str, float]:
        underlying = _current_underlying().upper()
        expiry = _current_expiry()
        kind = st.session_state.get(f"kind_{idx}", "Call")
        kind_text = str(kind).strip().upper()
        put_call = "CALL" if kind_text.startswith("C") else "PUT"
        strike_value = st.session_state.get(f"strike_{idx}", spot)
        try:
            strike = float(strike_value)
        except (TypeError, ValueError):
            strike = float("nan")
        return (underlying, expiry, put_call, strike)

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
        st.session_state["last_spot_refresh"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
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
        identity_changed = False
        for idx in range(4):
            if not st.session_state.get(f"include_{idx}", False):
                continue
            identity = _contract_identity(idx)
            prev_identity = st.session_state.get(f"bbg_contract_id_{idx}")
            if prev_identity is not None and prev_identity != identity:
                st.session_state[f"bbg_ticker_{idx}"] = ""
                identity_changed = True
            st.session_state[f"bbg_contract_id_{idx}"] = identity
        if identity_changed:
            st.session_state.pop("bbg_snapshot_df", None)
            st.session_state.pop("bbg_snapshot_time", None)
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
                st.session_state["bbg_snapshot_df"] = snapshot.copy()
                st.session_state["bbg_snapshot_time"] = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
                if base_underlying:
                    try:
                        underlying_snapshot = fetch_underlying_snapshot(
                            base_underlying
                        )
                        st.session_state["underlying_snapshot"] = (
                            underlying_snapshot
                        )
                        st.session_state["underlying_snapshot_status"] = {
                            "ok": True,
                            "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "ticker": base_underlying,
                            "source": "fill_leg_prices",
                        }
                    except Exception as exc:
                        st.session_state["underlying_snapshot"] = {
                            "error": str(exc)
                        }
                        st.session_state["underlying_snapshot_status"] = {
                            "ok": False,
                            "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "ticker": base_underlying,
                            "source": "fill_leg_prices",
                            "error": str(exc),
                        }
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
    leg_meta = []
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
                [0.5, 1.0, 1.0, 0.9, 1.0, 1.0, 0.9, 1.6]
            )
            header_cols[0].caption("")
            header_cols[1].caption("Type")
            header_cols[2].caption("Side")
            header_cols[3].caption("Qty")
            header_cols[4].caption("Strike")
            header_cols[5].caption("Premium")
            header_cols[6].caption("Override")
            header_cols[7].caption("Option Ticker")
            for idx in range(4):
                row_cols = st.columns(
                    [0.5, 1.0, 1.0, 0.9, 1.0, 1.0, 0.9, 1.6]
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
                    "Qty",
                    min_value=1,
                    step=1,
                    value=1,
                    key=f"ratio_{idx}",
                    label_visibility="collapsed",
                    disabled=disabled,
                )
                strike = row_cols[4].number_input(
                    "Strike",
                    min_value=0.01,
                    value=spot,
                    step=1.0,
                    key=f"strike_{idx}",
                    label_visibility="collapsed",
                    disabled=disabled,
                )
                manual_override_value = st.session_state.get(
                    f"manual_prem_{idx}", False
                )
                premium = row_cols[5].number_input(
                    "Premium",
                    min_value=0.0,
                    value=1.0,
                    step=0.1,
                    key=f"prem_{idx}",
                    label_visibility="collapsed",
                    disabled=disabled,
                    help=(
                        "Manual override enabled; this value will be used."
                        if manual_override_value
                        else "Market data can overwrite this value when available."
                    ),
                )
                manual_override = row_cols[6].checkbox(
                    "Manual",
                    key=f"manual_prem_{idx}",
                    label_visibility="collapsed",
                    disabled=disabled,
                )
                option_ticker = row_cols[7].text_input(
                    "Option ticker",
                    key=f"bbg_ticker_{idx}",
                    label_visibility="collapsed",
                    disabled=disabled,
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
                    leg_meta.append(
                        {
                            "index": idx + 1,
                            "kind": kind,
                            "side": position_label,
                            "ratio": ratio,
                            "strike": strike,
                            "premium": premium,
                            "ticker": option_ticker,
                            "override": manual_override,
                        }
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

            price_grid = results["price_grid"]
            combined_pnl = results["pnl"]
            option_only = StrategyInput(
                spot=spot,
                stock_position=0.0,
                avg_cost=0.0,
                legs=legs,
            )
            options_pnl = [
                _compute_pnl_for_price(option_only, price) for price in price_grid
            ]
            stock_pnl = [
                combined - option
                for combined, option in zip(combined_pnl, options_pnl)
            ]
            net_premium = compute_net_premium(strategy)
            if net_premium < 0:
                net_premium_text = f"Credit {abs(net_premium):.2f}"
            elif net_premium > 0:
                net_premium_text = f"Debit {net_premium:.2f}"
            else:
                net_premium_text = "0.00"
            breakevens = results.get("breakevens", [])
            breakeven_text = (
                ", ".join(f"{value:g}" for value in breakevens)
                if breakevens
                else "None"
            )
            summary_rows = [
                {"Metric": "Max Option PnL", "Value": f"{max(options_pnl):.2f}"},
                {"Metric": "Min Option PnL", "Value": f"{min(options_pnl):.2f}"},
                {"Metric": "Max Combined PnL", "Value": f"{max(combined_pnl):.2f}"},
                {"Metric": "Min Combined PnL", "Value": f"{min(combined_pnl):.2f}"},
                {"Metric": "Breakeven(s)", "Value": breakeven_text},
                {"Metric": "Net Premium", "Value": net_premium_text},
                {"Metric": "Strategy PoP", "Value": f"{pop * 100:.1f}%"},
                {"Metric": "Capital Basis", "Value": f"{total_basis:.2f}"},
            ]
            summary_df = pd.DataFrame(summary_rows)
            margin_rows = [
                {
                    "Metric": "Strategy Code",
                    "Value": classify_strategy(strategy),
                },
                {"Metric": "Margin Proxy", "Value": f"{margin_proxy:.2f}"},
                {"Metric": "ROI Policy", "Value": roi_policy},
            ]
            margin_df = pd.DataFrame(margin_rows)

            raw_strikes = []
            for leg in legs:
                strike = leg.strike
                if isinstance(strike, (int, float)) and math.isfinite(strike):
                    raw_strikes.append(float(strike))
            analysis_strikes = []
            for value in sorted(raw_strikes):
                if not analysis_strikes or abs(value - analysis_strikes[-1]) > 1e-6:
                    analysis_strikes.append(value)

            options_notional = sum(
                abs(leg.position) * leg.strike * leg.multiplier for leg in legs
            )
            combined_notional = options_notional + abs(stock_position * spot)
            net_prem_pct = (net_premium / spot * 100.0) if spot else 0.0

            option_roi_values = []
            net_roi_values = []
            if scenario_table is not None and not scenario_table.empty:
                option_roi_values = [
                    float(value)
                    for value in scenario_table["option_roi"].dropna().tolist()
                ]
                net_roi_values = [
                    float(value) for value in scenario_table["net_roi"].dropna().tolist()
                ]

            pop_text = f"{pop * 100:.1f}%"
            analysis_summary = {
                "max_profit_options": f"{max(options_pnl):.2f}" if options_pnl else "--",
                "max_profit_combined": f"{max(combined_pnl):.2f}" if combined_pnl else "--",
                "max_loss_options": f"{min(options_pnl):.2f}" if options_pnl else "--",
                "max_loss_combined": f"{min(combined_pnl):.2f}" if combined_pnl else "--",
                "capital_basis_options": f"{option_basis:.2f}",
                "capital_basis_combined": f"{total_basis:.2f}",
                "max_roi_options": f"{max(option_roi_values):.2f}"
                if option_roi_values
                else "--",
                "max_roi_combined": f"{max(net_roi_values):.2f}"
                if net_roi_values
                else "--",
                "min_roi_options": f"{min(option_roi_values):.2f}"
                if option_roi_values
                else "--",
                "min_roi_combined": f"{min(net_roi_values):.2f}"
                if net_roi_values
                else "--",
                "cost_credit_options": net_premium_text,
                "cost_credit_combined": net_premium_text,
                "notional_options": f"{options_notional:.2f}",
                "notional_combined": f"{combined_notional:.2f}",
                "net_prem_per_share": f"{net_premium:.2f}",
                "net_prem_pct_spot": f"{net_prem_pct:.2f}%",
                "pop_options": pop_text,
                "pop_combined": pop_text,
            }

            st.session_state["analysis_payoff"] = {
                "price_grid": list(price_grid) if price_grid is not None else [],
                "options_pnl": list(options_pnl),
                "stock_pnl": list(stock_pnl),
                "combined_pnl": list(combined_pnl),
                "strikes": analysis_strikes,
                "breakevens": list(breakevens) if breakevens is not None else [],
            }
            st.session_state["analysis_scenario_df"] = scenario_table.copy()
            st.session_state["analysis_summary"] = analysis_summary
            analysis_as_of = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.session_state["analysis_as_of"] = analysis_as_of

            underlying_profile = st.session_state.get("underlying_snapshot")
            base_underlying = resolved_underlying or underlying_input.strip()
            if base_underlying:
                try:
                    underlying_profile = fetch_underlying_snapshot(base_underlying)
                    st.session_state["underlying_snapshot"] = underlying_profile
                except Exception:
                    underlying_profile = st.session_state.get("underlying_snapshot")
            if not isinstance(underlying_profile, (dict, pd.Series)):
                underlying_profile = None
            analysis_pack = build_analysis_pack(
                strategy_input=strategy,
                strategy_meta={
                    "group": st.session_state.get("strategy_group"),
                    "subgroup": st.session_state.get("strategy_subgroup"),
                    "strategy_id": st.session_state.get("strategy_id"),
                    "strategy_name": (
                        selected_strategy_row["strategy_name"]
                        if selected_strategy_row is not None
                        else ""
                    ),
                    "expiry": chain_expiry,
                    "as_of": analysis_as_of,
                    "underlying_ticker": underlying_input.strip(),
                    "resolved_underlying": resolved_underlying,
                    "legs_meta": leg_meta,
                    "strategy_row": selected_strategy_row,
                },
                pricing_mode=pricing_mode,
                roi_policy=roi_policy,
                vol_mode=vol_mode,
                atm_iv=atm_iv,
                underlying_profile=underlying_profile,
                bbg_leg_snapshots=None,
                scenario_mode=scenario_mode,
                downside_tgt=downside_tgt,
                upside_tgt=upside_tgt,
            )
            assert "key_levels" in analysis_pack
            st.session_state["analysis_pack"] = analysis_pack

            payoff_cols = st.columns([1.6, 1.0])
            with payoff_cols[0]:
                chart_toggle_cols = st.columns(3)
                show_options = chart_toggle_cols[0].checkbox(
                    "Show Options PnL",
                    value=True,
                    key="show_options_pnl",
                )
                show_stock = chart_toggle_cols[1].checkbox(
                    "Show Stock PnL",
                    value=stock_position != 0,
                    key="show_stock_pnl",
                )
                show_combined = chart_toggle_cols[2].checkbox(
                    "Show Combined PnL",
                    value=True,
                    key="show_combined_pnl",
                )
                annotate_cols = st.columns(2)
                show_strikes = annotate_cols[0].checkbox(
                    "Show Strikes", value=True, key="show_strikes"
                )
                show_breakevens = annotate_cols[1].checkbox(
                    "Show Breakevens", value=True, key="show_breakevens"
                )

                fig = go.Figure()
                if show_options:
                    fig.add_trace(
                        go.Scatter(
                            x=price_grid,
                            y=options_pnl,
                            mode="lines",
                            name="Options PnL",
                            line=dict(color="#1f77b4"),
                        )
                    )
                if show_stock:
                    fig.add_trace(
                        go.Scatter(
                            x=price_grid,
                            y=stock_pnl,
                            mode="lines",
                            name="Stock PnL",
                            line=dict(color="#2ca02c", dash="dot"),
                        )
                    )
                if show_combined:
                    fig.add_trace(
                        go.Scatter(
                            x=price_grid,
                            y=combined_pnl,
                            mode="lines",
                            name="Combined PnL",
                            line=dict(color="#111111", width=2),
                        )
                    )

                label_positions = [
                    "top left",
                    "top right",
                    "bottom left",
                    "bottom right",
                ]
                if show_strikes:
                    raw_strikes = []
                    for leg in legs:
                        strike = leg.strike
                        if isinstance(strike, (int, float)) and math.isfinite(strike):
                            raw_strikes.append(float(strike))
                    strikes = []
                    for value in sorted(raw_strikes):
                        if not strikes or abs(value - strikes[-1]) > 1e-6:
                            strikes.append(value)
                    strike_label_limit = 6
                    for idx, strike in enumerate(strikes):
                        label = None
                        if idx < strike_label_limit:
                            label = f"K{idx + 1}={strike:g}"
                        if label:
                            fig.add_vline(
                                x=strike,
                                line_dash="dot",
                                line_color="rgba(0,0,0,0.35)",
                                annotation_text=label,
                                annotation_position=label_positions[
                                    idx % len(label_positions)
                                ],
                            )
                        else:
                            fig.add_vline(
                                x=strike,
                                line_dash="dot",
                                line_color="rgba(0,0,0,0.35)",
                            )

                if show_breakevens:
                    breakevens = []
                    for value in results.get("breakevens", []):
                        if isinstance(value, (int, float)) and math.isfinite(value):
                            breakevens.append(float(value))
                    breakevens = sorted(breakevens)
                    breakeven_label_limit = 4
                    for idx, breakeven in enumerate(breakevens):
                        label = None
                        if idx < breakeven_label_limit:
                            label = f"BE{idx + 1}={breakeven:g}"
                        if label:
                            fig.add_vline(
                                x=breakeven,
                                line_dash="dash",
                                line_color="rgba(255,0,0,0.45)",
                                annotation_text=label,
                                annotation_position=label_positions[
                                    idx % len(label_positions)
                                ],
                            )
                        else:
                            fig.add_vline(
                                x=breakeven,
                                line_dash="dash",
                                line_color="rgba(255,0,0,0.45)",
                            )
                fig.update_layout(
                    xaxis_title="Underlying Price at Expiry",
                    yaxis_title="PnL",
                    height=340,
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
                    st.dataframe(details, use_container_width=True, height=200)

            with payoff_cols[1]:
                st.caption("Payoff & Metrics")
                st.dataframe(
                    summary_df,
                    use_container_width=True,
                    height=260,
                    hide_index=True,
                )
                st.caption("Margin & Capital")
                st.dataframe(
                    margin_df,
                    use_container_width=True,
                    height=140,
                    hide_index=True,
                )
                dividend_risk = None
                if isinstance(analysis_pack, dict):
                    underlying_info = analysis_pack.get("underlying")
                    if isinstance(underlying_info, dict):
                        dividend_risk = underlying_info.get("dividend_risk")
                ex_div_date = (
                    dividend_risk.get("ex_div_date")
                    if isinstance(dividend_risk, dict)
                    else None
                )
                if isinstance(ex_div_date, datetime):
                    ex_div_display = ex_div_date.date().isoformat()
                elif isinstance(ex_div_date, date):
                    ex_div_display = ex_div_date.isoformat()
                elif ex_div_date:
                    ex_div_display = str(ex_div_date)
                else:
                    ex_div_display = "--"
                days_to_dividend = (
                    dividend_risk.get("days_to_dividend")
                    if isinstance(dividend_risk, dict)
                    else None
                )
                if isinstance(days_to_dividend, (int, float)) and not pd.isna(
                    days_to_dividend
                ):
                    days_display = str(int(days_to_dividend))
                else:
                    days_display = "--"
                before_expiry = (
                    dividend_risk.get("before_expiry")
                    if isinstance(dividend_risk, dict)
                    else None
                )
                if before_expiry is True:
                    before_display = "Yes"
                elif before_expiry is False:
                    before_display = "No"
                else:
                    before_display = "--"
                dividend_df = pd.DataFrame(
                    [
                        {"Metric": "Ex-div date", "Value": ex_div_display},
                        {"Metric": "Days to dividend", "Value": days_display},
                        {"Metric": "Before expiry", "Value": before_display},
                    ]
                )
                st.caption("Dividend")
                st.dataframe(
                    dividend_df,
                    use_container_width=True,
                    height=120,
                    hide_index=True,
                )

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
        display_cols = [
            "scenario",
            "price",
            "option_pnl",
            "stock_pnl",
            "combined_pnl",
            "net_roi",
            "commentary",
        ]
        scenario_display = scenario_table[display_cols].rename(
            columns={
                "scenario": "Scenario",
                "price": "Scenario Price",
                "option_pnl": "Option PnL",
                "stock_pnl": "Stock PnL",
                "combined_pnl": "Combined PnL",
                "net_roi": "ROI",
                "commentary": "Commentary",
            }
        )
        st.dataframe(
            scenario_display.head(10),
            use_container_width=True,
            height=260,
        )
        with st.expander("Show full scenario table"):
            st.dataframe(
                scenario_display,
                use_container_width=True,
                height=420,
            )

def render_bloomberg_data():
    st.title("Bloomberg Data")

    st.caption("Underlying Snapshot")
    underlying_rows = [
        {"Field": "Underlying", "Value": st.session_state.get("underlying_ticker", "")}
    ]
    resolved = st.session_state.get("resolved_underlying", "")
    if resolved:
        underlying_rows.append({"Field": "Resolved", "Value": resolved})
    underlying_rows.append(
        {
            "Field": "Spot",
            "Value": st.session_state.get("spot_value", ""),
        }
    )
    underlying_rows.append(
        {
            "Field": "Last Spot Refresh",
            "Value": st.session_state.get("last_spot_refresh", "Never"),
        }
    )
    st.table(pd.DataFrame(underlying_rows))

    st.caption("Dividend risk")
    analysis_pack = st.session_state.get("analysis_pack")
    dividend_risk = {}
    if isinstance(analysis_pack, dict):
        underlying_info = analysis_pack.get("underlying")
        if isinstance(underlying_info, dict):
            risk = underlying_info.get("dividend_risk")
            if isinstance(risk, dict):
                dividend_risk = risk

    ex_div_date = dividend_risk.get("ex_div_date")
    if isinstance(ex_div_date, datetime):
        ex_div_display = ex_div_date.date().isoformat()
    elif isinstance(ex_div_date, date):
        ex_div_display = ex_div_date.isoformat()
    elif ex_div_date:
        ex_div_display = str(ex_div_date)
    else:
        ex_div_display = "--"

    days_to_dividend = dividend_risk.get("days_to_dividend")
    days_display = (
        str(int(days_to_dividend))
        if isinstance(days_to_dividend, (int, float)) and not pd.isna(days_to_dividend)
        else "--"
    )

    before_expiry = dividend_risk.get("before_expiry")
    if ex_div_display == "--" or before_expiry is None:
        before_display = "--"
    else:
        before_display = "Yes" if before_expiry else "No"

    st.write(f"Ex-div date: {ex_div_display}")
    st.write(f"Days to dividend: {days_display}")
    st.write(f"Dividend before expiry: {before_display}")

    with st.expander("Dividend (BDS) debug"):
        snapshot = st.session_state.get("underlying_snapshot")
        debug_payload = None
        if isinstance(snapshot, pd.Series):
            debug_payload = snapshot.to_dict().get("dividend_debug")
        elif isinstance(snapshot, dict):
            debug_payload = snapshot.get("dividend_debug")
        if debug_payload is None:
            debug_payload = {}
        if isinstance(snapshot, (dict, pd.Series)):
            st.write(f"Underlying snapshot present: True (keys={len(snapshot)})")
        else:
            st.write("Underlying snapshot present: False")
        st.json(debug_payload)

    with st.expander("Key Levels (analysis_pack)"):
        has_pack = "analysis_pack" in st.session_state
        st.write("analysis_pack present:", has_pack)
        if has_pack:
            analysis_pack = st.session_state.get("analysis_pack")
            has_key_levels = (
                isinstance(analysis_pack, dict) and "key_levels" in analysis_pack
            )
            st.write("key_levels present:", has_key_levels)
            if has_key_levels:
                st.json(analysis_pack.get("key_levels"))
            else:
                st.warning("analysis_pack has no key_levels")
        else:
            st.warning("No analysis_pack in session_state")

    st.caption("Option Legs Snapshot")
    snapshot = st.session_state.get("bbg_snapshot_df")
    if not isinstance(snapshot, pd.DataFrame) or snapshot.empty:
        st.info("No snapshot data. Use Fill Leg Prices on Dashboard first.")
    else:
        snapshot_df = snapshot.copy()
        if "security" not in snapshot_df.columns:
            snapshot_df = snapshot_df.rename(columns={"Security": "security"})
        if "dte" not in snapshot_df.columns:
            dte_series = pd.to_numeric(
                snapshot_df.get("DAYS_TO_EXPIRATION"), errors="coerce"
            )
            if "DAYS_EXPIRE" in snapshot_df.columns:
                dte_series = dte_series.fillna(
                    pd.to_numeric(snapshot_df.get("DAYS_EXPIRE"), errors="coerce")
                )
            snapshot_df["dte"] = dte_series
        if snapshot_df["dte"].isna().all():
            fallback_expiry = st.session_state.get("chain_expiry")
            fallback_as_of = st.session_state.get("bbg_snapshot_time")
            expiry_dt = pd.to_datetime(fallback_expiry, errors="coerce")
            as_of_dt = pd.to_datetime(fallback_as_of, errors="coerce")
            if not pd.isna(expiry_dt) and not pd.isna(as_of_dt):
                dte_value = (expiry_dt.date() - as_of_dt.date()).days
                snapshot_df["dte"] = snapshot_df["dte"].fillna(dte_value)
        ticker_map = {}
        for _, row in snapshot_df.iterrows():
            security = str(row.get("security", "")).strip().upper()
            if security:
                ticker_map[security] = row

        leg_rows = []
        pricing_mode = st.session_state.get("pricing_mode", "")
        expiry_value = st.session_state.get("chain_expiry")
        expiry_text = (
            expiry_value.isoformat()
            if isinstance(expiry_value, date)
            else str(expiry_value)
            if expiry_value
            else ""
        )
        for idx in range(4):
            if not st.session_state.get(f"include_{idx}", False):
                continue
            ticker = st.session_state.get(f"bbg_ticker_{idx}", "").strip()
            row = ticker_map.get(ticker.upper()) if ticker else None
            put_call = row.get("OPT_PUT_CALL") if row is not None else None
            strike = row.get("OPT_STRIKE_PX") if row is not None else None
            expiry = row.get("OPT_EXPIRATION_DATE") if row is not None else None
            dte = None
            if row is not None:
                dte = row.get("dte")
                if pd.isna(dte):
                    dte = row.get("DAYS_TO_EXPIRATION")
                if pd.isna(dte):
                    dte = row.get("DAYS_EXPIRE")
                if pd.isna(dte):
                    expiry_value = expiry if expiry is not None else expiry_text
                    as_of_value = st.session_state.get("bbg_snapshot_time")
                    expiry_dt = pd.to_datetime(expiry_value, errors="coerce")
                    as_of_dt = pd.to_datetime(as_of_value, errors="coerce")
                    if not pd.isna(expiry_dt) and not pd.isna(as_of_dt):
                        dte = (expiry_dt.date() - as_of_dt.date()).days
                dte = pd.to_numeric(dte, errors="coerce")
                if pd.isna(dte):
                    dte = None
                else:
                    dte = int(dte)
            bid = row.get("BID") if row is not None else None
            ask = row.get("ASK") if row is not None else None
            mid = None
            if row is not None:
                mid = row.get("PX_MID")
                if pd.isna(mid):
                    mid = row.get("MID")
            iv = row.get("IVOL_MID") if row is not None else None
            override = st.session_state.get(f"manual_prem_{idx}", False)
            selected_premium = (
                st.session_state.get(f"prem_{idx}") if not override else None
            )

            if put_call is None:
                kind = st.session_state.get(f"kind_{idx}", "")
                put_call = "CALL" if kind == "Call" else "PUT" if kind else None
            if pd.isna(strike):
                strike = st.session_state.get(f"strike_{idx}")
            expiry_display = expiry if expiry is not None else expiry_text

            leg_rows.append(
                {
                    "Leg": idx + 1,
                    "Option Ticker": ticker,
                    "Put/Call": put_call,
                    "Strike": strike,
                    "Expiry": expiry_display,
                    "DTE": dte,
                    "Bid": bid,
                    "Mid": mid,
                    "Ask": ask,
                    "Selected Premium": selected_premium,
                    "Pricing Mode": pricing_mode,
                    "Override": override,
                    "IV": iv,
                }
            )
        if leg_rows:
            st.dataframe(
                pd.DataFrame(leg_rows),
                use_container_width=True,
                height=260,
            )
        else:
            st.info("No active legs to display.")

    with st.expander("Raw Bloomberg payload"):
        underlying_snapshot = st.session_state.get("underlying_snapshot")
        if isinstance(underlying_snapshot, pd.Series):
            st.json(underlying_snapshot.to_dict())
        elif isinstance(underlying_snapshot, dict):
            st.json(underlying_snapshot)
        else:
            st.info("No underlying snapshot payload available.")

        if isinstance(snapshot, pd.DataFrame) and not snapshot.empty:
            st.dataframe(snapshot_df, use_container_width=True, height=240)
        else:
            st.info("No option snapshot payload available.")

def render_client_report():
    from reporting.report_model import build_report_model

    model = build_report_model(st.session_state)

    analysis_payoff = st.session_state.get("analysis_payoff", {})
    price_grid = analysis_payoff.get("price_grid", []) if isinstance(analysis_payoff, dict) else []
    if not price_grid:
        st.info("Run Analysis on the Dashboard to preview the client report.")
        return

    payoff = model.get("payoff", {})

    def _as_text(value: object) -> str:
        if value is None:
            return "--"
        text = str(value).strip()
        return text if text else "--"

    def _header_cell(col, label: str, value: object, value_class: str = "report-value") -> None:
        col.markdown(f"<div class='report-label'>{label}</div>", unsafe_allow_html=True)
        col.markdown(
            f"<div class='{value_class}'>{_as_text(value)}</div>",
            unsafe_allow_html=True,
        )

    def _render_table(rows, columns) -> None:
        safe_rows = []
        for row in rows:
            safe_rows.append({col: _as_text(row.get(col, "--")) for col in columns})
        df = pd.DataFrame(safe_rows, columns=columns)
        html = df.to_html(index=False, classes="report-table", border=0, escape=False)
        st.markdown(html, unsafe_allow_html=True)

    def _to_float(value: object) -> Optional[float]:
        if value is None:
            return None
        if isinstance(value, (int, float)):
            return float(value) if math.isfinite(value) else None
        if isinstance(value, str):
            text = value.replace(",", "").strip()
            if text == "":
                return None
            try:
                return float(text)
            except ValueError:
                return None
        return None

    report_css = """
<style>
.report-title {color:#E60000;font-size:24px;font-weight:700;margin:0;}
.report-label {font-size:10px;text-transform:uppercase;color:#6B7280;letter-spacing:0.04em;margin-bottom:2px;}
.report-value {font-size:11px;color:#111827;margin:0;}
.report-section-title {font-size:12px;font-weight:700;text-transform:uppercase;color:#111827;margin:0 0 6px 0;}
.report-table {width:100%;border-collapse:collapse;font-size:10px;}
.report-table th {text-align:left;padding:4px 6px;background:#F3F4F6;color:#6B7280;text-transform:uppercase;}
.report-table td {padding:4px 6px;border-bottom:1px solid #E5E7EB;color:#111827;}
.report-disclaimer {font-size:9.5px;color:#6B7280;line-height:1.4;}
.report-footer {font-size:9px;text-transform:uppercase;color:#9CA3AF;letter-spacing:0.05em;}
.report-page-label {font-size:10px;text-transform:uppercase;color:#6B7280;letter-spacing:0.06em;margin:4px 0;}
</style>
"""

    layout_cols = st.columns([1, 3, 1])
    with layout_cols[1]:
        st.markdown(report_css, unsafe_allow_html=True)

        export_pdf = st.button("Export PDF", key="export_pdf")
        if export_pdf:
            scenario_df = st.session_state.get("analysis_scenario_df")
            expiry_value = st.session_state.get("chain_expiry")
            expiry_text = (
                expiry_value.isoformat()
                if isinstance(expiry_value, date)
                else str(expiry_value or "")
            )
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
                "ticker": st.session_state.get("underlying_ticker", ""),
                "resolved_ticker": st.session_state.get("resolved_underlying", ""),
                "strategy_name": st.session_state.get("analysis_strategy_name", ""),
                "expiry": expiry_text,
                "pricing_mode": st.session_state.get("pricing_mode", ""),
                "spot": st.session_state.get("spot_value", 0.0),
                "stock_position": st.session_state.get("stock_position", 0.0),
                "avg_cost": st.session_state.get("avg_cost", 0.0),
                "roi_policy": st.session_state.get("roi_policy", ""),
                "legs": legs_payload,
            }
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            summary_payload = st.session_state.get("analysis_summary_payload", {})
            warnings = model.get("warnings", {})
            dividend_warning = (
                warnings.get("dividend") if isinstance(warnings, dict) else None
            )
            if dividend_warning:
                summary_payload = dict(summary_payload)
                summary_payload["warning"] = dividend_warning
            notes = model.get("disclaimers", ["--"])
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                build_report_pdf(
                    tmp.name,
                    title="Options Strategy Report",
                    as_of=timestamp,
                    inputs=inputs_payload,
                    summary=summary_payload,
                    scenario_df=scenario_df,
                    notes=notes,
                    report_model=model,
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

        st.markdown("<div class='report-page-label'>Page 1</div>", unsafe_allow_html=True)

        header = model.get("header", {})
        with st.container(border=True):
            row1 = st.columns([1.1, 1.4, 1.0, 1.5, 1.0])
            _header_cell(row1[0], "Report Time", header.get("report_time", "--"))
            _header_cell(row1[1], "Underlying", header.get("ticker", "--"))
            _header_cell(row1[2], "Last Price", header.get("last_price", "--"))
            _header_cell(
                row1[3],
                "Strategy",
                header.get("strategy_name", "--"),
                value_class="report-title",
            )
            _header_cell(row1[4], "Expiry", header.get("expiry", "--"))

            row2 = st.columns([1.0, 1.1, 1.5, 1.2, 1.2, 1.2])
            _header_cell(row2[0], "Shares", header.get("shares", "--"))
            _header_cell(row2[1], "Avg Cost", header.get("avg_cost", "--"))
            _header_cell(row2[2], "Name", header.get("name", "--"))
            _header_cell(row2[3], "Sector", header.get("sector", "--"))
            _header_cell(
                row2[4],
                "52W High/Low",
                f"{_as_text(header.get('high_52w'))} / {_as_text(header.get('low_52w'))}",
            )
            _header_cell(row2[5], "Dividend Yield", header.get("dividend_yield", "--"))

            row3 = st.columns([1.2, 2.0, 2.8])
            _header_cell(row3[0], "Earnings Date", header.get("earnings_date", "--"))
            _header_cell(row3[1], "Policies", header.get("policies", "--"))
            _header_cell(row3[2], "Title", header.get("title", "--"))

        body_cols = st.columns([1.1, 1.6])
        structure = model.get("structure", {})
        with body_cols[0]:
            with st.container(border=True):
                st.markdown(
                    "<div class='report-section-title'>Structure</div>",
                    unsafe_allow_html=True,
                )
                _render_table(
                    structure.get("legs", []),
                    ["leg", "side", "expiry", "strike", "premium"],
                )
                st.markdown(
                    f"<div class='report-label'>Net Premium (total)</div>"
                    f"<div class='report-value'>{_as_text(structure.get('net_premium_total'))}</div>",
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f"<div class='report-label'>Net Premium (per share)</div>"
                    f"<div class='report-value'>{_as_text(structure.get('net_premium_per_share'))}</div>",
                    unsafe_allow_html=True,
                )

        with body_cols[1]:
            with st.container(border=True):
                st.markdown(
                    "<div class='report-section-title'>Payoff</div>",
                    unsafe_allow_html=True,
                )
                fig = go.Figure()
                price_grid = payoff.get("price_grid", [])
                combined_pnl = payoff.get("combined_pnl", [])
                options_pnl = payoff.get("options_pnl", [])
                stock_pnl = payoff.get("stock_pnl", [])
                has_stock_position = bool(model.get("has_stock_position"))
                if price_grid and combined_pnl:
                    if options_pnl and len(options_pnl) == len(price_grid):
                        fig.add_trace(
                            go.Scatter(
                                x=price_grid,
                                y=options_pnl,
                                mode="lines",
                                name="Options",
                                line=dict(color="#2563EB", width=2),
                            )
                        )
                    if has_stock_position and stock_pnl and len(stock_pnl) == len(price_grid):
                        fig.add_trace(
                            go.Scatter(
                                x=price_grid,
                                y=stock_pnl,
                                mode="lines",
                                name="Stock",
                                line=dict(color="#10B981", width=2),
                            )
                        )
                    fig.add_trace(
                        go.Scatter(
                            x=price_grid,
                            y=combined_pnl,
                            mode="lines",
                            name="Combined",
                            line=dict(color="#4B5563", width=2),
                        )
                    )
                    markers = []
                    key_levels = model.get("key_levels_rows", [])
                    for row in key_levels:
                        if not isinstance(row, dict):
                            continue
                        price = _to_float(row.get("price") or row.get("Price"))
                        if price is None:
                            continue
                        label = row.get("label") or row.get("Scenario") or row.get("scenario")
                        label_text = str(label).strip() if label is not None else ""
                        label_lower = label_text.lower()
                        if "current market price" in label_lower or label_lower == "spot":
                            markers.append(
                                {
                                    "price": price,
                                    "label": "Spot",
                                    "priority": 0,
                                }
                            )
                        elif "breakeven" in label_lower:
                            label_display = label_text.replace("Breakeven", "BE").replace(" ", "")
                            markers.append(
                                {
                                    "price": price,
                                    "label": label_display,
                                    "priority": 1,
                                }
                            )
                        elif "strike" in label_lower:
                            label_display = label_text.replace("Strike", "K").strip()
                            markers.append(
                                {
                                    "price": price,
                                    "label": label_display,
                                    "priority": 2,
                                }
                            )
                    markers = sorted(markers, key=lambda item: (item["priority"], item["price"]))
                    selected = []
                    for marker in markers:
                        if any(abs(marker["price"] - keep["price"]) < 0.01 for keep in selected):
                            continue
                        selected.append(marker)
                    label_positions = [
                        "top left",
                        "top right",
                        "bottom left",
                        "bottom right",
                    ]
                    for idx, marker in enumerate(selected):
                        fig.add_vline(
                            x=marker["price"],
                            line_dash="dot" if marker["priority"] == 2 else "dash",
                            line_color="#9CA3AF",
                            annotation_text=marker["label"],
                            annotation_position=label_positions[idx % len(label_positions)],
                        )
                    fig.update_layout(
                        xaxis_title="Underlying Price at Expiry",
                        yaxis_title="PnL",
                        height=420,
                        plot_bgcolor="#FFFFFF",
                        paper_bgcolor="#FFFFFF",
                        margin=dict(l=30, r=20, t=30, b=30),
                    )
                    fig.update_xaxes(showgrid=True, gridcolor="#E5E7EB")
                    fig.update_yaxes(showgrid=True, gridcolor="#E5E7EB")
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.info("No payoff data available.")

        metrics = model.get("metrics", {})
        with st.container(border=True):
            st.markdown(
                "<div class='report-section-title'>Payoff &amp; Metrics</div>",
                unsafe_allow_html=True,
            )
            _render_table(metrics.get("rows", []), ["metric", "options", "combined"])

        disclaimers = model.get("disclaimers", ["--"])
        with st.container(border=True):
            warnings = model.get("warnings", {})
            dividend_warning = (
                warnings.get("dividend") if isinstance(warnings, dict) else None
            )
            if dividend_warning:
                st.markdown(
                    f"<div class='report-disclaimer'>{_as_text(dividend_warning)}</div>",
                    unsafe_allow_html=True,
                )
            disclaimer_text = " ".join([_as_text(item) for item in disclaimers])
            st.markdown(
                f"<div class='report-disclaimer'>{_as_text(disclaimer_text)}</div>",
                unsafe_allow_html=True,
            )

        st.divider()
        st.markdown("<div class='report-page-label'>Page 2</div>", unsafe_allow_html=True)

        scenario_blocks = list(model.get("scenario_analysis_cards") or [])
        analysis_pack = st.session_state.get("analysis_pack")
        with st.expander("DEBUG: analysis_pack.narrative_scenarios", expanded=False):
            if isinstance(analysis_pack, dict):
                st.json(analysis_pack.get("narrative_scenarios"))
            else:
                st.json(None)
        with st.expander("Debug: Scenario Analysis Cards", expanded=False):
            st.json(scenario_blocks)
            if not scenario_blocks:
                st.warning(
                    "Scenario narratives unavailable — check analysis_pack.narrative_scenarios"
                )
        while len(scenario_blocks) < 3:
            scenario_blocks.append({"title": "--", "condition": "", "body": "--"})
        scenario_cols = st.columns(3)
        for idx, col in enumerate(scenario_cols):
            block = scenario_blocks[idx]
            title = _as_text(block.get("title") or block.get("level"))
            condition = block.get("condition") if isinstance(block, dict) else ""
            if not isinstance(condition, str):
                condition = str(condition) if condition is not None else ""
            condition = condition.strip()
            body = block.get("body") if isinstance(block, dict) else ""
            if not body:
                body = block.get("text") if isinstance(block, dict) else ""
            if not isinstance(body, str):
                body = str(body) if body is not None else ""
            with col:
                with st.container(border=True):
                    st.markdown(
                        f"<div class='report-section-title'>{title}</div>",
                        unsafe_allow_html=True,
                    )
                    if condition:
                        st.markdown(
                            f"<div class='report-label'>{condition}</div>",
                            unsafe_allow_html=True,
                        )
                    if body:
                        st.markdown(
                            f"<div class='report-value'>{body}</div>",
                            unsafe_allow_html=True,
                        )

        key_levels = (
            model.get("key_levels_display_rows_by_price")
            or model.get("key_levels_display_rows")
            or model.get("key_levels_rows")
            or model.get("scenario_table", {}).get("top10", [])
        )
        key_rows = []
        for row in key_levels:
            def pick(keys):
                for key in keys:
                    if key in row:
                        return _as_text(row.get(key))
                return "--"
            key_rows.append(
                {
                    "Scenario": pick(["label", "Scenario", "scenario"]),
                    "Price": pick(["Price", "price"]),
                    "Move %": pick(["Move %", "move_pct", "move_percent"]),
                    "Stock PnL": pick(["Stock PnL", "stock_pnl"]),
                    "Option PnL": pick(["Option PnL", "option_pnl"]),
                    "Option ROI": pick(["Option ROI", "option_roi"]),
                    "Net PnL": pick(["Net PnL", "net_pnl", "combined_pnl"]),
                    "Net ROI": pick(["Net ROI", "net_roi"]),
                }
            )
        with st.container(border=True):
            st.markdown(
                "<div class='report-section-title'>Key Levels</div>",
                unsafe_allow_html=True,
            )
            has_stock_position = bool(model.get("has_stock_position", False))
            if has_stock_position:
                display_cols = [
                    "Scenario",
                    "Price",
                    "Move %",
                    "Stock PnL",
                    "Option PnL",
                    "Option ROI",
                    "Net PnL",
                    "Net ROI",
                ]
            else:
                display_cols = [
                    "Scenario",
                    "Price",
                    "Move %",
                    "Option PnL",
                    "Option ROI",
                    "Net PnL",
                    "Net ROI",
                ]
            key_df = pd.DataFrame(
                key_rows,
                columns=display_cols,
            )
            def _highlight_spot(row):
                label = str(row.get("Scenario", "")).strip().lower()
                if label in {"spot", "current market price"}:
                    return ["background-color: #FEF9C3"] * len(row)
                return ["" for _ in row]
            styled = key_df.style.apply(_highlight_spot, axis=1)
            html = styled.to_html()
            st.markdown(html, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown(
                "<div class='report-section-title'>Commentary</div>",
                unsafe_allow_html=True,
            )
            groups = {
                "Spot": [],
                "Strikes": [],
                "Breakevens": [],
                "Low": [],
                "High": [],
            }
            for block in commentary_blocks:
                label = _as_text(block.get("level"))
                text = _as_text(block.get("text"))
                upper_label = label.upper()
                if upper_label.startswith("SPOT"):
                    groups["Spot"].append(text)
                elif "STRIKE" in upper_label:
                    groups["Strikes"].append(text)
                elif upper_label.startswith("BE") or "BREAK" in upper_label:
                    groups["Breakevens"].append(text)
                elif upper_label.startswith("LOW"):
                    groups["Low"].append(text)
                elif upper_label.startswith("HIGH"):
                    groups["High"].append(text)

            for title in ["Spot", "Strikes", "Breakevens", "Low", "High"]:
                block_text = " ".join(groups[title]) if groups[title] else "--"
                st.markdown(
                    f"<div class='report-label'>{title}</div>"
                    f"<div class='report-value'>{_as_text(block_text)}</div>",
                    unsafe_allow_html=True,
                )

        footer_cols = st.columns([1, 1])
        footer_cols[0].markdown(
            "<div class='report-footer'>UBS Financial Services Inc.</div>",
            unsafe_allow_html=True,
        )
        footer_cols[1].markdown(
            "<div class='report-footer' style='text-align:right;'>Page 2 of 2</div>",
            unsafe_allow_html=True,
        )


tabs = st.tabs(["Dashboard", "Bloomberg Data", "Client Report"])
with tabs[0]:
    render_dashboard()
with tabs[1]:
    render_bloomberg_data()
with tabs[2]:
    render_client_report()
