number = int(input())
word = input()
total_list = []
list_word = []
for _ in range(number):
    new_string = input()
    total_list.append(new_string)
    if word in new_string:
        list_word.append(new_string)

print(total_list)
print(list_word)