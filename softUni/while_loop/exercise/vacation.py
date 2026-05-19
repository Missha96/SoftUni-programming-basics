vacation_price = float(input())
own_money = float(input())

days = 0
spending_days = 0

while own_money < vacation_price and spending_days < 5:
    command = input()
    money = float(input())
    days += 1
    if command == 'save':
        own_money += money
        spending_days = 0
    elif command == 'spend':
        own_money -= money
        spending_days += 1
        if own_money < 0:
            own_money = 0

if spending_days >= 5:
    print("You can't save the money.")
    print(f'{days}')
if own_money >= vacation_price:
    print(f"You saved the money for {days} days.")