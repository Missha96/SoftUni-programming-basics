player_name = input()
game_points = 301
successful_shot = 0
failed_shot = 0
shoot_score = 0

while True:
    shoot_type = input()
    if shoot_type == 'Retire':
        print(f'{player_name} retired after {failed_shot} unsuccessful shots.')
        break
    points = int(input())
    if shoot_type == 'Single':
        shoot_score = points
    elif shoot_type == 'Double':
        shoot_score = points * 2
    elif shoot_type == 'Triple':
        shoot_score = points * 3

    if shoot_score <= game_points:
        game_points -= shoot_score
        successful_shot += 1
    else:
        failed_shot += 1

    if game_points == 0:
        print(f'{player_name} won the leg with {successful_shot} shots.')
        break



