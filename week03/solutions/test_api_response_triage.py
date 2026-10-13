# На тестирование api функции ушло около 40 минут. Всё писал сам за исключением согласования записи
# обоснования проверки.
# При написании руководствовался исключительно контрактом и памятью по предыдущим упражнениям.
# Затупил на проверке требования проверки того, что функция не изменяет входные аргументы; внешнего состояния нет.
# По итогу с агентом решили, что можно не делать эту проверку. Но на будущее стоит где-то её вкорячить.
# Мне понравилась идея проверки и её реализация - вызвать функцию один раз, записать результат.
# Вызвать ещё пару раз с другими данными. Вызвать ещё раз с теми же данными, что и в первый раз.
# Записать последний результат. Сравнить два результата. Должны быть равны. (а == б -> True)


import pytest
from week03.input_files.api_response_triage import classify_api_response



@pytest.mark.parametrize(
    'data, expected',
    [
        (
            (100, 10, True), 'OTHER' # Verify lower 1xx status boundary
        ),
        (
            (199, 10, True), 'OTHER' # Verify upper 1xx status boundary
        ),
        (
            (109, 1010, True), 'OTHER' # Verify 1xx status independence from latency
        ),
        (
            (101, 100, False), 'OTHER'  # Verify 1xx status independence from body
        ),
        (
            (300, 10, True), 'OTHER' # Verify lower 3xx status boundary
        ),
        (
            (399, 10, True), 'OTHER' # Verify upper 3xx status boundary
        ),
        (
            (395, 1001, True), 'OTHER' # Verify 3xx status independence from latency
        ),
        (
            (300, 10, False), 'OTHER' # Verify 3xx status independence from body
        ),
        (
            (200, 10, True), 'SUCCESS' # Verify lower 2xx status boundary
        ),
        (
            (299, 10, True), 'SUCCESS' # Verify upper 2xx status boundary
        ),
        (
            (200, 0, True), 'SUCCESS' # Verify zero latency for 2xx status
        ),
        (
            (200, 1000, True), 'SUCCESS' # Verify upper latency boundary for regular 2xx status success
        ),
        (
            (299, 10, False), 'EMPTY_SUCCESS' # Verify 'no body' for 2xx
        ),
        (
            (202, 1001, True), 'SLOW_SUCCESS' # Verify slow success for 2xx status
        ),
        (
            (200, 1003, False), 'EMPTY_SUCCESS' # Verify 'empty success' even for big latency for 2xx status
        ),
        (
            (400, 1, True), 'CLIENT_ERROR' # Verify lower 4xx status boundary
        ),
        (
            (499, 1, True), 'CLIENT_ERROR' # Verify upper 4xx status boundary
        ),
        (
            (400, 1, False), 'CLIENT_ERROR' # Verify 4xx status independence from body
        ),
        (
            (400, 1001, True), 'CLIENT_ERROR' # Verify 4xx status independence from latency
        ),
        (
            (500, 1, True), 'SERVER_ERROR' # Verify lower 5xx status boundary
        ),
        (
            (599, 1, True), 'SERVER_ERROR' # Verify upper 5xx status boundary
        ),
        (
            (500, 1, False), 'SERVER_ERROR' # Verify 5xx status independence from body
        ),
        (
            (500, 1001, True), 'SERVER_ERROR' # Verify 5xx status independence from latency
        ),
    ]
)
def test_verify_statuses(data, expected):
    assert classify_api_response(*data) == expected


@pytest.mark.parametrize(
    'data',
    [
        (99, 1, True), # Verify ValueError on status_code < 100
        (600, 1, True), # Verify ValueError on status_code > 599
        (0, 1, True), # Probably, excess check, but 0 is a special int...
        (0.5, 1, True), # Verify ValueError on status_code is not int
        (-100, 1, True), # Probably, excess check, but who knows the behavior with negative numbers...
        (True, 1, True), # Verify ValueError on status_code is bool
        ('100', -1, True), # Verify ValueError on status_code is any other type
        (100, -1, True), # Verify ValueError on latency < 0
        (100, 1.0, True), # Verify ValueError on latency is not int
        (100, True, True), # Verify ValueError on latency is bool
        (100, '1', True), # Verify ValueError on latency is other type
        (100, 1, 'True'), # Verify ValueError on body is other type
        (100, 1, 1), # Verify ValueError on body is int (not bool)

    ]
)
def test_invalid_data(data):
    with pytest.raises(ValueError):
        classify_api_response(*data)

