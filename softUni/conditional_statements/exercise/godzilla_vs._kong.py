budget = float(input())
people = int(input())
clothes_price = float(input())

decor = budget * 0.10
clothes = people * clothes_price

if people > 150:
    clothes *= 0.90

expenses = decor + clothes
difference = abs(budget - expenses)

if expenses > budget:
    print('Not enough money!')
    print(f'Wingard needs {difference:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {difference:.2f} leva left.')
