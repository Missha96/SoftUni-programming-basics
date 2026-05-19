lili_age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

toy_counter = 0
money_saved = 0
gift_in_money = 10

for age in range(1, lili_age + 1):
    if age % 2 == 0:
        money_saved += gift_in_money
        gift_in_money += 10
        money_saved -= 1
    else:
        toy_counter += 1

money_saved += toy_counter * price_per_toy
diff = abs(money_saved - washing_machine_price)

if money_saved >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')