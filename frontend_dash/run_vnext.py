"""Canonical Dash vNext entrypoint.

Run:
  python -m frontend_dash.run_vnext

Routes:
  /     — current vnext dashboard
  /v2   — DMC v2 dashboard shell (visual skeleton)
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
    from dash import Dash, html, dcc, Input, Output
    DASH_AVAILABLE = True
except ModuleNotFoundError:
    DASH_AVAILABLE = False
    Dash = None
    html = None
    dcc = None

from frontend_dash.vnext.callbacks import register_callbacks
from frontend_dash.vnext.layout import (
    layout_control_plane_stores,
    layout_shell,
)

# DMC v2 layout + callbacks (optional — gracefully degrades if unavailable)
try:
    from frontend_dash.vnext2.layout import layout_v2 as _layout_v2_fn
    from frontend_dash.vnext2.callbacks import register_v2_callbacks
    _V2_AVAILABLE = True
except Exception:
    _layout_v2_fn = None
    register_v2_callbacks = None
    _V2_AVAILABLE = False


class _DashStub:
    def __init__(self) -> None:
        self.layout = None
        self.validation_layout = None

    def callback(self, *args, **kwargs):
        def _wrapper(func):
            return func

        return _wrapper

    def run(self, *args, **kwargs) -> None:
        raise RuntimeError("Dash is not installed. Install 'dash' to run the app.")


app = Dash(__name__, suppress_callback_exceptions=True) if DASH_AVAILABLE else _DashStub()


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
    _vnext_shell = layout_shell(bloomberg_available=BLOOMBERG_AVAILABLE)

    # ── Layout: dcc.Location for client-side routing ─────────────────────
    # Stores live outside _page-content so they persist across route changes.
    # The routing callback swaps _page-content children based on URL path.
    app.layout = html.Div(
        children=[
            dcc.Location(id="_url", refresh=False),
            layout_control_plane_stores(),
            html.Div(id="_page-content"),
        ]
    )

    @app.callback(
        Output("_page-content", "children"),
        Input("_url", "pathname"),
    )
    def _route_page(pathname):
        if _V2_AVAILABLE and pathname and pathname.startswith("/v2"):
            return _layout_v2_fn()
        return _vnext_shell

    register_callbacks(
        app,
        _cache_get,
        _cache_put,
        BLOOMBERG_AVAILABLE,
        _bbg_resolve_security,
        _bbg_fetch_spot,
    )

    # ── v2 callbacks ─────────────────────────────────────────────────────
    if _V2_AVAILABLE and register_v2_callbacks is not None:
        register_v2_callbacks(
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
    app.run(debug=True, port=8051)
