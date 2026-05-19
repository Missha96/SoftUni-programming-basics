animals = input().split(", ")

position = animals.index("wolf")

if position == len(animals) - 1:
    print("Please go away and stop eating my sheep")
    sheep_number = len(animals) - 1

else:
    sheep_number = len(animals) - position - 1
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")