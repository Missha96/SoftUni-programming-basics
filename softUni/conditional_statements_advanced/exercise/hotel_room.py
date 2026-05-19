month = input()
nights = int(input())

type_of_room = ''
studio_price = 0
apartment_price = 0

# apartment

if (month == 'May') or (month == 'October'):
    apartment_price = 65
elif (month == 'June') or (month == 'September'):
    apartment_price = 68.70
elif (month == 'July') or (month == 'August'):
    apartment_price = 77
if nights > 14:
    apartment_price *= 0.90
apartment_all_nights = apartment_price * nights
print(f'Apartment: {apartment_all_nights:.2f} lv.')

# studio
if (month == 'May') or (month == 'October'):
    studio_price = 50
    if 7 < nights < 14:
        studio_price *= 0.95
    elif nights > 14:
        studio_price *= 0.70
elif (month == 'June') or (month == 'September'):
    studio_price = 75.20
    if nights > 14:
        studio_price *= 0.80
elif (month == 'July') or (month == 'August'):
    studio_price = 76
studio_all_nights = studio_price * nights
print(f'Studio: {studio_all_nights:.2f} lv.')
