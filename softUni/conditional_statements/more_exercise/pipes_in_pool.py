pool_volume = int(input())
p1 = int(input())
p2 = int(input())
hours = float(input())

p1_total = p1 * hours
p2_total = p2 * hours
pipes_total = (p1_total + p2_total)


p1_percent = (p1_total / pipes_total) * 100
p2_percent = (p2_total / pipes_total) * 100


if pipes_total <= pool_volume and pool_volume != 0:
    fill_percent = (pipes_total / pool_volume) * 100
    print(f'The pool is {fill_percent:.2f}% full. Pipe 1: {p1_percent:.2f}%. Pipe 2: {p2_percent:.2f}%.')
else:
    litters_overflow = (pipes_total - pool_volume)
    print(f'For {hours} hours the pool overflows with {litters_overflow:.2f} liters.')