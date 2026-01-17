from __future__ import annotations

from typing import Optional, Union


MID = "MID"
DEALABLE = "DEALABLE"


def _avg(bid: Optional[float], ask: Optional[float]) -> Optional[float]:
    if bid is None or ask is None:
        return None
    return (bid + ask) / 2.0


def select_price(
    pos: Union[int, float],
    bid: Optional[float],
    mid: Optional[float],
    ask: Optional[float],
    mode: str,
) -> Optional[float]:
    mode_key = mode.upper()
    if mode_key == MID:
        if mid is not None:
            return mid
        avg_price = _avg(bid, ask)
        if avg_price is not None:
            return avg_price
        if bid is not None:
            return bid
        if ask is not None:
            return ask
        return None

    if mode_key == DEALABLE:
        if pos > 0:
            if ask is not None:
                return ask
            if mid is not None:
                return mid
            avg_price = _avg(bid, ask)
            if avg_price is not None:
                return avg_price
            if bid is not None:
                return bid
            return ask
        if pos < 0:
            if bid is not None:
                return bid
            if mid is not None:
                return mid
            avg_price = _avg(bid, ask)
            if avg_price is not None:
                return avg_price
            if ask is not None:
                return ask
            return bid
        return select_price(pos, bid, mid, ask, MID)

    raise ValueError(f"Unknown pricing mode: {mode}")
