import pytest
from week03.input_files.build_gate import evaluate_build


input_data = [
        {'status': 'FAILED'},
        {'status': 'PASSED'},
        {'status': 'SKIPPED'},
        {'status': 'PASSED'},
        {'status': 'PASSED'},
        {'status': 'PASSED'},
    ]

@pytest.mark.parametrize(
    'result, max_failed, expected',
    [(input_data, 1, 'ACCEPTED'),
     (input_data, 2, 'ACCEPTED'),
     (input_data, 0, 'REJECTED'),
     ([{'status': 'ERROR'}], 2, 'BLOCKED'),
     ([], 1, 'ACCEPTED'),
     ([
          {'status': 'ERROR'},
          {'status': 'FAILED'},
          {'status': 'SKIPPED'},
          {'status': 'PASSED'},
      ], 2, 'BLOCKED')
    ]
)
def test_build_evaluator(result, max_failed, expected):
    assert evaluate_build(result, max_failed) == expected


@pytest.mark.parametrize(
    'result, max_failed',
    [
        ({'status': 'PASSED'}, 1),
        (['status', 'PASSED'], 1),
        ([{'status': 'skipped'}], 1),
        ([{'tutus': 'FAILED'}], 1),
        ([{'status':1}], 1),
        ([{'status': 'PASSED'}], 'one'),
        ([{'status': 'PASSED'}], -1),
        ([{'status': 'PASSED'}], True)
    ]
)
def test_invalid_input(result, max_failed):
    with pytest.raises(ValueError):
        evaluate_build(result, max_failed)