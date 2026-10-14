import unittest

from tools.validate_task_contract import validate

VALID = """# Task 21
## Контракт
Use week04/solutions/python_core_21.py
## Проверка и сдача
pytest
## Критерии PASS
Correct according to the contract.
"""


class ContractGuardTests(unittest.TestCase):
    def test_valid_contract(self):
        self.assertEqual(validate("week04/documentation/task_21.md", VALID, 4, 21), [])

    def test_wrong_week(self):
        errors = validate("week03/documentation/task_21.md", VALID, 4, 21)
        self.assertTrue(any("active week04" in e for e in errors))

    def test_wrong_solution_path(self):
        broken = VALID.replace("week04/solutions/", "week03/solutions/")
        self.assertTrue(any("outside week04" in e for e in validate(
            "week04/documentation/task_21.md", broken, 4, 21)))

    def test_missing_pass(self):
        broken = VALID.replace("## Критерии PASS", "## Пожелания")
        self.assertTrue(any("missing PASS" in e for e in validate(
            "week04/documentation/task_21.md", broken, 4, 21)))

    def test_legacy_untouched(self):
        self.assertEqual(validate("week03/documentation/task_20.md", "", 4, 21), [])


if __name__ == "__main__":
    unittest.main()
