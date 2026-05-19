n = int(input())
current = 1
is_current_bigger = False

for num in range(1,n + 1):
    for num1 in range(1, num + 1):
        if current > n:
            is_current_bigger = True
            break
        print(str(current) + ' ', end='')
        current += 1
    print()
