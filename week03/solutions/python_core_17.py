def summarize_results(results: list[dict]) -> dict:
    valid_statuses = ("PASSED", "FAILED", "SKIPPED", "ERROR")
    summarized_results: dict[str, int] = {'total': 0,
                          'passed': 0,
                          'failed': 0,
                          'skipped': 0,
                          'error': 0}
    if not isinstance(results, list):
        raise ValueError('Results must be a list!')
    for result in results:
        if not isinstance(result, dict):
            raise ValueError('Invalid result input!')
        status = result.get('status')
        if status not in valid_statuses:
            raise ValueError('Invalid status!')
        summarized_results[status.lower()] += 1
        summarized_results['total'] += 1

    return summarized_results


# - Для пустого списка все счётчики равны нулю.
# - Все пять ключей должны присутствовать всегда.
# - Валидация входа — та же, что у evaluate_build для параметра results.
# - Никакой мутации исходного списка и вложенных словарей.
