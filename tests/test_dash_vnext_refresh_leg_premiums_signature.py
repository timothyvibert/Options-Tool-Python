from pathlib import Path


def test_vnext_refresh_leg_premiums_keywords():
    text = Path("frontend_dash/app_vnext.py").read_text(encoding="utf-8")
    assert "refresh_leg_premiums(" in text
    for kw in [
        "raw_underlying=",
        "resolved_underlying=",
        "expiry=",
        "legs_rows=",
        "pricing_mode=",
    ]:
        assert kw in text
