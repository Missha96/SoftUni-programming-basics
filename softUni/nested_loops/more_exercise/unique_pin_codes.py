first = 0
second = 0
third = 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

first_limit = int(input())
second_limit = int(input())
third_limit = int(input())

for first in range(1, first_limit + 1):
    for second in range(1, second_limit + 1):
        for third in range(1, third_limit + 1):
            if first % 2 == 0 and third % 2 == 0 and is_prime(second):
                print(first, second, third)

