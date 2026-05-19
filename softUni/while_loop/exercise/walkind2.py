goal = 10000
total_steps = 0

command = input()

while command != 'Going home':
    steps = int(command)
    total_steps += steps

    if total_steps > goal:
        print(f'Goal reached! Good job! \n{abs(total_steps - goal)} steps over the goal!')
        break

    command = input()

else:
    steps = int(input())
    total_steps += steps
    if total_steps < goal:
        print(f'{abs(total_steps - goal)} more steps to reach goal.')
    else:
        print(f'Goal reached! Good job! \n{abs(total_steps - goal)} steps over the goal!')