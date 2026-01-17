from pathlib import Path

import pandas as pd


def _load_strategy_map() -> pd.DataFrame:
    repo_root = Path(__file__).resolve().parents[1]
    csv_path = repo_root / "data" / "strategy_map.csv"
    return pd.read_csv(csv_path)


def test_strategy_map_count():
    strategy_map = _load_strategy_map()
    assert len(strategy_map) == 63


def test_strategy_map_leg_ratios_are_ints():
    strategy_map = _load_strategy_map()
    ratio_cols = [f"leg_{i}_ratio" for i in range(1, 5)]
    for ratio_col in ratio_cols:
        ratios = pd.to_numeric(strategy_map[ratio_col], errors="coerce").dropna()
        assert (ratios == ratios.astype(int)).all()


def test_strategy_map_leg_types_are_clean():
    strategy_map = _load_strategy_map()
    leg_cols = [f"leg_{i}_type" for i in range(1, 5)]
    leg_values = [
        str(value).upper()
        for value in strategy_map[leg_cols].to_numpy().ravel()
        if pd.notna(value)
    ]
    assert "CUSTOM" not in leg_values


def test_strategy_map_template_kind_values():
    strategy_map = _load_strategy_map()
    assert "template_kind" in strategy_map.columns
    kinds = set(strategy_map["template_kind"].dropna().unique().tolist())
    assert kinds.issubset({"OPTIONS", "STOCK_ONLY", "MIXED"})


def test_strategy_map_options_have_call_put():
    strategy_map = _load_strategy_map()
    leg_cols = [f"leg_{i}_type" for i in range(1, 5)]
    call_put = strategy_map[leg_cols].isin(["CALL", "PUT"]).any(axis=1)
    options_mask = strategy_map["template_kind"] == "OPTIONS"
    assert call_put[options_mask].all()
