from pathlib import Path
from typing import Tuple

import pandas as pd


def _load_account_map() -> Tuple[Path, pd.DataFrame]:
    repo_root = Path(__file__).resolve().parents[1]
    csv_path = repo_root / "data" / "account_map.csv"
    return csv_path, pd.read_csv(csv_path)


def test_account_map_file_exists():
    csv_path, _ = _load_account_map()
    assert csv_path.exists()


def test_account_map_row_per_strategy_code():
    _, account_map = _load_account_map()
    counts = account_map.groupby("strategy_code").size()
    assert len(counts) >= 1
    assert (counts >= 1).all()


def test_account_map_required_fields():
    _, account_map = _load_account_map()
    required_cols = ["strategy_code", "account_type", "eligibility"]
    for col in required_cols:
        assert col in account_map.columns
        assert account_map[col].notna().all()
        assert (account_map[col].astype(str).str.strip() != "").all()
