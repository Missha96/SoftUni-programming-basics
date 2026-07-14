students = {}
command = input()
while ":" in command:
    data = command.split(":")
    name, id, course = data[0], data[1], data[2]
    if course not in students:
        students[course] = {}
    students[course][id] = name
    command = input()

course = " ".join(command.split("_"))
for key, value in students.items():
    if key == course:
        for id, name in value.items():
            print(f'{name} - {id}')