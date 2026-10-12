"""Training implementation for Task 19: cloud storage billing.

Write tests against the published contract; do not change this file.
"""


def calculate_storage_cost(used_gb: int, free_gb: int, price_per_gb: int) -> int:
    for value in (used_gb, free_gb, price_per_gb):
        if type(value) is not int or value < 0:
            raise ValueError('Storage billing arguments must be non-negative integers')

    if used_gb < free_gb:
        return 0

    return (used_gb - free_gb + 1) * price_per_gb
