from pathlib import Path


COMPONENT = ['component', 'status', 'duration']
INPUT_FILE = Path(__file__).parent.parent/'input_files'/'build_history.txt'
VALID_STATUSES = ['PASSED', 'FAILED', 'BROKEN']


def make_input_list() -> list[str]:
    """Make a list of every line in input file lines."""

    input_list: list[str] = []
    with open(INPUT_FILE, 'r') as file:
        for line in file.readlines():
            input_list.append(line.strip())

    return input_list


def make_valid_and_invalid_builds_lists(input_list: list[str]) -> tuple[list[list[str|int]], list[list[str]]]:
    """
    Make a list of lists of strings or ints for valid inputs.
    Make a list of lists of strings for invalid inputs.

    :param input_list: A list of every line in input file lines.
    """

    valid_builds_list: list[list[str|int]] = []
    invalid_builds_list: list[list[str]] = []

    for input_string in input_list:
        input_string_list: list[str] = input_string.split(',')
        if len(input_string_list) != 3:
            invalid_builds_list.append(input_string_list)
        elif input_string_list[1] not in VALID_STATUSES:
            invalid_builds_list.append(input_string_list)
        else:
            try:
                duration: int = int(input_string_list[2])
            except ValueError:
                invalid_builds_list.append(input_string_list)
                continue
            if duration >= 0:
                input_string_list[2] = duration
                valid_builds_list.append(input_string_list)
            else:
                invalid_builds_list.append(input_string_list)

    return valid_builds_list, invalid_builds_list


def count_statuses(valid_input: list[list[str|int]]) -> dict[str, int]:
    """Count every valid status number.

    :param valid_input: A list of valid lines from initial file.
    """

    counted_statuses: dict[str, int] = {}
    for status in VALID_STATUSES:
        counted_statuses[status] = 0

    for input_list in valid_input:
        counted_statuses[input_list[1]] += 1

    return counted_statuses


def count_total_and_average_duration(valid_input: list[list[str|int]]) -> tuple[int, float]:
    """Count total and average duration for valid runs.

    :param valid_input: A list of valid lines from initial file.
    """

    total_duration: int = 0

    for input_list in valid_input:
        total_duration += input_list[2]

    average_duration: float = round(total_duration/len(valid_input), 2)

    return total_duration, average_duration


def display_final_component_status(valid_input: list[list[str|int]]) -> dict[str, str]:
    """Create a dictionary to display final components statuses.

    :param valid_input: A list of valid lines from initial file.
    """

    final_component_status: dict[str, str] = {}
    for input_list in valid_input:
        final_component_status[input_list[0]] = input_list[1]

    return final_component_status


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


def build_history() -> None:
    """Parse and display info based on builds history input file."""

    input_list: list[str] = make_input_list()

    valid_input: list[list[str|int]]
    invalid_input: list[list[str]]
    valid_input, invalid_input = make_valid_and_invalid_builds_lists(input_list)

    total_duration: int
    average_duration: float
    total_duration, average_duration = count_total_and_average_duration(valid_input)

    status_count: dict[str, int] = count_statuses(valid_input)
    final_status: dict[str, str] = display_final_component_status(valid_input)

    by_status: str = format_list_to_output_string(format_dict_to_output_list(status_count))
    display_final_status: str = format_list_to_output_string(format_dict_to_output_list(final_status))

    print(f'Valid builds: {len(valid_input)}\n'
          f'Invalid lines: {len(invalid_input)}\n\n'
          f'By status:\n'
          f'{by_status}\n'
          f'Total duration: {total_duration}\n'
          f'Average duration: {average_duration}\n\n'
          f'Final component status:\n'
          f'{display_final_status}')

build_history()

