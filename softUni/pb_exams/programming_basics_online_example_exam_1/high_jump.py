target_high = int(input())
successful_jumps = 0
failed_jumps = 0
total_jumps = 0

initial_high = target_high - 30
target = initial_high
while True:
    jump = int(input())
    total_jumps += 1
    # if jump > target_high:
    #     print(f"Tihomir succeeded, he jumped over {jump}cm after {total_jumps} jumps.")
    #     break

    if jump > target:
        # successful_jumps += 1
        failed_jumps = 0
        if target >= target_high:
            print(f"Tihomir succeeded, he jumped over {target}cm after {total_jumps} jumps.")
            break
        target += 5

    else:
        failed_jumps += 1
    if failed_jumps >= 3:
        print(f'Tihomir failed at {target}cm after {total_jumps} jumps.')
        break




