RUNS = 'test_runs.txt'
PARAMS = ['test_name', 'test_status']


def parse_test_info():
    results_list = []
    with open(RUNS, 'r') as runs_file:
        for r in runs_file.readlines():
            info=r.strip().split(',')
            result = {}
            for index, param in enumerate(PARAMS):
                result[param] = info[index]
            results_list.append(result)

    return results_list


def final_run_results():
    result = parse_test_info()
    final = {}
    failed_ever = []
    for res in result:
        if res[PARAMS[1]] == 'FAILED':
            if res[PARAMS[0]] not in failed_ever:
                failed_ever.append(res[PARAMS[0]])
        final[res[PARAMS[0]]] = res[PARAMS[1]]

    return final, failed_ever


def get_tests_info():
    final, failed_ever = final_run_results()
    unique_tests = len(final)
    passed = recovered = still_failed = 0
    recovered_list = []
    still_failed_list = []

    for key, value in final.items():
        if key not in failed_ever and value == 'PASSED':
            passed += 1
        elif key in failed_ever and value != 'FAILED':
            passed += 1
            recovered += 1
            recovered_list.append(key)
        elif key in failed_ever and value == 'FAILED':
            still_failed += 1
            still_failed_list.append(key)

    return (unique_tests, passed, recovered, still_failed,
            recovered_list, still_failed_list, final)


def show_results():
    (unique_tests, passed, recovered, still_failed, recovered_list,
     still_failed_list, final) = get_tests_info()

    final_results = ''
    for key,value in final.items():
        final_results += f'{key}: {value}\n'

    recovered_after_retry_results = ''
    for elem in recovered_list:
        recovered_after_retry_results += f'- {elem}\n'

    still_failed_results = ''
    for elem in still_failed_list:
        still_failed_results += f'- {elem}\n'

    print(f'Unique tests: {unique_tests}\n'
          f'Passed: {passed}\n'
          f'Recovered: {recovered}\n'
          f'Failed: {still_failed}\n\n'
          f'Final results:\n'
          f'{final_results}\n'
          f'Recovered after retry:\n'
          f'{recovered_after_retry_results}\n'
          f'Still failing:\n'
          f'{still_failed_results}')

show_results()