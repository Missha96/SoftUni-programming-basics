number_of_rooms = int(input())
room = 0
total_chairs = 0
total_visitors = 0
for _ in range(number_of_rooms):
    room += 1
    chairs_and_visitors = input().split()
    chairs = int(len(chairs_and_visitors[0]))
    visitors = int(chairs_and_visitors[1])
    total_chairs += chairs
    total_visitors += visitors
    if visitors > chairs:
        print(f"{visitors - chairs} more chairs needed in room {room}")
if total_chairs >= total_visitors:
    print(f"Game On, {total_chairs - total_visitors} free chairs left")
