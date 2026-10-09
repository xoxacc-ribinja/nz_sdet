# Task 07 — Test Duration Validator

## Входной файл `test_durations.txt`

```text
login_test,PASSED,18
checkout_test,FAILED,42
api_test,PASSED,fast
broken_line
search_test,SKIPPED,27
profile_test,PASSED,35
payment_test,BROKEN,51
report_test,FAILED,-5
ui_test,PASSED,63
```

Формат: `test_name,status,duration`.
Допустимые статусы: `PASSED`, `FAILED`, `SKIPPED`.
`duration` должна преобразовываться в `int` и быть >= 0.

## Требования

Строка невалидна, если:
1. полей не ровно 3;
2. статус недопустим;
3. `duration` нельзя преобразовать в `int`;
4. `duration < 0`.

Для валидной записи `duration` хранить уже как `int`.

Вывести количество валидных/невалидных записей, счётчики по статусам, общую и среднюю duration (до 2 знаков), список исходных невалидных строк.

Ожидаемо:

```text
Valid tests: 5
Invalid lines: 4

By status:
PASSED: 3
FAILED: 1
SKIPPED: 1

Total duration: 185
Average duration: 37.0

Invalid input:
- api_test,PASSED,fast
- broken_line
- payment_test,BROKEN,51
- report_test,FAILED,-5
```

## Ограничения

- Файл читать ровно один раз.
- Использовать функции и параметры.
- Все функции: type hints параметров и return.
- Пустые локальные коллекции аннотировать.
- Ошибку преобразования duration обрабатывать именно `try/except ValueError`.
- Голый `except:` запрещён.
- Использовать `continue` там, где естественно.
- Другие exception в этой задаче специально не ловить.
- Не использовать `class`, `set`, `Counter`, `max`, `sort`, внешние библиотеки.
- Решение писать без AI; вопросы по синтаксису/ошибкам допустимы.

## PASS

Вывод совпадает; программа не падает на `fast`; валидная duration хранится как `int`; файл читается один раз; `ValueError` обработан явно; type hints соответствуют данным; на защите объясняются `ValueError`, `continue` и преобразование `str -> int`.
