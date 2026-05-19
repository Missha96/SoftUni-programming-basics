movie_type = input()
rows = int(input())
columns = int(input())

income = 0
capacity = rows * columns

if movie_type == "Premiere":
    income = 12
elif movie_type == "Normal":
    income = 7.50
elif movie_type == "Discount":
    income = 5

if income > 0:
    total = capacity * income
    print(f'{total:.2f} leva')
