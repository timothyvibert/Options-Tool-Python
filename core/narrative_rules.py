from __future__ import annotations

RULES = [
    {
        "rule_id": "covered_call_v1",
        "version": "1.0",
        "strategy_family": "COVERED_CALL",
        "conditions": [
            {"field": "classification", "op": "==", "value": "CCOV"},
            {"field": "has_stock_position", "op": "==", "value": True},
            {"field": "has_short_call", "op": "==", "value": True},
        ],
        "scenario_anchors": {
            "bear": ["downside", "zero"],
            "base": ["spot", "strike_1"],
            "bull": ["strike_1", "upside", "infinity"],
        },
        "templates": {
            "bear": "ccov_bear_v1",
            "base": "ccov_base_v1",
            "bull": "ccov_bull_v1",
        },
    },
    {
        "rule_id": "protective_put_v1",
        "version": "1.0",
        "strategy_family": "PROTECTIVE_PUT",
        "conditions": [
            {"field": "classification", "op": "==", "value": "PPRT"},
            {"field": "has_stock_position", "op": "==", "value": True},
            {"field": "has_long_put", "op": "==", "value": True},
        ],
        "scenario_anchors": {
            "bear": ["strike_1", "downside", "zero"],
            "base": ["spot", "strike_1"],
            "bull": ["upside", "infinity"],
        },
        "templates": {
            "bear": "pprt_bear_v1",
            "base": "pprt_base_v1",
            "bull": "pprt_bull_v1",
        },
    },
    {
        "rule_id": "iron_condor_v1",
        "version": "1.0",
        "strategy_family": "IRON_CONDOR",
        "conditions": [
            {"field": "iron_condor", "op": "==", "value": True},
            {"field": "has_stock_position", "op": "==", "value": False},
        ],
        "scenario_anchors": {
            "bear": ["strike_1", "strike_2", "downside", "zero"],
            "base": ["strike_2", "strike_3", "spot"],
            "bull": ["strike_3", "strike_4", "upside", "infinity"],
        },
        "templates": {
            "bear": "condor_bear_v1",
            "base": "condor_base_v1",
            "bull": "condor_bull_v1",
        },
    },
]

TEMPLATES = {
    "ccov_bear_v1": (
        "Downside still participates with the stock, but option premium cushions losses."
    ),
    "ccov_base_v1": (
        "If shares stay below the call strike, premium is retained and shares are kept."
    ),
    "ccov_bull_v1": (
        "Upside is capped above the call strike; gains beyond that level are given up."
    ),
    "pprt_bear_v1": (
        "The long put defines a floor near the strike, limiting downside versus stock-only."
    ),
    "pprt_base_v1": (
        "If shares stay near current levels, the put premium is a cost of protection."
    ),
    "pprt_bull_v1": "Upside remains open; the put may expire worthless.",
    "condor_bear_v1": (
        "If price falls below the lower strike, losses increase toward the long put."
    ),
    "condor_base_v1": (
        "Between the short strikes, the strategy seeks to retain premium."
    ),
    "condor_bull_v1": (
        "If price rises above the upper strike, losses increase toward the long call."
    ),
}
