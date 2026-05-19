n = int(input())
sum_odd = 0
sum_even = 0

for idx in range(n):
    new_number = int(input())
    if idx % 2 == 0:
        sum_even += new_number
    else:
        sum_odd += new_number

if sum_even == sum_odd:
    print(f'Yes\nSum = {sum_even}')
else:
    print(f'No\nDiff = {abs(sum_even - sum_odd)}')
