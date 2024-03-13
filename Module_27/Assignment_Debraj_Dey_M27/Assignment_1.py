# Given there is a string, we need to reverse the string without using inbuilt method reverse, we need to reverse the string using stack.

class MyStack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)


def reverse(string):
    output = ''
    stack = MyStack()
    for letter in string:
        stack.push(letter)

    while (not stack.is_empty()):
        output += stack.pop()

    return output


str = input('Enter a string to reverse: ')

print(reverse(str))
