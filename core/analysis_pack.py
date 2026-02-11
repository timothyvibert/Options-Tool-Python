from __future__ import annotations

import logging
from datetime import date, datetime
from typing import Dict, Iterable, List, Mapping, Optional

import math

logger = logging.getLogger(__name__)

import pandas as pd

from core.eligibility import determine_strategy_code, get_account_eligibility
from core.margin import classify_strategy, compute_margin_proxy, compute_margin_full
from core.models import StrategyInput
from core.narrative import build_narrative_scenarios
from core.payoff import _compute_pnl_for_price, _detect_unlimited, compute_payoff
from core.probability import strategy_pop, compute_all_probabilities
from core.roi import capital_basis, combined_capital_basis, compute_net_premium
from core.scenarios import build_scenario_points, compute_scenario_table


def _parse_date(value: object) -> Optional[date]:
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, pd.Timestamp):
        return value.date()
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return None
        try:
            return date.fromisoformat(text[:10])
        except ValueError:
            return None
    return None


def _extract_dividend_date(profile: object) -> Optional[date]:
    if profile is None:
        return None
    if isinstance(profile, pd.Series):
        profile = profile.to_dict()
    if not isinstance(profile, Mapping):
        return None
    normalized = {str(key).upper(): value for key, value in profile.items()}
    for field in [
        "EX_DIV_DATE",
        "DVD_EX_DT",
        "EQY_DVD_EX_DT",
        "DVD_EX_DATE",
        "EQY_DVD_EX_DATE",
        "EX_DIVIDEND_DATE",
    ]:
        candidate = normalized.get(field)
        parsed = _parse_date(candidate)
        if parsed is not None:
            return parsed
    return None


def _safe_list(value: object) -> List[dict]:
    if isinstance(value, list):
        return [item if isinstance(item, dict) else {} for item in value]
    return []


def _format_net_premium(net_premium: float) -> str:
    if net_premium < 0:
        return f"Credit ${abs(net_premium):,.2f}"
    if net_premium > 0:
        return f"Debit ${net_premium:,.2f}"
    return "$0.00"


def _format_number(value: Optional[float]) -> str:
    if value is None or not math.isfinite(value):
        return "--"
    return f"{value:.2f}"


def _format_dollar(value: Optional[float]) -> str:
    """Format numeric value with $ sign and commas."""
    if value is None or not math.isfinite(value):
        return "--"
    if value < 0:
        return f"-${abs(value):,.2f}"
    return f"${value:,.2f}"


def _unique_sorted(values: Iterable[float]) -> List[float]:
    deduped: List[float] = []
    for value in sorted(values):
        if not deduped or abs(value - deduped[-1]) > 1e-6:
            deduped.append(value)
    return deduped


def _closest_row(df: pd.DataFrame, price: float) -> Optional[pd.Series]:
    if df.empty or "price" not in df.columns:
        return None
    prices = pd.to_numeric(df["price"], errors="coerce")
    prices = prices.dropna()
    if prices.empty:
        return None
    idx = (prices - float(price)).abs().idxmin()
    return df.loc[idx]


def _key_row(label: str, row: Optional[pd.Series], spot: float) -> Dict[str, object]:
    if row is None:
        return {
            "Scenario": label,
            "Price": None,
            "Move %": None,
            "Stock PnL": None,
            "Option PnL": None,
            "Option ROI": None,
            "Net PnL": None,
            "Net ROI": None,
        }
    price = row.get("price")
    move_pct = None
    if isinstance(price, (int, float)) and spot:
        move_pct = (price / spot - 1.0) * 100.0
    return {
        "Scenario": label,
        "Price": price,
        "Move %": move_pct,
        "Stock PnL": row.get("stock_pnl"),
        "Option PnL": row.get("option_pnl"),
        "Option ROI": row.get("option_roi"),
        "Net PnL": row.get("combined_pnl"),
        "Net ROI": row.get("net_roi"),
    }


def _extract_commentary(row: Optional[pd.Series]) -> Optional[str]:
    if row is None:
        return None
    text = row.get("commentary")
    if text is None or (isinstance(text, float) and math.isnan(text)):
        return None
    text_value = str(text).strip()
    return text_value if text_value else None


def _label_from_row(row: Optional[pd.Series], fallback: str) -> str:
    if row is None:
        return fallback
    label = row.get("scenario")
    if label is None or (isinstance(label, float) and math.isnan(label)):
        return fallback
    text = str(label).strip()
    return text if text else fallback


def _row_by_price(df: pd.DataFrame, price: float) -> Optional[pd.Series]:
    if df.empty or "price" not in df.columns:
        return None
    prices = pd.to_numeric(df["price"], errors="coerce")
    mask = (prices - float(price)).abs() <= 1e-6
    if not mask.any():
        return None
    return df.loc[mask].iloc[0]


def _move_label(prefix: str, spot: float, price: float) -> str:
    if spot == 0:
        return f"{prefix} (--%)"
    pct = abs((price / spot - 1.0) * 100.0)
    return f"{prefix} ({int(round(pct))}%)"


def _fallback_label(price: float) -> str:
    return f"Scenario @ {price:.2f}"


def _risk_reward(max_prof: float, max_loss_val: float) -> str:
    """Format risk/reward ratio from max profit and max loss."""
    if max_loss_val == 0:
        return "\u221e" if max_prof > 0 else "N/A"
    return f"{abs(max_prof / max_loss_val):.2f}x"


def _auto_capital_basis(strategy_code: str, legs, shares: int,
                        avg_cost: float, margin_proxy: float) -> dict:
    """Auto-select the most appropriate capital basis."""
    if strategy_code in ("CSP", "SP", "CSPW", "CSPT", "cash_secured_put"):
        short_puts = [l for l in legs if l.kind.lower() == "put" and l.position < 0]
        amount = sum(l.strike * abs(l.position) * l.multiplier for l in short_puts)
        return {"mode": "cash_secured", "amount": amount, "label": "Cash-Secured (Treasury Collateral)"}

    if strategy_code in ("CC", "COL", "CW"):
        amount = avg_cost * shares if shares and avg_cost else 0
        return {"mode": "stock_cost", "amount": amount, "label": "Stock Cost Basis"}

    if strategy_code in ("BCS", "BPS", "BFS", "BEFS"):
        amount = abs(margin_proxy) if margin_proxy else 0
        return {"mode": "max_loss", "amount": amount, "label": "Net Debit / Max Loss"}

    amount = margin_proxy or 0
    return {"mode": "margin", "amount": amount, "label": "Margin Requirement"}


def _dedup_key_levels(levels: List[dict]) -> List[dict]:
    """Deduplicate key levels that share the same rounded price AND source.

    Only merges entries from the same source category (e.g., two upside
    targets at the same price).  Different categories (spot, strike,
    breakeven) at the same price are preserved so that every semantic
    level remains visible.  Upside/downside targets that land on a
    strike or breakeven price are removed in favour of the more
    informative label.
    """
    # Sources that should always be kept even when sharing a price with
    # another source.
    ALWAYS_KEEP = {"spot", "strike", "breakeven", "sentinel", "downside", "upside"}

    seen_ids: set = set()
    result: List[dict] = []
    # Map rounded-price → set of sources already included at that price
    price_sources: dict = {}
    # Map rounded-price → list of (source, level) for retroactive removal
    price_entries: dict = {}

    for level in levels:
        lid = level.get("id")
        if lid in seen_ids:
            continue  # duplicate id already present

        price = level.get("price")
        source = level.get("source", "sentinel")

        if price is None:
            # Sentinel rows (infinity, zero) — always keep, keyed by id
            seen_ids.add(lid)
            result.append(level)
            continue

        rp = round(float(price), 2)
        existing = price_sources.get(rp, set())

        if source in ALWAYS_KEEP:
            # Same source at same price — skip (e.g. two downside entries)
            if source in existing:
                continue
            # Retroactively remove non-ALWAYS_KEEP entries at this price
            if rp in price_entries:
                for entry_source, entry_level in list(price_entries[rp]):
                    if entry_source not in ALWAYS_KEEP:
                        result.remove(entry_level)
                        seen_ids.discard(entry_level.get("id"))
                price_entries[rp] = [
                    (s, l) for s, l in price_entries[rp]
                    if s in ALWAYS_KEEP
                ]
            # Always include spot/strike/breakeven/sentinel/downside/upside
            price_sources.setdefault(rp, set()).add(source)
            price_entries.setdefault(rp, []).append((source, level))
            seen_ids.add(lid)
            result.append(level)
        elif source in existing:
            # Duplicate same-source at same price — skip
            continue
        elif existing & ALWAYS_KEEP:
            # This target/upside/downside overlaps with a more important level — skip
            continue
        else:
            price_sources.setdefault(rp, set()).add(source)
            price_entries.setdefault(rp, []).append((source, level))
            seen_ids.add(lid)
            result.append(level)

    # Sort by price ascending, sentinels (None) at end
    result.sort(
        key=lambda lv: (
            lv.get("price") if lv.get("price") is not None else float("inf"),
        )
    )
    return result


def build_analysis_pack(
    strategy_input: StrategyInput,
    strategy_meta: dict,
    pricing_mode: str,
    roi_policy: str,
    vol_mode: str,
    atm_iv: float,
    underlying_profile: dict | None,
    bbg_leg_snapshots: dict | None,
    scenario_mode: str,
    downside_tgt: float,
    upside_tgt: float,
    risk_free_rate: float = 0.0,
) -> dict:
    meta = strategy_meta if isinstance(strategy_meta, Mapping) else {}
    as_of = meta.get("as_of") or "--"
    expiry_value = meta.get("expiry")
    expiry_date = _parse_date(expiry_value)
    as_of_date = _parse_date(as_of)
    profile_value = underlying_profile
    if isinstance(profile_value, pd.Series):
        profile_value = profile_value.to_dict()
    if not isinstance(profile_value, Mapping):
        profile_value = {}
    normalized_profile = {str(key).upper(): value for key, value in profile_value.items()}
    ex_div_date = _extract_dividend_date(profile_value)
    def _clean_value(value: object) -> object:
        try:
            if pd.isna(value):
                return None
        except Exception:
            pass
        return value

    high_52week = normalized_profile.get("HIGH_52WEEK")
    if high_52week is None:
        high_52week = (
            normalized_profile.get("WEEK_52_HIGH")
            or normalized_profile.get("PX_52W_HIGH")
            or normalized_profile.get("52WK_HIGH")
        )
    low_52week = normalized_profile.get("LOW_52WEEK")
    if low_52week is None:
        low_52week = (
            normalized_profile.get("WEEK_52_LOW")
            or normalized_profile.get("PX_52W_LOW")
            or normalized_profile.get("52WK_LOW")
        )
    high_dt_52week = normalized_profile.get("HIGH_DT_52WEEK")
    low_dt_52week = normalized_profile.get("LOW_DT_52WEEK")
    chg_pct_1yr = normalized_profile.get("CHG_PCT_1YR")
    eqy_trr_pct_1yr = normalized_profile.get("EQY_TRR_PCT_1YR")
    chg_pct_5d = normalized_profile.get("CHG_PCT_5D")
    chg_pct_3m = normalized_profile.get("CHG_PCT_3M")
    chg_pct_ytd = normalized_profile.get("CHG_PCT_YTD")
    vol_percentile = normalized_profile.get("VOL_PERCENTILE")
    impvol_3m_atm = normalized_profile.get("3MTH_IMPVOL_100.0%MNY_DF")
    chg_pct_1d = normalized_profile.get("CHG_PCT_1D")
    chg_net_1d = normalized_profile.get("CHG_NET_1D")
    impvol_6m_atm = (
        normalized_profile.get("6MTH_IMPVOL_100.0%MNY_DF")
        or normalized_profile.get("IMPVOL_6M_ATM")
    )
    earnings_related_implied_move = normalized_profile.get(
        "EARNINGS_RELATED_IMPLIED_MOVE"
    )
    expected_report_raw = normalized_profile.get("EXPECTED_REPORT_DT")
    expected_report_date = _parse_date(expected_report_raw)
    if expected_report_date is None and isinstance(expected_report_raw, str):
        text = expected_report_raw.strip()
        if text:
            try:
                expected_report_date = datetime.strptime(text[:10], "%m/%d/%Y").date()
            except ValueError:
                expected_report_date = None
    if expected_report_date is None and expected_report_raw:
        expected_report_value: object = expected_report_raw
    else:
        expected_report_value = expected_report_date
    earnings_date_for_risk = (
        _parse_date(expected_report_value) or expected_report_date
    )
    days_to_earnings = None
    if earnings_date_for_risk is not None and as_of_date is not None:
        days_to_earnings = (earnings_date_for_risk - as_of_date).days
    earnings_before_expiry = None
    if earnings_date_for_risk is not None and expiry_date is not None:
        earnings_before_expiry = earnings_date_for_risk < expiry_date
    projected_dividend = pd.to_numeric(
        normalized_profile.get("PROJECTED_DIVIDEND"), errors="coerce"
    )
    if pd.isna(projected_dividend):
        projected_dividend = None
    else:
        projected_dividend = float(projected_dividend)
    dividend_status = normalized_profile.get("DIVIDEND_STATUS")
    if dividend_status is not None:
        try:
            if pd.isna(dividend_status):
                dividend_status = None
        except TypeError:
            pass
    if dividend_status is not None:
        dividend_status = str(dividend_status).strip() or None
    days_to_dividend = None
    if ex_div_date is not None and as_of_date is not None:
        days_to_dividend = (ex_div_date - as_of_date).days
    before_expiry = None
    if ex_div_date is not None and expiry_date is not None:
        before_expiry = ex_div_date < expiry_date

    t = 1.0
    if expiry_date is not None and as_of_date is not None:
        days = (expiry_date - as_of_date).days
        t = max(days / 365.0, 1e-6)

    payoff_result = compute_payoff(strategy_input)
    price_grid = payoff_result.get("price_grid", [])
    combined_pnl = payoff_result.get("pnl", [])

    option_only = StrategyInput(
        spot=strategy_input.spot,
        stock_position=0.0,
        avg_cost=0.0,
        legs=strategy_input.legs,
    )
    options_pnl = [
        _compute_pnl_for_price(option_only, price) for price in price_grid
    ]
    stock_pnl = [
        combined - option for combined, option in zip(combined_pnl, options_pnl)
    ]

    # Detect unlimited upside/downside for both combined and options-only payoff
    combined_unlimited = _detect_unlimited(price_grid, combined_pnl)
    options_unlimited = _detect_unlimited(price_grid, options_pnl)

    strikes = _unique_sorted(
        [float(leg.strike) for leg in strategy_input.legs]
    )
    breakevens = payoff_result.get("breakevens", [])

    scenario_points = build_scenario_points(
        strategy_input,
        payoff_result,
        mode=scenario_mode,
        downside_tgt=downside_tgt,
        upside_tgt=upside_tgt,
    )
    strategy_row = meta.get("strategy_row")
    if isinstance(strategy_row, dict):
        strategy_row = pd.Series(strategy_row)
    scenario_df = compute_scenario_table(
        strategy_input,
        scenario_points,
        payoff_result=payoff_result,
        roi_policy=roi_policy,
        strategy_row=strategy_row if isinstance(strategy_row, pd.Series) else None,
        downside_tgt=downside_tgt if scenario_mode.upper() != "INFINITY" else None,
        upside_tgt=upside_tgt if scenario_mode.upper() != "INFINITY" else None,
    )

    # Compute net premium totals early (needed for capital basis override)
    net_premium = compute_net_premium(strategy_input)
    net_premium_total = sum(
        leg.position * leg.premium * leg.multiplier
        for leg in strategy_input.legs
    )

    option_basis = capital_basis(strategy_input, payoff_result, roi_policy)
    margin_proxy = compute_margin_proxy(strategy_input, payoff_result)

    # For credit strategies with unlimited loss, use margin as capital basis
    # (premium received is income, not capital at risk)
    is_net_credit = net_premium_total < 0
    has_unlimited = (
        options_unlimited["unlimited_downside"]
        or options_unlimited.get("unlimited_loss_upside", False)
    )
    if is_net_credit and has_unlimited and margin_proxy > 0:
        option_basis = margin_proxy

    total_basis = combined_capital_basis(strategy_input, option_basis)

    # Compute strategy_code early so it's available for summary metrics
    strategy_code = determine_strategy_code(strategy_input, roi_policy)

    # Auto capital basis — must run after strategy_code and margin_proxy
    # are available so the result feeds into summary metrics and ROI.
    auto_basis = _auto_capital_basis(
        strategy_code, strategy_input.legs,
        int(strategy_input.stock_position), strategy_input.avg_cost,
        margin_proxy,
    )
    if auto_basis["amount"] > 0:
        option_basis = auto_basis["amount"]
        total_basis = combined_capital_basis(strategy_input, option_basis)

    dte_days = 0.0
    if expiry_date is not None and as_of_date is not None:
        dte_days = float(max((expiry_date - as_of_date).days, 0))

    margin_full = compute_margin_full(
        strategy_input,
        payoff_result=payoff_result,
        dte=dte_days,
    )

    options_notional = sum(
        abs(leg.position) * leg.strike * leg.multiplier
        for leg in strategy_input.legs
    )
    combined_notional = options_notional + abs(
        strategy_input.stock_position * strategy_input.spot
    )

    option_roi_values = []
    net_roi_values = []
    if not scenario_df.empty:
        option_roi_values = [
            float(value)
            for value in pd.to_numeric(
                scenario_df["option_roi"], errors="coerce"
            )
            .dropna()
            .tolist()
        ]
        net_roi_values = [
            float(value)
            for value in pd.to_numeric(
                scenario_df["net_roi"], errors="coerce"
            )
            .dropna()
            .tolist()
        ]

    # net_premium and net_premium_total already computed above (before capital basis)
    net_premium_text = _format_net_premium(net_premium_total)

    # Net Prem/Share: total premium / shares (or / total contracts if no stock)
    shares = abs(strategy_input.stock_position) if strategy_input.stock_position else 0
    if shares > 0:
        net_prem_per_share = net_premium_total / shares
    else:
        total_contracts = sum(abs(leg.position) for leg in strategy_input.legs) or 1
        net_prem_per_share = net_premium_total / total_contracts

    net_premium_pct = (
        net_prem_per_share / strategy_input.spot * 100.0
        if strategy_input.spot
        else 0.0
    )

    per_leg_iv = [None for _ in strategy_input.legs]
    if isinstance(bbg_leg_snapshots, Mapping):
        iv_values = bbg_leg_snapshots.get("per_leg_iv")
        if isinstance(iv_values, list) and len(iv_values) == len(per_leg_iv):
            per_leg_iv = iv_values

    try:
        pop = strategy_pop(
            strategy_input,
            _compute_pnl_for_price,
            S0=strategy_input.spot,
            r=risk_free_rate,
            q=0.0,
            sigma_mode=vol_mode,
            atm_iv=atm_iv,
            per_leg_iv=per_leg_iv,
            t=t,
        )
    except Exception:
        logger.exception("Probability computation failed")
        pop = 0.0

    pop_text = f"{pop * 100:.1f}%"

    # Build leg dicts with IV for probability metrics
    legs_with_iv = []
    for idx, leg in enumerate(strategy_input.legs):
        leg_iv = per_leg_iv[idx] if idx < len(per_leg_iv) else None
        legs_with_iv.append({
            "qty": leg.position,
            "type": leg.kind.upper(),
            "strike": leg.strike,
            "premium": leg.premium,
            "iv": leg_iv or 0.0,
        })

    # Compute all probability metrics
    # Prefer VEGA_WEIGHTED when per-leg IVs are available; fall back to ATM
    try:
        from core.probability import effective_sigma, _fallback_atm
        _valid_ivs = [iv for iv in per_leg_iv if iv is not None and iv > 0]
        _eff_mode = "VEGA_WEIGHTED" if _valid_ivs else vol_mode
        eff_sigma = effective_sigma(
            strategy_input, per_leg_iv, _eff_mode, risk_free_rate, 0.0, t,
            atm_iv=atm_iv,
        )
    except Exception:
        # Fall back to simple average of available per-leg IVs, not a hardcoded 0.2
        from core.probability import _fallback_atm
        eff_sigma = _fallback_atm(per_leg_iv) or 0.2

    max_profit_val = max(options_pnl) if options_pnl else None
    # Target probs use options-only payoff so thresholds are meaningful
    # even when a stock overlay inflates combined PnL.  PoP uses the
    # combined payoff (already computed above) for the true position.
    try:
        prob_results = compute_all_probabilities(
            input_obj=option_only,
            payoff_fn=_compute_pnl_for_price,
            legs=legs_with_iv,
            spot=strategy_input.spot,
            r=risk_free_rate,
            q=0.0,
            sigma=eff_sigma,
            t=t,
            max_profit=max_profit_val,
        )
    except Exception:
        prob_results = {}
    # Override PoP with the combined-payoff value (the true position)
    prob_results["pop"] = pop
    prob_results["pop_pct"] = f"{pop * 100:.1f}%"

    # Annotate IV source so the UI can distinguish real vs fallback values
    if _valid_ivs:
        prob_results["iv_source"] = "vega_weighted"
    else:
        prob_results["iv_source"] = "atm_fallback"
        if "iv_used_pct" in prob_results:
            prob_results["iv_used_pct"] = f"{eff_sigma * 100:.1f}%"

    # Determine Max Profit / Max Loss with unlimited detection
    options_max_profit = (
        "Unlimited" if options_unlimited["unlimited_upside"]
        else _format_dollar(max(options_pnl) if options_pnl else None)
    )
    combined_max_profit = (
        "Unlimited" if combined_unlimited["unlimited_upside"]
        else _format_dollar(max(combined_pnl) if combined_pnl else None)
    )
    options_max_loss = (
        "Unlimited" if (options_unlimited["unlimited_downside"]
                        or options_unlimited.get("unlimited_loss_upside", False))
        else _format_dollar(min(options_pnl) if options_pnl else None)
    )
    combined_max_loss = (
        "Unlimited" if (combined_unlimited["unlimited_downside"]
                        or combined_unlimited.get("unlimited_loss_upside", False))
        else _format_dollar(min(combined_pnl) if combined_pnl else None)
    )

    # Risk/Reward Ratio (computed before summary_rows so it can be inline)
    options_max_profit_num = max(options_pnl) if options_pnl else 0
    options_max_loss_num = min(options_pnl) if options_pnl else 0
    combined_max_profit_num = max(combined_pnl) if combined_pnl else 0
    combined_max_loss_num = min(combined_pnl) if combined_pnl else 0

    rr_options = _risk_reward(options_max_profit_num, options_max_loss_num)
    rr_combined = _risk_reward(combined_max_profit_num, combined_max_loss_num)

    # Min ROI: show "N/A" when max loss is unlimited (huge negative is meaningless)
    if options_max_loss == "Unlimited":
        min_roi_options = "N/A"
    else:
        min_roi_options = _format_number(min(option_roi_values) if option_roi_values else None)

    if combined_max_loss == "Unlimited":
        min_roi_combined = "N/A"
    else:
        min_roi_combined = _format_number(min(net_roi_values) if net_roi_values else None)

    summary_rows = [
        {
            "metric": "Max Profit",
            "options": options_max_profit,
            "combined": combined_max_profit,
        },
        {
            "metric": "Max Loss",
            "options": options_max_loss,
            "combined": combined_max_loss,
        },
        {
            "metric": "Risk/Reward",
            "options": rr_options,
            "combined": rr_combined,
        },
        {
            "metric": "Capital Basis",
            "options": _format_dollar(option_basis),
            "combined": _format_dollar(total_basis),
        },
        {
            "metric": "Max ROI",
            "options": _format_number(max(option_roi_values) if option_roi_values else None),
            "combined": _format_number(max(net_roi_values) if net_roi_values else None),
        },
        {
            "metric": "Min ROI",
            "options": min_roi_options,
            "combined": min_roi_combined,
        },
        {
            "metric": "Cost/Credit",
            "options": net_premium_text,
            "combined": net_premium_text,
        },
        {
            "metric": "Notional Exposure",
            "options": _format_dollar(options_notional),
            "combined": _format_dollar(combined_notional),
        },
        {
            "metric": "Net Prem/Share",
            "options": _format_dollar(net_prem_per_share),
            "combined": _format_dollar(net_prem_per_share),
        },
        {
            "metric": "Net Prem % Spot",
            "options": f"{net_premium_pct:.2f}%",
            "combined": f"{net_premium_pct:.2f}%",
        },
        {
            "metric": "PoP",
            "options": pop_text,
            "combined": pop_text,
        },
    ]

    # Closest Breakeven and BE Distance %
    spot = float(strategy_input.spot)
    if breakevens:
        closest_be = min(breakevens, key=lambda be: abs(be - spot))
        closest_be_str = f"${closest_be:,.2f}"
        be_distance_pct = ((closest_be - spot) / spot) * 100 if spot else 0
        be_distance_str = f"{be_distance_pct:+.2f}%"
    else:
        closest_be_str = "N/A"
        be_distance_str = "N/A"

    summary_rows.append({"metric": "Closest Breakeven", "options": closest_be_str, "combined": closest_be_str})
    summary_rows.append({"metric": "BE Distance %", "options": be_distance_str, "combined": be_distance_str})

    # Treasury Obligation (cash-secured strategies only)
    is_cash_secured = strategy_code in ("CSP", "SP", "CSPW", "CSPT", "cash_secured_put")
    if is_cash_secured:
        short_puts = [l for l in strategy_input.legs if l.kind.lower() == "put" and l.position < 0]
        treasury_obligation = sum(l.strike * abs(l.position) * l.multiplier for l in short_puts)
        treasury_str = f"${treasury_obligation:,.2f}"

        if treasury_obligation > 0:
            treasury_interest = treasury_obligation * risk_free_rate * (dte_days / 365)
            treasury_return_str = f"${treasury_interest:,.2f}"
            treasury_return_pct = (treasury_interest / treasury_obligation) * 100
            treasury_return_pct_str = f"{treasury_return_pct:.2f}%"
        else:
            treasury_return_str = "N/A"
            treasury_return_pct_str = "N/A"

        summary_rows.append({"metric": "Treasury Obligation", "options": treasury_str, "combined": treasury_str})
        summary_rows.append({"metric": "Treasury Interest", "options": treasury_return_str, "combined": treasury_return_str})
        summary_rows.append({"metric": "Treasury Return %", "options": treasury_return_pct_str, "combined": treasury_return_pct_str})

    legs_meta = _safe_list(meta.get("legs_meta") or meta.get("legs"))
    bbg_quotes = []
    if isinstance(bbg_leg_snapshots, Mapping):
        bbg_quotes = bbg_leg_snapshots.get("leg_quotes") or []
    legs = []
    for idx, leg in enumerate(strategy_input.legs):
        meta_leg = legs_meta[idx] if idx < len(legs_meta) else {}
        side = "Long" if leg.position > 0 else "Short"
        ratio = abs(leg.position)
        quote = bbg_quotes[idx] if idx < len(bbg_quotes) and isinstance(bbg_quotes[idx], dict) else {}
        legs.append(
            {
                "index": meta_leg.get("index", idx + 1),
                "kind": str(meta_leg.get("kind", leg.kind)).upper(),
                "side": meta_leg.get("side", side),
                "ratio": meta_leg.get("ratio", ratio),
                "strike": meta_leg.get("strike", leg.strike),
                "premium": meta_leg.get("premium", leg.premium),
                "ticker": meta_leg.get("ticker"),
                "override": bool(meta_leg.get("override", False)),
                "delta": quote.get("delta"),
                "delta_mid": quote.get("delta"),  # alias for backward compat
                "gamma": quote.get("gamma"),
                "theta": quote.get("theta"),
                "vega": quote.get("vega"),
                "rho": quote.get("rho"),
            }
        )

    key_rows = []
    spot = float(strategy_input.spot)
    spot_row = _closest_row(scenario_df, spot)
    spot_label = _label_from_row(spot_row, "Current Market Price")
    key_rows.append(_key_row(spot_label, spot_row, spot))

    for idx, strike in enumerate(strikes):
        row = _closest_row(scenario_df, strike)
        strike_label = _label_from_row(row, f"Strike {idx + 1}")
        key_rows.append(_key_row(strike_label, row, spot))

    for idx, breakeven in enumerate(breakevens):
        row = _closest_row(scenario_df, breakeven)
        breakeven_label = _label_from_row(row, f"Breakeven {idx + 1}")
        key_rows.append(_key_row(breakeven_label, row, spot))

    price_values = pd.to_numeric(scenario_df["price"], errors="coerce").dropna()
    if not price_values.empty:
        low_price = float(price_values.min())
        high_price = float(price_values.max())
        low_row = _closest_row(scenario_df, low_price)
        high_row = _closest_row(scenario_df, high_price)
        low_label = _label_from_row(low_row, "Low")
        high_label = _label_from_row(high_row, "High")
        key_rows.append(_key_row(low_label, low_row, spot))
        key_rows.append(_key_row(high_label, high_row, spot))

    spot_texts = [text for text in [_extract_commentary(spot_row)] if text]
    strike_texts = []
    for strike in strikes:
        text = _extract_commentary(_closest_row(scenario_df, strike))
        if text:
            strike_texts.append(text)
    breakeven_texts = []
    for breakeven in breakevens:
        text = _extract_commentary(_closest_row(scenario_df, breakeven))
        if text:
            breakeven_texts.append(text)
    low_text = _extract_commentary(
        _closest_row(scenario_df, float(price_values.min()))
    ) if not price_values.empty else None
    high_text = _extract_commentary(
        _closest_row(scenario_df, float(price_values.max()))
    ) if not price_values.empty else None

    commentary_blocks = [
        {"level": "Spot", "text": " ".join(spot_texts) if spot_texts else "--"},
        {
            "level": "Strikes",
            "text": " ".join(strike_texts) if strike_texts else "--",
        },
        {
            "level": "Breakevens",
            "text": " ".join(breakeven_texts) if breakeven_texts else "--",
        },
        {"level": "Low", "text": low_text or "--"},
        {"level": "High", "text": high_text or "--"},
    ]

    key_levels = {
        "meta": {
            "as_of": as_of_date,
            "expiry": expiry_date,
            "spot": spot,
            "has_stock_position": bool(strategy_input.stock_position),
            "shares": int(strategy_input.stock_position)
            if strategy_input.stock_position
            else None,
            "avg_cost": (
                float(strategy_input.avg_cost)
                if strategy_input.stock_position
                else None
            ),
        },
        "levels": [],
    }

    def add_level(
        level_id: str,
        label: str,
        row: Optional[pd.Series],
        price: Optional[float],
        source: str,
    ) -> None:
        move_pct = None
        if price is not None and spot:
            move_pct = (float(price) / spot - 1.0) * 100.0
        key_levels["levels"].append(
            {
                "id": level_id,
                "label": label,
                "price": price,
                "move_pct": move_pct,
                "stock_pnl": row.get("stock_pnl") if row is not None else None,
                "option_pnl": row.get("option_pnl") if row is not None else None,
                "net_pnl": row.get("combined_pnl") if row is not None else None,
                "net_roi": row.get("net_roi") if row is not None else None,
                "source": source,
            }
        )

    def _row_for_price(price: float) -> pd.Series:
        row = _row_by_price(scenario_df, price)
        if row is not None:
            return row
        option_pnl = _compute_pnl_for_price(option_only, price)
        combined_pnl = _compute_pnl_for_price(strategy_input, price)
        stock_pnl = combined_pnl - option_pnl
        option_roi = option_pnl / option_basis if option_basis else None
        net_roi = combined_pnl / total_basis if total_basis else None
        return pd.Series(
            {
                "price": price,
                "option_pnl": option_pnl,
                "stock_pnl": stock_pnl,
                "combined_pnl": combined_pnl,
                "option_roi": option_roi,
                "net_roi": net_roi,
            }
        )

    spot_row_exact = _row_by_price(scenario_df, spot)
    add_level(
        "spot",
        _label_from_row(spot_row_exact, "Current Market Price"),
        spot_row_exact,
        spot,
        "spot",
    )

    # Add downside/upside target levels using the actual target prices
    # from the UI (downside_tgt/upside_tgt factors), not min/max of
    # the scenario table (which would pick up strikes instead).
    if scenario_mode.upper() != "INFINITY":
        downside_price = spot * downside_tgt
        downside_row = _row_for_price(downside_price)
        downside_label = _move_label("Downside Target", spot, downside_price)
        add_level("downside", downside_label, downside_row, downside_price, "downside")

        upside_price = spot * upside_tgt
        upside_row = _row_for_price(upside_price)
        upside_label = _move_label("Upside Target", spot, upside_price)
        add_level("upside", upside_label, upside_row, upside_price, "upside")

    for idx, strike in enumerate(strikes, start=1):
        row = _row_by_price(scenario_df, strike)
        label = _label_from_row(row, f"Strike {idx}")
        add_level(f"strike_{idx}", label, row, strike, "strike")

    for idx, breakeven in enumerate(breakevens, start=1):
        row = _row_for_price(breakeven)
        label = f"Breakeven {idx}"
        add_level(f"breakeven_{idx}", label, row, breakeven, "breakeven")

    zero_row = _row_for_price(0.0)
    add_level("zero", "Stock to Zero", zero_row, 0.0, "sentinel")

    # Bug 2D: Compute actual PnL values for "Stock to Infinity" using a
    # proxy high price instead of showing "--" for all fields.
    max_strike = max((leg.strike for leg in strategy_input.legs), default=spot)
    inf_proxy = max(max_strike * 10, spot * 10)
    opt_pnl_inf = _compute_pnl_for_price(option_only, inf_proxy)
    comb_pnl_inf = _compute_pnl_for_price(strategy_input, inf_proxy)
    stock_pnl_inf = comb_pnl_inf - opt_pnl_inf
    opt_roi_inf = opt_pnl_inf / option_basis if option_basis else None
    net_roi_inf = comb_pnl_inf / total_basis if total_basis else None
    infinity_row = pd.Series({
        "price": None,
        "option_pnl": opt_pnl_inf,
        "stock_pnl": stock_pnl_inf,
        "combined_pnl": comb_pnl_inf,
        "option_roi": opt_roi_inf,
        "net_roi": net_roi_inf,
    })
    add_level("infinity", "Stock to Infinity", infinity_row, None, "sentinel")

    eligibility_error = None
    try:
        eligibility_df = get_account_eligibility(strategy_code)
    except Exception as exc:
        eligibility_df = pd.DataFrame(
            columns=["account_type", "eligibility"]
        )
        eligibility_error = str(exc)

    analysis_pack = {
        "as_of": as_of,
        "underlying": {
            "ticker": meta.get("underlying_ticker"),
            "resolved": meta.get("resolved_underlying"),
            "spot": strategy_input.spot,
            "high_52week": _clean_value(high_52week),
            "low_52week": _clean_value(low_52week),
            "week_52_high": _clean_value(high_52week),
            "week_52_low": _clean_value(low_52week),
            "high_dt_52week": _clean_value(high_dt_52week),
            "low_dt_52week": _clean_value(low_dt_52week),
            "chg_pct_ytd": _clean_value(chg_pct_ytd),
            "chg_pct_1yr": _clean_value(chg_pct_1yr),
            "chg_pct_5d": _clean_value(chg_pct_5d),
            "chg_pct_3m": _clean_value(chg_pct_3m),
            "eqy_trr_pct_1yr": _clean_value(eqy_trr_pct_1yr),
            "vol_percentile": _clean_value(vol_percentile),
            "impvol_3m_atm": _clean_value(impvol_3m_atm),
            "chg_pct_1d": _clean_value(chg_pct_1d),
            "chg_net_1d": _clean_value(chg_net_1d),
            "impvol_6m_atm": _clean_value(impvol_6m_atm),
            "earnings_related_implied_move": _clean_value(
                earnings_related_implied_move
            ),
            "ubs_rating": _clean_value(normalized_profile.get("UBS_RATING")
                or normalized_profile.get("BEST_ANALYST_REC")
                or profile_value.get("ubs_rating")),
            "ubs_target": _clean_value(normalized_profile.get("UBS_TARGET")
                or normalized_profile.get("BEST_TARGET_PRICE")
                or profile_value.get("ubs_target")),
            "mov_avg_200d": _clean_value(normalized_profile.get("MOV_AVG_200D") or normalized_profile.get("MOV_AVG_200D".lower()) or profile_value.get("mov_avg_200d")),
            "earnings_date": expected_report_value,
            "earnings_risk": {
                "earnings_date": (
                    earnings_date_for_risk or expected_report_value
                ),
                "days_to_earnings": days_to_earnings,
                "before_expiry": earnings_before_expiry,
            },
            "profile": profile_value,
            "dividend_risk": {
                "ex_div_date": ex_div_date,
                "days_to_dividend": days_to_dividend,
                "before_expiry": before_expiry,
                "projected_dividend": projected_dividend,
                "dividend_status": dividend_status,
            },
            "put_call_oi_ratio": _clean_value(profile_value.get("put_call_oi_ratio")),
            "put_call_vol_ratio": _clean_value(profile_value.get("put_call_vol_ratio")),
            "realized_vol_3m": _clean_value(profile_value.get("realized_vol_3m")),
            "iv_rv_spread": _clean_value(profile_value.get("iv_rv_spread")),
            "iv_skew_3m": _clean_value(profile_value.get("iv_skew_3m")),
            "iv_term_premium": _clean_value(profile_value.get("iv_term_premium")),
            "iv_rv_percentile": _clean_value(profile_value.get("iv_rv_percentile")),
            "iv_skew_percentile": _clean_value(profile_value.get("iv_skew_percentile")),
            "iv_term_premium_percentile": _clean_value(profile_value.get("iv_term_premium_percentile")),
        },
        "strategy": {
            "group": meta.get("group"),
            "subgroup": meta.get("subgroup"),
            "name": meta.get("strategy_name"),
            "id": meta.get("strategy_id"),
            "strategy_code": strategy_code,
            "expiry": expiry_value,
        },
        "policies": {
            "pricing_mode": pricing_mode,
            "roi_policy": roi_policy,
            "vol_mode": vol_mode,
            "risk_free_rate": risk_free_rate,
            "auto_capital_basis": auto_basis,
        },
        "legs": legs,
        "payoff": {
            "price_grid": price_grid,
            "options_pnl": options_pnl,
            "stock_pnl": stock_pnl,
            "combined_pnl": combined_pnl,
            "strikes": strikes,
            "breakevens": breakevens,
        },
        "summary": {
            "rows": summary_rows,
            "net_premium_total": net_premium_text,
            "net_premium_total_value": net_premium_total,
            "net_premium_per_share": _format_number(net_prem_per_share),
        },
        "margin": {
            "classification": classify_strategy(strategy_input),
            "margin_proxy": margin_proxy,
            "full": margin_full,
        },
        "probabilities": prob_results,
        "scenario": {
            "df": scenario_df,
            "top10": scenario_df.head(10).copy(),
            "key_levels": key_rows,
        },
        "eligibility": {
            "strategy_code": strategy_code,
            "table": eligibility_df,
            "error": eligibility_error,
        },
        "commentary_blocks": commentary_blocks,
    }
    # Bug 2A: Deduplicate key levels that share the same price
    key_levels["levels"] = _dedup_key_levels(key_levels["levels"])
    analysis_pack["key_levels"] = key_levels
    analysis_pack["dividend_schedule"] = None  # Populated by callback layer via fetch_dividend_sum_to_expiry
    # Store vol surface metadata (data from callback layer, not fetched here)
    analysis_pack["vol_surface"] = {
        "atm_iv_at_expiry": None,  # populated by callback layer
        "source": "IVOL_SURFACE_STRIKE" if vol_mode == "surface_atm" else "3M_ATM_BDP",
    }
    analysis_pack["narrative_scenarios"] = build_narrative_scenarios(
        strategy_input=strategy_input,
        key_levels=key_levels,
        payoff_result=payoff_result,
        summary_rows=summary_rows,
    )
    return analysis_pack
