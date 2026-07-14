employees = {}

while True:
    command = input().split(" -> ")
    if command[0] == 'End':
        break
    company_name = command[0]
    id = command[1]
    if company_name in employees.keys():
        if id not in employees[company_name]:
            employees[company_name].append(id)
    else:
        employees[company_name] = [id]

for company_name, id in employees.items():
    print(f'{company_name}')
    for each_id in id:
        print(f'-- {each_id}')

