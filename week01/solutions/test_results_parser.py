file_path = ''
file_name = "test_results.txt"


def parse_test_results(filename):
    failed_list = []
    total_test_count = 0
    passed = skipped = failed = 0

    with open(filename, 'r') as result:
        for line in result.readlines():
            if line.startswith('test'):
                total_test_count += 1
                if ' PASSED' in line:
                    passed += 1
                elif ' SKIPPED' in line:
                    skipped += 1
                elif ' FAILED' in line:
                    failed += 1
                    test_name = line.split(' ')[0]
                    failed_list.append(test_name)
                else:
                    unknown_test_status = line.split(' ')[0]
                    print('Something wrong with the test %s' % (unknown_test_status))

        failed_tests = '\n'.join(failed_list)
        unknown = total_test_count - passed - failed - skipped


    return total_test_count, passed, failed, skipped, unknown, failed_tests


def print_results ():
    total_test_count, passed, failed, skipped, unknown, failed_tests = parse_test_results(file_name)
    print('TOTAL: %s\nPassed: %s,\nFailed: %s,\nSkipped: %s,\nUnknown: %s'
          '\n\nFailed tests:\n%s' % (total_test_count, passed, failed, skipped, unknown, failed_tests))

print_results()
