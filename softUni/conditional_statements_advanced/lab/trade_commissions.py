city = input()
sales = float(input())
percent = -1

if city == "Sofia":
    if 0 <= sales <= 500:
        percent = 0.05
    elif 500 < sales <= 1000:
        percent = 0.07
    elif 1000 < sales <= 10000:
        percent = 0.08
    elif sales > 10000:
        percent = 0.12
elif city == "Varna":
    if 0 <= sales <= 500:
        percent = 0.045
    elif 500 < sales <= 1000:
        percent = 0.075
    elif 1000 < sales <= 10000:
        percent = 0.10
    elif sales > 10000:
        percent = 0.13
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        percent = 0.055
    elif 500 < sales <= 1000:
        percent = 0.08
    elif 1000 < sales <= 10000:
        percent = 0.12
    elif sales > 10000:
        percent = 0.145

if percent >= 0:
    profit = sales * percent
    print(f'{profit:.2f}')
else:
    print('error')