target_high = int(input())
successful_jumps = 0
failed_jumps = 0
total_jumps = 0

initial_high = target_high - 30  # Задайте го само веднъж
target = initial_high

while True:
    jump = int(input())

    if jump > target:
        successful_jumps += 1
        total_jumps += 1
        target += 5  # Увеличаване на `target` след успешен скок
        if jump > target_high:  # Проверка за успех
            print(f"Tihomir succeeded, he jumped over {jump}cm after {total_jumps} jumps.")
            break
    else:
        failed_jumps += 1
        total_jumps += 1
        if failed_jumps >= 3:  # Проверка за 3 неуспешни скока
            print(f'Tihomir failed at {initial_high}cm after {total_jumps} jumps.')
            break