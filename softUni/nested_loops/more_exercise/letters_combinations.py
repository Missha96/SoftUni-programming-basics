import string
interval_start = input()
interval_end = input()
skip = input()
total_combinations = 0
alphabet = string.ascii_lowercase

start = alphabet.index(interval_start)
end = alphabet.index(interval_end)

interval = alphabet[start:end + 1]
combination = ''

for char in interval:
    if char == skip:
        continue
    first = char
    for char2 in interval:
        if char2 == skip:
            continue
        second = char2
        for char3 in interval:
            if char3 == skip:
                continue
            third = char3
            total_combinations += 1
            combination = char + char2 + char3
            print(combination, end=' ')
print(total_combinations)