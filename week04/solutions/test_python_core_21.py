import pytest
from week04.solutions.python_core_21 import failures_before_success

@pytest.mark.parametrize(
    'data, expected',
 [
     ([True, False, True], 0),
     ([False, False, True], 2),
     ([False, False, False], None),
     ([], None)
 ]
)
def test_validate_solution(data, expected):
 assert failures_before_success(data) == expected