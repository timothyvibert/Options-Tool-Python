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


def _find_component(node, target_id: str):
    if node is None:
        return None
    if isinstance(node, (list, tuple)):
        for child in node:
            found = _find_component(child, target_id)
            if found is not None:
                return found
        return None
    if getattr(node, "id", None) == target_id:
        return node
    children = getattr(node, "children", None)
    if children is not None:
        return _find_component(children, target_id)
    return None


def test_vnext_tab_routing_and_keylevels():
    if not getattr(dash_app, "DASH_AVAILABLE", False):
        pytest.skip("Dash not available")
    layout = getattr(dash_app.app, "validation_layout", None) or dash_app.app.layout
    if callable(layout):
        layout = layout()
    ids: set[str] = set()
    _collect_ids(layout, ids)
    assert "vnext-tabs" in ids
    assert "vnext-page" in ids
    assert "panel-scenario-table" not in ids

    scenario_mode = _find_component(layout, "cp-scenario-mode")
    assert scenario_mode is not None, "cp-scenario-mode not found in layout"
    options = getattr(scenario_mode, "options", None) or []
    values = {opt.get("value") for opt in options if isinstance(opt, dict)}
    assert values == {"targets", "infinity"}
