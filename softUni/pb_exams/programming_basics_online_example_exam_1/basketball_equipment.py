year_tax = int(input())

trainers_price = year_tax * 0.60
equip_price = trainers_price * 0.80
ball_price = equip_price / 4
accesoaries_price = ball_price / 5

total = year_tax + trainers_price + equip_price + ball_price + accesoaries_price
print(f'{total:.2f}')