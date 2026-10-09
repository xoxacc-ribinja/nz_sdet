# Task 10 — Component Run Summary

Use the full task statement from the accompanying ChatGPT message.

## Required functions
- `collect_valid_runs(runs)`
- `collect_final_statuses(valid_runs)`
- `count_component_durations(valid_runs)`

## Core requirements
A run is valid only if it has exactly 3 fields, its status is PASSED/FAILED/BROKEN, duration converts to int, and duration is non-negative.

Return:
1. valid runs with integer durations;
2. last valid status per component;
3. summed valid duration per component.

Do not mutate the original input. No Counter, defaultdict, set, max, sort, classes, external libraries, old-task copying, or AI/code-completion.

Type hints, docstrings, corporate style, and report formatting are deliberately not required.

Measure elapsed time to the first working version and report whether you looked at Tasks 08/09, used external help, and where you got stuck.
