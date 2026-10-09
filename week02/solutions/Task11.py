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
    ['worker', 'PASSED', '23'],
    ['database', 'PASSED', '-4'],
    ['frontend', 'FAILED', '10'],
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


def collect_component_stats(valid_runs):
    component_stats = {}

    for run in valid_runs:
        if run[0] not in component_stats:
            component_stats[run[0]] = {'total': 0, 'passed': 0, 'failed': 0}
        component_stats[run[0]]['total'] += 1
        if run[1].lower() == 'passed':
            component_stats[run[0]]['passed'] += 1
        elif run[1].lower() == 'failed':
            component_stats[run[0]]['failed'] += 1

    return component_stats


def collect_unstable_components(component_stats):
    unstable_components = []

    for key, value in component_stats.items():
        if value['total'] >= 2:
            if value['passed'] >= 1 and value['failed'] >= 1:
                unstable_components.append(key)

    return unstable_components

print(collect_valid_runs(runs), '\n')
print(collect_component_stats(collect_valid_runs(runs)), '\n')
print(collect_unstable_components(collect_component_stats(collect_valid_runs(runs))))
