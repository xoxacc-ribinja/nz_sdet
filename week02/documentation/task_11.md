# Task 11 — Component Stability Report

Use the full task statement from the accompanying ChatGPT message.

Required functions:
- collect_valid_runs(runs)
- collect_component_stats(valid_runs)
- collect_unstable_components(component_stats)

A valid run has exactly 3 fields, status PASSED/FAILED/BROKEN, 
integer-convertible non-negative duration. 
Return valid records with integer durations without mutating the input.

Build per-component nested stats with keys total, passed, failed. BROKEN increases only total.

Return unstable components that have at least 2 valid runs, at least one PASSED and at least one FAILED. Preserve first-valid-appearance order.

No type hints/docstrings/file reading/style gate for this task. No Counter/defaultdict/set/max/sort/classes/external libraries/old-task copying/AI completion.

Measure time to first working version and do not polish before review.
