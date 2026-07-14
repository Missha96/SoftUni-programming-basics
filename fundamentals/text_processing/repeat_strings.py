text = input().split()
repeating_string = ''
for _ in range(len(text)):
    single_text = text[0]
    repetitions = len(single_text)
    repeating_string += single_text * int(repetitions)
    text.pop(0)
print(repeating_string)