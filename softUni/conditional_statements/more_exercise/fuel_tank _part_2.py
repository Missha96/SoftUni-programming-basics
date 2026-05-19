fuel_type = input()
fuel_qty = float(input())
discount_card = input()
price = float(0)
total_price = 0

if fuel_type == 'Gas':
    price = 0.93
    if 20 <= fuel_qty <= 25:
        price *= 0.92
    elif fuel_qty > 25:
        price *= 0.90
        print(price)
    elif discount_card == 'Yes':
        price = 0.93 - 0.08

elif fuel_type == 'Gasoline':
    price = 2.22
    if 20 <= fuel_qty <= 25:
        total_price *= total_price * 0.92
    elif fuel_qty > 25:
        total_price *= total_price * 0.90
    elif discount_card == 'Yes':
        price = (2.22 - 0.18)

elif fuel_type == 'Diesel':
    price = 2.33
    if 20 <= fuel_qty <= 25:
        total_price *= total_price * 0.92
    elif fuel_qty > 25:
        total_price *= total_price * 0.90
    elif discount_card == 'Yes':
        price = (2.33 - 0.12)
        total_price = (fuel_qty * price)
    print(total_price)




