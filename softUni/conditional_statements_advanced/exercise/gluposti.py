month = input()
nights = int(input())

type_of_room = ''
price = 0

apartment_all_nights = price * nights
studio_all_nights = price * nights

if type_of_room == 'apartment':
    if (month == 'May') or (month == 'October'):
        price = 65
    elif (month == 'June') or (month == 'September'):
        price = 68.70
    elif (month == 'July') or (month == 'August'):
        price = 77
    elif nights > 14:
        price *= 0.90

if (month == 'May') or (month == 'October'):
    price = 50
    if 7 < nights < 14:
        price *= 0.95
    elif nights > 14:
        price *= 0.70
elif (month == 'June') or (month == 'September'):
    price = 75.20
    if nights > 14:
        price *= 0.80
elif (month == 'July') or (month == 'August'):
    price = 76
    print(f'Apartment: {apartment_all_nights:.2f} lv.')
    print(f'Studio: {studio_all_nights:.2f} lv.')
