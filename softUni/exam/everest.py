sleep = input()

top = 8848
days = 1
total_climbed = 0
total = 0
while sleep != 'END':
    climbed_meters = int(input())
    if sleep == 'Yes':
        days += 1
        initial_meters = 5364
        total_climbed += climbed_meters
        total = initial_meters + total_climbed
    elif sleep == "No":
        climbed_meters = int(input())
        total += climbed_meters
    if climbed_meters >= top:
        break
    print(f"Goal reached for {days} days!")
    # if sleep == 'END' or climbed_meters > top or days > 5:
    #     if climbed_meters > top:
    #         print(f"Goal reached for {days} days!")
    #     else:
    #         print("Failed!")
    #         print(f"{abs(climbed_meters - top)}")
    # break
