from core.strategy_map import (
    get_strategy,
    list_groups,
    list_strategies,
    list_subgroups,
    load_strategy_map,
)


def test_strategy_groups_exist():
    groups = list_groups()
    assert len(groups) >= 1


def test_strategy_subgroups_for_known_group():
    group = list_groups()[0]
    subgroups = list_subgroups(group.lower())
    assert len(subgroups) >= 1


def test_strategy_list_for_known_subgroup():
    group = list_groups()[0]
    subgroup = list_subgroups(group)[0]
    strategies = list_strategies(group.lower(), subgroup.lower())
    assert len(strategies) >= 1


def test_get_strategy_returns_one_row():
    strategy_map = load_strategy_map()
    strategy_id = int(strategy_map["strategy_id"].iloc[0])
    result = get_strategy(strategy_id)
    assert len(result) == 1
