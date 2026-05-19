vegetables_price = float(input())
fruits_price = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())

vegetables_total = vegetables_kg * vegetables_price
fruits_total = fruits_kg * fruits_price
total_in_euro = (vegetables_total + fruits_total) / 1.94

form = f"{total_in_euro:.2f}"

print(form)