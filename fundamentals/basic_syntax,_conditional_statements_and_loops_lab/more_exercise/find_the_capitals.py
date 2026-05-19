word = input()
digits = []
new_word = list(word)
for index, digit in enumerate(new_word):
    if digit.isupper():
        digits.append(index)

print(digits)