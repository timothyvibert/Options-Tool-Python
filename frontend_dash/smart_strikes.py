from __future__ import annotations

import math


def get_smart_strike_interval(price: float) -> float:
    if price <= 0:
        return 1.0
    log_price = round(math.log10(price), 0)
    multiplier = 10 ** (log_price - 1)
    div_log = price / (10 ** log_price)
    if div_log >= 12:
        base_interval = 10
    elif div_log >= 6:
        base_interval = 5
    elif div_log >= 3:
        base_interval = 2.5
    elif div_log >= 1.2:
        base_interval = 1
    elif div_log >= 0.65:
        base_interval = 0.5
    else:
        base_interval = 0.25
    raw_interval = base_interval * multiplier
    # Institutional equity strike grid clamp layered on top of Excel heuristic.
    allowed_steps = [0.25, 0.5, 1.0, 2.5, 5.0, 10.0, 25.0]
    if price < 500:
        max_interval = 5.0
    elif price < 1000:
        max_interval = 10.0
    else:
        max_interval = 25.0
    capped = min(raw_interval, max_interval)
    chosen = None
    for step in allowed_steps:
        if step <= capped:
            chosen = step
    if chosen is None:
        chosen = allowed_steps[0]
    return float(chosen)


def get_strike_offset(descriptor: str) -> float:
    if not descriptor:
        return 0.0
    key = str(descriptor).strip().lower()
    mapping = {
        "lowest": -3,
        "low": -2,
        "lower": -1,
        "low-mid": -1,
        "mid": 0,
        "atm": 0,
        "high-mid": 1,
        "higher": 1,
        "high": 2,
        "highest": 3,
    }
    return float(mapping.get(key, 0))


def compute_default_strike(spot: float, descriptor: str) -> float:
    interval = get_smart_strike_interval(spot)
    atm = round(spot / interval) * interval
    strike = atm + get_strike_offset(descriptor) * interval
    # Keep fractional intervals precise while rounding whole-step strikes cleanly.
    if interval in {0.25, 0.5, 2.5}:
        return float(round(strike, 2))
    return float(round(strike, 0))


def is_number_like(value: object) -> bool:
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False
