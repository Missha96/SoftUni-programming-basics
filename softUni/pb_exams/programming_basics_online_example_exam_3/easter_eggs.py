painted_eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0
total_eggs = []
colors = ['red', 'orange', 'blue', 'green']

for egg in range(painted_eggs):
    color = input()
    if color == 'red':
        red += 1
    elif color == 'orange':
        orange += 1
    elif color == 'blue':
        blue += 1
    elif color == 'green':
        green += 1
total_eggs += red, orange, blue, green
max_eggs = max(total_eggs)
position_max = total_eggs.index(max(total_eggs))
print(f'Red eggs: {red}')
print(f'Orange eggs: {orange}')
print(f'Blue eggs: {blue}')
print(f'Green eggs: {green}')
print(f'Max eggs: {max_eggs} -> {colors[position_max]}')


