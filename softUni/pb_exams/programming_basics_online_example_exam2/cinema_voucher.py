voucher = int(input())
command = ''

cinema_ticket = 0
product = 0

while command != 'End':
    command = input()
    if command == 'End':
        break
    if len(command) > 8:
        price = ord(command[0]) + ord(command[1])
        if voucher >= price:
            voucher -= price
            cinema_ticket += 1
        else:
            break

    else:
        price = ord(command[0])
        if voucher >= price:
            voucher -= price
            product += 1
        else:
            break

print(cinema_ticket)
print(product)
