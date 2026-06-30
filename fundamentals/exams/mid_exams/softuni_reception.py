first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
total_students = int(input())
time = 0
time_for_break = 0

total_employees_capacity_per_hour = first_employee + second_employee + third_employee
while total_students:
    if time_for_break == 3:
        time += 1
        time_for_break = 0
    if total_students >= total_employees_capacity_per_hour:
        total_students -= total_employees_capacity_per_hour
        time += 1
        time_for_break += 1
    if total_students < total_employees_capacity_per_hour and total_students != 0:
        total_students -= total_students
        time += 1
        time_for_break += 1
        break
print(f'Time needed: {time}h.')



