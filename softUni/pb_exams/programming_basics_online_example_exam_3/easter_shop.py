eggs = int(input())
command = ''
sold = 0

while True:
    command = input()

    if command == 'Close':
        print('Store is closed!')
        print(f'{sold} eggs sold.')
        break
    new_eggs = int(input())
    if command == 'Buy':
        if new_eggs > eggs:
            print('Not enough eggs in store!')
            print(f'You can buy only {eggs}.')
            break
        else:
            eggs -= new_eggs
            sold += new_eggs
    elif command == 'Fill':
        eggs += new_eggs

