free_days = int(input())

year = 365
working_days = year - free_days
free_days_play_minutes = 127
working_days_play_minutes = 63
norm_minutes = 30000
total_free_days_minutes = free_days_play_minutes * free_days
total_working_days_play_minutes = working_days_play_minutes * working_days
total_play_minutes = total_working_days_play_minutes + total_free_days_minutes
difference = abs(norm_minutes - total_play_minutes)
hours = difference // 60
minutes = difference - (hours * 60)


if total_play_minutes > norm_minutes:
     print('Tom will run away')
     print(f'{hours} hours and {minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')