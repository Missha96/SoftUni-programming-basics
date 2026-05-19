divisor = int(input())
boundary = int(input())
numbers = []


for num in range(1, boundary + 1):
    if (num % divisor == 0) and (num > 0) and (num <= boundary):
        numbers.append(num)
print(max(numbers))
