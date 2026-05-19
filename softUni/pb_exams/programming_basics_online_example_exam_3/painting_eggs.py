eggs_size = input()
color = input()
lot = int(input())
total = 0
end = 0
price = 0


if color == 'Red':
    if eggs_size == 'Large':
        price = 16
    elif eggs_size == 'Medium':
        price = 13
    elif eggs_size == 'Small':
        price = 9
elif color == 'Green':
    if eggs_size == 'Large':
        price = 12
    elif eggs_size == 'Medium':
        price = 9
    elif eggs_size == 'Small':
        price = 8
elif color == 'Yellow':
    if eggs_size == 'Large':
        price = 9
    elif eggs_size == 'Medium':
        price = 7
    elif eggs_size == 'Small':
        price = 5

total = price * lot
end = total * 0.65
print(f'{end:.2f} leva.')
