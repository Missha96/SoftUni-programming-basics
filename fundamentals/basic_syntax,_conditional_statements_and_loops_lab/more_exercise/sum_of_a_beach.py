text = input()
new_text = text.lower()
beach_words = 0
word = ''

if 'sand' in new_text:
    word = 'sand'
    beach_words += new_text.count(word)
if 'fish' in new_text:
    word = 'fish'
    beach_words += new_text.count(word)
if 'sun' in new_text:
    word = 'sun'
    beach_words += new_text.count(word)
if 'water' in new_text:
    word = 'water'
    beach_words += new_text.count(word)
print(beach_words)
