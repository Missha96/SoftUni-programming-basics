male = int(input())
female = int(input())
tables = int(input())
counter = 0
is_free = False

for m in range(1, male + 1):
    if is_free:
        break
    for f in range(1, female + 1):
        print(f"({m} <-> {f})", end=' ')
        counter += 1
        if counter >= tables:
            is_free = True
            break
