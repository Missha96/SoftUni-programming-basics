sentance = input()
new_sentance = ''
for char in sentance:
    new_char = ord(char) + 3
    new_sentance += chr(new_char)

print(new_sentance)