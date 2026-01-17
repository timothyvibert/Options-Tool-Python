import pandas as pd

from core.advisory import load_advisory_templates, select_template
from core.models import OptionLeg, StrategyInput
from core.payoff import compute_payoff
from core.roi import NET_PREMIUM
from core.scenarios import compute_scenario_table


def test_advisory_templates_load():
    templates = load_advisory_templates()
    assert not templates.empty
    assert {"archetype", "scenario_key", "template"}.issubset(templates.columns)


def test_template_selection_fallback():
    templates = pd.DataFrame(
        [
            {
                "archetype": "GENERIC",
                "scenario_key": "BETWEEN_BOUNDS",
                "template": "generic-between",
            }
        ]
    )
    template = select_template("MISSING", "ABOVE_UPPER_BOUND", templates)
    assert template == "generic-between"


def test_commentary_varies_for_covered_call():
    strategy = StrategyInput(
        spot=100.0,
        stock_position=100.0,
        avg_cost=100.0,
        legs=[OptionLeg(kind="call", position=-1, strike=110.0, premium=2.0)],
    )
    payoff = compute_payoff(strategy)
    points = [90.0, 120.0]
    table = compute_scenario_table(
        strategy,
        points,
        payoff_result=payoff,
        roi_policy=NET_PREMIUM,
    )
    commentary = table["commentary"].tolist()
    assert commentary[0] != ""
    assert commentary[1] != ""
    assert commentary[0] != commentary[1]
