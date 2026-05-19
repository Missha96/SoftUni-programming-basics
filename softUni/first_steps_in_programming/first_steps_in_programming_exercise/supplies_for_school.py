pens_quantity = int(input())
marker_quantity = int(input())
litters_cleaning_spray = int(input())
discount = int(input())

price_per_pen = 5.80
price_per_marker = 7.20
price_per_cleaning_spray = 1.20

total_for_pens = price_per_pen * pens_quantity
total_for_markers = price_per_marker * marker_quantity
total_for_cleaning_spray = litters_cleaning_spray * price_per_cleaning_spray
discount2 = discount / 100

total = total_for_pens + total_for_markers + total_for_cleaning_spray

total_with_discount = total - (total * discount2)
print(total_with_discount)