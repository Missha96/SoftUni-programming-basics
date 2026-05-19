import string
n = int(input())
l = int(input())


for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(l):
            for d in range(l):
                for e in range(1, n + 1):
                    if (e > a) and (e > b):
                        print(f'{a}{b}{string.ascii_lowercase[c]}{string.ascii_lowercase[d]}{e}', end=' ')

