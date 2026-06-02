number = int(input())
counter_positive = 0
sum_negatives = 0
list_positive = []
list_negative = []
for _ in range(number):
    num = int(input())
    if num >= 0:
        counter_positive += 1
        list_positive.append(num)
    else:
        sum_negatives += num
        list_negative.append(num)
print(list_positive)
print(list_negative)
print(f'Count of positives: {counter_positive}')
print(f'Sum of negatives: {sum_negatives}')
