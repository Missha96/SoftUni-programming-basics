n = int(input())
grand_total = 0
for _ in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if (0.01 <= price_per_capsule <= 100.00) and (1 <= days <= 31) and (1 <= capsules <= 2000):
        total = price_per_capsule * days * capsules
        print(f'The price for the coffee is: ${total:.2f}')
        grand_total += total
    else:
        continue
print(f'Total: ${grand_total:.2f}')