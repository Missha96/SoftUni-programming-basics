command = input()
total = 0.0
while command != 'NoMoreMoney':
    new_sum = float(command)
    if new_sum < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {new_sum:.2f}')
    total += new_sum
    command = input()

print(f'Total: {total:.2f}')
