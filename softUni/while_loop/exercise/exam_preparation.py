bad_grades = int(input())

last_task = ''
tasks = 0
fail = 0
grade_sum = 0

while True:
    task_name = input()

    if task_name == 'Enough':
        average_score = grade_sum / tasks
        print(f'Average score: {average_score:.2f}')
        print(f'Number of problems: {tasks}')
        print(f'Last problem: {last_task}')
        break

    grade = float(input())
    grade_sum += grade
    tasks += 1
    last_task = task_name 

    if grade <= 4:
        fail += 1
        if fail >= bad_grades:
            print(f'You need a break, {fail} poor grades.')
            break
