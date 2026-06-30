notes = [0] * 10

while True:
    command = input()
    if command == 'End':
        break
    to_do_list = command.split("-")
    priority = int(to_do_list[0]) - 1
    note = to_do_list[1]
    notes.pop(priority)
    notes.insert(priority, note)
    new_list = [action for action in notes if action != 0]
print(new_list)