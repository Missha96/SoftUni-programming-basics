lost_fight = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
fights = 0
shield_breaks = 0
expenses = 0

for game in range(1, lost_fight + 1):
    if game % 2 == 0:
        expenses += helmet_price
    if game % 3 == 0:
        expenses += sword_price
        if game % 2 == 0:
            expenses += shield_price
            shield_breaks += 1
            if shield_breaks == 2:
                expenses += armor_price
                shield_breaks = 0
print(f'Gladiator expenses: {expenses:.2f} aureus')