season = input()
group_type = input()
students = int(input())
nights = int(input())

sport = ''
price = 0

if season == 'Winter':
    if group_type == "boys":
        price = 9.60
        sport = 'Judo'
    elif group_type == "girls":
        price = 9.60
        sport = 'Gymnastics'
    else:
        price = 10
        sport = 'Ski'
elif season == 'Spring':
    if group_type == "boys":
        price = 7.20
        sport = 'Tennis'
    elif group_type == "girls":
        price = 7.20
        sport = 'Athletics'
    else:
        price = 9.50
        sport = 'Cycling'
elif season == 'Summer':
    if group_type == "boys":
        price = 15
        sport = 'Football'
    elif group_type == "girls":
        price = 15
        sport = 'Volleyball'
    else:
        price = 20
        sport = 'Swimming'



if students >= 50:
    price *= 0.50
elif 20 <= students < 50:
    price *= 0.85
elif 10 <= students < 20:
    price *= 0.95

total_price = price * nights * students

print(f'{sport} {total_price:.2f} lv.')

