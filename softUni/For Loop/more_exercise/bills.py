months = int(input())
water = 20
internet = 15
total_electricity = 0
others = 0
average = 0
for _ in range(1, months + 1):
    electricity = float(input())
    total_electricity += electricity
    total_internet = internet * months
    total_water = water * months
    others = (total_electricity + total_internet + total_water) * 1.20
    average = (total_electricity + total_water + total_internet + others) / months

print(f'Electricity: {total_electricity:.2f} lv')
print(f'Water: {total_water:.2f} lv')
print(f'Internet: {total_internet:.2f} lv')
print(f'Other: {others:.2f} lv')
print(f'Average: {average:.2f} lv')
