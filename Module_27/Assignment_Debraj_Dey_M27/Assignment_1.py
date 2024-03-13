# Given there is a string, we need to reverse the string without using inbuilt method reverse, we need to reverse the string using stack.

from Stack import MyStack


def reverse(string):
    output = ''
    stack = MyStack()
    for letter in string:
        stack.push(letter)

    while (not stack.is_empty()):
        output += stack.pop()

    return output


results = []
test_cases = int(input())
while (test_cases > 0):
    str = input()
    results.append(reverse(str))
    test_cases -= 1

print('\n')
for result in results:
    print(result)
