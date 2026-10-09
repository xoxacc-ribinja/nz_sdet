log_lines = [
    '2026-10-07 10:00:01 runner started',
    'TEST | test_login | PASSED | ok',
    'TEST | test_payment | FAILED | timeout waiting for response',
    'worker heartbeat',
    'TEST | test_profile | FAILED |',
    'TEST | test_search | BROKEN | connection reset',
    'TEST | test_payment | FAILED | status code 500',
    'TEST | test_logout | FAILED | session was not closed',
    'TEST | test_login | FAILED | invalid token',
    'TEST | test_catalog | FAILED | database unavailable | retry exhausted',
    'runner finished',
]

def extract_failed_tests(log_lines):
    failed_tests = []

    for line in log_lines:
        listed_line = line.split('|')
        print(listed_line)
        if len(listed_line) == 4:
            stripped_lines = [item.strip() for item in listed_line]
            if (stripped_lines[0] == 'TEST' and stripped_lines[2] == 'FAILED'
                    and stripped_lines[1] != '' and stripped_lines[3] != ''):
                failed_test = {}
                failed_test['test'] = stripped_lines[1]
                failed_test['error'] = stripped_lines[3]
                failed_tests.append(failed_test)
            print(stripped_lines)

    return failed_tests


def build_incident_report(failed_tests):
    report = {}

    for test in failed_tests:
        if test['test'] not in report:
            report[test['test']] = {'failures': 0, 'last_error': ''}

        report[test['test']]['failures'] += 1
        report[test['test']]['last_error'] = test['error']

    return report

extract_failed_tests(log_lines)