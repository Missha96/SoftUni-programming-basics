from math import ceil
guests = int(input())
budget = int(input())

sweat_bread = 4.00
egg = 0.45

bread = guests / 3
eggs = guests * 2

breads = ceil(bread)
total = (breads * sweat_bread) + (eggs * egg)
if budget >= total:
    print(f"Lyubo bought {breads} Easter bread and {eggs} eggs.")
    print(f"He has {abs(total - budget):.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {abs(total - budget):.2f} lv. more.")

