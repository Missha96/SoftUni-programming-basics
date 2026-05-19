start = int(input())
end = int(input())
magic = int(input())
counter = 0
magic_count = 0

for num in range(start, end + 1):
    for num2 in range(start, end + 1):
        counter += 1
        if num + num2 == magic:
            magic_count += 1
            if magic_count == 1:
                print(f'Combination N:{counter} ({num} + {num2} = {magic})')
            break


if magic_count == 0:
    print(f'{counter} combinations - neither equals {magic}')
