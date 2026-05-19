first_game_result = input()
second_game_result = input()
third_game_result = input()

win = 0
lost = 0
drawn = 0

if first_game_result[0] > first_game_result[2]:
    win += 1
elif first_game_result[0] < first_game_result[2]:
    lost += 1
else:
    drawn += 1

if second_game_result[0] > second_game_result[2]:
    win += 1
elif second_game_result[0] < second_game_result[2]:
    lost += 1
else:
    drawn += 1

if third_game_result[0] > third_game_result[2]:
    win += 1
elif third_game_result[0] < third_game_result[2]:
    lost += 1
else:
    drawn += 1

print(f'Team won {win} games.')
print(f'Team lost {lost} games.')
print(f'Drawn games: {drawn}')
