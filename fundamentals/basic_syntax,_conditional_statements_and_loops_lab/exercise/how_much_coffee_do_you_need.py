command = input()
coffee_qty = 0

while command != 'END':

    if command != 'coding' and command != 'CODING' and command != 'dog' and command != 'cat' and command != 'DOG' and command != 'CAT' and command != 'movie' and command != 'MOVIE':
        command = input()
        continue
    if coffee_qty >= 5:
        print('You need extra sleep')
        break
    if command == 'coding':
        coffee_qty += 1
    elif command == 'CODING':
        coffee_qty += 2
    elif command == 'dog' or command == 'cat':
        coffee_qty += 1
    elif command == 'DOG' or command == 'CAT':
        coffee_qty += 2
    elif command == 'movie':
        coffee_qty += 1
    elif command == 'MOVIE':
        coffee_qty += 2
    command = input()
else:
    print(coffee_qty)

