control_min = int(input())
control_sec = int(input())
meters = float(input())
hundred_meters_sec = int(input())

control_time = (control_min * 60) + control_sec
times_time = meters / 120
total_less_time = times_time * 2.5
martin_time = ((meters / 100) * hundred_meters_sec) - total_less_time
if martin_time <= control_time:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {martin_time:.3f}.')
else:
    print(f'No, Marin failed! He was {abs(control_time - martin_time):.3f} second slower.')

