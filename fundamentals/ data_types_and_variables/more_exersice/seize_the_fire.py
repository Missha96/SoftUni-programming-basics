total_fire = 0
total_effort = 0
fire_out_cells = []

fires = input().split('#')
water = int(input())
high = range(81, 125 + 1)
medium = range(51, 80 + 1)
low = range(1, 50 + 1)

for fire in fires:
    fire_type, fire_level = fire.split(' = ')
    fire_level = int(fire_level)
    fire_is_valid = False
    if fire_type == 'High':
        if fire_level in high:
            fire_is_valid = True
    elif fire_type == 'Medium':
        if fire_level in medium:
            fire_is_valid = True
    elif fire_type == 'Low':
        if fire_level in low:
            fire_is_valid = True
    if fire_is_valid:
        if water >= fire_level:
            water -= fire_level
            fire_out_cells.append(fire_level)
            total_effort += fire_level * 0.25
            total_fire += fire_level

print('Cells:')
for fire_out_cell in fire_out_cells:
    print(f'- {fire_out_cell}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')
