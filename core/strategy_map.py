from __future__ import annotations

from pathlib import Path
from typing import List, Optional

import pandas as pd


_STRATEGY_MAP: Optional[pd.DataFrame] = None


def _strategy_map_path() -> Path:
    return Path(__file__).resolve().parents[1] / "data" / "strategy_map.csv"


def load_strategy_map() -> pd.DataFrame:
    global _STRATEGY_MAP
    if _STRATEGY_MAP is None:
        _STRATEGY_MAP = pd.read_csv(_strategy_map_path())
    return _STRATEGY_MAP


def _casefold_series(series: pd.Series) -> pd.Series:
    return series.fillna("").astype(str).str.strip().str.casefold()


def list_groups() -> List[str]:
    strategy_map = load_strategy_map()
    groups = strategy_map["group"].dropna()
    return groups.drop_duplicates().tolist()


def list_subgroups(group: str) -> List[str]:
    strategy_map = load_strategy_map()
    group_key = group.strip().casefold()
    mask = _casefold_series(strategy_map["group"]) == group_key
    subgroups = strategy_map.loc[mask, "subgroup"].dropna()
    return subgroups.drop_duplicates().tolist()


def list_strategies(group: str, subgroup: Optional[str] = None) -> pd.DataFrame:
    strategy_map = load_strategy_map()
    group_key = group.strip().casefold()
    mask = _casefold_series(strategy_map["group"]) == group_key
    if subgroup is not None:
        subgroup_key = subgroup.strip().casefold()
        mask = mask & (_casefold_series(strategy_map["subgroup"]) == subgroup_key)
    return strategy_map.loc[mask].copy()


def get_strategy(strategy_id: int) -> pd.DataFrame:
    strategy_map = load_strategy_map()
    return strategy_map.loc[strategy_map["strategy_id"] == int(strategy_id)].copy()


def get_strategy_description(strategy_name: str) -> Optional[str]:
    strategy_map = load_strategy_map()
    if "description" not in strategy_map.columns:
        return None
    mask = _casefold_series(strategy_map["strategy_name"]) == strategy_name.strip().casefold()
    matches = strategy_map.loc[mask, "description"]
    if matches.empty:
        return None
    value = matches.iloc[0]
    if pd.isna(value):
        return None
    text = str(value).strip()
    return text if text else None
