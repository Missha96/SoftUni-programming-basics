number = int(input())
my_list = []
new_list = []
for _ in range(number):
    num = int(input())
    my_list.append(num)

command = input()
if command == 'even':
    for num in my_list:
        if num % 2 == 0 or num == 0:
            new_list.append(num)
elif command == 'odd':
    for num in my_list:
        if num % 2 != 0:
            new_list.append(num)
elif command == 'negative':
    for num in my_list:
        if num < 0:
            new_list.append(num)
elif command == 'positive':
    for num in my_list:
        if num >= 0:
            new_list.append(num)

print(new_list)
