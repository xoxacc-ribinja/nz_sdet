# Task 13 — Retry Decision Engine (исторический контракт)

**Источник:** полный текст задания в учебном чате, 2026-10-07. Восстановлено задним числом; критерии не изменяются.

Написать одну функцию принятия решения тестового раннера:

```python
def decide_retry_action(test_name, attempt, max_attempts, error_type):
    ...
```

`attempt` — номер **только что завершившейся неудачной попытки**, `max_attempts` — общее допустимое число попыток. Возвращается **ровно** одна строка: `RETRY`, `STOP`, `QUARANTINE` или `INVALID`.

## Приоритет правил

1. Сначала `INVALID`, если имя теста — пустая строка, `attempt < 1`, `max_attempts < 1`, `attempt > max_attempts` или `error_type` не входит в `TIMEOUT`, `NETWORK`, `ASSERTION`, `CRASH`.
2. Валидный `ASSERTION` → `STOP` всегда.
3. Валидный `CRASH` → `QUARANTINE` всегда, независимо от оставшихся попыток.
4. Валидные `TIMEOUT` и `NETWORK` → `RETRY`, если `attempt < max_attempts`, иначе `STOP`.

**Важная граница исторического контракта:** `None`, `float`, строки вместо чисел и другие неожиданные типы обрабатывать не требовалось.

## Примеры

```python
decide_retry_action('test_payment', 1, 3, 'TIMEOUT')   # 'RETRY'
decide_retry_action('test_payment', 3, 3, 'TIMEOUT')   # 'STOP'
decide_retry_action('test_login', 1, 3, 'ASSERTION')   # 'STOP'
decide_retry_action('test_worker', 1, 3, 'CRASH')      # 'QUARANTINE'
decide_retry_action('', 1, 3, 'NETWORK')              # 'INVALID'
decide_retry_action('test_api', 4, 3, 'NETWORK')       # 'INVALID'
```

## Ограничения и PASS

- Не использовать циклы, списки или словари для агрегирования, классы, внешние библиотеки; не копировать предыдущие задания.
- Не оценивались type hints, docstrings, корпоративный стиль, чтение файлов.
- AI/code completion для готового решения не использовать; поиск синтаксиса разрешён при последующем указании.
- Проверялись перечисленные невалидные случаи, **приоритет** правил, поведение всех четырёх типов ошибок, hidden inputs и защита решений.

**Исторический статус:** функциональный PASS и отдельная скрытая проверка на 540 комбинациях по сохранённому диалогу; это историческое свидетельство, не текущий повторный прогон.
