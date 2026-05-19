import sys
from sys import maxsize

n = int(input())

max_number = -maxsize
total_sum = 0

for _ in range(n):
    new_number = int(input())
    total_sum += new_number
    if new_number > max_number:
        max_number = new_number

if (total_sum - max_number) == max_number:
    print(f'Yes\nSum = {max_number}')
else:
    diff = max_number - (total_sum - max_number)
    print(f'No\nDiff = {abs(diff)}')
