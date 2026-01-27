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


def test_vnext_no_missing_state_ids():
    if not getattr(dash_app, "DASH_AVAILABLE", False):
        pytest.skip("Dash not available")
    layout = getattr(dash_app.app, "validation_layout", None) or dash_app.app.layout
    if callable(layout):
        layout = layout()
    ids: set[str] = set()
    _collect_ids(layout, ids)

    for meta in dash_app.app.callback_map.values():
        for item in meta.get("inputs", []):
            cid = item.get("id")
            if cid is not None:
                assert str(cid) in ids, f"Missing input id in layout: {cid}"
        for item in meta.get("state", []):
            cid = item.get("id")
            if cid is not None:
                assert str(cid) in ids, f"Missing state id in layout: {cid}"
        out = meta.get("output")
        if isinstance(out, str):
            out_id = out.split(".", 1)[0]
            assert out_id in ids, f"Missing output id in layout: {out_id}"
