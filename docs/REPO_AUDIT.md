# Repository audit — 2026-10-09

Scope: read-only inspection of GitHub `main` at initial commit `ed98a906b1f1ec21f48ccce1da8a87a7fb4edbaf`. No complete test run was performed.

## Observed structure

- `week01/`, `week02/`, `week03/` contain documentation, input files and solutions.
- There was no root README, state file, roadmap or .gitignore.
- `week03/solutions/pytest_log.log` records four passed tests for `test_users.py` on one Mac run, not the entire suite.
- `assist.py` hardcodes local `/Users/mac/Desktop/...` paths. Make them configurable in a separate refactoring task.
- `week02/solutions/tupka.py` converts `run[2]` in-place, mutating input; assess against intended contract before changing.
- `week03/solutions/python_core_16.py`: `final_users_list.append(user_info)` intentionally left outside `if is_valid_age(...)` **by the author as a deliberate defect**. Invalid first record can raise `UnboundLocalError`; a later invalid record may append stale data. **Do not silently fix this line or treat it as an accidental student mistake**; its purpose is debugging practice.
- `week03/documentation/task_15.md` requests at least 6 regular delivery cases and 3 invalid weight cases. `week03/solutions/test_delivery_parametrized.py` contains 5 regular, 5 express and 2 invalid cases. **Historical clarification:** these counts were accepted during the lesson and Task 15 was marked PASS. Treat this as a changed/relaxed acceptance agreement, not an unresolved student failure. The Markdown task text was not retrospectively rewritten.
- `week03/input_files/delivery.py` has a known boundary mismatch around 5 kg relative to Task 14 contract. Intentional red tests are expected and should not be hidden.
- Some historical assignments are absent as individual files. Avoid inventing their exact wording.

## Deferred work

1. Discuss code-level findings separately from repository organization.
2. Decide whether `assist.py` belongs under `tools/`, and replace hardcoded paths with arguments.
3. Decide whether historical pytest logs should remain as evidence or be moved into reports. `.gitignore` will not untrack existing files.
4. Reconstruct missing task documentation only from verified sources.
5. Add environment/dependency instructions after verifying the actual installation and test commands.

No historical files were moved, removed or edited during this documentation PR.
