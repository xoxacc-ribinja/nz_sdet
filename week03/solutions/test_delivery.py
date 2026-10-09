import pytest
from week03.input_files.delivery import delivery_cost



def test_weight_positive():
    result = delivery_cost(1, False)
    assert result == 200


def test_weight_negative():
    with pytest.raises(ValueError):
        delivery_cost(-2, False)


def test_weight_zero():
    with pytest.raises(ValueError):
        delivery_cost(0, False)


def test_less_one_kg():
    result = delivery_cost(0.57, False)
    assert result == 200


def test_one_to_five_kgs():
    result = delivery_cost(3.3, False)
    assert result == 400

def test_edge_case_five_kgs():
    result = delivery_cost(5, False)
    assert result == 400


def test_more_than_five_kgs():
    result = delivery_cost(5.001, False)
    assert result == 700


def test_express_positive():
    result = delivery_cost(3.3, True)
    assert result == 700


def test_express_negative():
    with pytest.raises(ValueError):
        delivery_cost(-2, True)





