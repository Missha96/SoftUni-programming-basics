square_meters_for_landscaping = float(input())

price_for_landscaping = square_meters_for_landscaping * 7.61

discount = price_for_landscaping * 0.18

total_price = price_for_landscaping - discount

print (f'The final price is: {total_price} lv.')
print (f"The discount is: {discount} lv.")

