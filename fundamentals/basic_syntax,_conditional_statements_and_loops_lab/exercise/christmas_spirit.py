decorations_qty = int(input())
days_until_christmas = int(input())

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
spirit = 0
total = 0

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        decorations_qty += 2
    if day % 2 == 0:
        total += ornament_set_price * decorations_qty
        spirit += 5
    if day % 3 == 0:
        total += tree_skirt_price * decorations_qty + tree_garland_price * decorations_qty
        spirit += 3 + 10
    if day % 5 == 0:
        total += tree_lights_price * decorations_qty
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        total += tree_skirt_price + tree_garland_price + tree_lights_price
if days_until_christmas % 10 == 0:
    spirit -= 30
print(f"Total cost: {total}")
print(f"Total spirit: {spirit}")


