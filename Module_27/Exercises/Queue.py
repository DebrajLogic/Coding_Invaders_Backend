class MyQueue():
    def __init__(self):
        self.queue = list()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(self.queue)


queue = MyQueue()
queue.enqueue('1')
queue.enqueue('2')
queue.enqueue('3')
queue.dequeue()
print(queue.is_empty())
queue.display()
