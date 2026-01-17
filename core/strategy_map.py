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


def list_strategies(group: str, subgroup: str) -> pd.DataFrame:
    strategy_map = load_strategy_map()
    group_key = group.strip().casefold()
    subgroup_key = subgroup.strip().casefold()
    mask = (_casefold_series(strategy_map["group"]) == group_key) & (
        _casefold_series(strategy_map["subgroup"]) == subgroup_key
    )
    return strategy_map.loc[mask].copy()


def get_strategy(strategy_id: int) -> pd.DataFrame:
    strategy_map = load_strategy_map()
    return strategy_map.loc[strategy_map["strategy_id"] == int(strategy_id)].copy()
