string = input().split()
dictionary = {}
for i in range(0, len(string), 2):
    key = string[i]
    value = string[i + 1]
    dictionary[key] = int(value)
print(dictionary)

