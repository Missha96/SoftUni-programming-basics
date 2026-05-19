price_of_mackerel = float(input())
price_of_sprinkle = float(input()) #caca
bonito_kg = float(input())  #palamud
safrid_kg = float(input())
mussels_kg = int(input())

price_of_bonito = price_of_mackerel + price_of_mackerel * 0.60
price_of_safrid = price_of_sprinkle + price_of_sprinkle * 0.80
price_of_mussels = 7.50

bonito_total = price_of_bonito * bonito_kg
safrid_total = price_of_safrid * safrid_kg
mussels_total = price_of_mussels * mussels_kg

total = bonito_total + safrid_total + mussels_total

final = f"{total:.2f}"

print(final)