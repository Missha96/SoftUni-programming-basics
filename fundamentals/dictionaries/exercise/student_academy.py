rows = int(input())
students = {}

for student in range(rows):
    student_name = input()
    grade = float(input())
    if student_name not in students:
        students[student_name] = []
        students[student_name].append(grade)
    else:
        students[student_name].append(grade)
for student_name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student_name} -> {average_grade:.2f}")

