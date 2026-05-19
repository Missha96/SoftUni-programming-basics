period = int(input())
doctors = 7
days = 0
treated = 0
untreated = 0

for _ in range(1, period + 1):
    patients = int(input())
    days += 1
    if days == 3:
        if untreated > treated:
            doctors += 1
            days = 0
        else:
            days = 0
    if patients >= doctors:
        untreated += (patients - doctors)
        treated += doctors
    else:
        treated += patients

print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')
