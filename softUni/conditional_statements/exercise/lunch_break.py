from math import ceil

series_name = input()
episode = int(input())
break_time = int(input())

lunch_time = break_time / 8
rest_time = break_time / 4

free_time = break_time - lunch_time - rest_time
difference = abs(free_time - episode)

if free_time >= episode:
    print(f'You have enough time to watch {series_name} and left with {ceil(difference)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(difference)} more minutes.")
