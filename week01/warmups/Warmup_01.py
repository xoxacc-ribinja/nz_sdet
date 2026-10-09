DURATIONS = [
    '18',
    'fast',
    '42',
    '-5',
    '0',
    'slow',
    '63',
]


def parse_durations(durations):
    valid = []
    invalid = []
    for duration in durations:
        try:
            check_duration = int(duration)
        except ValueError:
            invalid.append(duration)
            continue
        if check_duration >= 0:
            valid.append(check_duration)
        else:
            invalid.append(duration)

    return valid, invalid


# Она должна вернуть два списка:
# 1. valid — числа, которые удалось преобразовать в int и которые >= 0. Хранить именно как int.
# 2. invalid — исходные строки, которые нельзя преобразовать в int или которые после преобразования оказались < 0.
# Для данных выше результат должен быть:
# valid == [18, 42, 0, 63]invalid == ['fast', '-5', 'slow']