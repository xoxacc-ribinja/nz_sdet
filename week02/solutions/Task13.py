def decide_retry_action(test_name, attempt, max_attempts, error_type):
    error_types = [
        'TIMEOUT',
        'NETWORK',
        'ASSERTION',
        'CRASH'
    ]

    if (test_name == ''
            or attempt < 1
            or max_attempts < 1
            or attempt > max_attempts
            or error_type not in error_types):
            return 'INVALID'
    elif error_type == 'ASSERTION':
        return 'STOP'
    elif error_type == 'CRASH':
        return 'QUARANTINE'
    elif error_type in ('TIMEOUT', 'NETWORK'):
        if attempt < max_attempts:
            return 'RETRY'
        else:
            return 'STOP'

print(decide_retry_action('test_api', 3, 3, 'NETWORK'))