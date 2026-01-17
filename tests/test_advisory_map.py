from pathlib import Path
from typing import Tuple

import pandas as pd


def _load_advisory_map() -> Tuple[Path, pd.DataFrame]:
    repo_root = Path(__file__).resolve().parents[1]
    csv_path = repo_root / "data" / "scenario_advisory_map.csv"
    return csv_path, pd.read_csv(csv_path)


def test_advisory_map_file_exists():
    csv_path, _ = _load_advisory_map()
    assert csv_path.exists()


def test_advisory_map_row_count():
    _, advisory_map = _load_advisory_map()
    assert len(advisory_map) >= 50


def test_advisory_map_required_fields():
    _, advisory_map = _load_advisory_map()
    required_cols = ["archetype", "scenario_key", "template"]
    for col in required_cols:
        assert col in advisory_map.columns
        assert advisory_map[col].notna().all()
        assert (advisory_map[col].astype(str).str.strip() != "").all()


def test_advisory_map_template_length():
    _, advisory_map = _load_advisory_map()
    template_lengths = advisory_map["template"].astype(str).str.len()
    assert (template_lengths > 10).all()
