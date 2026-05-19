n = int(input())

for num in range(1111, 9999 + 1):
    text_num = str(num)
    for position in range(len(str(num))):
        if position > 0:
            if n % position[0] == 0:
                special_number = num
                print(special_number)