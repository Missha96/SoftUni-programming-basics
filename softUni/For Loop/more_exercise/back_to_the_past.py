inherited_money = float(input())
year_living = int(input())
ivancho_years = 18

for year in range(1800, year_living + 1):
    if year % 2 == 0:
        inherited_money -= 12000
        ivancho_years += 1
    else:
        inherited_money -= 12000 + 50 * ivancho_years
        ivancho_years += 1

if inherited_money >= 0:
    print(f'Yes! He will live a carefree life and will have {abs(inherited_money):.2f} dollars left.')
else:
    print(f'He will need {abs(inherited_money):.2f} dollars to survive.')