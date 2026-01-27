from frontend_dash import app_vnext as dash_app


def test_vnext_key_levels_sort_order():
    levels = [
        {"label": "Stock to Infinity", "price": None, "source": "sentinel", "id": "infinity"},
        {"label": "Downside", "price": 80.0, "source": "downside"},
        {"label": "Breakeven 1", "price": 95.0, "source": "breakeven"},
        {"label": "Spot", "price": 100.0, "source": "spot"},
        {"label": "Strike Low", "price": 90.0, "source": "strike"},
        {"label": "Strike High", "price": 110.0, "source": "strike"},
        {"label": "Upside", "price": 120.0, "source": "upside"},
        {"label": "Strike Tie", "price": 100.0, "source": "strike"},
    ]
    sorted_levels = dash_app._sort_key_levels(levels)
    labels = [lvl.get("label") for lvl in sorted_levels]
    assert labels == [
        "Downside",
        "Strike Low",
        "Breakeven 1",
        "Spot",
        "Strike Tie",
        "Strike High",
        "Upside",
        "Stock to Infinity",
    ]
