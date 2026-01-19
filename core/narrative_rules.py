from __future__ import annotations

RULES = [
    {
        "rule_id": "covered_call_v3",
        "version": "3.0",
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
            "bear": "ccov_bear_v3",
            "base": "ccov_base_v3",
            "bull": "ccov_bull_v3",
        },
    },
    {
        "rule_id": "protective_put_v3",
        "version": "3.0",
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
            "bear": "pprt_bear_v3",
            "base": "pprt_base_v3",
            "bull": "pprt_bull_v3",
        },
    },
    {
        "rule_id": "collar_v3",
        "version": "3.0",
        "strategy_family": "COLLAR",
        "conditions": [
            {"field": "classification", "op": "==", "value": "COL_EQ"},
            {"field": "has_stock_position", "op": "==", "value": True},
            {"field": "has_long_put", "op": "==", "value": True},
            {"field": "has_short_call", "op": "==", "value": True},
        ],
        "scenario_anchors": {
            "bear": ["strike_1", "downside", "zero"],
            "base": ["spot", "strike_1"],
            "bull": ["strike_1", "upside", "infinity"],
        },
        "templates": {
            "bear": "collar_bear_v3",
            "base": "collar_base_v3",
            "bull": "collar_bull_v3",
        },
    },
    {
        "rule_id": "iron_condor_v3",
        "version": "3.0",
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
            "bear": "condor_bear_v3",
            "base": "condor_base_v3",
            "bull": "condor_bull_v3",
        },
    },
]

TEMPLATES = {
    "ccov_bear_v3": (
        "This overlay is intended to generate income on the equity position and applies to {coverage_clause}. "
        "Below {cap_strike}, shares participate in downside while premium offers a cushion."
    ),
    "ccov_base_v3": (
        "This overlay is intended to generate income on the equity position and applies to {coverage_clause}. "
        "Between {spot} and {cap_strike}, the call stays out of the money and premium can be retained."
    ),
    "ccov_bull_v3": (
        "This overlay is intended to generate income on the equity position and applies to {coverage_clause}. "
        "Above {cap_strike}, upside is {cap_phrase} on {coverage_scope} and shares may be called away."
    ),
    "pprt_bear_v3": (
        "This overlay is intended to protect the equity position and applies to {coverage_clause}. "
        "Below {put_strike}, downside is {protection_phrase} on {coverage_scope}."
    ),
    "pprt_base_v3": (
        "This overlay is intended to protect the equity position and applies to {coverage_clause}. "
        "Between {put_strike} and {spot}, the shares drive outcomes while protection remains in place."
    ),
    "pprt_bull_v3": (
        "This overlay is intended to protect the equity position and applies to {coverage_clause}. "
        "Above {spot}, upside participation continues and the put may expire worthless."
    ),
    "collar_bear_v3": (
        "This overlay is intended to define a range on the equity position and applies to {coverage_clause}. "
        "Below {put_strike}, downside is {protection_phrase} on {coverage_scope}."
    ),
    "collar_base_v3": (
        "This overlay is intended to define a range on the equity position and applies to {coverage_clause}. "
        "Between {put_strike} and {cap_strike}, outcomes are primarily stock-driven with option income."
    ),
    "collar_bull_v3": (
        "This overlay is intended to define a range on the equity position and applies to {coverage_clause}. "
        "Above {cap_strike}, upside is {cap_phrase} on {coverage_scope} and shares may be called away."
    ),
    "condor_bear_v3": (
        "This options-only strategy targets a defined range at expiry. "
        "Below {lower_short}, losses can increase toward the lower hedge at {lower_long}."
    ),
    "condor_base_v3": (
        "This options-only strategy targets a defined range at expiry. "
        "Between {lower_short} and {upper_short}, the strategy seeks to retain premium."
    ),
    "condor_bull_v3": (
        "This options-only strategy targets a defined range at expiry. "
        "Above {upper_short}, losses can increase toward the upper hedge at {upper_long}."
    ),
}
