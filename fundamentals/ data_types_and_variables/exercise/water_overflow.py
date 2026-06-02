lines = int(input())
tank = 255
total_liters = 0
for _ in range(lines):
    liters = int(input())
    if liters > tank:
        print('Insufficient capacity!')
    else:
        total_liters += liters
        tank -= liters
print(f'{total_liters}')