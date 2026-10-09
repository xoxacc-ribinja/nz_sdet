runs = [
    ['api', 'PASSED', '25'],
    ['worker', 'FAILED', 'oops'],
    ['frontend', 'FAILED', '40'],
    ['database', 'BROKEN', '-5'],
    ['auth', 'FAILED', '15'],
]

def collect_valid_failed(runs):
    valid_failed = {}

    for run in runs:
        if run[1] == 'FAILED':
            try:
                run[2] = int(run[2])
            except ValueError:
                continue

            if run[2] >= 0:
                valid_failed[run[0]] = run[2]

    return valid_failed
