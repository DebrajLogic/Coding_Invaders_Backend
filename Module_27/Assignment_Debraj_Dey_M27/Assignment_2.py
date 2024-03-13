# Given a string containing opening and closing braces, branches can be [ ] OR { } OR ( ). check if it represents a balanced expression or not.

from Stack import MyStack


def check_expression(expression):
    stack = MyStack()
    opening = {'[': ']', '{': '}', '(': ')', ']': '[', '}': '{', ')': '('}
    length = len(expression)

    # if the expression is does not start with a opening bracket
    if expression[0] == ']' or expression[0] == '}' or expression[0] == ')':
        return 'The expression is not balanced'
    else:
        stack.push(expression[0])
        # print('\nInitial state:')
        # stack.display()

    for i in range(1, length):
        # print('\nIteration', i)
        if not stack.is_empty():
            previous_bracket = stack.pop()
            stack.push(previous_bracket)
        else:
            previous_bracket = 'None'
        # print(f'previous bracket = {previous_bracket}')
        # print(f'current bracket = {expression[i]}')
        if previous_bracket == opening[expression[i]]:
            if stack.is_empty():
                continue
            removed_item = stack.pop()
            # print(f'removed {removed_item}')
            # stack.display()
        else:
            stack.push(expression[i])
            # stack.display()

    if stack.is_empty():
        return 'The expression is balanced'
    else:
        return 'The expression is not balanced'


# expression = '{[{}{}]}[()]'
# print(check_expression(expression))


results = []
test_cases = int(input())
while (test_cases > 0):
    expression = input()
    results.append(check_expression(expression))
    test_cases -= 1

for result in results:
    print(result)
