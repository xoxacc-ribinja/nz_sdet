def failures_before_success(results: list[bool]) -> int | None:
    if True not in results:
        return None

    fails_before_success: int = 0
    for result in results:
        if result:
            return fails_before_success
        else:
            fails_before_success += 1

