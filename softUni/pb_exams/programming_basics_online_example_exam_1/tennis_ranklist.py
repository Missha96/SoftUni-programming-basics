from math import floor
tournaments = int(input())
starting_points = int(input())
points = 0
final_points = 0
win = 0
for _ in range(tournaments):
    stage = input()
    if stage == 'W':
        points += 2000
        win += 1
    elif stage == 'F':
        points += 1200
    elif stage == 'SF':
        points += 720


final_points = starting_points + points
average_points = points / tournaments
percent = win / tournaments * 100

print(f"Final points: {final_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percent:.2f}%")
