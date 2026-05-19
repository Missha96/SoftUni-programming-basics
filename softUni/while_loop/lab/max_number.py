from sys import maxsize

max_number = -maxsize

while True:
    new_command = input()
    if new_command == 'Stop':
        break
    number = int(new_command)
    if number > max_number:
        max_number = number
print(max_number)
