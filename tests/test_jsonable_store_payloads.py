import json

import pytest


def _assert_strict_json(payload: object) -> None:
    json.dumps(payload, allow_nan=False)


def test_to_jsonable_dataframe_is_strict_json():
    pd = pytest.importorskip("pandas")
    np = pytest.importorskip("numpy")
    from frontend_dash.analysis_adapter import to_jsonable

    df = pd.DataFrame(
        {
            "a": [1.0, np.nan, np.inf],
            "b": [pd.Timestamp("2025-01-02"), pd.NaT, "x"],
            "c": [np.int64(7), np.float64(2.5), None],
        }
    )
    payload = to_jsonable(df)
    _assert_strict_json(payload)
    records = payload.get("records", [])
    assert records[1]["a"] is None
    assert records[2]["a"] is None


def test_to_jsonable_series_is_strict_json():
    pd = pytest.importorskip("pandas")
    np = pytest.importorskip("numpy")
    from frontend_dash.analysis_adapter import to_jsonable

    series = pd.Series([np.nan, pd.Timestamp("2025-02-03"), np.int64(3)])
    payload = to_jsonable(series)
    _assert_strict_json(payload)


def test_analysis_pack_to_store_strict_json():
    pd = pytest.importorskip("pandas")
    np = pytest.importorskip("numpy")
    from frontend_dash.analysis_adapter import analysis_pack_to_store

    df = pd.DataFrame({"x": [np.nan, 1.0]})
    series = pd.Series([np.inf, 2.0])
    payload = analysis_pack_to_store({"df": df, "series": series})
    _assert_strict_json(payload)
