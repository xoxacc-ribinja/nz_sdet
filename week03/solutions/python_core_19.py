# На написание функции потратил примерно 25 минут. Сверялся с контрактом постоянно,
# на каждое условие контракта делал проверку в функции. Каких-то затыков или проблем не обнаружил. Ни с чем не сверялся,
# никуда не подсматривал. Чисто на уже ранее отработанных схемах писал. Просто мы уже это делали только что. :(

def buy_item(coins: int, price: int, inventory: list[str], item_name: str) -> dict:
    new_inventory = []
    result: dict[str, int | list[str]] = {}
    if type(coins) != int or coins < 0:
        raise ValueError('Invalid coins value!')
    if type(price) != int or price <= 0:
        raise ValueError('Invalid price value!')
    if type(inventory) != list:
        raise ValueError('Invalid inventory list!')
    if type(item_name) != str or item_name == '':
        raise ValueError('Invalid item name!')
    if coins < price:
        raise ValueError('Not enough coins!')

    for item in inventory:
        if type(item) != str or item == '':
            raise ValueError('Invalid item in inventory!')
        else:
            new_inventory.append(item)
    new_inventory.append(item_name)
    result['coins'] = coins - price
    result['inventory'] = new_inventory

    return result
