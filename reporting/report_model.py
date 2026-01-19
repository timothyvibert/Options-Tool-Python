from __future__ import annotations

from datetime import date, datetime
from typing import Any, Dict, Iterable, List, Mapping, Optional

import math

try:
    import pandas as pd
except Exception:  # pragma: no cover - optional import for type checks
    pd = None  # type: ignore


MISSING = "--"


def _is_missing(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return value.strip() == ""
    if isinstance(value, (int, float)):
        if isinstance(value, float) and math.isnan(value):
            return True
    return False


def _fmt_text(value: object) -> str:
    if _is_missing(value):
        return MISSING
    return str(value)


def _fmt_date(value: object) -> str:
    if _is_missing(value):
        return MISSING
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d")
    if isinstance(value, date):
        return value.isoformat()
    return str(value)


def _fmt_long_date(value: object) -> str:
    if _is_missing(value):
        return MISSING
    if isinstance(value, datetime):
        return value.strftime("%b %d, %Y")
    if isinstance(value, date):
        return value.strftime("%b %d, %Y")
    if isinstance(value, str):
        text = value.strip()
        if text:
            try:
                parsed = datetime.fromisoformat(text[:10])
                return parsed.strftime("%b %d, %Y")
            except ValueError:
                return text
    return str(value)


def _fmt_currency(value: object) -> str:
    if _is_missing(value):
        return MISSING
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float)):
        return f"{value:,.2f}"
    return str(value)


def _fmt_percent(value: object) -> str:
    if _is_missing(value):
        return MISSING
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float)):
        return f"{value:.2f}%"
    return str(value)


def _fmt_dividend_yield(value: object) -> str:
    numeric = _coerce_float(value)
    if numeric is None:
        return MISSING
    # Bloomberg fields may arrive as percent points (1.7) or fractions (0.017).
    if 0 < abs(numeric) <= 0.2:
        numeric *= 100.0
    return f"{numeric:.1f}%"


def _get_from_snapshot(snapshot: Optional[Mapping[str, object]], keys: Iterable[str]) -> object:
    if snapshot is None:
        return None
    for key in keys:
        if isinstance(snapshot, Mapping) and key in snapshot:
            value = snapshot.get(key)
            if not _is_missing(value):
                return value
        if hasattr(snapshot, "get"):
            try:
                value = snapshot.get(key)  # type: ignore[call-arg]
            except Exception:
                continue
            if not _is_missing(value):
                return value
    if isinstance(snapshot, Mapping):
        lowered = {str(k).lower(): k for k in snapshot.keys()}
        for key in keys:
            lowered_key = str(key).lower()
            if lowered_key in lowered:
                value = snapshot.get(lowered[lowered_key])
                if not _is_missing(value):
                    return value
    return None


def _normalize_rows(value: object) -> List[Dict[str, object]]:
    if value is None:
        return []
    if pd is not None and isinstance(value, pd.DataFrame):
        return value.to_dict(orient="records")
    if isinstance(value, list):
        return [row if isinstance(row, dict) else {"value": row} for row in value]
    return []


def _scenario_row_from_source(row: Mapping[str, object]) -> Dict[str, str]:
    def pick(keys: Iterable[str]) -> object:
        for key in keys:
            if key in row:
                return row[key]
        return None

    return {
        "scenario": _fmt_text(pick(["scenario", "Scenario"])),
        "price": _fmt_currency(pick(["price", "Price"])),
        "move_pct": _fmt_percent(pick(["move_pct", "Move %", "move_percent"])),
        "stock_pnl": _fmt_currency(pick(["stock_pnl", "Stock PnL"])),
        "option_pnl": _fmt_currency(pick(["option_pnl", "Option PnL"])),
        "option_roi": _fmt_percent(pick(["option_roi", "Option ROI"])),
        "net_pnl": _fmt_currency(pick(["net_pnl", "combined_pnl", "Net PnL"])),
        "net_roi": _fmt_percent(pick(["net_roi", "Net ROI"])),
    }


def _scenario_card_text(value: object) -> str:
    if _is_missing(value):
        return ""
    return str(value)


def _normalize_scenario_key(value: object) -> str:
    if value is None:
        return ""
    text = str(value).strip().lower()
    for ch in [" ", "-", "_"]:
        text = text.replace(ch, "")
    if text.startswith("bear"):
        return "bearish"
    if text.startswith("bull"):
        return "bullish"
    if text.startswith("stag") or text.startswith("base") or text.startswith("neutral"):
        return "stagnant"
    return text


def _extract_scenario_value(scenario: Mapping[str, object], keys: Iterable[str]) -> str:
    for key in keys:
        if key in scenario:
            value = scenario.get(key)
            if isinstance(value, Mapping):
                value = (
                    value.get("text")
                    or value.get("value")
                    or value.get("label")
                    or value.get("content")
                )
            return _scenario_card_text(value)
    return ""


def _coerce_float(value: object) -> Optional[float]:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        if isinstance(value, float) and math.isnan(value):
            return None
        return float(value)
    if isinstance(value, str):
        text = value.strip()
        if text == "":
            return None
        if text.endswith("%"):
            text = text[:-1].strip()
        text = text.replace(",", "")
        try:
            return float(text)
        except ValueError:
            return None
    return None


def _get_option_basis(
    analysis_pack: Optional[Mapping[str, object]],
    row: Mapping[str, object],
) -> Optional[float]:
    for key in [
        "option_capital_basis",
        "options_capital_basis",
        "option_basis",
        "capital_basis_options",
    ]:
        if key in row:
            value = _coerce_float(row.get(key))
            if value is not None:
                return value

    if not isinstance(analysis_pack, Mapping):
        return None
    metrics = analysis_pack.get("metrics")
    if isinstance(metrics, Mapping):
        for key in ["capital_basis_options", "option_capital_basis", "option_basis"]:
            if key in metrics:
                value = _coerce_float(metrics.get(key))
                if value is not None:
                    return value
    summary = analysis_pack.get("summary")
    if isinstance(summary, Mapping):
        rows = summary.get("rows")
        if isinstance(rows, list):
            for metric_row in rows:
                if not isinstance(metric_row, Mapping):
                    continue
                if metric_row.get("metric") == "Capital Basis":
                    value = _coerce_float(metric_row.get("options"))
                    if value is not None:
                        return value
    return None


def _fmt_price(value: object) -> str:
    numeric = _coerce_float(value)
    if numeric is None:
        return MISSING
    return f"{numeric:.2f}"


def _fmt_move_pct(value: object) -> str:
    numeric = _coerce_float(value)
    if numeric is None:
        return MISSING
    return f"{numeric:.1f}"


def _fmt_pnl(value: object) -> str:
    numeric = _coerce_float(value)
    if numeric is None:
        return MISSING
    if abs(numeric) < 1e-6:
        return "0.00"
    return f"{numeric:.2f}"


def _fmt_roi(value: object) -> str:
    if value is None:
        return MISSING
    if isinstance(value, str):
        text = value.strip()
        if text == "":
            return MISSING
        if "%" in text:
            numeric = _coerce_float(text)
            if numeric is None:
                return text
            if abs(numeric) < 1e-6:
                numeric = 0.0
            return f"{numeric:.1f}%"
    numeric = _coerce_float(value)
    if numeric is None:
        return MISSING
    if abs(numeric) < 1e-6:
        numeric = 0.0
    if abs(numeric) <= 2.0:
        numeric *= 100.0
    return f"{numeric:.1f}%"


def _key_level_sort_key(row: Mapping[str, object]) -> tuple[int, int, float]:
    label = row.get("label")
    if _is_missing(label):
        label = row.get("Scenario") or row.get("scenario")
    label_text = str(label).strip().lower() if label is not None else ""
    row_id = row.get("id")
    is_infinity = False
    if isinstance(row_id, str) and row_id.strip().lower() == "infinity":
        is_infinity = True
    if "infinity" in label_text:
        is_infinity = True
    if row.get("is_infinity") is True:
        is_infinity = True
    price = _coerce_float(row.get("price", row.get("Price")))
    is_missing = price is None
    if is_infinity:
        return (1, 1, float("inf"))
    if is_missing:
        return (0, 1, 0.0)
    return (0, 0, float(price))


def build_report_model(state: Dict[str, object]) -> Dict[str, object]:
    snapshot = state.get("underlying_snapshot")
    analysis_pack = state.get("analysis_pack")
    if not isinstance(analysis_pack, Mapping):
        analysis_pack = None
    pack_underlying = analysis_pack.get("underlying", {}) if analysis_pack else {}
    if not isinstance(pack_underlying, Mapping):
        pack_underlying = {}
    pack_strategy = analysis_pack.get("strategy", {}) if analysis_pack else {}
    if not isinstance(pack_strategy, Mapping):
        pack_strategy = {}
    pack_summary = analysis_pack.get("summary", {}) if analysis_pack else {}
    if not isinstance(pack_summary, Mapping):
        pack_summary = {}
    pack_payoff = analysis_pack.get("payoff", {}) if analysis_pack else {}
    if not isinstance(pack_payoff, Mapping):
        pack_payoff = {}
    pack_scenario = analysis_pack.get("scenario", {}) if analysis_pack else {}
    if not isinstance(pack_scenario, Mapping):
        pack_scenario = {}
    pack_policies = analysis_pack.get("policies", {}) if analysis_pack else {}
    if not isinstance(pack_policies, Mapping):
        pack_policies = {}

    analysis_summary = state.get("analysis_summary", {})
    if not isinstance(analysis_summary, Mapping):
        analysis_summary = {}

    policy_value = state.get("policies")
    if _is_missing(policy_value):
        policy_parts = []
        for key in ["pricing_mode", "roi_policy", "vol_mode"]:
            value = pack_policies.get(key)
            if not _is_missing(value):
                policy_parts.append(_fmt_text(value))
        if not policy_parts:
            policy_parts = [
                _fmt_text(state.get("pricing_mode")),
                _fmt_text(state.get("roi_policy")),
                _fmt_text(state.get("vol_mode")),
            ]
        policy_value = " / ".join(
            [part for part in policy_parts if not _is_missing(part)]
        )

    profile_source = pack_underlying.get("profile")
    if not isinstance(profile_source, Mapping):
        profile_source = snapshot

    raw_dividend_yield = _get_from_snapshot(
        profile_source, ["EQY_DVD_YLD_IND", "DVD_YLD", "DVD_YLD_IND", "EQY_DVD_YLD"]
    )
    dividend_yield_text = _fmt_dividend_yield(raw_dividend_yield)

    header = {
        "report_time": _fmt_text(
            (analysis_pack or {}).get("as_of")
            or state.get("analysis_as_of")
            or state.get("report_time")
        ),
        "ticker": _fmt_text(
            pack_underlying.get("resolved")
            or pack_underlying.get("ticker")
            or state.get("resolved_underlying")
            or state.get("underlying_ticker")
        ),
        "last_price": _fmt_currency(
            pack_underlying.get("spot")
            or (state.get("spot_value") if "spot_value" in state else state.get("spot"))
        ),
        "strategy_name": _fmt_text(
            pack_strategy.get("name")
            or state.get("analysis_strategy_name")
            or state.get("strategy_name")
        ),
        "expiry": _fmt_date(
            pack_strategy.get("expiry")
            or (state.get("chain_expiry") if "chain_expiry" in state else state.get("expiry"))
        ),
        "shares": _fmt_text(state.get("stock_position")),
        "avg_cost": _fmt_currency(state.get("avg_cost")),
        "name": _fmt_text(_get_from_snapshot(profile_source, ["NAME"])),
        "sector": _fmt_text(
            _get_from_snapshot(profile_source, ["GICS_SECTOR_NAME", "INDUSTRY_SECTOR"])
        ),
        "high_52w": _fmt_currency(_get_from_snapshot(profile_source, ["52WK_HIGH"])),
        "low_52w": _fmt_currency(_get_from_snapshot(profile_source, ["52WK_LOW"])),
        "dividend_yield": dividend_yield_text,
        "earnings_date": _fmt_text(
            _get_from_snapshot(profile_source, ["EARNINGS_ANNOUNCEMENT_DATE"])
        ),
        "policies": _fmt_text(policy_value),
        "title": _fmt_text(state.get("title")),
    }

    expiry_text = header["expiry"]
    structure_legs: List[Dict[str, str]] = []
    pack_legs = analysis_pack.get("legs") if analysis_pack else None
    if isinstance(pack_legs, list) and pack_legs:
        for idx, leg in enumerate(pack_legs):
            if not isinstance(leg, Mapping):
                continue
            structure_legs.append(
                {
                    "leg": _fmt_text(leg.get("index", idx + 1)),
                    "side": _fmt_text(leg.get("side")),
                    "expiry": _fmt_text(leg.get("expiry") or expiry_text),
                    "strike": _fmt_currency(leg.get("strike")),
                    "premium": _fmt_currency(leg.get("premium")),
                }
            )
    else:
        for idx in range(4):
            include = bool(state.get(f"include_{idx}", False))
            structure_legs.append(
                {
                    "leg": str(idx + 1),
                    "side": _fmt_text(state.get(f"pos_{idx}") if include else None),
                    "expiry": _fmt_text(expiry_text if include else None),
                    "strike": _fmt_currency(
                        state.get(f"strike_{idx}") if include else None
                    ),
                    "premium": _fmt_currency(
                        state.get(f"prem_{idx}") if include else None
                    ),
                }
            )

    net_premium_total = pack_summary.get("net_premium_total")
    if _is_missing(net_premium_total):
        net_premium_total = state.get("net_premium_total")
    if _is_missing(net_premium_total):
        net_premium_total = analysis_summary.get(
            "cost_credit_options",
            analysis_summary.get("cost_credit_combined"),
        )
    net_premium_per_share = pack_summary.get("net_premium_per_share")
    if _is_missing(net_premium_per_share):
        net_premium_per_share = state.get("net_premium_per_share")
    if _is_missing(net_premium_per_share):
        net_premium_per_share = analysis_summary.get("net_prem_per_share")

    structure = {
        "legs": structure_legs,
        "net_premium_total": _fmt_currency(net_premium_total),
        "net_premium_per_share": _fmt_currency(net_premium_per_share),
    }

    if pack_payoff:
        price_grid = pack_payoff.get("price_grid", [])
        combined_pnl = pack_payoff.get("combined_pnl", pack_payoff.get("pnl", []))
        breakevens = pack_payoff.get("breakevens", [])
        strikes = pack_payoff.get("strikes", [])
    else:
        analysis_payoff = state.get("analysis_payoff", {})
        if isinstance(analysis_payoff, Mapping):
            price_grid = analysis_payoff.get("price_grid", [])
            combined_pnl = analysis_payoff.get("combined_pnl", [])
            breakevens = analysis_payoff.get("breakevens", [])
            strikes = analysis_payoff.get("strikes", [])
        else:
            price_grid = []
            combined_pnl = []
            breakevens = []
            strikes = []
    if not isinstance(strikes, list) or not strikes:
        strikes = [leg.get("strike") for leg in structure_legs]

    payoff = {
        "price_grid": price_grid,
        "combined_pnl": combined_pnl,
        "strikes": strikes,
        "breakevens": breakevens,
    }

    def metric_value(key: str) -> object:
        if key in analysis_summary:
            return analysis_summary.get(key)
        return state.get(key)

    metrics_rows = []
    pack_rows = pack_summary.get("rows")
    if isinstance(pack_rows, list) and pack_rows:
        for row in pack_rows:
            if not isinstance(row, Mapping):
                continue
            metrics_rows.append(
                {
                    "metric": _fmt_text(row.get("metric")),
                    "options": _fmt_text(row.get("options")),
                    "combined": _fmt_text(row.get("combined")),
                }
            )
    else:
        metrics_map = [
            ("Max Profit", "max_profit_options", "max_profit_combined"),
            ("Max Loss", "max_loss_options", "max_loss_combined"),
            ("Capital Basis", "capital_basis_options", "capital_basis_combined"),
            ("Max ROI", "max_roi_options", "max_roi_combined"),
            ("Min ROI", "min_roi_options", "min_roi_combined"),
            ("Cost/Credit", "cost_credit_options", "cost_credit_combined"),
            ("Notional Exposure", "notional_options", "notional_combined"),
            ("Net Prem/Share", "net_prem_per_share", "net_prem_per_share"),
            ("Net Prem % Spot", "net_prem_pct_spot", "net_prem_pct_spot"),
            ("PoP", "pop_options", "pop_combined"),
        ]
        for label, opt_key, comb_key in metrics_map:
            metrics_rows.append(
                {
                    "metric": label,
                    "options": _fmt_text(metric_value(opt_key)),
                    "combined": _fmt_text(metric_value(comb_key)),
                }
            )

    metrics = {
        "rows": metrics_rows,
    }

    key_levels_source = pack_scenario.get("key_levels")
    if key_levels_source is None:
        key_levels_source = state.get("key_levels")
    key_levels = _normalize_rows(key_levels_source)

    scenario_source = None
    if pack_scenario:
        if "df" in pack_scenario:
            scenario_source = pack_scenario.get("df")
        elif "full" in pack_scenario:
            scenario_source = pack_scenario.get("full")
        elif "top10" in pack_scenario:
            scenario_source = pack_scenario.get("top10")
    if scenario_source is None:
        scenario_source = state.get("analysis_scenario_df")
    if scenario_source is None:
        scenario_rows = []
    else:
        scenario_rows = _normalize_rows(scenario_source)
    normalized_rows = [_scenario_row_from_source(row) for row in scenario_rows]
    scenario_table = {
        "top10": normalized_rows[:10],
        "full": normalized_rows,
    }

    commentary_source = (
        analysis_pack.get("commentary_blocks") if analysis_pack else None
    )
    if commentary_source is None:
        commentary_source = state.get("commentary_blocks")
    commentary_blocks = _normalize_rows(commentary_source)
    if not commentary_blocks:
        commentary_blocks = [{"level": MISSING, "text": MISSING}]

    scenario_analysis_cards: List[Dict[str, str]] = []
    narrative_scenarios = analysis_pack.get("narrative_scenarios") if analysis_pack else None
    scenario_map: Dict[str, Mapping[str, object]] = {}
    scenario_list: List[Mapping[str, object]] = []
    if isinstance(narrative_scenarios, list):
        scenario_list = [
            item for item in narrative_scenarios if isinstance(item, Mapping)
        ]
    elif isinstance(narrative_scenarios, Mapping):
        scenarios_value = narrative_scenarios.get("scenarios")
        if isinstance(scenarios_value, list):
            scenario_list = [
                item for item in scenarios_value if isinstance(item, Mapping)
            ]
        else:
            for key, value in narrative_scenarios.items():
                if isinstance(value, Mapping):
                    normalized_key = _normalize_scenario_key(key)
                    if normalized_key and normalized_key not in scenario_map:
                        scenario_map[normalized_key] = value

    for scenario in scenario_list:
        title_value = (
            scenario.get("title")
            or scenario.get("name")
            or scenario.get("label")
        )
        normalized_key = _normalize_scenario_key(title_value)
        if normalized_key and normalized_key not in scenario_map:
            scenario_map[normalized_key] = scenario

    if scenario_map:
        for label, key in [
            ("Bearish", "bearish"),
            ("Stagnant", "stagnant"),
            ("Bullish", "bullish"),
        ]:
            scenario = scenario_map.get(key)
            if not isinstance(scenario, Mapping):
                continue
            title = _scenario_card_text(scenario.get("title") or label)
            condition = _extract_scenario_value(
                scenario, ["condition", "conditions", "condition_str"]
            )
            body = _extract_scenario_value(
                scenario, ["body", "narrative", "text", "body_str"]
            )
            scenario_analysis_cards.append(
                {"title": title or label, "condition": condition, "body": body}
            )

    key_levels_rows: List[Dict[str, object]] = []
    key_levels_meta: Mapping[str, object] = {}
    key_levels_block = None
    if isinstance(analysis_pack, Mapping):
        key_levels_block = analysis_pack.get("key_levels")
        if isinstance(key_levels_block, Mapping):
            levels = key_levels_block.get("levels")
            if isinstance(levels, list):
                key_levels_rows = list(levels)
            meta = key_levels_block.get("meta")
            if isinstance(meta, Mapping):
                key_levels_meta = meta
    if key_levels_meta:
        has_stock_position = bool(key_levels_meta.get("has_stock_position", False))
    elif isinstance(key_levels_block, Mapping):
        has_stock_position = bool(key_levels_block.get("has_stock_position", False))
    else:
        has_stock_position = False
    key_levels_rows_by_price = sorted(key_levels_rows, key=_key_level_sort_key)
    key_levels_display_rows_by_price: List[Dict[str, str]] = []
    for row in key_levels_rows_by_price:
        if not isinstance(row, Mapping):
            continue
        label = row.get("label")
        if _is_missing(label):
            label = row.get("Scenario") or row.get("scenario")
        label_text = _fmt_text(label)
        net_roi_value = row.get("net_roi", row.get("Net ROI"))
        option_roi_value = row.get("option_roi", row.get("Option ROI"))
        if (
            not has_stock_position
            and _is_missing(option_roi_value)
            and not _is_missing(net_roi_value)
        ):
            option_roi_value = net_roi_value
        if (
            has_stock_position
            and _is_missing(option_roi_value)
        ):
            option_pnl_value = _coerce_float(row.get("option_pnl", row.get("Option PnL")))
            option_basis_value = _get_option_basis(analysis_pack, row)
            if (
                option_pnl_value is not None
                and option_basis_value not in (None, 0.0)
            ):
                option_roi_value = option_pnl_value / option_basis_value
        key_levels_display_rows_by_price.append(
            {
                "Scenario": label_text,
                "Price": _fmt_price(row.get("price", row.get("Price"))),
                "Move %": _fmt_move_pct(row.get("move_pct", row.get("Move %"))),
                "Stock PnL": _fmt_pnl(row.get("stock_pnl", row.get("Stock PnL"))),
                "Option PnL": _fmt_pnl(row.get("option_pnl", row.get("Option PnL"))),
                "Option ROI": _fmt_roi(option_roi_value),
                "Net PnL": _fmt_pnl(
                    row.get("net_pnl", row.get("Net PnL", row.get("combined_pnl")))
                ),
                "Net ROI": _fmt_roi(net_roi_value),
            }
        )
    key_levels_display_rows = key_levels_display_rows_by_price

    warnings = {"dividend": None}
    dividend_risk = None
    if isinstance(pack_underlying, Mapping):
        dividend_risk = pack_underlying.get("dividend_risk")
    if isinstance(dividend_risk, Mapping):
        before_expiry = dividend_risk.get("before_expiry")
        if before_expiry is True:
            ex_div_date = dividend_risk.get("ex_div_date")
            date_text = _fmt_long_date(ex_div_date)
            if date_text != MISSING:
                warning_text = (
                    f"This strategy spans an ex-dividend date ({date_text}). "
                    "Early assignment risk may apply."
                )
            else:
                warning_text = (
                    "This strategy spans an ex-dividend date. "
                    "Early assignment risk may apply."
                )
            warnings["dividend"] = warning_text

    disclaimers = state.get("disclaimers")
    if isinstance(disclaimers, list) and disclaimers:
        disclaimer_list = [str(item) if str(item).strip() else MISSING for item in disclaimers]
    else:
        disclaimer_list = [MISSING]

    page_meta = {
        "size": {"width_pt": 612, "height_pt": 792},
        "margin": {"left_pt": 30, "right_pt": 30, "top_pt": 24, "bottom_pt": 18},
    }

    stock_banner = {
        "dividend_yield": dividend_yield_text,
    }

    return {
        "page_meta": page_meta,
        "header": header,
        "structure": structure,
        "payoff": payoff,
        "metrics": metrics,
        "key_levels": key_levels,
        "key_levels_rows": key_levels_rows,
        "key_levels_rows_by_price": key_levels_rows_by_price,
        "key_levels_display_rows": key_levels_display_rows,
        "key_levels_display_rows_by_price": key_levels_display_rows_by_price,
        "has_stock_position": has_stock_position,
        "stock_banner": stock_banner,
        "scenario_table": scenario_table,
        "scenario_analysis_cards": scenario_analysis_cards,
        "commentary_blocks": commentary_blocks,
        "warnings": warnings,
        "disclaimers": disclaimer_list,
    }
