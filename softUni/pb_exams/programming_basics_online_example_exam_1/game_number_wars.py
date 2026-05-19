
player1_name = input()
player2_name = input()
player1_points = 0
player2_points = 0

while True:
    command = input()

    if command == "End of game":
        print(f"{player1_name} has {player1_points} points")
        print(f"{player2_name} has {player2_points} points")
        break

    player1_card = int(command)
    player2_card = int(input())

    if player1_card > player2_card:
        player1_points += player1_card - player2_card
    elif player1_card < player2_card:
        player2_points += player2_card - player1_card
    else:
        print("Number wars!")
        player1_last_card = int(input())
        player2_last_card = int(input())

        if player1_last_card > player2_last_card:
            print(f"{player1_name} is winner with {player1_points} points")
        else:
            print(f"{player2_name} is winner with {player2_points} points")
            break