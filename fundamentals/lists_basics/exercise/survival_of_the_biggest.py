numbers = input().split()
count_of_numbers_to_remove = int(input())

numbers_int = []
for number in numbers:
    numbers_int.append(int(number))

for num in range(count_of_numbers_to_remove):
    numbers_int.remove(min(numbers_int))
result = ", ".join(str(x) for x in numbers_int)
print(result)
