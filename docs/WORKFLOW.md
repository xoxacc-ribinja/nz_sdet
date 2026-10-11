# Workflow: learning tasks and reviews

## Roles

- **Student:** writes solutions, runs tests, explains decisions and owns final code.
- **Assistant:** formulates assignments, reviews changes and updates documentation with clear evidence; does not mark PASS by assumption.

## Daily comprehension warm-up

On the student's first message of a calendar day in the learning chat, offer **3–4 short questions** on previously covered Python Core, pytest, Git and test-design concepts. Rotate subjects and occasionally revisit older material. Answers should be possible directly in chat **without writing or running code**; after the student answers, briefly review the reasoning and correct misconceptions.

These warm-ups are for retention, **not extra PASS criteria**, and must not change the contract of an active task. If the student explicitly wants to finish an ongoing task first, handle that work before the warm-up. Do not create a scheduled reminder or unsolicited notification: the warm-up is part of an active chat exchange.

## Workload and retention checks

- **Historical weekly target: 3–5 hours; new budget pending agreement.** Do not increase hours automatically because recall is difficult. The target is an orientation, not a quota to compensate for missed days.
- Reduce nearly identical exercises. Reuse already taught tools in different problem contexts; do not increase difficulty or introduce unannounced syntax merely for novelty.
- Practice retrieval without hints through daily verbal warm-ups and revisit previously covered concepts after several days (spaced repetition).
- During review, report **correctness** separately from **independence**: solved without help / after a leading hint / after a full explanation. These labels are diagnostic, not extra acceptance criteria or grounds for retroactive regrading.
- In daily learning summaries distinguish time spent **writing code**, **engineering work** (requirements, test design, debugging, reviews, Git), and **process overhead** (resolving avoidable administrative mistakes). Do not present process overhead as coding practice. Do not invent precise splits where only estimates are available.
- Keep published task contracts and PASS criteria unchanged unless the student explicitly agrees to an update.

## Bug Investigation

Use Bug Investigation as a recurring exercise format alongside implementation and test design. Publish the full task contract first. The learner analyzes an unknown failure, reads the traceback and pytest output, proposes a root-cause hypothesis, finds and fixes the defect with a minimal change, and verifies by running tests. Distinguish detecting a defect from independently diagnosing it. Explain unfamiliar tools before requiring them.

Read small unfamiliar codebases only occasionally, without displacing the student's own coding. Do not require pytest internals, external open-source PRs, fixed weekly themes, or a day-by-day schedule. A new weekly hour budget is pending agreement.

## Task publication and fixed acceptance criteria

**Before any new task is assigned for implementation**, the assistant must:

1. Read the repository guidance: `README.md`, `PROJECT_STATE.md`, `LEARNING_LOG.md`, `DECISIONS.md`, `docs/WORKFLOW.md`, `ROADMAP.md` and the relevant existing tasks.
2. Publish a numbered assignment Markdown file under `weekXX/documentation/task_NN.md` in GitHub, with an explicit contract, expected outputs/exceptions, scope, constraints, and PASS criteria. Provide its link to the student. The assignment must be available **before coding starts**, not reconstructed after completion.
3. Explain any new Python syntax, APIs or testing techniques **before** requiring them in an exercise. New constructs cannot appear as unannounced mandatory requirements.
4. Keep assessment against the published, agreed criteria. Do not introduce new mandatory edge cases, test counts, tools, or acceptance conditions mid-review.
5. If a change to requirements is genuinely needed, discuss it first, obtain agreement, and update the assignment in GitHub **before** evaluating against it. Never retroactively revoke an already accepted PASS.

## Work cycle

1. Confirm that the assignment is published in GitHub and review its fixed criteria.
2. Create a branch, e.g. `task/17`, from up-to-date `main`.
3. Implement without copying an AI-generated solution. Record any assistance used.
4. Run targeted checks and capture command plus meaningful output.
5. Push and open a Pull Request. Link task, summarize approach and unresolved questions.
6. Review diff and discuss boundary cases, independent decisions and regressions.
7. Merge only after the owner accepts the result. Update `LEARNING_LOG.md` and `PROJECT_STATE.md`.

## Assistant documentation check

Before proposing a new task, reviewing a submission, recording PASS, or writing to GitHub, re-read the relevant repository documents and current assignment instead of relying only on chat context. If a document is outdated, flag it and propose a documentation change through a PR; do not silently assume it reflects the current state.

## GitHub access boundaries

- **Only repository:** `xoxacc-ribinja/nz_sdet`.
- **Only connection:** GitHub account `xoxacc-ribinja` (ChatGPT connection `Xoxacc_SDET`).
- Never modify repositories owned by `rpgarchive`.
- Before each write, verify the exact owner/repository and target branch.
- Prefer PRs to direct commits to `main`. Never force-push or rewrite historical submissions without explicit agreement.

## Hidden checks after defense

After a student submits a solution and completes code review and oral defense, the assistant may **occasionally** check the code with previously undisclosed input data. This is not mandatory for every task.

- Hidden inputs must follow the **original or explicitly agreed updated contract**; no surprise requirements or retroactive grading criteria.
- Do not disclose exact inputs before the defense. Keep the concrete cases out of the public assignment and PR until the check has been completed.
- Check meaningful boundaries and robustness, including empty collections, duplicates, ordering, invalid inputs and unwanted mutation **only when relevant to the contract**.
- If a runnable environment is available, execute the solution with the hidden inputs and record actual results. Otherwise describe the check as an unexecuted review or ask for a local run; never claim that unrun tests passed.
- After checking, explain failed cases and expected behavior. The student should diagnose and fix defects independently before another review.
- Record whether a hidden check was performed and its result in the learning log. Do not make every task a guessing game.

## Request decomposition and completion check

For a multi-part request, explicitly separate requested **actions**, **outputs** and **object-specific constraints**. A restriction on one output (e.g. “NZ Daily only in chat”) does not prohibit a separate requested GitHub documentation update.

Before closing a multi-step request, verify every deliverable against the request; distinguish prepared locally, written to a branch, PR opened, merged into main, and tests actually run. After GitHub writes, **read back** the target files from the target branch; inspect the PR file list, do not infer completion from a successful write API response.

When documenting earlier exercises, label original historical contracts separately from later reconstructions or reviews. Never change old PASS criteria retroactively or portray a retroactively published task as published before work.

## Reporting cadence and recovery

- **NZ DAILY**, **NZ WEEKLY** and monthly summaries are available on request; do not automatically post reports or schedule reminders. The report destination is determined per user instruction.
- Distinguish real coding time, engineering work, and process overhead; do not treat missed study days as debt or automatically increase weekly hours.
- End-of-November check is a diagnostic skills gate (historically proposed 60–90 min unfamiliar Python task without AI and defense), not a rigid deadline or new PASS requirement.

## Evidence and reporting

- A failing test can be correct when it exposes a defect in code under test.
- A saved log is historical evidence, not a guarantee of current CI health.
- Publish only technical information safe for a public repository.
- Use `reports/templates/` for public, concise summaries. Keep private notes outside Git.

## Restoring context

Read in this order: `README.md` → `PROJECT_STATE.md` → `LEARNING_LOG.md` → `DECISIONS.md` → current task and PR.
