movie_name = input()
cinema_type = input()
tickets = int(input())


if movie_name == 'A Star Is Born':
    if cinema_type == 'normal':
        price = 7.50
    elif cinema_type == 'luxury':
        price = 10.50
    else:
        price = 13.50
elif movie_name == 'Bohemian Rhapsody':
    if cinema_type == 'normal':
        price = 7.35
    elif cinema_type == 'luxury':
        price = 9.45
    else:
        price = 12.75
elif movie_name == 'Green Book':
    if cinema_type == 'normal':
        price = 8.15
    elif cinema_type == 'luxury':
        price = 10.25
    else:
        price = 13.25
elif movie_name == 'The Favourite':
    if cinema_type == 'normal':
        price = 8.75
    elif cinema_type == 'luxury':
        price = 11.55
    else:
        price = 13.95

total = price * tickets
print(f'{movie_name} -> {total:.2f} lv.')