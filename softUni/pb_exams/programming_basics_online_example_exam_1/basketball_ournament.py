tournament_name = input()
game = 0
win = 0
lost = 0
total_games = 0
while True:
    command = input()
    if command == 'End of tournaments':
        break
    games = int(command)
    total_games += games

    for _ in range(games):
        desi_point = int(input())
        others_point = int(input())
        game += 1
        if desi_point > others_point:
            win += 1
            print(f'Game {game} of tournament {tournament_name}: win with {abs(desi_point - others_point)} points.')
        else:
            lost += 1
            print(f"Game {game} of tournament {tournament_name}: lost with {abs(desi_point - others_point)} points.")
    game = 0
    tournament_name = input()
    if tournament_name == 'End of tournaments':
        print(f'{(win / total_games * 100):.2f}% matches win')
        print(f'{(lost / total_games * 100):.2f}% matches lost')
        break


