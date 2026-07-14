inventory = {

}
while True:
    command = input().split()
    if command[0] == 'buy':
        break
    product = command[0]
    price = float(command[1])
    qty = int(command[2])
    if product not in inventory.keys():
        inventory[product] = {"price": price, "qty": qty}
    elif product in inventory.keys():
        inventory[product]["qty"] += qty
        if inventory[product]["price"] != price:
            inventory[product]["price"] = price
for product, info in inventory.items():
    float_price = info["price"]
    int_qty = info["qty"]
    total_price = float_price * int_qty
    print(f'{product} -> {total_price:.2f}')

