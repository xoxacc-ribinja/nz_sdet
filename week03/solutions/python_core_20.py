# Потратил от получаса до часа на написание функции. Тупил с разбором контракта - уж очень громоздко.
# Плюс отвлекался на домашние дела и чтение сообщений. Это исказило замер времени.
# Порадовался, когда увидел знакомые требования из сильно прошлых задач и смог вспомнить и сделать так,
# чтобы функция их выполнила. (привет dict.get()!)
# Во время выполнения задания думал, как бы написать функцию-валидатор, которая бы обрабатывала входные данные,
# чтобы я не писал каждый раз вот эти raise ValueError'ы :)
# Решение по функции самостоятельное, никаких гуглов, помощи ИИ или поисков в прошлых работах. Всё по памяти.
# На тестах возникла проблема, обсудил с агентом, нашёл критический баг функции.
# На поиск и исправление потрачено +10 минут.

def reconcile_stock(current: dict[str, int], deliveries: list[dict[str, str | int]]) -> dict[str, int]:
    result: dict[str, int] = {}
    if type(current) is not dict:
        raise ValueError('"Current" must be a dictionary!')
    if type(deliveries) is not list:
        raise ValueError('"Deliveries" must be a list!')

    for key, value in current.items():
        if type(key) is not str or key == '':
            raise ValueError('"Current" key must be a non-empty string!')
        elif type(value) is not int or value < 0:
            raise ValueError('"Current" values must be int!')

        result[key] = value

    for unit in deliveries:
        if type(unit) is not dict:
            raise ValueError('"deliveries" must be a dictionary!')
        elif type(unit.get('sku')) is not str or unit.get('sku') == '':
            raise ValueError('"sku" must be a non-empty string!')
        elif type(unit.get('quantity')) is not int or unit.get('quantity') <= 0:
            raise ValueError('"quantity" must be a non-zero positive int!')

        if not result.get(unit['sku']):
            result[unit['sku']] = unit['quantity']
        else:
            result[unit['sku']] += unit['quantity']

    return result
