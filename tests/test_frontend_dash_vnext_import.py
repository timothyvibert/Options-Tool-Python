def test_frontend_dash_vnext_app_import():
    from frontend_dash import app_vnext as dash_vnext

    assert hasattr(dash_vnext, "app")
