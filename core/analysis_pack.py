from __future__ import annotations

from datetime import date, datetime
from typing import Dict, Iterable, List, Mapping, Optional

import math

import pandas as pd

from core.margin import classify_strategy, compute_margin_proxy
from core.models import StrategyInput
from core.narrative import build_narrative_scenarios
from core.payoff import _compute_pnl_for_price, compute_payoff
from core.probability import strategy_pop
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
        return f"Credit {abs(net_premium):.2f}"
    if net_premium > 0:
        return f"Debit {net_premium:.2f}"
    return "0.00"


def _format_number(value: Optional[float]) -> str:
    if value is None or not math.isfinite(value):
        return "--"
    return f"{value:.2f}"


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
    )

    option_basis = capital_basis(strategy_input, payoff_result, roi_policy)
    total_basis = combined_capital_basis(strategy_input, option_basis)
    margin_proxy = compute_margin_proxy(strategy_input, payoff_result)

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

    net_premium = compute_net_premium(strategy_input)
    net_premium_text = _format_net_premium(net_premium)
    net_premium_pct = (
        net_premium / strategy_input.spot * 100.0
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
            r=0.0,
            q=0.0,
            sigma_mode=vol_mode,
            atm_iv=atm_iv,
            per_leg_iv=per_leg_iv,
            t=t,
        )
    except Exception:
        pop = 0.0

    pop_text = f"{pop * 100:.1f}%"

    summary_rows = [
        {
            "metric": "Max Profit",
            "options": _format_number(max(options_pnl) if options_pnl else None),
            "combined": _format_number(max(combined_pnl) if combined_pnl else None),
        },
        {
            "metric": "Max Loss",
            "options": _format_number(min(options_pnl) if options_pnl else None),
            "combined": _format_number(min(combined_pnl) if combined_pnl else None),
        },
        {
            "metric": "Capital Basis",
            "options": _format_number(option_basis),
            "combined": _format_number(total_basis),
        },
        {
            "metric": "Max ROI",
            "options": _format_number(max(option_roi_values) if option_roi_values else None),
            "combined": _format_number(max(net_roi_values) if net_roi_values else None),
        },
        {
            "metric": "Min ROI",
            "options": _format_number(min(option_roi_values) if option_roi_values else None),
            "combined": _format_number(min(net_roi_values) if net_roi_values else None),
        },
        {
            "metric": "Cost/Credit",
            "options": net_premium_text,
            "combined": net_premium_text,
        },
        {
            "metric": "Notional Exposure",
            "options": _format_number(options_notional),
            "combined": _format_number(combined_notional),
        },
        {
            "metric": "Net Prem/Share",
            "options": _format_number(net_premium),
            "combined": _format_number(net_premium),
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

    legs_meta = _safe_list(meta.get("legs_meta") or meta.get("legs"))
    legs = []
    for idx, leg in enumerate(strategy_input.legs):
        meta_leg = legs_meta[idx] if idx < len(legs_meta) else {}
        side = "Long" if leg.position > 0 else "Short"
        ratio = abs(leg.position)
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

    if not price_values.empty:
        downside_price = float(price_values.min())
        downside_row = _row_by_price(scenario_df, downside_price)
        downside_label = _move_label("Downside", spot, downside_price)
        add_level("downside", downside_label, downside_row, downside_price, "downside")

        upside_price = float(price_values.max())
        upside_row = _row_by_price(scenario_df, upside_price)
        upside_label = _move_label("Upside", spot, upside_price)
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
    add_level("infinity", "Stock to Infinity", None, None, "sentinel")

    analysis_pack = {
        "as_of": as_of,
        "underlying": {
            "ticker": meta.get("underlying_ticker"),
            "resolved": meta.get("resolved_underlying"),
            "spot": strategy_input.spot,
            "profile": profile_value,
            "dividend_risk": {
                "ex_div_date": ex_div_date,
                "days_to_dividend": days_to_dividend,
                "before_expiry": before_expiry,
                "projected_dividend": projected_dividend,
                "dividend_status": dividend_status,
            },
        },
        "strategy": {
            "group": meta.get("group"),
            "subgroup": meta.get("subgroup"),
            "name": meta.get("strategy_name"),
            "id": meta.get("strategy_id"),
            "expiry": expiry_value,
        },
        "policies": {
            "pricing_mode": pricing_mode,
            "roi_policy": roi_policy,
            "vol_mode": vol_mode,
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
            "net_premium_per_share": _format_number(net_premium),
        },
        "margin": {
            "classification": classify_strategy(strategy_input),
            "margin_proxy": margin_proxy,
        },
        "scenario": {
            "df": scenario_df,
            "top10": scenario_df.head(10).copy(),
            "key_levels": key_rows,
        },
        "commentary_blocks": commentary_blocks,
    }
    analysis_pack["key_levels"] = key_levels
    analysis_pack["narrative_scenarios"] = build_narrative_scenarios(
        strategy_input=strategy_input,
        key_levels=key_levels,
        payoff_result=payoff_result,
    )
    return analysis_pack
