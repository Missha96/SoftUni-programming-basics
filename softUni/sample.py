km = int(input())
time_of_day = input()

taxi_tax = 0.70
taxi_day = 0.79
taxi_night = 0.90
bus_tax = 0.09
train_tax = 0.06

if km <= 20 and time_of_day == 'day':
    total_day_taxi = taxi_tax + (km * taxi_day)
    print(f'{total_day_taxi:.2f}')
elif km <= 20 and time_of_day == 'night':
    total_night_taxi = taxi_tax + (km * taxi_night)
    print(f'{total_night_taxi:.2f}')
elif 20 < km <= 100 and (time_of_day == 'day' or time_of_day == 'night'):
    total_day_taxi = taxi_tax + (km * taxi_day)
    total_night_taxi = taxi_tax + (km * taxi_night)
    travel_bus = km * bus_tax
    all_transport = min(total_day_taxi, total_night_taxi, travel_bus)
    print(f'{all_transport:.2f}')
elif km > 100 and (time_of_day == 'day' or time_of_day == 'night'):
    total_day_taxi = taxi_tax + (km * taxi_day)
    total_night_taxi = taxi_tax + (km * taxi_night)
    travel_bus = km * bus_tax
    travel_train = km * train_tax
    all_transport = min(total_day_taxi, total_night_taxi, travel_bus, travel_train)
    print(f'{all_transport:.2f}')