chiken_menu_qty = int(input())
fish_menu_qty = int(input())
vegetarian_menu_qty = int(input())

price_for_chiken = 10.35
price_for_fish = 12.40
price_for_vegetarian = 8.15
delivery = 2.50

total_for_food = (chiken_menu_qty * price_for_chiken) + (fish_menu_qty * price_for_fish) + (vegetarian_menu_qty * price_for_vegetarian)

dessert = total_for_food * 0.20

total = total_for_food + dessert + delivery

print(total)