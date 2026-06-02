events = input().split("|")
bakery_is_open = True
initial_energy = 100
initial_coins = 100
for event in events:
    event_values = event.split('-')
    event_type = event_values[0]
    event_value = int(event_values[1])
    if event_type == 'rest':
        total_energy = initial_energy
        initial_energy += event_value
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - total_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
    elif event_type == 'order':
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins >= event_value:
            initial_coins -= event_value
            print(f"You bought {event_type}.")
        else:
            bakery_is_open = False
            break
if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
else:
    print(f"Closed! Cannot afford {event_type}.")

