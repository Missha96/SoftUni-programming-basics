budget = float(input())
videocard = int(input())
procesor = int(input())
ram = int(input())

videocard_price = 250
total_videocard_price = videocard * videocard_price

procesor_price = total_videocard_price * 0.35
total_procesor_price = procesor_price * procesor

ram_price = total_videocard_price * 0.10
total_ram_price = ram * ram_price

total = total_videocard_price + total_procesor_price + total_ram_price

if videocard > procesor:
    total *= 0.85

difference = abs(total - budget)

if budget >= total:
    print(f'You have {difference:.2f} leva left!')
else:
    print(f'Not enough money! You need {difference:.2f} leva more!')