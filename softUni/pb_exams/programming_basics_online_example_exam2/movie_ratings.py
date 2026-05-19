import sys
movies_qty = int(input())
qty = []
movie_name = ''
movies = []
total_rating = 0

for _ in range(movies_qty):
    movie_name = input()
    rating = float(input())
    qty.append(rating)
    movies.append(movie_name)
    total_rating += rating

position_max = qty.index(max(qty))
position_min = qty.index(min(qty))
position_movie_max = position_max
position_movie_min = position_min


print(f'{movies[position_movie_max]} is with highest rating: {max(qty)}')
print(f'{movies[position_movie_min]} is with lowest rating: {min(qty)}')
print(f'Average rating: {(total_rating / movies_qty):.1f}')