start = int(input())
end = int(input())

for num1 in range(start, end + 1):
    for num2 in range(start, end + 1):
        for num3 in range(start, end +1):
            for num4 in range(start, end + 1):
                if (num2 + num3) % 2 == 0 and (num1 > num4):
                    if num1 % 2 == 0 and num4 % 2 != 0 or num1 % 2 != 0 and num4 % 2 == 0:
                        number = str(num1) + str(num2) + str(num3) + str(num4)
                        print(number, end=' ')





