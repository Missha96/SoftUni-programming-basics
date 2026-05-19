n = int(input())

current_number = 0
odd_sum = 0
odd_min = None
odd_max = None
even_sum = 0
even_min = None
even_max = None
counter = 1

for _ in range(1, n + 1):
    number = float(input())
    current_number = number
    if counter % 2 == 0:
        even_sum += current_number
        if even_min is None or current_number < even_min:
            even_min = current_number
        if even_max is None or current_number > even_max:
            even_max = current_number
    elif counter % 2 != 0:
        odd_sum += current_number
        if odd_min is None or current_number < odd_min:
            odd_min = current_number
        if odd_max is None or current_number > odd_max:
            odd_max = current_number
    counter += 1

print(f'OddSum={odd_sum:.2f},')
print(f'OddMin={f"{odd_min:.2f}" if odd_min is not None else "No"},')
print(f'OddMax={f"{odd_max:.2f}" if odd_max is not None else "No"},')
print(f'EvenSum={even_sum:.2f},')
print(f'EvenMin={f"{even_min:.2f}" if even_min is not None else "No"},')
print(f'EvenMax={f"{even_max:.2f}" if even_max is not None else "No"}')

