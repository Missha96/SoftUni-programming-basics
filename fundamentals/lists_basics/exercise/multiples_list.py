factor = int(input())
count = int(input())
my_list = []
new_factor = 0
for _ in range(count):
    new_factor += factor
    my_list.append(new_factor)

print(my_list)