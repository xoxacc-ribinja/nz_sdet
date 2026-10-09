Task 08 — Build History Analyzer


Есть файл **build_history.txt:**
frontend,PASSED,128
backend,FAILED,94
api,PASSED,76
frontend,FAILED,135
backend,PASSED,101
worker,BROKEN,82
api,PASSED,fast
frontend,PASSED,119
database,FAILED,67
backend,PASSED,88

Формат:
component,status,duration

Допустимые статусы:
['PASSED', 'FAILED', 'BROKEN']


Строка считается невалидной, если количество полей не равно 3, статус неизвестен, duration нельзя преобразовать в int или duration < 0.
Для валидных записей нужно определить:
1. количество валидных и невалидных строк;
2. количество PASSED, FAILED, BROKEN;
3. суммарную длительность;
4. среднюю длительность;
5. последний известный статус каждого компонента.
То есть для frontend:
frontend,PASSED,128
frontend,FAILED,135
frontend,PASSED,119

итоговый статус:
frontend: PASSED

Ожидаемый результат для данных выше:
Valid builds: 9
Invalid lines: 1

By status:
PASSED: 5
FAILED: 3
BROKEN: 1

Total duration: 890
Average duration: 98.89

Final component status:
frontend: PASSED
backend: PASSED
api: PASSED
worker: BROKEN
database: FAILED

Тут специально есть сочетание уже изученных механизмов: 
parsing, validation, try/except/continue, dict-counter и 
словарь, где повторное присваивание одному ключу естественным образом оставляет последний статус.

Ограничения: 
файл читается один раз; 
минимум 4 функции; 
все функции имеют type hints; 
локальные коллекции аннотируй по корпоративному стилю; 
docstrings — по вашему code_style; 
Counter, max, sort, set, классы и внешние библиотеки не использовать. 
Единственная новая библиотека — pathlib.

И главное новое требование:
from pathlib import Path


Путь к build_history.txt должен строиться относительно расположения самого .py, не относительно CWD.
PASS criteria
Программа должна дать указанный результат, 
не падать на fast, 
хранить валидную duration как int, 
прочитать файл ровно один раз и 
продолжить работать, если запустить тот же .py из другой рабочей директории.