guests = int(input())
price_per_person = float(input())
budget = float(input())

if 10 <= guests <= 15:
    price_per_person = price_per_person * 0.85
elif 15 < guests <= 20:
    price_per_person = price_per_person * 0.80
elif guests > 20:
    price_per_person = price_per_person * 0.75

cake = budget * 0.10
total = cake + (price_per_person * guests)
if budget >= total:
    print(f'It is party time! {abs(budget - total):.2f} leva left.')
else:
    print(f'No party! {abs(budget - total):.2f} leva needed.')