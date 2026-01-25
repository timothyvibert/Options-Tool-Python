import json

import pytest


def test_to_jsonable_dataframe_is_strict_json():
    pd = pytest.importorskip("pandas")
    pytest.importorskip("numpy")
    from frontend_dash.analysis_adapter import to_jsonable

    df = pd.DataFrame({"a": [float("nan"), float("inf"), -float("inf")]})
    payload = to_jsonable(df)
    json.dumps(payload, allow_nan=False)
    records = payload.get("records", [])
    assert records[0]["a"] is None
    assert records[1]["a"] is None
    assert records[2]["a"] is None


def test_cached_strategy_row_is_strict_json():
    pd = pytest.importorskip("pandas")
    from core.strategy_map import load_strategy_map
    from frontend_dash import app as dash_app

    strategy_map = load_strategy_map()
    strategy_id = int(strategy_map["strategy_id"].dropna().iloc[0])
    row = dash_app._cached_strategy_row(strategy_id)
    assert isinstance(row, dict)
    json.dumps(row, allow_nan=False)
