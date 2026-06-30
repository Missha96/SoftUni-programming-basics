numbers_as_list = list(map(int, input().split(", ")))

indices = [index for index in range(len(numbers_as_list)) if numbers_as_list[index] % 2 == 0]

print(indices)