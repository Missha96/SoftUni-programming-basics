flower_type = input()
qty = int(input())
budget = int(input())

price = 0
total = int()

if flower_type == "Roses":
    price = 5
    if qty > 80:
        total = (price * qty) * 0.90
    else:
        total = price * qty
if flower_type == "Dahlias":
    price = 3.80
    if qty > 90:
        total = (price * qty) * 0.85
    else:
        total = price * qty
if flower_type == "Tulips":
    price = 2.80
    if qty > 80:
        total = (price * qty) * 0.85
    else:
        total = price * qty
if flower_type == "Narcissus":
    price = 3
    if qty < 120:
        total = (price * qty) * 1.15
    else:
        total = price * qty
if flower_type == "Gladiolus":
    price = 2.50
    if qty < 80:
        total = (price * qty) * 1.20
    else:
        total = price * qty

difference = abs(budget - total)

if budget >= total:
    print(f'Hey, you have a great garden with {qty} {flower_type} and {difference:.2f} leva left.')
else:
    print(f'Not enough money, you need {difference:.2f} leva more.')