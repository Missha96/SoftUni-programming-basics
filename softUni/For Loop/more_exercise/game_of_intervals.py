moves = int(input())

score = 0
point = 0
point2 = 0
point3 = 0
point4 = 0
point5 = 0
point6 = 0

for _ in range(moves):
    number = int(input())

    if 0 <= number <= 9:
        score += number * 0.20
        point += 1
    elif 10 <= number <= 19:
        score += number * 0.30
        point2 += 1
    elif 20 <= number <= 29:
        score += number * 0.40
        point3 += 1
    elif 30 <= number <= 39:
        score += 50
        point4 += 1
    elif 40 <= number <= 50:
        score += 100
        point5 += 1
    else:
        score = score / 2
        point6 += 1

print(f"{score:.2f}")
print(f"From 0 to 9: {(point / moves * 100):.2f}%")
print(f"From 10 to 19: {(point2 / moves * 100):.2f}%")
print(f"From 20 to 29: {(point3 / moves * 100):.2f}%")
print(f"From 30 to 39: {(point4 / moves * 100):.2f}%")
print(f"From 40 to 50: {(point5 / moves * 100):.2f}%")
print(f"Invalid numbers: {(point6 / moves * 100):.2f}%")

