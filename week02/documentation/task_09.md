# Task 09 — Component Failure Durations

## Input

```python
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
```

## Task

Write `collect_failure_durations(runs)`.

Return a dictionary containing components that have at least one valid FAILED run.
For each component, the value is the sum of durations of all its valid FAILED runs.

A FAILED run is valid when duration can be converted to int and is not negative.
Other statuses do not participate.

Expected result:

```python
{
    'frontend': 42,
    'api': 21,
    'worker': 17,
}
```

Dictionary order is irrelevant.

## Requirements

- Use a for loop.
- Use try/except ValueError.
- Use continue where appropriate.
- Do not modify the original runs.
- Return the dictionary.
- Do not use Counter, defaultdict, set, classes, or external libraries.
- Do not copy code from previous tasks.

## PASS criteria

- Correct result for the provided input.
- Invalid duration does not break processing.
- Negative duration is excluded.
- Non-FAILED runs are excluded.
- Repeated components accumulate durations rather than overwrite them.
- Original runs remains unchanged after the function call.

## Not required

- Type hints.
- Docstrings.
- File reading.
- Report formatting/printing.
