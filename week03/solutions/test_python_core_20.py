# Потратил больше двух часов на написание тестов. Слишком много входных данных для обработки.
# Плюс закономерно много ошибок (сказывается усталость и невнимательность). Ошибки требуют разбора -> увеличивается
# продолжительность выполнения задачи.
# # Заметка на будущее: не пытаться взять две задачи в день.
# # Ограничиться одной задачей и несколькими блицами + новые темы.
# Увидев количество необходимых проверок, задизморалился от количества ручного ввода данных в параметры.
# Но потом пришёл за советом к агенту, разобрали list comprehension.
# Будет попытка внести эти знания при генерации параметров теста.
# Спустя полчаса после попыток генерировать входные данные сдался. Устал. Отложил на следующий день.
# На следующий день подготовка и красивая запись тестовых данных вручную заняла около полутора часов. Слишком много!!!
# Если уметь пользоваться генераторами на уровне грамотного инженера, этот процесс можно сократить раза в три-четыре.


import copy
import pytest

from week03.solutions.python_core_20 import reconcile_stock


@pytest.mark.parametrize(
    'data, expected',
    [
        (
            (
                {'hat': 1},
                [{'sku': 'jacket', 'quantity': 1}]
                    # Verify regular case with 1 unit in stock and another 1 in deliveries
            ),
            {'hat': 1, 'jacket': 1}
        ),
        (
            (
                {},
                [{'sku': 'jacket', 'quantity': 1}]
                    # Verify with no units in stock and 1 in deliveries
            ),
            {'jacket': 1}
        ),
        (
            (
                {'hat': 2},
                [{'sku': 'hat', 'quantity': 2}]
                    # Verify case with more than 1 unit in stock and same unit in deliveries.
                    # Probably, excess case?
            ),
            {'hat': 4}
        ),
        (
            (
                {'hat': 2},
                [{'sku': 'hat', 'quantity': 1}, {'sku': 'hat', 'quantity': 2}, {'sku': 'hat', 'quantity': 3}]
                    # Verify case with more than 1 unit in stock and same unit in deliveries several times.
            ),
            {'hat': 8}
        ),
        (
            (
                {'hat': 1},
                []
                    # Verify case with 1 unit in stock and no units in deliveries
            ),
            {'hat': 1}
        ),
        (
            (
                {'  ': 1},
                [{'sku': 'jacket', 'quantity': 1}]
                    # Verify case with spaces in unit's name in stock and 1 regular unit in deliveries
            ),
            {'  ': 1, 'jacket': 1}
        ),
        (
            (
                {'hat': 1},
                [{'sku': '   ', 'quantity': 1}]
                    # Verify case with 1 regular unit in stock and unit with spaces in its name in deliveries
            ),
            {'hat': 1, '   ': 1}
        ),
        (
            (
                {' ': 1},
                [{'sku': '  ', 'quantity': 1}]
                    # Verify case with different spaces count in both units in stock and deliveries
            ),
            {' ': 1, '  ': 1}
        ),
        (
            (
                {'hat': 0},
                [{'sku': 'jacket', 'quantity': 1}]
                    # Verify case with 0 in stock unit and 1 regular unit in deliveries
            ),
            {'hat': 0, 'jacket': 1}
        ),
        (
            (
                {'hat': 1},
                [{'sku': 'jacket', 'quantity': 1, 'second-hand': True}]
                    # Verify case with additional key in deliveries
            ),
            {'hat': 1, 'jacket': 1}
        ),
        (
            (
                {},
                []
                    # Verify case with both empy current and deliveries
            ),
            {}
        ),
    ]
)
def test_verify_contract(data, expected):
    assert reconcile_stock(*data) == expected


@pytest.mark.parametrize(
    'data',
    [
        (
            {'': 1},
            [{'sku': 'jacket', 'quantity': 1}]
                # Verify ValueError on empty string in current key
        ),
        (
            {True: 1},
            [{'sku': 'jacket', 'quantity': 1}]
                # Verify ValueError on non-string in current key
        ),
        (
            {'hat': 1.0},
            [{'sku': 'jacket', 'quantity': 1}]
                # Verify ValueError on float in current value
        ),
        (
            {'hat': -1},
            [{'sku': 'jacket', 'quantity': 1}]
                # Verify ValueError on negative number in current value
        ),
        (
            {'hat': '1'},
            [{'sku': 'jacket', 'quantity': 1}]
                # Verify ValueError on str in current value
        ),
        (
            {'hat': True},
            [{'sku': 'jacket', 'quantity': 1}]
                # Verify ValueError on bool in current value
        ),
        (
            [{'hat': 1}],
            [{'sku': 'jacket', 'quantity': 1}]
                # Verify ValueError on non-dictionary current
        ),
        (
            {'hat': 1},
            ({'sku': 'jacket', 'quantity': 1})
                # Verify ValueError on non-list deliveries
        ),
        (
            {'hat': 1},
            [[{'sku': 'jacket', 'quantity': 1}]]
                # Verify ValueError on non-dict deliveries unit
        ),
        (
            {'hat': 1},
            [{'quantity': 1}]
                # Verify ValueError on missing deliveries sku key.
        ),
        (
            {'hat': 1},
            [{'sku': 'jacket', 'pantity': 1}]
                # Verify ValueError on missing deliveries' quantity key.
        ),
        (
            {'hat': 1},
            [{'sku': ['jacket'], 'quantity': 1}]
                # Verify ValueError on wrong deliveries' sku value type.
        ),
        (
            {'hat': 1},
            [{'sku': '', 'quantity': 1}]
                # Verify ValueError on deliveries' sku value is empty str.
        ),
        (
            {'hat': 1},
            [{'sku': 'jacket', 'quantity': 1.0}]
                # Verify ValueError on deliveries' quantity value is float.
        ),
        (
            {'hat': 1},
            [{'sku': 'jacket', 'quantity': -1}]
                # Verify ValueError on deliveries' quantity value is negative.
        ),
        (
            {'hat': 1},
            [{'sku': 'jacket', 'quantity': 0}]
                # Verify ValueError on deliveries' quantity value is zero.
        ),
        (
            {'hat': 1},
            [{'sku': 'jacket', 'quantity': '1'}]
                # Verify ValueError on deliveries' quantity value is other type.
        ),
    ]
)
def test_invalid_data(data):
    with pytest.raises(ValueError):
        reconcile_stock(*data)


@pytest.mark.parametrize(
    'data',
    [
        (
            {'hat': 1, 'gloves': 1, 'pants': 1, },
            [{'sku': 'jacket', 'quantity': 1}]
         )
    ]
)
def test_immutable_current(data):
    original_current = copy.deepcopy(data[0])
    reconcile_stock(*data)
    assert original_current == data[0]


@pytest.mark.parametrize(
    'data',
    [
        (
            {'hat': 1, 'gloves': 1, 'pants': 1, },
            [{'sku': 'jacket', 'quantity': 1}]
         )
    ]
)
def test_immutable_deliveries(data):
    original_deliveries = copy.deepcopy(data[1])
    reconcile_stock(*data)
    assert original_deliveries == data[1]


@pytest.mark.parametrize(
    'data',
    [
        (
            {'hat': 1, 'gloves': 1, 'pants': 1, },
            [{'sku': 'jacket', 'quantity': 1}]
         )
    ]
)
def test_immutable_internal_dicts(data):
    original_dict = copy.deepcopy(data[1][0])
    reconcile_stock(*data)
    assert original_dict == data[1][0]


def test_result_is_another_object_than_current_with_empty_deliveries():
    current = {'hat': 1, 'gloves': 1}
    result = reconcile_stock(current, deliveries=[])
    assert result is not current


def test_result_is_another_object_than_current_with_non_empty_deliveries():
    current = {'hat': 1, 'gloves': 1}
    deliveries = [{'sku': 'pants', 'quantity': 1}]
    result = reconcile_stock(current, deliveries)
    assert result is not current


@pytest.mark.parametrize(
    'current, deliveries',
    [
        (
            {'': 1},
            [{'sku': 'jacket', 'quantity': -1}]
        )
    ]
)
def test_immutable_input_data_on_valueError(current, deliveries):
    original_current = copy.deepcopy(current)
    original_deliveries = copy.deepcopy(deliveries)
    with pytest.raises(ValueError):
        reconcile_stock(current, deliveries)
    assert original_current == current and original_deliveries == deliveries




