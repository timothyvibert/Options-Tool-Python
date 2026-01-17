from core.eligibility import determine_strategy_code, get_account_eligibility
from core.models import OptionLeg, StrategyInput
from core.roi import CASH_SECURED


def test_strategy_code_cash_secured_short_puts():
    strategy = StrategyInput(
        spot=100.0,
        legs=[OptionLeg(kind="put", position=-1, strike=90.0, premium=2.0)],
    )
    code = determine_strategy_code(strategy, CASH_SECURED)
    assert code == "CSPT"


def test_account_eligibility_lookup_non_empty():
    eligibility = get_account_eligibility("CCOV")
    assert not eligibility.empty
