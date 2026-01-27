from pathlib import Path

import pytest

from frontend_dash import app_vnext as dash_app


def _find_component_by_id(node, target_id):
    if node is None:
        return None
    if isinstance(node, (list, tuple)):
        for child in node:
            found = _find_component_by_id(child, target_id)
            if found is not None:
                return found
        return None
    if getattr(node, "id", None) == target_id:
        return node
    children = getattr(node, "children", None)
    if children is not None:
        return _find_component_by_id(children, target_id)
    return None


def test_vnext_roi_policy_dropdown_options():
    if not getattr(dash_app, "DASH_AVAILABLE", False):
        pytest.skip("Dash not available")
    layout = getattr(dash_app.app, "validation_layout", None) or dash_app.app.layout
    if callable(layout):
        layout = layout()
    dropdown = _find_component_by_id(layout, "cp-roi-policy")
    assert dropdown is not None, "cp-roi-policy not found in layout"
    options = getattr(dropdown, "options", [])
    values = {opt.get("value") for opt in options if isinstance(opt, dict)}
    assert values == {"premium", "max_loss", "cash_secured", "margin"}


def test_vnext_roi_policy_mapping_strings_present():
    text = Path("frontend_dash/app_vnext.py").read_text(encoding="utf-8")
    for token in ["NET_PREMIUM", "RISK_MAX_LOSS", "CASH_SECURED", "MARGIN_PROXY"]:
        assert token in text
