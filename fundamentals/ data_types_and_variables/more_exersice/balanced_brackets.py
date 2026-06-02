lines = int(input())
stack = []

for _ in range(lines):
    string = input()
    if string == '(':
        stack.append(string)
    elif string == ')':
        if not stack:
            print('UNBALANCED')
            break
        stack.pop()
else:
    print('BALANCED' if not stack else 'UNBALANCED')
