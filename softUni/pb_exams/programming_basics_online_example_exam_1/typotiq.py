sleep = input()

top = 8848
days = 1
total_climbed = 0
total = 5364

while sleep != "END":
    climbed_meters = int(input())

    if sleep == "Yes":
        days += 1

    if days > 5:
        break

    total_climbed += climbed_meters
    total = 5364 + total_climbed

    if total >= top:
        break

    sleep = input()

if total >= top:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(total)