def test_frontend_dash_app_import():
    from frontend_dash import app as dash_app

    assert hasattr(dash_app, "app")
