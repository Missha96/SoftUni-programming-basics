from math import floor, ceil
vineyard = int(input())
grape = float(input())
litters_wine = int(input())
workers = int(input())

total_grape_kg = vineyard * grape
grape_per_litter = 2.5
total_litters = (total_grape_kg / grape_per_litter) * 0.40

if total_litters < litters_wine:
    needed_qty = floor(litters_wine - total_litters)
    print(f'It will be a tough winter! More {needed_qty} liters wine needed.')
else:
    extra_wine = floor(total_litters - litters_wine)
    wine_per_worker = ceil(extra_wine / workers)
    print(f'Good harvest this year! Total wine: {floor(total_litters)} liters.')
    print(f'{ceil(extra_wine)} liters left -> {wine_per_worker} liters per person.')