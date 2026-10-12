# Потрачено не более 30 минут на продумывание тестовых сценариев и их запись.
# Во время самопроверки без запуска кода обнаружил, что невнимательно прочитал условие контракта о пустом списке.
# Исправил вовремя. Есть сомнения на счёт количества проверок, считаю избыточным. Нужен разбор и обсуждение.
# Во время финального прогона обнаружил ошибку E   TypeError: object of type 'int' has no len() -
# следствие невнимательности при записи параметров. +5 минут на разбор ошибки.
# На первичном ревью возникли вопросы к покрытию (не все пункты контракта обработаны)
# и изначальной неправильной проверке неизменяемости исходного списка. +20 минут на понимание проблемы со списком,
# разбора путаницы с != и is not и редактированием тестов.
# Ещё полчаса после полноценного ревью с непотерянными данными разбора.
# Затык на реализации test_immutable_original_inventory_with_no_buying. Потребовалась куча объяснений.

import pytest

from week03.solutions.python_core_19 import buy_item


@pytest.mark.parametrize(
    'data, expected',
    [
        (
            (100, 5, ['sword', 'hat'], 'potion'), {'coins': 95, 'inventory': ['sword', 'hat', 'potion']}
        ),
        (
            (5, 5, ['sword', 'hat'], 'potion'), {'coins': 0, 'inventory': ['sword', 'hat', 'potion']}
        ),
        (
            (100, 5, ['sword', 'sword'], 'potion'), {'coins': 95, 'inventory': ['sword', 'sword', 'potion']}
        ),
        (
            (100, 5, ['sword', 'sowrd'], 'potion'), {'coins': 95, 'inventory': ['sword', 'sowrd', 'potion']}
        ),
        (
            (100, 5, ['sword', 'hat'], '   '), {'coins': 95, 'inventory': ['sword', 'hat', '   ']}
        ),
        (
            (100, 5, ['sword', 'sword'], 'sword'), {'coins': 95, 'inventory': ['sword', 'sword', 'sword']}
        ),
        (
            (100, 5, [], 'potion'), {'coins': 95, 'inventory': ['potion']}
        ),
    ]
)
def test_normal_buy(data, expected):
    assert buy_item(*data) == expected


@pytest.mark.parametrize(
    'data',
    [
        (0, 5, ['sword', 'hat'], 'potion'),
        (7.4, 5, ['sword', 'hat'], 'potion'),
        (7, 5.3, ['sword', 'hat'], 'potion'),
        (7, 5.0, ['sword', 'hat'], 'potion'),
        (7.0, 5, ['sword', 'hat'], 'potion'),
        (100, 0, ['sword', 'hat'], 'potion'),
        (True, 5, ['sword', 'hat'], 'potion'),
        (1, 5, ['sword', 'hat'], 'potion'),
        (-100, 5, ['hat', 'sword'], 'potion'),
        (1, -5, ['sword', 'hat'], 'potion'),
        (100, 5, ['sword', ''], 'potion'),
        (100, 5, ['sword', 3], 'potion'),
        (100, 5, ['sword', 'hat'], ''),
        (100, 5, ['sword', 'hat'], 3),
        (100, 5, ['sword', 'hat'], False),
        (100, 5, ('sword', 'hat'), 'potion'),
    ]
)
def test_is_data_valid(data):
    with pytest.raises(ValueError):
        buy_item(*data)


@pytest.mark.parametrize(
    'coins, price, inventory, item_name',
    [(100, 5, ['sword'], 'hat'),
     ]
)
def test_immutable_original_inventory(coins, price, inventory, item_name):
    original_inventory = inventory.copy()
    buy_item(coins, price, inventory,item_name)
    assert inventory == original_inventory

@pytest.mark.parametrize(
    'coins, price, inventory, item_name',
    [(3, 5, ['sword'], 'hat')]
)
def test_immutable_original_inventory_with_no_buying(coins, price, inventory, item_name):
    original_inventory = inventory.copy()

    with pytest.raises(ValueError):
        buy_item(coins, price, inventory, item_name)

    assert inventory == original_inventory


@pytest.mark.parametrize(
    'coins, price, inventory, item_name',
    [(100, 5,['sword'], 'hat')]
)
def test_new_object_returned(coins, price, inventory,item_name):
    assert buy_item(coins, price, inventory, item_name)['inventory'] is not inventory