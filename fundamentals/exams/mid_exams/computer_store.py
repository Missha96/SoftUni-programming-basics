total_price_without_tax = 0.0
tax = 0.0
total = 0.0
while True:
    command = input()

    if command != 'special' and command != 'regular':
        price = float(command)
        if price < 0:
            print('Invalid price!')
        else:
            total_price_without_tax += price

    if command == 'special':
        tax = total_price_without_tax * 0.20
        total = (total_price_without_tax + tax) * 0.90
        if total == 0:
            print('Invalid order!')
        else:
            print("Congratulations you've just bought a new computer!")
            print(f'Price without taxes: {total_price_without_tax:.2f}$')
            print(f'Taxes: {tax:.2f}$')
            print('-----------')
            print(f'Total price: {total:.2f}$')
            break
    elif command == 'regular':
        tax = total_price_without_tax * 0.20
        total = total_price_without_tax + tax
        if total == 0:
            print('Invalid order!')
        else:
            print("Congratulations you've just bought a new computer!")
            print(f'Price without taxes: {total_price_without_tax:.2f}$')
            print(f'Taxes: {tax:.2f}$')
            print('-----------')
            print(f'Total price: {total:.2f}$')
        break


