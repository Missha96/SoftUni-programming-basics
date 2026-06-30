input_operator = input()
first_num = int(input())
second_num = int(input())


def solve_operation(a, b, operator):
    result = None
    if operator == 'add':
        result = a + b

    elif operator == 'subtract':
        result = a - b

    elif operator == 'multiply':
        result = a * b

    elif operator == 'divide':
        result = a // b

    return result


print(solve_operation(first_num, second_num, input_operator))