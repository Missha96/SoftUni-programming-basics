target_sum = int(input())
counter = 0
total_cash = 0
total_card = 0
cash = 0
card = 0

while True:
    command = input()
    if command == 'End':
        print(f"Failed to collect required money for charity.")
        break

    money = int(command)
    counter += 1
    if (counter == 1) and (money <= 100):
        total_cash += money
        # counter += 1
        cash += 1
        print(f'Product sold!')
    elif (counter == 1) and (money > 100):
        # counter += 1
        print('Error in transaction!')
    if (counter == 2) and (money >= 10):
        total_card += money
        # counter += 1
        counter = 0
        card += 1
        print(f'Product sold!')
    elif (counter == 2) and (money < 10):
        counter = 0
        print('Error in transaction!')
    if target_sum <= (total_card + total_cash):
        print(f'Average CS: {(total_cash / cash):.2f}')
        print(f'Average CC: {(total_card / card):.2f}')
        break
