while True:
    word = input()
    if word == 'end':
        break
    else:
        new_word = word[::-1]
        print(f'{word} = {new_word}')