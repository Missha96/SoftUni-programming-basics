control = int(input())
counter = 0
password = ''
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d:
                    if (a * b) + (c * d) == control:
                        counter += 1
                        print(f' {a}{b}{c}{d}', end="")
                        if counter == 4:
                            password = str(a) + str(b) + str(c) + str(d)
if password == '':
    print()
    print('No!')
else:
    print()
    print(f'Password: {password}')

