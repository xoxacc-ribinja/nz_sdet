import copy
import pytest
from week03.solutions.python_core_17 import summarize_results


@pytest.mark.parametrize(
    'results, expected',
    [
        (
            [
                {'status': 'FAILED'},
                {'status': 'PASSED'},
                {'status': 'SKIPPED'},
            ],
            {'total': 3, 'passed': 1, 'failed': 1, 'skipped': 1, 'error': 0}
        ),
        (
                [], {'total': 0, 'passed': 0, 'failed': 0, 'skipped': 0, 'error': 0}
        ),
    ]
)
def test_summarized_results(results, expected):
    assert summarize_results(results) == expected

@pytest.mark.parametrize(
    'results',
    [
        ({'status': 'FAILED'}),
        [{'status': 'BROKEN'}],
        [{'status': 1}],
        [{1, 'PASSED'}]
    ]
)
def test_invalid_results(results):
    with pytest.raises(ValueError):
        summarize_results(results)


def test_not_modified_input():
    input_data = [
        {'status': 'FAILED'},
        {'status': 'PASSED'},
        {'status': 'SKIPPED'},
        {'status': 'PASSED'},
        {'status': 'PASSED'},
        {'status': 'PASSED'},
    ]
    original = copy.deepcopy(input_data)
    summarize_results(input_data)
    assert input_data == original

