def count_failures_by_suite(runs: list[dict]) -> dict[str, int]:
    failures_by_suite = {}
    for run in runs:
        if not failures_by_suite.get(run['suite']):
            if run['passed'] == True:
                failures_by_suite[run['suite']] = 0
            else:
                failures_by_suite[run['suite']] = 1

        elif run['passed'] == False:
            failures_by_suite[run['suite']] += 1

    return failures_by_suite
