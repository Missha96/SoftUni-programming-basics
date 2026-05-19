last_sector = input()
rows_first = int(input())
seats_odd = int(input())

total_seats = 0

for sector_code in range(ord('A'), ord(last_sector) + 1):
    sector = chr(sector_code)

    rows = rows_first + (sector_code - ord('A'))

    for row in range(1, rows + 1):

        if row % 2 == 0:
            seats = seats_odd + 2
        else:
            seats = seats_odd

        for seat in range(seats):
            print(f"{sector}{row}{chr(97 + seat)}")
            total_seats += 1

print(total_seats)
