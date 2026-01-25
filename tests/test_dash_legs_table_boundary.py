import pytest

from frontend_dash import app as dash_app


def _parse_outputs(out_key: str) -> list[str]:
    if out_key.startswith("..") and out_key.endswith(".."):
        inner = out_key[2:-2]
        return inner.split("...") if inner else []
    return [out_key]


def _find_callback_metas_for_output(callback_map: dict, target: str) -> list[dict]:
    metas = []
    for out_key, meta in callback_map.items():
        if target in _parse_outputs(out_key):
            metas.append(meta)
    return metas


def _inputs_set(meta: dict) -> set[str]:
    return {
        f"{item.get('id')}.{item.get('property')}"
        for item in meta.get("inputs", [])
    }


def test_store_analysis_pack_updates_only_on_run():
    if not getattr(dash_app, "DASH_AVAILABLE", False):
        pytest.skip("Dash not available")
    app = dash_app.app
    metas = _find_callback_metas_for_output(app.callback_map, "store-analysis-pack.data")
    assert len(metas) == 1, "Expected exactly one callback for store-analysis-pack.data"
    assert _inputs_set(metas[0]) == {"run-analysis-button.n_clicks"}


def test_store_inputs_updates_only_on_run():
    if not getattr(dash_app, "DASH_AVAILABLE", False):
        pytest.skip("Dash not available")
    app = dash_app.app
    metas = _find_callback_metas_for_output(app.callback_map, "store-inputs.data")
    assert len(metas) == 1, "Expected exactly one callback for store-inputs.data"
    assert _inputs_set(metas[0]) == {"run-analysis-button.n_clicks"}


def test_store_market_updates_only_on_refresh():
    if not getattr(dash_app, "DASH_AVAILABLE", False):
        pytest.skip("Dash not available")
    app = dash_app.app
    metas = _find_callback_metas_for_output(app.callback_map, "store-market.data")
    assert len(metas) == 1, "Expected exactly one callback for store-market.data"
    assert _inputs_set(metas[0]) == {"refresh-button.n_clicks"}


def test_store_ref_updates_only_on_ticker_commit():
    if not getattr(dash_app, "DASH_AVAILABLE", False):
        pytest.skip("Dash not available")
    app = dash_app.app
    metas = _find_callback_metas_for_output(app.callback_map, "store-ref.data")
    assert len(metas) == 1, "Expected exactly one callback for store-ref.data"
    assert _inputs_set(metas[0]) == {
        "ticker-input.n_submit",
        "ticker-input.n_blur",
    }
