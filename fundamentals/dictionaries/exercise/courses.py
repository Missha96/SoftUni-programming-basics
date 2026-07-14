courses = {}
while True:
    command = input().split(" : ")
    course = command[0]
    if command[0] == 'end':
        break
    if course not in courses.keys():
        name = command[1]
        courses[course] = []
        courses[course].append(name)
    else:
        name = command[1]
        # courses[course] = []
        courses[course].append(name)
for course, names in courses.items():

    print(f'{course}: {len(names)}')
    for name in names:
        print(f"-- {name}")
