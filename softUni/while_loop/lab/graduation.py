name = input()
fail = 0
grade = 1
score = 0

while True:
    year_grade = float(input())
    if year_grade < 4.00:
        fail += 1
        if fail > 1:
            print(f"{name} has been excluded at {grade} grade")
            break
        continue

    score += year_grade
    if grade == 12:
        average_grade = score / 12
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break
    grade += 1
