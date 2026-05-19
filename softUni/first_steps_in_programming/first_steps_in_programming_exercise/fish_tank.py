lenght = int(input())
widht = int(input())
hight = int(input())
percent = float(input())

capacity  = lenght * widht * hight
litters = capacity / 1000

occupied_space = percent / 100
litters_occupied = litters * occupied_space

water_needed = litters-litters_occupied

print (water_needed)