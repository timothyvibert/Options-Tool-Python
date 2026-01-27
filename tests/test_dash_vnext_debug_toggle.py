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


def test_vnext_debug_toggle_ids():
    if not getattr(dash_app, "DASH_AVAILABLE", False):
        pytest.skip("Dash not available")
    bloomberg = dash_app.layout_bloomberg()
    ids: set[str] = set()
    _collect_ids(bloomberg, ids)
    for target in (
        "debug-mode-toggle",
        "debug-container",
        "bbg-mode",
        "ref-debug",
        "market-debug",
        "refresh-debug",
        "analysis-key-debug",
        "analysis-pack-debug",
        "analysis-render-debug",
    ):
        assert target in ids, f"Missing bloomberg id: {target}"

    dashboard = dash_app.layout_dashboard()
    dash_ids: set[str] = set()
    _collect_ids(dashboard, dash_ids)
    for target in (
        "bbg-mode",
        "ref-debug",
        "market-debug",
        "refresh-debug",
        "analysis-key-debug",
        "analysis-pack-debug",
        "analysis-render-debug",
    ):
        assert target not in dash_ids, f"Debug id present on dashboard: {target}"
