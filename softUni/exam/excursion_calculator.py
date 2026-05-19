people_qty = int(input())
season = input()
if people_qty <= 5:
    if season == 'spring':
        price = 50.00
    elif season == 'summer':
        price = 48.50 * .85
    elif season == 'autumn':
        price = 60.00
    elif season == 'winter':
        price = 86.00 * 1.08
elif people_qty > 5:
    if season == 'spring':
        price = 48.00
    elif season == 'summer':
        price = 45.00 * 0.85
    elif season == 'autumn':
        price = 49.50
    elif season == 'winter':
        price = 85.00 * 1.08

trip_price = price * people_qty
print(f'{trip_price:.2f} leva.')

