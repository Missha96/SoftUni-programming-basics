n = int(input())

for _ in range(n):
    string = input()
    chars = list(string)

    if '_' not in chars and '.' not in chars and ',' not in chars:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')

