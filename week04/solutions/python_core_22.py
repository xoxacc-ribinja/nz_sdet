def first_adjacent_duplicate(steps: list[str]) -> tuple[int, str] | None:
    if len(steps) < 2:
        return None
    for index, value in enumerate(steps):
        if steps[index-1] == steps[index] and index != 0:
            return index, value

    return None

# При выборе алгоритма столкнулся с забавным багом в случае steps=['API','DB','API'].
# Если выбирать steps[index-1] == steps[index], то программа посчитает 0 и -1 элементы списка.
# То есть, прочитает первый и последний элемент. И в указанном случае даст неверный результат.