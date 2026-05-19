from math import floor, ceil
magnolia_qty = int(input())
hyacinth_qty = int(input())
rose_qty = int(input())
cactus_qty = int(input())
gift_price = float(input())

magnolia_price = 3.25
hyacinth_price = 4
rose_price = 3.50
cactus_price = 8

total_order = (magnolia_price * magnolia_qty) + (hyacinth_price * hyacinth_qty) + (rose_price * rose_qty) + (cactus_price * cactus_qty)
profit = total_order - (total_order * 0.05)
diff = abs(profit - gift_price)

if total_order >= gift_price:
    print(f'She is left with {floor(diff)} leva.')
else:
    print(f'She will have to borrow {ceil(diff)} leva.')