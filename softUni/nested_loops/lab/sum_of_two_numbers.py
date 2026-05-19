start = int(input())
end = int(input())
magic_number = int(input())

combination = 0
is_found = False

for num in range(start, end +1):
    for num2 in range(start, end +1):
        combination += 1
        if num + num2 == magic_number:
            is_found = True
            print(f'Combination N:{combination} ({num} + {num2} = {magic_number})')
            break

    if is_found:
        break

else:
    print(f'{combination} combinations - neither equals {magic_number}')