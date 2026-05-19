stage = input()
ticket_type = input()
tickets_qty = int(input())
picture = input()
price = 0

if stage == 'Quarter final':
    if ticket_type == 'Standard':
        price = 55.50
    elif ticket_type == 'Premium':
        price = 105.20
    elif ticket_type == 'VIP':
        price = 118.90
elif stage == 'Semi final':
    if ticket_type == 'Standard':
        price = 75.88
    elif ticket_type == 'Premium':
        price = 125.22
    elif ticket_type == 'VIP':
        price = 300.40
elif stage == 'Final':
    if ticket_type == 'Standard':
        price = 110.10
    elif ticket_type == 'Premium':
        price = 160.66
    elif ticket_type == 'VIP':
        price = 400

total_tickets_price = tickets_qty * price

if total_tickets_price > 4000:
    total_tickets_price *= 0.75
elif (total_tickets_price > 2500) and (total_tickets_price <= 4000):
    total_tickets_price *= 0.90
    if picture == 'Y':
        total_tickets_price += (40 * tickets_qty)
elif total_tickets_price < 4000:
    if picture == 'Y':
        total_tickets_price += (40 * tickets_qty)

print(f'{total_tickets_price:.2f}')
