days = int(input())
hours = int(input())
days_counter = 0
total = 0
total_for_day = 0

for day in range(1, days + 1):
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            tax = 2.50
            total_for_day += tax
        elif day % 2 != 0 and hour % 2 == 0:
            tax = 1.25
            total_for_day += tax
        else:
            tax = 1
            total_for_day += tax

    print(f'Day: {day} - {total_for_day:.2f} leva')
    total += total_for_day
    total_for_day = 0
print(f'Total: {total:.2f} leva')
