k = int(input())
l = int(input())
m = int(input())
n = int(input())

for num in range(k, 8 + 1):
    if num % 2 == 0:
        k = num
    for num2 in range(9, l - 1):
        if l % 2 == 1:
            l = num2
        for num3 in range(m, 8 + 1):
            if m % 2 == 0:
                m = num3
            for num4 in range(9, n + 1):
                if n % 2 == 1:
                    n = num4

if (k == m) and (l == n):
    print("Cannot change the same player.")
else:
    print(f'{k}{l} - {m}{n}')