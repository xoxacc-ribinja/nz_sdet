VALID_STATUSES = ['PASSED', 'FAILED', 'SKIPPED', 'ERROR']


def extract_problem_tests(results: list[dict]) -> list[str]:
    problem_tests = []
    if not isinstance(results, list):
        raise ValueError('Results expected to be a list!')

    for item in results:
        if not isinstance(item, dict):
            raise ValueError('Elements must be a dictionary!')

        name = item.get('name')
        if not isinstance(name, str) or name == '' or not name:
            raise ValueError('Name must be a non-empty string!')

        status = item.get('status')
        if status not in VALID_STATUSES:
            raise ValueError('No valid statuses found!')

        if status == 'FAILED' or status == 'ERROR':
            if name not in problem_tests:
                problem_tests.append(name)

    return problem_tests


