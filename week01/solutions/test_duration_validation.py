INPUT_FILES_DIR: str = '../input_files' # Considering CWD is where the .py file is
TEST_RUNS_FILE: str = f'{INPUT_FILES_DIR}/test_durations.txt'
VALID_STATUSES: list[str] = ['PASSED', 'FAILED', 'SKIPPED']
TEST_RUN_PARAMETERS: list[str] = ['test_name', 'status', 'duration']


def make_test_run_parameters_list() -> list[list[str]]:
    """Make the list of lines from test_duration.txt file for further parsing."""

    test_run_parameters_list: list[list[str]] = []
    with open(TEST_RUNS_FILE, 'r') as tests_list:
        for line in tests_list.readlines():
            test_run_parameters_list.append(line.strip().split(','))

    return test_run_parameters_list


def make_statuses_count_dict(tests: list[dict[str, str|int]]) -> dict[str, int]:
    """Make a dictionary with keys as status names and values as status counts.

    :param tests: A list of dictionaries for valid test runs strings.
    """

    statuses: dict[str, int] = {}
    for status in VALID_STATUSES:
        statuses[status] = 0

    for test in tests:
        statuses[test['status']] += 1

    return statuses


def make_invalid_runs_list(test_run_parameters_list: list[list[str]]) -> list[list[str]]:
    """Make a list with string of invalid parameters.

    :param test_run_parameters_list: A list of all test runs strings.
    """
    invalid_runs_list: list[list[str]] = []
    for test_run in test_run_parameters_list:
        if len(test_run) != 3:
            invalid_runs_list.append(test_run)
        elif test_run[1] not in VALID_STATUSES:
            invalid_runs_list.append(test_run)
        else:
            try:
                test_run[2] = int(test_run[2])
            except ValueError:
                invalid_runs_list.append(test_run)
                continue
            if test_run[2] < 0:
                test_run[2] = str(test_run[2])
                invalid_runs_list.append(test_run)

    return invalid_runs_list


def make_valid_runs_list(test_run_parameters_list: list[list[str]],
                         invalid_runs_list: list[list[str]]) -> list[dict[str, str|int]]:
    """Make a list of dictionary with valid runs results,
    where keys are strings and values could be either string or int.

    :param test_run_parameters_list: A list of all test runs strings.
    :param invalid_runs_list: a list of invalid parameters strings.
    """

    valid_runs_list: list[dict[str, str|int]] = []
    for test_run in test_run_parameters_list:
        if test_run not in invalid_runs_list:
            valid_run: dict[str, str|int] = {}
            for index, parameter in enumerate(TEST_RUN_PARAMETERS):
                    valid_run[parameter] = test_run[index]
            valid_runs_list.append(valid_run)

    return valid_runs_list


def count_duration(valid_runs: list[dict[str, str|int]]) -> tuple[int, float]:
    """Count total and average test run duration.

    :param valid_runs: A list of dictionary with valid runs results.
    """
    total_duration: int = 0

    for run in valid_runs:
        total_duration += run['duration']

    average_duration: float = round(total_duration / len(valid_runs), 2)

    return total_duration, average_duration


def format_dict_to_output_list(dic: dict[str, str|int]) -> list[str]:
    """Format the dictionary to a list with {key:value} pair as a single string.

    :param dic: An input dictionary to format to list.
    """

    output_list: list[str] = []
    for key, value in dic.items():
        output_list.append(f'{key}: {value}')

    return output_list


def format_list_to_output_string(lst: list[str]) -> str:
    """Format a list to a single string.

    :param lst: An input list to format to string.
    """

    output_str: str = ''
    for item in lst:
        output_str += f'- {item}\n'

    return output_str


def output() -> None:
    """Parse and print statistics for test runs."""

    test_run_parameters_list: list[list[str]] = make_test_run_parameters_list()
    invalid_runs_list: list[list[str]] = make_invalid_runs_list(test_run_parameters_list)
    valid_runs: list[dict[str, str|int]] = make_valid_runs_list(test_run_parameters_list, invalid_runs_list)

    total_duration: int
    average_duration: float
    total_duration, average_duration = count_duration(valid_runs)

    print_by_status: str = format_list_to_output_string(
        format_dict_to_output_list(
            make_statuses_count_dict(valid_runs)
        )
    )
    print_invalid_lines: list[str] = []
    for line in invalid_runs_list:
        output_line: str = ','.join(line)
        print_invalid_lines.append(output_line)


    print(f'Valid tests: {len(valid_runs)}\n'
          f'Invalid lines: {len(invalid_runs_list)}\n\n'
          f'By status:\n'
          f'{print_by_status}\n'
          f'Total duration: {total_duration}\n'
          f'Average duration: {average_duration}\n\n'
          f'Invalid input:\n'
          f'{format_list_to_output_string(print_invalid_lines)}')

output()
