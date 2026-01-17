import logging
import math
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import pandas as pd


LOGGER = logging.getLogger(__name__)
LEG_COUNT = 4
ALLOWED_LEG_TYPES = {"CALL", "PUT", "STOCK"}


def _is_missing(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, float) and math.isnan(value):
        return True
    if isinstance(value, str) and value.strip() in ("", "-"):
        return True
    return False


def _normalize_text(value: Any) -> Optional[str]:
    if _is_missing(value):
        return None
    return str(value).strip()


def _normalize_leg_type(value: Any) -> Optional[str]:
    text = _normalize_text(value)
    if text is None:
        return None
    normalized = text.upper()
    if normalized in ALLOWED_LEG_TYPES:
        return normalized
    LOGGER.warning("Unknown leg type %r; setting to None.", text)
    return None


def _normalize_side(value: Any) -> Optional[str]:
    text = _normalize_text(value)
    if text is None:
        return None
    return text.upper()


def _normalize_ratio(value: Any) -> Optional[int]:
    if _is_missing(value):
        return None
    if isinstance(value, bool):
        raise ValueError("Ratio must be an integer, not bool.")
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        if value.is_integer():
            return int(value)
        raise ValueError(f"Ratio must be an integer: {value}")
    text = str(value).strip()
    if text == "":
        return None
    try:
        number = float(text)
    except ValueError as exc:
        raise ValueError(f"Ratio must be an integer: {value}") from exc
    if not number.is_integer():
        raise ValueError(f"Ratio must be an integer: {value}")
    return int(number)


def _normalize_strike(value: Any) -> Optional[Union[int, float, str]]:
    if _is_missing(value):
        return None
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if isinstance(value, float) and math.isnan(value):
            return None
        if isinstance(value, float) and value.is_integer():
            return int(value)
        return value
    text = str(value).strip()
    if text == "":
        return None
    try:
        number = float(text)
    except ValueError:
        return text.upper()
    if number.is_integer():
        return int(number)
    return number


def validate_strategy_map(strategy_map: pd.DataFrame) -> None:
    assert not strategy_map["strategy_id"].duplicated().any()
    leg_cols = [f"leg_{i}_type" for i in range(1, LEG_COUNT + 1)]
    call_put = strategy_map[leg_cols].isin(["CALL", "PUT"]).any(axis=1)
    for template_kind, mask in strategy_map.groupby("template_kind").groups.items():
        mask = strategy_map.index.isin(mask)
        if template_kind == "OPTIONS":
            assert call_put[mask].all()
        elif template_kind == "STOCK_ONLY":
            assert (~call_put[mask]).all()
        elif template_kind == "MIXED":
            assert call_put[mask].all()
        else:
            raise AssertionError(f"Unknown template_kind: {template_kind}")
    LOGGER.info("Loaded %s strategies", len(strategy_map))


def export_strategy_map(xlsm_path: str, out_path: str) -> None:
    raw_df = pd.read_excel(xlsm_path, sheet_name="StrategyMap")
    records: List[Dict[str, Any]] = []

    for _, row in raw_df.iterrows():
        record: Dict[str, Any] = {
            "strategy_id": int(row["ID"]),
            "group": _normalize_text(row["Group"]),
            "subgroup": _normalize_text(row["Subgroup"]),
            "strategy_name": _normalize_text(row["Strategy"]),
        }
        leg_types: List[Optional[str]] = []
        for leg_index in range(1, LEG_COUNT + 1):
            leg_type = _normalize_leg_type(row[f"Leg{leg_index}_Type"])
            record[f"leg_{leg_index}_type"] = leg_type
            leg_types.append(leg_type)
            record[f"leg_{leg_index}_side"] = _normalize_side(
                row[f"Leg{leg_index}_Side"]
            )
            record[f"leg_{leg_index}_ratio"] = _normalize_ratio(
                row[f"Leg{leg_index}_Ratio"]
            )
            record[f"leg_{leg_index}_strike"] = _normalize_strike(
                row[f"Leg{leg_index}_Strike"]
            )

        has_call_put = any(leg in {"CALL", "PUT"} for leg in leg_types)
        has_stock = "STOCK" in leg_types
        strategy_name = record["strategy_name"] or ""
        upper_name = strategy_name.upper()
        name_indicates_stock = "LONG STOCK" in upper_name or "SHORT STOCK" in upper_name
        if has_call_put and has_stock:
            template_kind = "MIXED"
        elif has_call_put:
            template_kind = "OPTIONS"
        elif has_stock or name_indicates_stock:
            template_kind = "STOCK_ONLY"
        else:
            template_kind = "STOCK_ONLY"
        record["template_kind"] = template_kind
        records.append(record)

    column_order = [
        "strategy_id",
        "group",
        "subgroup",
        "strategy_name",
        "template_kind",
    ]
    for leg_index in range(1, LEG_COUNT + 1):
        column_order.extend(
            [
                f"leg_{leg_index}_type",
                f"leg_{leg_index}_side",
                f"leg_{leg_index}_ratio",
                f"leg_{leg_index}_strike",
            ]
        )

    strategy_map = pd.DataFrame.from_records(records, columns=column_order)
    for leg_index in range(1, LEG_COUNT + 1):
        ratio_col = f"leg_{leg_index}_ratio"
        strategy_map[ratio_col] = strategy_map[ratio_col].astype("Int64")

    validate_strategy_map(strategy_map)

    out_file = Path(out_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    strategy_map.to_csv(out_file, index=False)
