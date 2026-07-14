products = input().split()
searched_products = input().split()
inventory = {}
for i in range(0, len(products), 2):
    product = products[i]
    qty = products[i + 1]
    inventory[product] = qty
for product in searched_products:
    if product in inventory:
        print(f'We have {inventory[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")
