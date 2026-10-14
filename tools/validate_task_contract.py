"""Validate NEW/CHANGED task contracts, not historical submissions.

Usage: python tools/validate_task_contract.py [paths...]
No arguments: validate documentation paths changed against origin/main.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASK_RE = re.compile(r"^week(\d{2})/documentation/task_(\d+)\.md$")
PATH_RE = re.compile(r"week\d{2}/(?:solutions|documentation|input_files)/[^\s\x60)]+")
REQUIRED = ("##", "PASS", "Контракт")


def validate(path: str, text: str, active_week: int, first_guarded_task: int) -> list[str]:
    issues = []
    normalized = path.replace("\\", "/")
    match = TASK_RE.fullmatch(normalized)
    if not match:
        if re.search(r"task_\d+\.md$", normalized):
            return [f"{path}: contract must be weekXX/documentation/task_N.md"]
        return []
    week, task = map(int, match.groups())
    if task < first_guarded_task:
        return []
    if week != active_week:
        issues.append(f"{path}: task {task} belongs to active week{active_week:02d}, not week{week:02d}")
    if not text.lstrip().startswith("# "):
        issues.append(f"{path}: missing H1 title")
    if not re.search(r"(?im)^#{1,4}\s+.*(?:PASS|критерии\s+приёмки)", text):
        issues.append(f"{path}: missing PASS/acceptance heading")
    if not re.search(r"(?im)^#{1,4}\s+.*(?:контракт|функци|услови|требовани)", text):
        issues.append(f"{path}: missing contract/behavior heading")
    if not re.search(r"(?im)^#{1,4}\s+.*(?:сдач|проверк|тест)", text):
        issues.append(f"{path}: missing submission/check heading")
    # Warn against accidental paths pointing to a different week.
    for candidate in set(PATH_RE.findall(text)):
        if not candidate.startswith(f"week{week:02d}/"):
            issues.append(f"{path}: referenced path {candidate} points outside week{week:02d}")
    return issues


def changed_paths() -> list[str]:
    proc = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", "origin/main...HEAD"],
        cwd=ROOT, text=True, capture_output=True, check=True
    )
    return proc.stdout.splitlines()


def main(args: list[str]) -> int:
    cfg = json.loads((ROOT / "docs/ACTIVE_WEEK.json").read_text(encoding="utf-8"))
    paths = args if args else changed_paths()
    errors = []
    checked = 0
    for path in paths:
        if not (path.startswith("week") and path.endswith(".md") and "task_" in path):
            continue
        target = ROOT / path
        if not target.is_file():
            continue
        checked += 1
        errors.extend(validate(path, target.read_text(encoding="utf-8"),
                               cfg["active_week"], cfg["first_guarded_task"]))
    for err in errors:
        print("ERROR:", err)
    print(f"Contract guard: checked {checked} file(s), {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
