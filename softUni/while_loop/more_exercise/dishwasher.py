detergent = int(input())
detergent_ml = 750
counter = 0
total_dishes = 0
total_pods = 0
needed_detergent = 0
total_detergent = detergent * detergent_ml

while True:
    command = input()
    if command == 'End':
        break
    dishes = int(command)
    counter += 1
    if counter == 3:
        needed_detergent += dishes * 15
        total_pods += dishes
        counter = 0
    else:
        needed_detergent += dishes * 5
        total_dishes += dishes
    if total_detergent < needed_detergent:
        print(f"Not enough detergent, {abs(total_detergent - needed_detergent)} ml. more necessary!")
        break

if total_detergent >= needed_detergent:
    print(f"Detergent was enough!")
    print(f"{total_dishes} dishes and {total_pods} pots were washed.")
    print(f"Leftover detergent {abs(total_detergent - needed_detergent)} ml.")




