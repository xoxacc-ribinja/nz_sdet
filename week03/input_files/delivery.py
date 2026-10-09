def delivery_cost(weight, express):
    if weight <= 0:
        raise ValueError('Weight must be positive')
    if weight <= 1:
        cost = 200
    elif weight < 5:
        cost = 400
    else:
        cost = 700
    if express:
        cost += 300
    return cost