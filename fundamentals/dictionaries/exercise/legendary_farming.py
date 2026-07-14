
materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item_obtained = False
legendary_item = ""

while not legendary_item_obtained:
    current_materials = input().split()
    for index in range(0, len(current_materials), 2):
        material = current_materials[index + 1].lower()
        qty = int(current_materials[index])
        if material not in materials.keys():
            materials[material] = 0
        materials[material] += qty
        if materials["shards"] >= 250:
            legendary_item_obtained = True
            materials["shards"] -= 250
            legendary_item = 'Shadowmourne'
        elif materials["fragments"] >= 250:
            legendary_item_obtained = True
            materials["fragments"] -= 250
            legendary_item = 'Valanyr'
        elif materials["motes"] >= 250:
            legendary_item_obtained = True
            materials["motes"] -= 250
            legendary_item = 'Dragonwrath'
        if legendary_item_obtained:
            break
print(f"{legendary_item} obtained!")
for material, qty  in materials.items():
    print(f'{material}: {qty}')
