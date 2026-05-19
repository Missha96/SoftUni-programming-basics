fuel_type = input()
fuel_qty = float(input())
discount_card = input()

if fuel_type == "Gas":
    price_per_liter = 0.93
    card_discount = 0.08
elif fuel_type == "Gasoline":
    price_per_liter = 2.22
    card_discount = 0.18
elif fuel_type == "Diesel":
    price_per_liter = 2.33
    card_discount = 0.12
else:
    price_per_liter = 0
    card_discount = 0
if discount_card == "Yes":
    price_per_liter -= card_discount

total_price = fuel_qty * price_per_liter

if 20 <= fuel_qty <= 25:
    total_price *= 0.92
elif fuel_qty > 25:
    total_price *= 0.90
print(f"{total_price:.2f} lv.")