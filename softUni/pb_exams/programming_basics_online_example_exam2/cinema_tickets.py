movie_name = input()
student = 0
standard = 0
kid = 0
total_tickets = 0


while movie_name != 'Finish':
    free_seats = int(input())
    sold_for_movie = 0
    while True:
        ticket_type = input()
        if ticket_type == 'End':
            break
        sold_for_movie += 1
        total_tickets += 1

        if ticket_type == 'student':
            student += 1
        elif ticket_type == 'standard':
            standard += 1
        elif ticket_type == 'kid':
            kid += 1

        if sold_for_movie == free_seats:
            break

    percent_full = sold_for_movie / free_seats * 100
    print(f"{movie_name} - {percent_full:.2f}% full.")
    movie_name = input()

print(f'Total tickets: {total_tickets}')
print(f'{(student / total_tickets * 100):.2f}% student tickets.')
print(f'{(standard / total_tickets * 100):.2f}% standard tickets.')
print(f'{(kid / total_tickets * 100):.2f}% kids tickets.')

