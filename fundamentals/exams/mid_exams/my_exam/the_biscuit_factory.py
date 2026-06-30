from math import floor
biscuits_per_day = int(input())
workers = int(input())
competing_factory_biscuits = int(input())
day = 0
month = 30
total_biscuits = 0
percentage = 0
difference = 0
for day in range(month):
    day += 1
    if day % 3 == 0:
        total_biscuits += floor((biscuits_per_day * workers) * 0.75)
    else:
        total_biscuits += biscuits_per_day * workers
print(f"You have produced {total_biscuits} biscuits for the past month.")

if total_biscuits > competing_factory_biscuits:
    difference = total_biscuits - competing_factory_biscuits
    percentage = (difference / competing_factory_biscuits) * 100
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    difference = total_biscuits - competing_factory_biscuits
    percentage = (difference / competing_factory_biscuits) * 100
    print(f"You produce {abs(percentage):.2f} percent less biscuits.")

