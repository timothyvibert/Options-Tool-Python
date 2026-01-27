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


def test_vnext_dashboard_ids_exist():
    if not getattr(dash_app, "DASH_AVAILABLE", False):
        pytest.skip("Dash not available")
    layout = getattr(dash_app.app, "validation_layout", None) or dash_app.app.layout
    if callable(layout):
        layout = layout()
    ids: set[str] = set()
    _collect_ids(layout, ids)
    for target in (
        "vnext-tabs",
        "vnext-page",
        "panel-payoff-metrics",
        "panel-margin-capital",
        "panel-dividend",
        "legs-table",
        "payoff-chart",
    ):
        assert target in ids, f"Missing layout id: {target}"
