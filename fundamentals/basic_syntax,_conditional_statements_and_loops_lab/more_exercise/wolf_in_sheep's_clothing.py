animals = input().split(", ")

position = animals.index("wolf")

if position == 0:
    sheep_number = len(animals) - position - 1
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")
else:
    sheep_number = len(animals) - position
    print("Please go away and stop eating my sheep")