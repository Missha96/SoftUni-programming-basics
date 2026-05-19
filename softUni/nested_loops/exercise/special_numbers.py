n = int(input())
special_num = 0


for idx in range(1111, 9999 + 1):
    num_str = str(idx)
    is_special = True

    for char in num_str:
        digit = int(char)
        if digit == 0 or n % digit != 0:
            is_special = False
            break
    if is_special:
        print(idx, end=' ')


