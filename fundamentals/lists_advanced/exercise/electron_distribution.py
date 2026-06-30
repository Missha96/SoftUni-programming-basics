number_of_electrons = int(input())
electrons_list = []
shell = 1


while number_of_electrons:
    electrons_to_fill = 2 * shell ** 2
    shell += 1
    if electrons_to_fill <= number_of_electrons:
        electrons_list.append(electrons_to_fill)
        number_of_electrons -= electrons_to_fill
    else:
        electrons_list.append(number_of_electrons)
        number_of_electrons -= number_of_electrons
        break
print(electrons_list)