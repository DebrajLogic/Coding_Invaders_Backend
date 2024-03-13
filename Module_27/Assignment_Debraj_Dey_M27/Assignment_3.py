'''Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
boolean is_empty() Returns true if the queue is empty, false otherwise.

Note:
You must use only standard operations of a stack, which means only push to top, pop from top, size, and check empty operations are valid.
'''


class MyQueue:
    def __init__(self):
        self.queue = list()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def empty(self) -> bool:
        return len(self.queue) == 0


myQueue = MyQueue()
myQueue.push(1)  # queue have: [1]
print(myQueue.queue)
# queue will be having: [1, 2] (leftmost is front of the queue)
myQueue.push(2)
print(myQueue.queue)
print(myQueue.pop())   # return 1, queue will have [2]
print(myQueue.queue)
print(myQueue.empty())  # return false
