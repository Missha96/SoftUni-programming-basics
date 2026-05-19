season = input()
km = float(input())

price = 0

if km <= 5000:
    if (season == "Spring") or (season == "Autumn"):
        price = 0.75
    elif season == 'Summer':
        price = 0.90
    elif season == "Winter":
        price = 1.05
if 5000 < km <= 10000:
    if (season == 'Spring') or (season == 'Autumn'):
        price = 0.95
    elif season == 'Summer':
        price = 1.10
    elif season == "Winter":
        price = 1.25
if 10000 < km <= 20000:
    price = 1.45

salary = ((price * km) * 4) * 0.90
print(f'{salary:.2f}')
