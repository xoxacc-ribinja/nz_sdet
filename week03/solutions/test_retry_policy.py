import pytest
from week03.input_files.retry_policy import should_retry


@pytest.mark.parametrize(
    'status, expected',
    [
        ('PASSED', False),
        ('SKIPPED', False),
        ('FAILED', False),
        ('ERROR', False)
    ]
)
def test_statuses(status, expected):
    assert should_retry(status, attempt=1, max_attempts=1) == expected


@pytest.mark.parametrize(
    'status, attempt, max_attempts, expected',
    [
        ('PASSED', 1, 4, False),
        ('SKIPPED', 1, 2, False),
        ('FAILED', 1, 2, True),
        ('ERROR', 1, 2, True),
        ('FAILED', 2, 2, False),
        ('ERROR', 3, 3, False)
    ]
)
def test_attempts(status, attempt, max_attempts, expected):
    assert should_retry(status, attempt, max_attempts) == expected

@pytest.mark.parametrize(
    'status, attempt, max_attempts',
    [
        ('PISSED', 1, 1),
        ('skipped', 1, 1),
        (['PASSED'], 1, 1),
        ('PASSED', 0, 1),
        ('PASSED', 'zero', 1),
        ('PASSED', -1, 1),
        ('PASSED', 2, 1),
        ('PASSED', False, 1),
        ('PASSED', 1, 0)

    ]
)
def test_invalid_inputs(status, attempt, max_attempts):
    with pytest.raises(ValueError):
        should_retry(status, attempt, max_attempts)
