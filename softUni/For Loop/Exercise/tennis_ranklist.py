from math import floor
tournaments = int(input())
initial_points = int(input())

points = 0
wins = 0

for _ in range(tournaments):
    stage = input()

    if stage == 'W':
        points += 2000
        wins += 1
    elif stage == 'F':
        points += 1200
    elif stage == 'SF':
        points += 720
final_points = initial_points + points
average_points = points / tournaments
percent = wins / tournaments * 100

print(f'Final points: {final_points}')
print(f'Average points: {floor(average_points)}')
print(f'{percent:.2f}%')