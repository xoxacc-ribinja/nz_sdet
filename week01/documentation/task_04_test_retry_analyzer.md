# Task 4 — Test Retry Analyzer

## Goal
Write a Python program that analyzes chronological test execution history. A test may run more than once after a failure. The last occurrence determines its final status.

## Input
File: `test_runs.txt`

```text
test_login,PASSED
test_vm_start,FAILED
test_network,FAILED
test_vm_start,PASSED
test_snapshot,FAILED
test_network,FAILED
test_logout,PASSED
test_snapshot,PASSED
```

## Rules
- Final status = status from the last occurrence of that test.
- Recovered after retry = was FAILED at least once, but final status is PASSED.
- A test that remains FAILED is not recovered.

## Required output
```text
Unique tests: 5
Passed: 4
Failed: 1

Final results:
test_login: PASSED
test_vm_start: PASSED
test_network: FAILED
test_snapshot: PASSED
test_logout: PASSED

Recovered after retry:
- test_vm_start
- test_snapshot

Still failing:
- test_network
```

## Requirements
- Read from `test_runs.txt`.
- Use at least 3 functions.
- Use `list`, `dict`, `for`, `if`, functions, file reading, and `split()`.
- No classes.
- No `set`.
- No external libraries.
- Do not hardcode test names, counts, or expected results.

## Learning objective
Practice updating dictionary values when the same key appears again.

The final-status dictionary alone is not enough for `Recovered after retry`, because previous statuses are lost. Preserve enough information to determine whether a finally-passing test failed earlier.

## Current progress
Your parser should produce data like:

```python
[
    {'test_name': 'test_login', 'status': 'PASSED'},
    {'test_name': 'test_vm_start', 'status': 'FAILED'},
    {'test_name': 'test_network', 'status': 'FAILED'},
    {'test_name': 'test_vm_start', 'status': 'PASSED'}
]
```

### Current next step
Write a function that receives the parsed list and returns the FINAL status of every unique test.

Expected shape:

```python
{
    'test_login': 'PASSED',
    'test_vm_start': 'PASSED',
    'test_network': 'FAILED'
}
```

Then continue toward the complete report.

## AI rule
AI may explain Python syntax, error messages, or how a specific construct works. Do not ask AI to write the solution, algorithm, or function.
