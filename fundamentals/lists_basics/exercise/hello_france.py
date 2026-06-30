collection_of_items = input().split('|')
budget = int(input())
initial_budget = budget
item_price = 0
train_ticket = 150
all_items = []
new_item_price = 0
for item in collection_of_items:

    item_name, item_price = item.split('->')
    item_price = float(item_price)
    clothes_max = 50.00
    shoes_max = 35.00
    accessories_max = 20.50
    if item_price <= budget:
        if item_name == 'Clothes':
            if item_price <= clothes_max:
                budget -= item_price
                new_item_price = item_price * 1.40
                all_items.append(f'{new_item_price:.2f}')
        elif item_name == 'Shoes':
            if item_price <= shoes_max:
                budget -= item_price
                new_item_price = item_price * 1.40
                all_items.append(f'{new_item_price:.2f}')
        elif item_name == 'Accessories':
            if item_price <= accessories_max:
                budget -= item_price
                new_item_price = item_price * 1.40
                all_items.append(f'{new_item_price:.2f}')

formated_all_items = " ".join(str(x) for x in all_items)
print(formated_all_items)
budget_after = list(map(float, all_items))
total_earnings = sum(budget_after)
profit = abs(total_earnings - initial_budget + budget)
print(f'Profit: {profit:.2f}')

if (total_earnings + budget) >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
