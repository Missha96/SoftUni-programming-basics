goal = 10000
total_steps = 0
while True:
    command = input()
    if command != 'Going home':
        steps = int(command)
        total_steps += steps

        if total_steps > goal:
            print(f'Goal reached! Good job! {abs(total_steps - goal)} steps over the goal!')
        # else:
        #     print(f'{abs(total_steps - goal)} more steps to reach goal.')

    elif command == 'Going home':
        steps = int(input())
        total_steps += steps
        if total_steps > goal:
            print(f'Goal reached! Good job! {abs(total_steps - goal)} steps over the goal!')
        # else:
        #     print(f'{abs(total_steps - goal)} more steps to reach goal.')
        if total_steps > goal:
            print(f'Goal reached! Good job! {abs(total_steps - goal)} steps over the goal!')
        else:
            print(f'{abs(total_steps - goal)} more steps to reach goal.')
        # print(f'{abs(total_steps - goal)} more steps to reach goal.')
        # print(f'Goal reached! Good job! {abs(total_steps - goal)} steps over the goal!')
    # else:
    #     print(f'{abs(total_steps - goal)} more steps to reach goal.')

