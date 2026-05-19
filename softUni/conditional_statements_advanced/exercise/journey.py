budget = float(input())
season = input()

destination = ''
place = ''
price = 0

if budget <= 100:
    destination = 'Bulgaria'
elif 100 < budget <= 1000:
    destination = 'Balkans'
elif budget > 1000:
    destination = 'Europe'

if destination == 'Bulgaria' and season == 'summer':
    price = budget * 0.30
elif destination == 'Bulgaria' and season == 'winter':
    price = budget * 0.70
if destination == 'Balkans' and season == 'summer':
    price = budget * 0.40
elif destination == 'Balkans' and season == 'winter':
    price = budget * 0.80

if destination == 'Europe':
    price = budget * 0.90

if ((destination == "Bulgaria")
    or (destination == "Balkans")) and season == 'summer':
    place = 'Camp'
elif ((destination == "Bulgaria")
    or (destination == "Balkans")) and season == 'winter':
    place = 'Hotel'
elif destination == "Europe":
    place = 'Hotel'

if budget > 0:
    print(f'Somewhere in {destination}')
    print(f'{place} - {price:.2f}')
