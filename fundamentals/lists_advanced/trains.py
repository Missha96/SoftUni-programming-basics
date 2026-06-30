wagons = int(input())

train = []
for _ in range(wagons):
    train.append(wagons * 0)

while True:
    command = input().split()
    if command[0] == 'End':
        break
    current_command = command[0]
    if current_command == 'add':
        people = int(command[1])
        train[-1] += people
    elif current_command == 'insert':
        index = int(command[1])
        train[index] += int(command[2])
    elif current_command == 'leave':
        index = int(command[1])
        train[index] -= int(command[2])
    if current_command == 'End':
        break
print(train)
