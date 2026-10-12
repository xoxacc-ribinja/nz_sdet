# Потраченное время - не более получаса с обдумыванием и обсуждением возможностей. (см. историю чата)
# Если история чата касаемо этой задачи недоступна, просто фиксируем время выполнения. Особых сложностей не испытывал.
# Для написания именно синтаксиса никуда не подсматривал.

import pytest
from week03.input_files.storage_billing import calculate_storage_cost

@pytest.mark.parametrize(
    'data, expected',
    [
        ((1, 2, 3), 0),
        ((2, 2, 2), 0),
        ((3, 2, 2), 2),
        ((3, 2, 0), 0),
        ((0, 1, 0), 0),
        ((0, 0, 0), 0),
        ((3, 0, 2), 6)
    ]
)
def test_input_data(data, expected):
    assert calculate_storage_cost(*data) == expected


@pytest.mark.parametrize(
    'data',
    [
        (0.5, 1, 2),
        (True, 1, 2),
        (1, 'one', 0),
        (1, 1, False),
        (1, 2, -3),
        (1, -2, 3),
        (-1, 2, 3),
    ]
)
def test_invalid_inputs(data):
    with pytest.raises(ValueError):
        calculate_storage_cost(*data)


@pytest.mark.parametrize(
    'data, expected',
    [
        ((3, 2, 2), int)
    ]
)
def test_input_type(data, expected):
    assert type(calculate_storage_cost(*data)) == expected

