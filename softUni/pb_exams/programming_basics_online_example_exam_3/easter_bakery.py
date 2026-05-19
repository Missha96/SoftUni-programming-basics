flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs = int(input())
yeast = int(input())


sugar_price = flour_price * 0.75
eggs_price = flour_price * 1.10
yeast_price = sugar_price * 0.20

total = (flour_kg * flour_price) + (sugar_price * sugar_kg) + (eggs_price * eggs) + (yeast_price * yeast)
print(f'{total:.2f}')