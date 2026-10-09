runs = [
    ['api', 'PASSED', '18'],
    ['worker', 'FAILED', 'oops'],
    ['frontend', 'FAILED', '42'],
    ['api', 'FAILED', '21'],
    ['database', 'BROKEN', '30'],
    ['worker', 'FAILED', '17'],
    ['frontend', 'FAILED', '-5'],
    ['auth', 'PASSED', '12'],
]

def collect_failure_durations(runs):
    failure_durations = {}

    for run in runs:
        if run[1] == 'FAILED':
            try:
                duration = int(run[2])
            except ValueError:
                continue
            if duration >= 0:
                if run[0] not in failure_durations:
                    failure_durations[run[0]] = duration
                else:
                    failure_durations[run[0]] += duration

    return  failure_durations
