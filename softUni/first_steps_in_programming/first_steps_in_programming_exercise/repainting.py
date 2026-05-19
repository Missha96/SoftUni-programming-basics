plastic_cover_qty = int(input())
paint_qty = int(input())
paint_thinner_qty = int(input())
hours = int(input())

plastic_cover_price = 1.5
paint_price = 14.50
thinner_price = 5
bags = 0.40

plastic_cover_extra = plastic_cover_qty + 2
paint_extra = paint_qty + (paint_qty * 0.10)

total_materials = (plastic_cover_extra * plastic_cover_price) + (paint_extra * paint_price) + (paint_thinner_qty * thinner_price) + bags

total_for_handyman = (total_materials * 0.30) * hours

total = total_materials + total_for_handyman

print(total)