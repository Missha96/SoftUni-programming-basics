groups = int(input())

total_people = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

for idx in range(groups):
    people = int(input())
    total_people += people
    if people <= 5:
        count1 += people
    elif 6 <= people <= 12:
        count2 += people
    elif 13 <= people <= 25:
        count3 += people
    elif 26 <= people <= 40:
        count4 += people
    else:
        count5 += people

print(f'{(count1 / total_people * 100):.2f}%')
print(f'{(count2 / total_people * 100):.2f}%')
print(f'{(count3 / total_people * 100):.2f}%')
print(f'{(count4 / total_people * 100):.2f}%')
print(f'{(count5 / total_people * 100):.2f}%')
