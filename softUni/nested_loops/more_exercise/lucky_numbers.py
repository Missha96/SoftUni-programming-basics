n = int(input())

for num in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range (1, 10):
            for num4 in range(1, 10):
                if (num + num2 == num3 + num4) and n % (num + num2) == 0:
                    number = str(num) + str(num2) + str(num3) + str(num4)
                    int_num = int(number)
                    if 1000 <= int_num <= 9999:
                        print(number, end=' ')