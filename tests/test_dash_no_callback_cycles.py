import pytest

from frontend_dash import app as dash_app


def _parse_outputs(out_key: str) -> list[str]:
    if out_key.startswith("..") and out_key.endswith(".."):
        inner = out_key[2:-2]
        return inner.split("...") if inner else []
    return [out_key]


def test_no_callback_cycles():
    if not getattr(dash_app, "DASH_AVAILABLE", False):
        pytest.skip("Dash not available")
    app = dash_app.app
    if not hasattr(app, "callback_map"):
        pytest.skip("Dash app has no callback map")
    graph: dict[str, list[str]] = {}
    for out_key, meta in app.callback_map.items():
        outputs = _parse_outputs(out_key)
        for o in outputs:
            for inp in meta.get("inputs", []):
                src = f"{inp['id']}.{inp['property']}"
                graph.setdefault(src, []).append(o)
    visited: dict[str, int] = {}
    stack: list[str] = []
    cycle: list[str] = []

    def dfs(node: str) -> bool:
        visited[node] = 1
        stack.append(node)
        for nxt in graph.get(node, []):
            state = visited.get(nxt, 0)
            if state == 0 and dfs(nxt):
                return True
            if state == 1:
                idx = stack.index(nxt)
                cycle.extend(stack[idx:] + [nxt])
                return True
        stack.pop()
        visited[node] = 2
        return False

    for node in list(graph):
        if visited.get(node, 0) == 0 and dfs(node):
            break
    assert not cycle, f"Callback cycle detected: {' -> '.join(cycle)}"
