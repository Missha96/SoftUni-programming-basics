country = input()
discipline = input()
max_score = 20


if country == 'Bulgaria':
    if discipline == 'ribbon':
        difficulty = 9.600
        performance = 9.400
    elif discipline == 'hoop':
        difficulty = 9.550
        performance = 9.750
    elif discipline == 'rope':
        difficulty = 9.500
        performance = 9.400
elif country == 'Russia':
    if discipline == 'ribbon':
        difficulty = 9.100
        performance = 9.400
    elif discipline == 'hoop':
        difficulty = 9.300
        performance = 9.800
    elif discipline == 'rope':
        difficulty = 9.600
        performance = 9.000
elif country == 'Italy':
    if discipline == 'ribbon':
        difficulty = 9.200
        performance = 9.500
    elif discipline == 'hoop':
        difficulty = 9.450
        performance = 9.350
    elif discipline == 'rope':
        difficulty = 9.700
        performance = 9.150
score = difficulty + performance
percent = (max_score - score) / max_score * 100
print(f'The team of {country} get {score:.3f} on {discipline}.')
print(f'{percent:.2f}%')