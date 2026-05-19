paper_qty = int(input())
plat_qty = int(input())
glue_liters = float(input())
percent_discount = int(input())

paper = 5.80
plat = 7.20
glue = 1.20

total_sum = (paper * paper_qty) + (plat * plat_qty) + (glue * glue_liters)
total_percent = percent_discount / 100
percent = 1 - total_percent
total = total_sum * percent

print(f'{total:.3f}')