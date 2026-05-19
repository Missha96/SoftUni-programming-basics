cargo = int(input())
bus = 0
truck = 0
train = 0
total = 0
price_bus = 200
price_truck = 175
price_train = 120

for _ in range(cargo):
    ton = int(input())
    if ton <= 3:
        bus += ton
        total += ton
    elif 4 <= ton <= 11:
        truck += ton
        total += ton
    else:
        train += ton
        total += ton

avr_price = ((bus * price_bus) + (truck * price_truck) + (train * price_train)) / total

print(f'{avr_price:.2f}')
print(f'{(bus / total * 100):.2f}%')
print(f'{(truck / total * 100):.2f}%')
print(f'{(train / total * 100):.2f}%')
