juniors = int(input())
seniors = int(input())
trace = input()

junior_tax = 0
senior_tax = 0

if trace == 'trail':
    junior_tax = 5.50
    senior_tax = 7
elif trace == 'cross-country':
    junior_tax = 8
    senior_tax = 9.50
elif trace == 'downhill':
    junior_tax = 12.25
    senior_tax = 13.75
elif trace == 'road':
    junior_tax = 20
    senior_tax = 21.50

total_bikers = juniors + seniors
if total_bikers >= 50 and trace == 'cross-country':
    junior_tax *= 0.75
    senior_tax *= 0.75

total_tax = (junior_tax * juniors) + (senior_tax * seniors)
total_tax *= 0.95
print(f'{total_tax:.2f}')