words = input().split()
searched_palindrome = input()
palindromes = []
counter = 0
for word in words:
    if word == "".join(reversed(word)):
        palindromes.append(word)
    if searched_palindrome in palindromes:
        counter = palindromes.count(searched_palindrome)
print(palindromes)
print(f'Found palindrome {counter} times')