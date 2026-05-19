students = int(input())
avr = 0
top = 0
four = 0
three = 0
fail = 0

for _ in range(students):
    grade = float(input())
    if grade >= 5:
        avr += grade
        top += 1
    elif 4 <= grade <= 4.99:
        avr += grade
        four += 1
    elif 3 <= grade <= 3.99:
        avr += grade
        three += 1
    else:
        avr += grade
        fail += 1

print(f"Top students: {(top / students * 100):.2f}%")
print(f"Between 4.00 and 4.99: {(four / students * 100):.2f}%")
print(f"Between 3.00 and 3.99: {(three / students * 100):.2f}%")
print(f"Fail: {(fail / students * 100):.2f}%")
print(f'Average: {(avr / students):.2f}')
