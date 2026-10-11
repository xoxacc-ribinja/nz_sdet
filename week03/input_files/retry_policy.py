def should_retry(status, attempt, max_attempts):
    if status not in ('PASSED', 'FAILED', 'SKIPPED', 'ERROR'):
        raise ValueError('Invalid status')

    if type(attempt) is not int or attempt < 1:
        raise ValueError('Invalid attempt')

    if type(max_attempts) is not int or max_attempts < 1:
        raise ValueError('Invalid max_attempts')

    if attempt > max_attempts:
        raise ValueError('Attempt exceeds max_attempts')

    return status == 'FAILED' and attempt < max_attempts
