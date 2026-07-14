text = input()
rage_message = ''
new_text = ''
repetitions = ''
for index in range(len(text)):
    if text[index].isdigit():
        repetitions += text[index]
        if index + 1 < len(text):
            if text[index + 1].isdigit():
                repetitions += text[index + 1]
        rage_message += new_text * int(repetitions)
        new_text = ''
        repetitions = ''
    else:
        new_text += text[index].upper()
    if repetitions == 1:
        rage_message += new_text
print(f'Unique symbols used: {len(set(rage_message))}')
print(rage_message)
