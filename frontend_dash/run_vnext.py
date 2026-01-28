"""Canonical Dash vNext entrypoint.

Run:
  python -m frontend_dash.run_vnext
"""

from __future__ import annotations

from time import time
import uuid

try:
    from adapters.bloomberg import resolve_security as _bbg_resolve_security
    from adapters.bloomberg import fetch_spot as _bbg_fetch_spot
    BLOOMBERG_AVAILABLE = True
except Exception:
    _bbg_resolve_security = None
    _bbg_fetch_spot = None
    BLOOMBERG_AVAILABLE = False

try:
    from dash import Dash, html
    DASH_AVAILABLE = True
except ModuleNotFoundError:
    DASH_AVAILABLE = False
    Dash = None
    html = None

from frontend_dash.vnext.callbacks import register_callbacks
from frontend_dash.vnext.layout import (
    get_validation_layout,
    layout_control_plane_stores,
    layout_shell,
)


class _DashStub:
    def __init__(self) -> None:
        self.layout = None
        self.validation_layout = None

    def callback(self, *args, **kwargs):
        def _wrapper(func):
            return func

        return _wrapper

    def run_server(self, *args, **kwargs) -> None:
        raise RuntimeError("Dash is not installed. Install 'dash' to run the app.")


app = Dash(__name__) if DASH_AVAILABLE else _DashStub()


_ANALYSIS_CACHE: dict[str, dict] = {}
_ANALYSIS_CACHE_TS: dict[str, float] = {}
MAX_CACHE_ENTRIES = 20
CACHE_TTL_SECONDS = 1800


def _cache_prune() -> None:
    now = time()
    expired = [
        key
        for key, ts in _ANALYSIS_CACHE_TS.items()
        if now - ts > CACHE_TTL_SECONDS
    ]
    for key in expired:
        _ANALYSIS_CACHE.pop(key, None)
        _ANALYSIS_CACHE_TS.pop(key, None)
    if len(_ANALYSIS_CACHE_TS) > MAX_CACHE_ENTRIES:
        ordered = sorted(_ANALYSIS_CACHE_TS.items(), key=lambda item: item[1])
        for key, _ in ordered[: len(ordered) - MAX_CACHE_ENTRIES]:
            _ANALYSIS_CACHE.pop(key, None)
            _ANALYSIS_CACHE_TS.pop(key, None)


def _cache_put(pack: dict) -> str:
    _cache_prune()
    key = uuid.uuid4().hex
    _ANALYSIS_CACHE[key] = pack
    _ANALYSIS_CACHE_TS[key] = time()
    _cache_prune()
    return key


def _cache_get(key: str | None) -> dict | None:
    if not key:
        return None
    _cache_prune()
    return _ANALYSIS_CACHE.get(key)


if DASH_AVAILABLE:
    _base_layout = html.Div(
        children=[
            layout_control_plane_stores(),
            layout_shell(bloomberg_available=BLOOMBERG_AVAILABLE),
        ]
    )
    app.layout = _base_layout
    app.validation_layout = get_validation_layout(
        base_layout=_base_layout,
        bloomberg_available=BLOOMBERG_AVAILABLE,
    )
    register_callbacks(
        app,
        _cache_get,
        _cache_put,
        BLOOMBERG_AVAILABLE,
        _bbg_resolve_security,
        _bbg_fetch_spot,
    )
else:
    app.layout = None


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
