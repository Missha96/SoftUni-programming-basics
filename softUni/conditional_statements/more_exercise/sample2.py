km = int(input())
time_of_day = input()

taxi_tax = 0.70
taxi_day = 0.79
taxi_night = 0.90
bus_tax = 0.09
train_tax = 0.06

# Taxi
if time_of_day == 'day':
    cheapest_price = taxi_tax + (km * taxi_day)
else:
    cheapest_price = taxi_tax + (km * taxi_night)

# Bus
if km >= 20:
    bus_price = km * bus_tax
    if bus_price < cheapest_price:
        cheapest_price = bus_price

# Train
if km >= 100:
    train_price = km * train_tax
    if train_price < cheapest_price:
        cheapest_price = train_price

print(f"{cheapest_price:.2f}")