budget = float(input())
people = int(input())
price_for_clothes = float(input())

decor = budget * 0.10
if people > 150:
    price_for_clothes -= price_for_clothes * 0.10

total = (people * price_for_clothes) + decor
if budget < total:
    print("Not enough money!")
    print(f"Wingard needs {abs(budget - total):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(budget - total):.2f} leva left.")
