from core.models import OptionLeg, StrategyInput
from core.probability import build_probability_details, effective_sigma


def test_vol_mode_affects_sigma_choice():
    strategy = StrategyInput(
        spot=100.0,
        legs=[
            OptionLeg(kind="call", position=1, strike=90.0, premium=2.0),
            OptionLeg(kind="put", position=1, strike=110.0, premium=2.0),
        ],
    )
    per_leg_iv = [0.1, 0.2]
    atm_iv = 0.5
    sigma_atm = effective_sigma(
        strategy,
        per_leg_iv=per_leg_iv,
        mode="ATM",
        r=0.0,
        q=0.0,
        t=0.5,
        atm_iv=atm_iv,
    )
    sigma_vega = effective_sigma(
        strategy,
        per_leg_iv=per_leg_iv,
        mode="VEGA_WEIGHTED",
        r=0.0,
        q=0.0,
        t=0.5,
        atm_iv=atm_iv,
    )
    assert sigma_atm == atm_iv
    assert sigma_vega < atm_iv


def test_probability_details_structure():
    details = build_probability_details(
        S0=100.0,
        r=0.0,
        q=0.0,
        sigma=0.2,
        t=1.0,
        breakevens=[100.0, 110.0],
    )
    assert {"terminal_price", "cum_prob", "breakeven"}.issubset(details.columns)
    assert not details.empty
    assert details["breakeven"].any()
