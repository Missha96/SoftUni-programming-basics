number = int(input())
sum_number = 0
while True:
    new_number = int(input())
    sum_number += new_number
    if sum_number >= number:
        print(sum_number)
        break