countries = input().split(", ")
capitals = input().split(", ")

new = dict(zip(countries, capitals))

for country, capital in new.items():
    print(f'{country} -> {capital}')