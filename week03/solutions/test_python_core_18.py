import copy
import pytest
from week03.solutions.python_core_18 import extract_problem_tests


@pytest.mark.parametrize(
    'results, expected',
    [
        (
                [
                    {'name': 'login', 'status': 'PASSED'},
                    {'name': 'checkout', 'status': 'FAILED'},
                    {'name': 'api', 'status': 'SKIPPED'},
                    {'name': 'network', 'status': 'ERROR'}
                ],
            ['checkout', 'network']
        ),
        (
                [
                    {'name': 'login', 'status': 'PASSED'},
                    {'name': 'checkout', 'status': 'FAILED'},
                    {'name': 'checkout', 'status': 'ERROR'},
                    {'name': 'login', 'status': 'ERROR'}
                ],
                ['checkout', 'login']
        ),
        (
                [
                    {'name': 'login', 'status': 'PASSED'},
                    {'name': 'checkout', 'status': 'SKIPPED'},
                    {'name': 'api', 'status': 'PASSED'},
                    {'name': 'network', 'status': 'PASSED'}
                ],
                []
        ),
        (
                [], []
        )
    ]
)
def test_summarized_results(results, expected):
    assert extract_problem_tests(results) == expected


@pytest.mark.parametrize(
    'results',
    [
            {'name': 'login', 'status': 'PASSED'},
            [{'fame': 'checkout', 'status': 'SKIPPED'}],
            [{'name': 'api'}],
            [{'name': 'network', 'status': 'BROKEN'}]
    ]
)
def test_invalid_results(results):
    with pytest.raises(ValueError):
        extract_problem_tests(results)


def test_not_modified_input():
    input_data = [
        {'name': 'login', 'status': 'PASSED'},
        {'name': 'checkout', 'status': 'FAILED'},
    ]
    original = copy.deepcopy(input_data)
    extract_problem_tests(input_data)
    assert input_data == original

