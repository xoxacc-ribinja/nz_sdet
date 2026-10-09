def normalize_name(name: str) -> str:
    normal_name: str = name.strip().capitalize()
    return normal_name


def is_valid_age(age: int) -> bool:
    if 18 <= age <= 65:
        return True
    else:
        return False


def prepare_users(raw_users: list[dict]) -> list[dict]:
    final_users_list: list[dict[str, str | int]] = []
    for user in raw_users:
        if is_valid_age(user['age']):
            user_info: dict[str, str | int] = {'name': normalize_name(user['name']), 'age': user['age']}
        final_users_list.append(user_info)

    return final_users_list




