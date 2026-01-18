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


def _get_from_snapshot(snapshot: Optional[Mapping[str, object]], keys: Iterable[str]) -> object:
    if snapshot is None:
        return None
    for key in keys:
        if isinstance(snapshot, Mapping) and key in snapshot:
            return snapshot.get(key)
        if hasattr(snapshot, "get"):
            try:
                return snapshot.get(key)  # type: ignore[call-arg]
            except Exception:
                continue
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


def build_report_model(state: Dict[str, object]) -> Dict[str, object]:
    snapshot = state.get("underlying_snapshot")
    header = {
        "report_time": _fmt_text(
            state.get("analysis_as_of") or state.get("report_time")
        ),
        "ticker": _fmt_text(
            state.get("resolved_underlying") or state.get("underlying_ticker")
        ),
        "last_price": _fmt_currency(
            state.get("spot_value") if "spot_value" in state else state.get("spot")
        ),
        "strategy_name": _fmt_text(
            state.get("analysis_strategy_name") or state.get("strategy_name")
        ),
        "expiry": _fmt_date(
            state.get("chain_expiry") if "chain_expiry" in state else state.get("expiry")
        ),
        "shares": _fmt_text(state.get("stock_position")),
        "avg_cost": _fmt_currency(state.get("avg_cost")),
        "name": _fmt_text(_get_from_snapshot(snapshot, ["NAME"])),
        "sector": _fmt_text(
            _get_from_snapshot(snapshot, ["GICS_SECTOR_NAME", "INDUSTRY_SECTOR"])
        ),
        "high_52w": _fmt_currency(_get_from_snapshot(snapshot, ["52WK_HIGH"])),
        "low_52w": _fmt_currency(_get_from_snapshot(snapshot, ["52WK_LOW"])),
        "dividend_yield": _fmt_percent(
            _get_from_snapshot(snapshot, ["DVD_YLD", "EQY_DVD_YLD_IND"])
        ),
        "earnings_date": _fmt_text(
            _get_from_snapshot(snapshot, ["EARNINGS_ANNOUNCEMENT_DATE"])
        ),
        "policies": _fmt_text(
            state.get("policies")
            or " / ".join(
                [
                    _fmt_text(state.get("pricing_mode")),
                    _fmt_text(state.get("roi_policy")),
                    _fmt_text(state.get("vol_mode")),
                ]
            )
        ),
        "title": _fmt_text(state.get("title")),
    }

    expiry_text = header["expiry"]
    structure_legs: List[Dict[str, str]] = []
    for idx in range(4):
        include = bool(state.get(f"include_{idx}", False))
        structure_legs.append(
            {
                "leg": str(idx + 1),
                "side": _fmt_text(state.get(f"pos_{idx}") if include else None),
                "expiry": _fmt_text(expiry_text if include else None),
                "strike": _fmt_currency(state.get(f"strike_{idx}") if include else None),
                "premium": _fmt_currency(state.get(f"prem_{idx}") if include else None),
            }
        )

    structure = {
        "legs": structure_legs,
        "net_premium_total": _fmt_currency(state.get("net_premium_total")),
        "net_premium_per_share": _fmt_currency(state.get("net_premium_per_share")),
    }

    results = state.get("analysis_results", {})
    if isinstance(results, Mapping):
        price_grid = results.get("price_grid", [])
        combined_pnl = results.get("pnl", [])
        breakevens = results.get("breakevens", [])
    else:
        price_grid = []
        combined_pnl = []
        breakevens = []

    payoff = {
        "price_grid": price_grid,
        "combined_pnl": combined_pnl,
        "strikes": [leg.get("strike") for leg in structure_legs],
        "breakevens": breakevens,
    }

    metrics_source = state.get("metrics", {})
    if not isinstance(metrics_source, Mapping):
        metrics_source = {}

    def metric_value(key: str) -> object:
        if key in metrics_source:
            return metrics_source.get(key)
        return state.get(key)

    metrics_rows = []
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

    key_levels = _normalize_rows(state.get("key_levels"))

    scenario_source = (
        state.get("scenario_table")
        or state.get("analysis_scenario_table")
        or []
    )
    scenario_rows = _normalize_rows(scenario_source)
    normalized_rows = [_scenario_row_from_source(row) for row in scenario_rows]
    scenario_table = {
        "top10": normalized_rows[:10],
        "full": normalized_rows,
    }

    commentary_blocks = _normalize_rows(state.get("commentary_blocks"))
    if not commentary_blocks:
        commentary_blocks = [{"level": MISSING, "text": MISSING}]

    disclaimers = state.get("disclaimers")
    if isinstance(disclaimers, list) and disclaimers:
        disclaimer_list = [str(item) if str(item).strip() else MISSING for item in disclaimers]
    else:
        disclaimer_list = [MISSING]

    page_meta = {
        "size": {"width_pt": 612, "height_pt": 792},
        "margin": {"left_pt": 30, "right_pt": 30, "top_pt": 24, "bottom_pt": 18},
    }

    return {
        "page_meta": page_meta,
        "header": header,
        "structure": structure,
        "payoff": payoff,
        "metrics": metrics,
        "key_levels": key_levels,
        "scenario_table": scenario_table,
        "commentary_blocks": commentary_blocks,
        "disclaimers": disclaimer_list,
    }
