name = input()
starting_points = float(input())
judges = int(input())

grade = 0
judge_name = ''

for _ in range(judges):
    judge_name = input()
    judge_points = float(input())
    grade = starting_points + (len(judge_name) * judge_points / 2)
    starting_points = grade
    if starting_points > 1250.5:
        break
if starting_points > 1250.5:
    print(f'Congratulations, {name} got a nominee for leading role with {starting_points:.1f}!')
else:
    print(f'Sorry, {name} you need {1250.5 - grade:.1f} more!')