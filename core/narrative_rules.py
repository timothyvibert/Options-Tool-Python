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
    {
        "rule_id": "call_spread_debit_v1",
        "version": "1.0",
        "strategy_family": "CALL_SPREAD_DEBIT",
        "conditions": [
            {"field": "classification", "op": "==", "value": "SPR"},
            {"field": "has_stock_position", "op": "==", "value": False},
            {"field": "has_short_call", "op": "==", "value": True},
            {"field": "has_long_call", "op": "==", "value": True},
            {"field": "option_structure", "op": "==", "value": "call_spread"},
            {"field": "is_debit", "op": "==", "value": True},
        ],
        "scenario_anchors": {
            "bear": ["strike_1"],
            "base": ["strike_1", "strike_2", "spot"],
            "bull": ["strike_2"],
        },
        "templates": {
            "bear": "call_spread_debit_bear_v1",
            "base": "call_spread_debit_base_v1",
            "bull": "call_spread_debit_bull_v1",
        },
    },
]

TEMPLATES = {
    "ccov_bear_v3": (
        "Below {cap_strike}, the call strike is the key level for {coverage_clause}. "
        "At expiry below {cap_strike}, the call expires worthless and the premium cushions downside on {coverage_scope}."
    ),
    "ccov_base_v3": (
        "Between {spot} and {cap_strike}, results are driven by the shares for {coverage_clause}. "
        "At expiry in this range, the call expires worthless and the option premium is retained on {coverage_scope}."
    ),
    "ccov_bull_v3": (
        "Above {cap_strike}, upside is limited by the call strike for {coverage_clause}. "
        "At expiry above {cap_strike}, shares may be called away at the strike and upside is {cap_phrase} on {coverage_scope}.{coverage_tail_bull}"
    ),
    "pprt_bear_v3": (
        "Below {put_strike}, the put strike defines the floor for {coverage_clause}. "
        "At expiry below {put_strike}, the put settles at intrinsic value and downside is {protection_phrase} on {coverage_scope}.{coverage_tail_bear}"
    ),
    "pprt_base_v3": (
        "Between {put_strike} and {spot}, the shares drive results for {coverage_clause}. "
        "At expiry in this range, protection remains in place while the premium is the cost of insurance on {coverage_scope}."
    ),
    "pprt_bull_v3": (
        "Above {spot}, upside participation continues for {coverage_clause}. "
        "At expiry above {spot}, the put expires worthless and gains follow the shares on {coverage_scope}."
    ),
    "collar_bear_v3": (
        "Below {put_strike}, the put strike defines the floor for {coverage_clause}. "
        "At expiry below {put_strike}, downside is {protection_phrase} on {coverage_scope}.{coverage_tail_bear}"
    ),
    "collar_base_v3": (
        "Between {put_strike} and {cap_strike}, the strike band defines outcomes for {coverage_clause}. "
        "At expiry in this range, the put expires worthless and the call stays out of the money; the net option premium is realized on {coverage_scope}."
    ),
    "collar_bull_v3": (
        "Above {cap_strike}, upside is limited by the call strike for {coverage_clause}. "
        "At expiry above {cap_strike}, shares may be called away at the strike and upside is {cap_phrase} on {coverage_scope}.{coverage_tail_bull}"
    ),
    "condor_bear_v3": (
        "Below {lower_short}, the downside short strike is the key level. "
        "At expiry below {lower_short}, losses increase toward the lower hedge at {lower_long}."
    ),
    "condor_base_v3": (
        "Between {lower_short} and {upper_short}, the short strikes frame the range. "
        "At expiry in this range, the short options expire worthless and the strategy retains the net credit."
    ),
    "condor_bull_v3": (
        "Above {upper_short}, the upside short strike is the key level. "
        "At expiry above {upper_short}, losses increase toward the upper hedge at {upper_long}."
    ),
    "call_spread_debit_bear_v1": (
        "Below {lower_short}, the lower strike is the key level. "
        "At expiry below {lower_short}, both calls expire worthless."
    ),
    "call_spread_debit_base_v1": (
        "Between {lower_short} and {upper_short}, the strike band defines outcomes. "
        "At expiry between {lower_short} and {upper_short}, intrinsic value increases as price rises."
    ),
    "call_spread_debit_bull_v1": (
        "Above {upper_short}, the upper strike is the key level. "
        "At expiry above {upper_short}, gains are capped at maximum profit."
    ),
}
