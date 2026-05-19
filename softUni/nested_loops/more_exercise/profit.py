coin1 = int(input())
coin2 = int(input())
money5 = int(input())
total_sum = int(input())


for lev in range(coin1 + 1):
    for dva in range(coin2 + 1):
        for pet in range(money5 + 1):
            if ((lev * 1) + (dva * 2) + (pet * 5)) == total_sum:
                print(f'{lev} * 1 lv. + {dva} * 2 lv. + {pet} * 5 lv. = {total_sum} lv.')



