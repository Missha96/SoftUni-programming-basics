sums = input().split(', ')
beggars = int(input())
money_as_int = []

for money in sums:
    money_as_int.append(int(money))
beggars_sum = []
start_index = 0
for current_beggar in range(beggars):
    current_beggar_sum = 0
    for index in range(start_index, len(money_as_int), beggars):
        current_beggar_sum += money_as_int[index]
    beggars_sum.append(current_beggar_sum)
    start_index += 1
print(beggars_sum)
