from math import ceil
sweat_bread = int(input())
sugar_package = 0
flour_package = 0
total_sugar = 0
total_flour = 0
sugar_grams = []
flour_grams = []

for _ in range(sweat_bread):
    sugar = int(input())
    flour = int(input())
    total_sugar += sugar
    total_flour += flour
    sugar_grams.append(sugar)
    flour_grams.append(flour)
sugar_package = ceil(total_sugar / 950)
flour_package = ceil(total_flour / 750)
print(f'Sugar: {sugar_package}')
print(f'Flour: {flour_package}')
print(f'Max used flour is {max(flour_grams)} grams, max used sugar is {max(sugar_grams)} grams.')
