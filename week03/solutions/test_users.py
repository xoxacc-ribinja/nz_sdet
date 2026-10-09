import pytest

@pytest.fixture
def users():
    return [
        {"name": "Jane", "active": True, "role": "admin"},
        {"name": "Mike", "active": False, "role": "admin"},
        {"name": "Peter", "active": True, "role": "user"},
        {"name": "Victoria", "active": False, "role": "user"}
    ]


def test_users_count(users):
    assert len(users) == 4


def test_active_users(users):
    active_users = 0
    for user in users:
        if user["active"]:
            active_users += 1
    assert active_users == 2


def test_admins_count(users):
    admins = 0
    for user in users:
        if user["role"] == "admin":
            admins += 1
    assert admins == 2


def test_active_admins(users):
    active_admins = 0
    for user in users:
        if user["role"] == "admin" and user["active"]:
            active_admins += 1
    assert active_admins == 1
