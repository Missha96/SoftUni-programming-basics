annual_tax_for_trainning = int(input())

shoes = annual_tax_for_trainning * 0.40
shoes_price = annual_tax_for_trainning - shoes

equip = shoes_price * 0.20
equip_price = shoes_price - equip

ball = equip_price / 4

acsesoaries = ball / 5

total = annual_tax_for_trainning + shoes_price + equip_price + ball + acsesoaries

print(total)