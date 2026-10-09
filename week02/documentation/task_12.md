# Task 12 — Test Log Incident Extractor

## Context

You are writing a small SDET utility.

A test runner writes a plain-text log. Most lines are ordinary noise. Some lines describe failed tests in a strict format:

    TEST | <test_name> | FAILED | <error_message>

Your utility must extract valid failed-test records and build a short incident report.

## Input

Use this data:

```python
log_lines = [
    '2026-10-07 10:00:01 runner started',
    'TEST | test_login | PASSED | ok',
    'TEST | test_payment | FAILED | timeout waiting for response',
    'worker heartbeat',
    'TEST | test_profile | FAILED |',
    'TEST | test_search | BROKEN | connection reset',
    'TEST | test_payment | FAILED | status code 500',
    'TEST | test_logout | FAILED | session was not closed',
    'TEST | test_login | FAILED | invalid token',
    'TEST | test_catalog | FAILED | database unavailable | retry exhausted',
    'runner finished',
]
```

## Rules

A line is a valid failed-test record only if:

1. After splitting by `|`, it has exactly 4 fields.
2. Leading and trailing spaces around every field do not matter.
3. The first field is exactly `TEST`.
4. The third field is exactly `FAILED`.
5. The test name is not empty.
6. The error message is not empty.

Ignore every other line.

For every valid failed-test record, return:

```python
{
    'test': <test_name>,
    'error': <error_message>
}
```

The order must be the same as in the original log.

For the supplied input, the extracted records must be:

```python
[
    {'test': 'test_payment', 'error': 'timeout waiting for response'},
    {'test': 'test_payment', 'error': 'status code 500'},
    {'test': 'test_logout', 'error': 'session was not closed'},
    {'test': 'test_login', 'error': 'invalid token'},
]
```

Notice that the `test_catalog` line is invalid: the extra `|` creates more than four fields.

## Incident report

From the extracted records, build a report containing one entry per test:

```python
{
    'test_payment': {
        'failures': 2,
        'last_error': 'status code 500'
    },
    'test_logout': {
        'failures': 1,
        'last_error': 'session was not closed'
    },
    'test_login': {
        'failures': 1,
        'last_error': 'invalid token'
    }
}
```

`failures` is the number of valid failed records for that test.

`last_error` is the error from the last valid failed record for that test.

## Required functions

Write exactly these two main processing functions:

```python
def extract_failed_tests(log_lines):
    ...

def build_incident_report(failed_tests):
    ...
```

You may add `print()` calls for checking the result.

## Constraints

- Do not modify `log_lines`.
- Do not modify the list returned by `extract_failed_tests()` inside `build_incident_report()`.
- Do not use `Counter`, `defaultdict`, `set`, classes, regular expressions, or external libraries.
- Do not copy code from Tasks 08–11.
- Do not use AI/code completion to write the solution.
- Documentation, type hints, corporate code-style cleanup, and file reading are NOT part of this task.
- Searching Python syntax/documentation is allowed if you get stuck, but record what you had to look up.

## Measurement

Record:

1. Time to first working version.
2. Whether you looked at any previous task.
3. Whether you searched documentation/Google, and what syntax you searched.
4. Whether AI/code completion contributed any code.

## PASS criteria

- Correct extraction according to all six validation rules.
- Correct incident report.
- Correct handling of repeated failures of the same test.
- `last_error` is really the last valid error.
- Original input is not mutated.
- Extracted records are not mutated by report generation.
- Hidden input within the same contract passes.
- You can explain the important lines during defense.

Do not optimize prematurely. First make a version that you believe is correct.
