width = int(input())
length = int(input())

cake_pieces = width * length

command = input()
while command != 'STOP':
    pieces_taken = int(command)
    cake_pieces -= pieces_taken

    if cake_pieces < 0:
        print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
        break

    command = input()

else:
    print(f'{cake_pieces} pieces are left.')
