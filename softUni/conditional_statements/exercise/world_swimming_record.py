record_sec = float(input())
distance_m = float (input())
meter_sec = float(input())

every_15_meters = 12.5
time_ivan = distance_m * meter_sec
times_slow = distance_m / 15
total_slow = times_slow * every_15_meters
total_time = time_ivan + total_slow

if record_sec > total_time:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    record_sec >= total_time
    difference = abs(record_sec - total_time)
    print(f'No, he failed! He was {difference:.2f} seconds slower.')
