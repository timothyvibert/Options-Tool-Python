from core.pricing import DEALABLE, MID, select_price


def test_dealable_long_uses_ask():
    price = select_price(1, bid=1.0, mid=1.5, ask=2.0, mode=DEALABLE)
    assert price == 2.0


def test_dealable_short_uses_bid():
    price = select_price(-1, bid=1.0, mid=1.5, ask=2.0, mode=DEALABLE)
    assert price == 1.0


def test_mid_prefers_mid():
    price = select_price(1, bid=1.0, mid=1.5, ask=2.0, mode=MID)
    assert price == 1.5


def test_fallbacks_when_values_missing():
    price = select_price(1, bid=1.2, mid=None, ask=None, mode=DEALABLE)
    assert price == 1.2
    price = select_price(1, bid=1.0, mid=None, ask=3.0, mode=MID)
    assert price == 2.0
