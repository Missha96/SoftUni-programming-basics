room_rent = int(input())

statue = room_rent * 0.70
catering = statue * 0.85
music = catering / 2

total = room_rent + statue + catering + music
print(f'{total:.2f}')