chrysanthemum_qty = int(input())
rose_qty = int(input())
tulip_qty = int(input())
season = input()
holiday = input()

flowers = 0
chrysanthemum = 0.0
rose = 0.0
tulip = 0.0

if (season == 'Summer') or (season == 'Spring'):
    chrysanthemum = 2.00
    rose = 4.10
    tulip = 2.50
elif (season == 'Autumn') or (season == 'Winter'):
    chrysanthemum = 3.75
    rose = 4.50
    tulip = 4.15
flowers = (chrysanthemum_qty * chrysanthemum) + (rose_qty * rose) + (tulip_qty * tulip)
flowers_qty = chrysanthemum_qty + rose_qty + tulip_qty
if flowers_qty > 20:
    flowers *= 0.80

if tulip_qty > 7 and season == 'Spring':
    flowers *= 0.95
elif rose_qty >= 10 and season == 'Winter':
    flowers *= 0.90

if holiday == 'Y':
    flowers *= 1.15

bouquet = flowers + 2.00
print(f'{bouquet:.2f}')
