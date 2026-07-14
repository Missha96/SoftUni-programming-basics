inventory = {}

while True:
    command = input()
    if command == 'statistics':
        break
    product, qty = command.split(": ")
    qty = int(qty)
    if product in inventory:
        inventory[product] += qty
    else:
        inventory[product] = qty
product_count = len(inventory)
total_count = sum(inventory.values())

print("Products in stock:")
for product, qty in inventory.items():
    print(f'- {product}: {qty}')
print(f'Total Products: {product_count}')
print(f'Total Quantity: {total_count}')