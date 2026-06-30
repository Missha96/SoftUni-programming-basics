numbers = input(). split(", ")

positive = [num for num in numbers if int(num) >= 0]
print(f'Positive: {", ".join(positive)}')
negative = [num for num in numbers if int(num) < 0]
print(f'Negative: {", ".join(negative)}')
even = [num for num in numbers if int(num) % 2 == 0]
print(f'Even: {", ".join(even)}')
odd = [num for num in numbers if int(num) % 2 != 0]
print(f'Odd: {", ".join(odd)}')