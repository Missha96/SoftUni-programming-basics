product = input()
qty = int(input())


def total_order(product: str, qty: int):
    result = None
    if product == 'coffee':
        price = 1.50
        result = price * qty
    elif product == 'water':
        price = 1.00
        result = price * qty
    elif product == 'coke':
        price = 1.40
        result = price * qty
    else:
        return None
    return f'{result:.2f}'


print(total_order(product, qty))