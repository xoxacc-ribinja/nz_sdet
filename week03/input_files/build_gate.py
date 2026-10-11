
def evaluate_build(results, max_failed):
    if type(max_failed) is not int or max_failed < 0:
        raise ValueError("Invalid failure limit")

    if not isinstance(results, list):
        raise ValueError("Invalid results")

    statuses = []

    for result in results:
        if not isinstance(result, dict):
            raise ValueError("Invalid record")

        status = result.get("status")

        if status not in ("PASSED", "FAILED", "SKIPPED", "ERROR"):
            raise ValueError("Invalid status")

        statuses.append(status)

    if "ERROR" in statuses:
        return "BLOCKED"

    if statuses.count("FAILED") >= max_failed:
        return "REJECTED"

    return "ACCEPTED"
