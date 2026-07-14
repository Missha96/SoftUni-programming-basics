characters = input().split(", ")
chars = {}

for char in characters:
    char_value = ord(char)
    chars[char] = char_value

print(chars)