from math import floor, ceil
days = int(input())
total_food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

dog_food_eaten = dog_food * days
cat_food_eaten = cat_food * days
turtle_food_eaten = (turtle_food * days) / 1000

all_food_eaten = dog_food_eaten + cat_food_eaten + turtle_food_eaten
diff = abs(total_food - all_food_eaten)

if total_food >= all_food_eaten:
    print(f'{floor(diff)} kilos of food left.')
else:
    print(f'{ceil(diff)} more kilos of food are needed.')