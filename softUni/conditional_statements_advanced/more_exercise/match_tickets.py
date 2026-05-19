budget = float(input())
category = input()
people = int(input())

VIP = 499.99
Normal = 249.99
transport = 0
price_of_ticket = 0.0

if 1 <= people <= 4:
    transport = budget * 0.75
elif 4 < people <= 9:
    transport = budget * 0.60
elif 10 <= people <= 24:
    transport = budget * 0.50
elif 25 <= people <= 49:
    transport = budget * 0.40
elif people >= 50:
    transport = budget * 0.25

if category == 'VIP':
    price_of_ticket = 499.99
elif category == 'Normal':
    price_of_ticket = 249.99

total_tickets = price_of_ticket * people
total = transport + total_tickets
diff = abs(budget - total)


if total < budget:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print (f'Not enough money! You need {diff:.2f} leva.')