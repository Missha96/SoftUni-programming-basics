key = int(input())
lines = int(input())
new_word = ''
for _ in range(lines):
    letter = input()
    new_letter = ord(letter) + key
    new_word += chr(new_letter)
print(f'{new_word}')
