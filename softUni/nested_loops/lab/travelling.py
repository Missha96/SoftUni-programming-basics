while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    total_savings = 0.0

    while total_savings < budget:
        savings = float(input())
        total_savings += savings

    print(f'Going to {destination}!')

