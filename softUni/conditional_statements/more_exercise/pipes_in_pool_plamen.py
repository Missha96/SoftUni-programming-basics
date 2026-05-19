from math import floor
pool_volume = int(input())
p1 = int(input())
p2 = int(input())
hours = float(input())


total_litters = (p1 + p2) * hours


if total_litters <= pool_volume:
    percent_full = (total_litters / pool_volume) * 100
    p1_percent = (p1 * hours / total_litters) * 100 if total_litters > 0 else 0
    p2_percent = (p2 * hours / total_litters) * 100 if total_litters > 0 else 0
    print(f'The pool is {percent_full}% full. Pipe 1: {p1_percent:.2f}%. Pipe 2: {p2_percent:.2f}%.')
else:
    litters_overflow = total_litters - pool_volume
    print(f'For {hours:.2f} hours the pool overflows with {litters_overflow:.2f} liters.')