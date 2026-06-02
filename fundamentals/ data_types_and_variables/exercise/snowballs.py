snowballs = int(input())
highest = 0
best_weight = 0
best_quality = 0
best_time = 0
for _ in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    new_highest = (weight // time) ** quality
    if highest < new_highest:
        highest = new_highest
        best_weight = weight
        best_quality = quality
        best_time = time
print(f'{best_weight} : {best_time} = {highest} ({best_quality})')