favourite_book = input()
book_name = input()
books = 0


while book_name != 'No More Books':
    if book_name == favourite_book:
        print(f'You checked {books} books and found it.')
        break

    books += 1
    book_name = input()

else:
    print('The book you search is not here!')
    print(f'You checked {books} books.')

