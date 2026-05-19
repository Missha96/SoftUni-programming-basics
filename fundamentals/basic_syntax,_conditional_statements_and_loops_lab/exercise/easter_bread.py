budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25
colored_eggs_qty = 0
loaves = 0
recipe = eggs_price + flour_price + (milk_price / 4)
bread = 0

while budget >= recipe:
    budget -= recipe
    loaves += 1
    bread += 1
    colored_eggs_qty += 3
    if loaves == 3:
        colored_eggs_qty -= (bread - 2)
        loaves = 0
print(f'You made {bread} loaves of Easter bread! Now you have {colored_eggs_qty} eggs and {budget:.2f}BGN left.')
