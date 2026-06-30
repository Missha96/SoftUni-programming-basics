crops = input().split(" & ")
i = 0
while True:

    command = input().split()
    current_command = command[0]

    if current_command == 'Collect!':
        print(" | ".join(crops))
        break

    if current_command == 'Plant':
        crop = command[1]
        if crop not in crops:
            crops.insert(0, crop)

    elif current_command == 'Transplant':
        crop = command[1]
        if crop in crops:
            crops.remove(crop)
            crops.append(crop)

    elif current_command == 'Replace':
        index1 = int(command[1])
        index2 = int(command[2])
        if 0 <= index1 < len(crops) and 0 <= index2 < len(crops):
            crops[index1], crops[index2] = crops[index2], crops[index1]

    elif current_command == 'Uproot':
        crop = command[1]
        if crop in crops:
            crops.remove(crop)
