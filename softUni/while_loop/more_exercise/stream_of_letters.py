import string
from string import ascii_letters

word = ""
c = 0
o = 0
n = 0
special = ''
special_word = ['c', 'o', 'n']
word_count = 0
new_word = ''
while True:
    command = input()

    if command == '':
        break

    if all(char in special for char in special_word):
        word_count += 1
        special = ''
        word += new_word
        word += ' '
        new_word = ''
        n = 0
        o = 0
        c = 0
    if command == 'End':
        break
    if command in string.punctuation:
        continue
    if command in string.ascii_letters:
        if command == 'c' and c < 1:
            c += 1
            special += command
            if c > 1:
                # c = 0
                new_word += command
        elif command == 'o' and o < 1:
            o += 1
            special += command
            if o > 1:
                # o = 0
                new_word += command
        elif command == 'n' and n < 1:
            n += 1
            special += command
            if n > 1:
                # n = 0
                new_word += command
        else:
            new_word += command

print(word)
