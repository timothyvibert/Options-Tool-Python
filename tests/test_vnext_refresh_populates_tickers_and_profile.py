import pytest

from frontend_dash import analysis_adapter as adapter


def test_refresh_populates_tickers_and_profile(monkeypatch):
    try:
        import adapters.bloomberg as bbg
    except Exception as exc:  # pragma: no cover - repo should have adapters
        pytest.skip(f"Bloomberg adapter unavailable: {exc}")

    def _resolve_security(raw):
        return "TEST US Equity"

    def _resolve_option_ticker(base, expiry, put_call, strike):
        return f"{base} {expiry} {put_call} {strike:.1f}"

    def _fetch_option_snapshot(tickers):
        return {
            ticker: {
                "BID": 1.0,
                "ASK": 3.0,
                "PX_MID": 2.0,
                "PX_LAST": 2.5,
                "IVOL_MID": 0.2,
            }
            for ticker in tickers
        }

    def _fetch_spot(resolved):
        return {"spot": 123.45}

    def _fetch_underlying_snapshot(resolved):
        return {"name": "Test Co"}

    monkeypatch.setattr(bbg, "resolve_security", _resolve_security, raising=False)
    monkeypatch.setattr(
        bbg, "resolve_option_ticker_from_strike", _resolve_option_ticker, raising=False
    )
    monkeypatch.setattr(
        bbg, "fetch_option_snapshot", _fetch_option_snapshot, raising=False
    )
    monkeypatch.setattr(bbg, "fetch_spot", _fetch_spot, raising=False)
    monkeypatch.setattr(
        bbg, "fetch_underlying_snapshot", _fetch_underlying_snapshot, raising=False
    )

    legs = [
        {"kind": "call", "strike": 100.0, "side": "Long", "qty": 1, "premium": 0.0},
        {"kind": "put", "strike": 90.0, "side": "Short", "qty": 1, "premium": 0.0},
        {"kind": "", "strike": None},
        {"kind": "call"},
    ]

    updated_rows, market_snapshot, _ = adapter.refresh_leg_premiums(
        raw_underlying="TEST",
        resolved_underlying=None,
        expiry="2026-01-01",
        legs_rows=legs,
        pricing_mode="mid",
    )

    assert isinstance(updated_rows, list)
    assert updated_rows[0].get("option_ticker")
    assert updated_rows[1].get("option_ticker")
    assert updated_rows[2].get("option_ticker") is None
    assert updated_rows[3].get("option_ticker") is None

    assert market_snapshot.get("market_spot") == 123.45
    assert market_snapshot.get("underlying_profile") == {"name": "Test Co"}
    assert market_snapshot.get("leg_tickers") == [
        updated_rows[0].get("option_ticker"),
        updated_rows[1].get("option_ticker"),
        None,
        None,
    ]
    assert market_snapshot.get("errors") == []
