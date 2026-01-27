import pytest

from frontend_dash import app_vnext as dash_app


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


def test_vnext_validation_layout_contains_pages():
    if not getattr(dash_app, "DASH_AVAILABLE", False):
        pytest.skip("Dash not available")
    layout = getattr(dash_app.app, "validation_layout", None)
    assert layout is not None, "validation_layout is required for vNext"
    ids: set[str] = set()
    _collect_ids(layout, ids)
    assert "cp-expiry" in ids
    assert "bbg-mode" in ids
