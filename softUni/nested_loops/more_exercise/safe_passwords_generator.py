a = int(input())
b = int(input())
max_passwords = int(input())

A = 35
B = 64
count = 0

for x in range(1, a + 1):
    for y in range(1, b + 1):
        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}|", end="")
        count += 1

        A += 1
        B += 1

        if A > 55:
            A = 35

        if B > 96:
            B = 64

        if count >= max_passwords:
            exit()