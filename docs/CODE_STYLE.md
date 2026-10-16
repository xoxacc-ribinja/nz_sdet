# Python code style — NZ SDET

> **Status: proposed public learning guide.** Adapted for this personal educational repository from general Python conventions and the owner's reference notes. This is **not** a copy of any employer's internal policy, and it does not claim to be a mandatory corporate standard.

## Scope and priorities

- Applies to **new or deliberately refactored Python code**. Do not mass-reformat historical exercises just to make them look consistent.
- Review in this order: **correctness and contract → test coverage → maintainability → style**.
- A deliberate bug in an exercise is not a formatting defect to be silently corrected. State the exercise intent in the task or PR.
- Use PEP 8 and PEP 257 as defaults where this guide is silent. Rules can be challenged with a reasoned explanation.

## Formatting

- Target a maximum of **120 characters per line**.
- Use **4 spaces** for indentation; no tabs.
- Prefer **single quotes** for ordinary strings. Use double quotes when that avoids escaping an apostrophe. Docstrings use triple double quotes.
- Split long function calls and collections into readable, consistently indented multiline blocks.
- Use a blank line to separate logical sections. Avoid gratuitous whitespace and unrelated formatting changes.

Optional local formatting check (after installing Black):

```bash
python -m black --check --line-length 120 --skip-string-normalization week03/
```

To format files intentionally, remove `--check`. Do **not** run Black on the whole historical repository without agreeing to that refactor.

## Naming

- `snake_case` for functions, methods, variables and modules; `PascalCase` for classes; `UPPER_SNAKE_CASE` for constants.
- Functions should describe an **action**: `normalize_name`, `calculate_total`, `collect_failed_runs`.
- Name collections in the plural: `users`, `test_results`.
- Distinguish `file_name` (a name) from `file_path` (a path). Include units where helpful, e.g. `timeout_seconds`.
- Prefer explicit names over single letters, except short loop counters and conventional small contexts.
- Prefix module-private helpers with `_` when that improves clarity.
- Do not impose a large, workplace-specific constant-prefix catalogue on beginner exercises.

## Types

- Add parameter and return annotations to new non-trivial functions where the expected types are known.
- Prefer modern built-ins such as `list[str]` and `dict[str, int]`.
- Use `-> None` for functions that intentionally return nothing.
- Avoid redundant local annotations when a type is obvious from the assignment.
- Type hints **do not validate values at runtime**. Test input validation separately when it is part of the contract.
- For pytest test functions and simple fixtures, annotate when it adds value; do not let type hints distract from the testing objective.

```python
def normalize_name(name: str) -> str:
    return name.strip().capitalize()
```

## Comments and docstrings

- Explain **why** a non-obvious choice is needed, not what every Python expression does.
- Use a short docstring for reusable functions with a non-obvious contract. Describe inputs, output and important exceptions.
- Use PEP 257 conventions. For longer API documentation, reStructuredText fields (`:param name:`, `:return:`) are acceptable.
- Do not copy company-specific documentation templates or internal ticket references into this repository.
- Use `TODO` and `FIXME` only for actionable work; ideally link a GitHub issue.

## Imports and dependencies

- Group imports into standard library, third-party packages, and local modules.
- Avoid wildcard imports and unused imports.
- Keep imports sorted consistently; `isort` may be used locally.
- Prefer standard library solutions when they meet the assignment; introduce external dependencies only when justified.
- Do not commit credentials, local virtual environments or machine-specific absolute paths.

## Logging and errors

- Raise meaningful exceptions when the function contract requires them; do not hide errors with a bare `except:`.
- Use f-strings for ordinary human-readable text.
- When using Python's `logging`, prefer deferred interpolation:

```python
logger.info('Processed %s records', record_count)
```

- Do not introduce logging machinery into tiny exercises that only need a return value or an assertion.

## pytest and deliberate failures

- Derive expected values from the **written contract**, not from the implementation under test.
- Cover meaningful boundaries, valid/invalid inputs and error cases.
- Prefer readable parametrization when it reduces duplication without hiding the intent.
- Keep fixtures focused and avoid unnecessary shared mutable state.
- If a test is intentionally red because the production code violates the contract, document that fact in the PR. Do not change the expected value just to make the test green.
- Distinguish an intentionally broken **exercise implementation** from an accidental defect in a student's solution.

## Review checklist

- [ ] Does the behavior meet the stated task contract?
- [ ] Were relevant tests actually run? Is the command and result recorded?
- [ ] Is any red test intentional and explained?
- [ ] Are names, formatting and type hints proportionate to the exercise?
- [ ] Were inputs mutated only when the contract permits it?
- [ ] Are there any secrets, personal data or machine-specific paths?
- [ ] Can the author explain the solution without relying on AI?

## Adoption

This guide applies prospectively. Historical code is evidence of learning and is not automatically considered non-compliant. No linter score threshold or automatic CI gate is enforced until a separate tool-configuration PR is reviewed and merged.
