runs = [
    ['api', 'PASSED', '18'],
    ['worker', 'FAILED', 'oops'],
    ['frontend', 'FAILED', '42'],
    ['api', 'FAILED', '21'],
    ['database', 'BROKEN', '30'],
    ['worker', 'FAILED', '17'],
    ['frontend', 'PASSED', '38'],
    ['auth', 'SKIPPED', '12'],
    ['api', 'PASSED', '16'],
    ['worker', 'PASSED', '-3'],
]

VALID_STATUSES = ['PASSED', 'FAILED', 'BROKEN']

def collect_valid_runs(runs):
    valid_runs = []

    for run in runs:
        if len(run) == 3:
            if run[1] in VALID_STATUSES:
                try:
                    duration = int(run[2])
                except ValueError:
                    continue
                if duration >= 0:
                    valid_runs.append([run[0], run[1], duration])
    return valid_runs


def collect_final_statuses(valid_runs):
    final_statuses = {}

    for valid_run in valid_runs:
        final_statuses[valid_run[0]] = valid_run[1]

    return final_statuses

def count_component_durations(valid_runs):
    component_durations = {}

    for valid_run in valid_runs:
        if valid_run[0] not in component_durations:
            component_durations[valid_run[0]] = valid_run[2]
        else:
            component_durations[valid_run[0]] += valid_run[2]

    return component_durations

