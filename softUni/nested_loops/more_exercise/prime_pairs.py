first_start = int(input())
second_start = int(input())
first_difference = int(input())
second_difference = int(input())

first_end = first_start + first_difference
second_end = second_start + second_difference


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for first in range(first_start, first_end + 1):
    for second in range(second_start, second_end + 1):
        if is_prime(first) and is_prime(second):
            print(f'{first}{second}')
