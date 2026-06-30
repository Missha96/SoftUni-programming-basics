word = input()
vowels = ['a', 'o', 'u', 'e', 'i']
lower = word.lower()

new_word = "".join([char for char in word if char.lower() not in vowels])
print(new_word)