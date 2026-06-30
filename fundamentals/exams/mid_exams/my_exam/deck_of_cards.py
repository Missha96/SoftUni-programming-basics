list_of_card = input().split(", ")
number_of_commands = int(input())

for command in range(number_of_commands):
    new_command = input().split(", ")
    action = new_command[0]
    if action == 'Add':
        card_name = new_command[1]
        if card_name not in list_of_card:
            list_of_card.append(card_name)
            print('Card successfully added')
        else:
            print('Card is already in the deck')

    elif action == 'Remove':
        card_name = new_command[1]
        if card_name not in list_of_card:
            print('Card not found')
        else:
            list_of_card.remove(card_name)
            print('Card successfully removed')

    elif action == 'Remove At':
        index = int(new_command[1])
        if 0 >= index < len(list_of_card) and 0 >= index < len(list_of_card):
            print('Index out of range')
        else:
            list_of_card.pop(index)
            print('Card successfully removed')

    elif action == 'Insert':
        index = int(new_command[1])
        card_name = new_command[2]
        if card_name in list_of_card:
            print('Card is already added')
        elif card_name not in list_of_card:
            if 0 >= index < len(list_of_card) and 0 >= index < len(list_of_card):
                print('Index out of range')
            else:
                list_of_card.insert(index, card_name)
                print('Card successfully added')
print(", ".join(list_of_card))

