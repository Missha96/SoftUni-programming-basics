zoo_list = []

for _ in range(3):
    name = input()
    zoo_list.append(name)

zoo_list[0], zoo_list[2] = zoo_list[2], zoo_list[0]

print(zoo_list)
