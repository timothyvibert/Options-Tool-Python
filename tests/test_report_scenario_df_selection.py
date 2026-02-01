import pandas as pd

from reporting.report_model import _pick_first_df


def test_pick_first_df_prefers_non_empty_top10():
    top10 = pd.DataFrame([{"price": 100.0}])
    full = pd.DataFrame([{"price": 90.0}])
    selected = _pick_first_df(top10, full)
    assert selected is top10


def test_pick_first_df_falls_back_to_full_df():
    top10 = pd.DataFrame([])
    full = pd.DataFrame([{"price": 90.0}])
    selected = _pick_first_df(top10, full)
    assert selected is full
