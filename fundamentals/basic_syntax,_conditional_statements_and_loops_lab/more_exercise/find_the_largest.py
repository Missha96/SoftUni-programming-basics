number = int(input())
digits = str(number)
all_digits = ''
for digit in str(digits):
    all_digits += digit
    new_string = sorted(all_digits, reverse=True)


print("".join(new_string))