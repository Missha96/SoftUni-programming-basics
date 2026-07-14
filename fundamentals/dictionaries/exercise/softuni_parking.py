parking = {}

number_of_commands = int(input())
for command in range(number_of_commands):
    current_command = input().split()
    if current_command[0] == 'register':
        name = current_command[1]
        plate_number = current_command[2]
        if name in parking.keys():
            print(f'ERROR: already registered with plate number {plate_number}')
        elif name not in parking.keys():
            parking[name] = plate_number
            print(f'{name} registered {plate_number} successfully')
    elif current_command[0] == 'unregister':
        name = current_command[1]
        if name not in parking.keys():
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del (parking[name])

for name, plate_number in parking.items():
    print(f'{name} => {plate_number}')