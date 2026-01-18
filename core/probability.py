from __future__ import annotations

import math
from typing import Iterable, List, Optional

import pandas as pd
from scipy.stats import norm

from core.models import OptionLeg, StrategyInput


def norm_cdf(x: float) -> float:
    return float(norm.cdf(x))


def _norm_pdf(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def bs_d2(S: float, K: float, r: float, q: float, sigma: float, t: float) -> float:
    if t <= 0.0 or sigma <= 0.0 or S <= 0.0 or K <= 0.0:
        if S > K:
            return float("inf")
        if S < K:
            return float("-inf")
        return 0.0
    denom = sigma * math.sqrt(t)
    return (math.log(S / K) + (r - q - 0.5 * sigma * sigma) * t) / denom


def _bs_d1(S: float, K: float, r: float, q: float, sigma: float, t: float) -> Optional[float]:
    if t <= 0.0 or sigma <= 0.0 or S <= 0.0 or K <= 0.0:
        return None
    denom = sigma * math.sqrt(t)
    return (math.log(S / K) + (r - q + 0.5 * sigma * sigma) * t) / denom


def prob_finish_above(
    S: float, K_star: float, r: float, q: float, sigma: float, t: float
) -> float:
    d2 = bs_d2(S, K_star, r, q, sigma, t)
    return norm_cdf(d2)


def prob_finish_below(
    S: float, K_star: float, r: float, q: float, sigma: float, t: float
) -> float:
    return 1.0 - prob_finish_above(S, K_star, r, q, sigma, t)


def leg_pop_at_expiry(
    leg: OptionLeg, S: float, r: float, q: float, sigma: float, t: float
) -> float:
    if leg.kind.lower() == "call":
        threshold = leg.strike + leg.premium
        long_prob = prob_finish_above(S, threshold, r, q, sigma, t)
    else:
        threshold = leg.strike - leg.premium
        long_prob = prob_finish_below(S, threshold, r, q, sigma, t)
    if leg.position < 0:
        return 1.0 - long_prob
    return long_prob


def leg_itm_prob(
    leg: OptionLeg, S: float, r: float, q: float, sigma: float, t: float
) -> float:
    if leg.kind.lower() == "call":
        return prob_finish_above(S, leg.strike, r, q, sigma, t)
    return prob_finish_below(S, leg.strike, r, q, sigma, t)


def _bs_vega(S: float, K: float, r: float, q: float, sigma: float, t: float) -> float:
    d1 = _bs_d1(S, K, r, q, sigma, t)
    if d1 is None:
        return 0.0
    return S * math.exp(-q * t) * math.sqrt(t) * _norm_pdf(d1)


def _safe_sigma(value: Optional[float]) -> Optional[float]:
    if value is None:
        return None
    try:
        sigma = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(sigma):
        return None
    return sigma


def _fallback_atm(per_leg_iv: Iterable[Optional[float]]) -> Optional[float]:
    values = [v for v in (_safe_sigma(v) for v in per_leg_iv) if v is not None]
    if not values:
        return None
    return sum(values) / len(values)


def effective_sigma(
    input: StrategyInput,
    per_leg_iv: List[Optional[float]],
    mode: str,
    r: float,
    q: float,
    t: float,
    atm_iv: Optional[float] = None,
) -> float:
    mode_key = mode.upper()
    atm_value = _safe_sigma(atm_iv)
    if atm_value is None:
        atm_value = _fallback_atm(per_leg_iv)

    if mode_key == "ATM":
        if atm_value is None:
            raise ValueError("ATM volatility is required.")
        return max(atm_value, 1e-6)

    if mode_key == "VEGA_WEIGHTED":
        weights = []
        sigmas = []
        for leg, sigma in zip(input.legs, per_leg_iv):
            sigma_value = _safe_sigma(sigma)
            if sigma_value is None:
                continue
            if not isinstance(leg.strike, (int, float)):
                continue
            vega = _bs_vega(
                S=input.spot,
                K=float(leg.strike),
                r=r,
                q=q,
                sigma=sigma_value,
                t=t,
            )
            if vega <= 0.0:
                continue
            weight = vega * abs(leg.position) * leg.multiplier
            weights.append(weight)
            sigmas.append(sigma_value)
        if weights:
            total_weight = sum(weights)
            weighted_sigma = sum(w * s for w, s in zip(weights, sigmas)) / total_weight
            return max(weighted_sigma, 1e-6)
        if atm_value is None:
            raise ValueError("ATM volatility is required for fallback.")
        return max(atm_value, 1e-6)

    raise ValueError(f"Unknown sigma mode: {mode}")


def strategy_pop(
    input: StrategyInput,
    payoff_fn,
    S0: float,
    r: float,
    q: float,
    sigma_mode: str,
    atm_iv: float,
    per_leg_iv: List[Optional[float]],
    t: float,
    z_min: float = -5.0,
    z_max: float = 5.0,
    steps: int = 400,
) -> float:
    sigma = effective_sigma(
        input, per_leg_iv, sigma_mode, r, q, t, atm_iv=atm_iv
    )
    if t <= 0.0 or sigma <= 0.0:
        pnl = payoff_fn(input, S0)
        return 1.0 if pnl > 0.0 else 0.0

    step = (z_max - z_min) / (steps - 1)
    total_prob = 0.0
    positive_prob = 0.0
    drift = (r - q - 0.5 * sigma * sigma) * t
    vol_term = sigma * math.sqrt(t)

    for i in range(steps):
        z = z_min + step * i
        prob = _norm_pdf(z) * step
        terminal = S0 * math.exp(drift + vol_term * z)
        pnl = payoff_fn(input, terminal)
        total_prob += prob
        if pnl > 0.0:
            positive_prob += prob

    if total_prob <= 0.0:
        return 0.0
    return max(0.0, min(1.0, positive_prob / total_prob))


def build_probability_details(
    S0: float,
    r: float,
    q: float,
    sigma: float,
    t: float,
    breakevens: List[float],
    z_min: float = -5.0,
    z_max: float = 5.0,
    steps: int = 200,
) -> pd.DataFrame:
    if t <= 0.0 or sigma <= 0.0:
        df = pd.DataFrame(
            {"terminal_price": [S0], "cum_prob": [1.0], "breakeven": [False]}
        )
        return df

    step = (z_max - z_min) / (steps - 1)
    drift = (r - q - 0.5 * sigma * sigma) * t
    vol_term = sigma * math.sqrt(t)

    rows = []
    cum_prob = 0.0
    for i in range(steps):
        z = z_min + step * i
        prob = _norm_pdf(z) * step
        terminal = S0 * math.exp(drift + vol_term * z)
        cum_prob += prob
        rows.append({"terminal_price": terminal, "cum_prob": cum_prob})

    df = pd.DataFrame(rows)
    df["breakeven"] = False
    if breakevens:
        prices = df["terminal_price"].to_numpy()
        for breakeven in breakevens:
            idx = (abs(prices - breakeven)).argmin()
            df.at[idx, "breakeven"] = True
    return df
