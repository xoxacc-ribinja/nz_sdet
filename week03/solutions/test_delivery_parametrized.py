import pytest
from week03.input_files.delivery import delivery_cost

@pytest.mark.parametrize(
    'weight, expected',
    [
        (0.57, 200),
        (1, 200),
        (4.03, 400),
        (5, 400),
        (5.04, 700)
    ]
)
def test_regular_delivery(weight, expected):
    assert delivery_cost(weight, False) == expected


@pytest.mark.parametrize(
    'weight, expected',
    [
        (0.00000057, 500),
        (1, 500),
        (4.03, 700),
        (5, 700),
        (5.04, 1000)
    ]
)
def test_express_delivery(weight, expected):
    assert delivery_cost(weight, True) == expected


@pytest.mark.parametrize(
    'weight',
    [0, -0.00000001, ]
)
def test_invalid_weights(weight):
    with pytest.raises(ValueError):
        delivery_cost(weight, False)
