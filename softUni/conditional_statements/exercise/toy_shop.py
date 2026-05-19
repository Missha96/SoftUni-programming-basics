price_of_vacation = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
truck = int(input())

puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

total = ((puzzle * puzzle_price) + (doll * doll_price) + (bear * bear_price) + (minion * minion_price) + (truck * truck_price))

qtty = puzzle + doll + bear + minion + truck

if qtty >= 50:
    total *= 0.75
rent = total * 0.10
profit = total - rent

difference = abs(profit - price_of_vacation)

if profit >= price_of_vacation:
    print(f'Yes! {difference:.2f} lv left.')
else:
    print(f'Not enough money! {difference:.2f} lv needed.')