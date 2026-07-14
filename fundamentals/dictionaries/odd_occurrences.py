words = input().split()
odd_occurrences = {}
# words = [word.lower() for word in words]

for word in words:
    word_lower = word.lower()
    if word_lower not in odd_occurrences:
        odd_occurrences[word_lower] = 0
    odd_occurrences[word_lower] += 1

for (key, value) in odd_occurrences.items():
    if value % 2 != 0:
        print(key, end=" ")



