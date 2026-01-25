import pytest

from frontend_dash import app as dash_app


def _parse_outputs(out_key: str) -> list[str]:
    if out_key.startswith("..") and out_key.endswith(".."):
        inner = out_key[2:-2]
        return inner.split("...") if inner else []
    return [out_key]


def _collect_ids(node, ids: set[str]) -> None:
    if node is None:
        return
    if isinstance(node, (list, tuple)):
        for child in node:
            _collect_ids(child, ids)
        return
    comp_id = getattr(node, "id", None)
    if comp_id is not None:
        ids.add(str(comp_id))
    children = getattr(node, "children", None)
    if children is not None:
        _collect_ids(children, ids)


def test_callback_output_ids_exist():
    if not getattr(dash_app, "DASH_AVAILABLE", False):
        pytest.skip("Dash not available")
    app = dash_app.app
    if not hasattr(app, "callback_map"):
        pytest.skip("Dash app has no callback map")
    layout = getattr(app, "validation_layout", None) or app.layout
    if callable(layout):
        layout = layout()
    ids: set[str] = set()
    _collect_ids(layout, ids)
    missing = []
    for out_key in app.callback_map:
        for output in _parse_outputs(out_key):
            comp_id = output.rsplit(".", 1)[0]
            if comp_id not in ids:
                missing.append(comp_id)
    assert not missing, f"Missing output IDs in layout: {sorted(set(missing))}"
