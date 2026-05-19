from math import ceil
days = int(input())
km_first_day = float(input())
total_km = 0
ttl = 0


for _ in range(1, days + 1):
    percent_increase = int(input())
    km = km_first_day
    percent = percent_increase / 100
    run_km = km_first_day + (km_first_day * percent)
    km_first_day = run_km
    total_km += km_first_day
    ttl = total_km + km
if ttl >= 1000:
    print(f"You've done a great job running {ceil(ttl - 1000)} more   kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(abs(1000 - ttl))} more kilometers")
