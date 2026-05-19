visitors = int(input())

back = 0
chest = 0
legs = 0
abs = 0
shake = 0
bar = 0


for visitor in range(1, visitors + 1):
    activity = input()
    if activity == 'Back':
        back += 1
    elif activity == 'Chest':
        chest += 1
    elif activity == 'Legs':
        legs += 1
    elif activity == 'Abs':
        abs += 1
    elif activity == 'Protein shake':
        shake += 1
    elif activity == 'Protein bar':
        bar += 1
percent_training = (back + chest + legs + abs) / visitors * 100
percent_buying = (shake + bar) / visitors * 100

print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abs} - abs')
print(f'{shake} - protein shake')
print(f'{bar} - protein bar')
print(f'{percent_training:.2f}% - work out')
print(f'{percent_buying:.2f}% - protein')