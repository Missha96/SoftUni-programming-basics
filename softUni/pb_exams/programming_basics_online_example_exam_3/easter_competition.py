kozunak_count = int(input())

best_baker = ""
best_points = 0

for _ in range(kozunak_count):
    baker_name = input()

    total_points = 0

    while True:
        command = input()

        if command == "Stop":
            break

        points = int(command)
        total_points += points

    print(f"{baker_name} has {total_points} points.")

    if total_points > best_points:
        best_points = total_points
        best_baker = baker_name
        print(f"{baker_name} is the new number 1!")

print(f"{best_baker} won competition with {best_points} points!")