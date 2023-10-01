class Queue:
    def __init__(self):
        self.items = []

    # Time complexity: O(1)
    def enqueue(self, element):
        self.items.append(element)

    # Time complexity: O(N)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    # Time complexity: O(1)
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    # Time complexity: O(1)
    def is_empty(self):
        return len(self.items) == 0

    # Time complexity: O(1)
    def size(self):
        return len(self.items)

    # Time complexity: O(N)
    def print(self):
        print(self.items)

queue = Queue()
print(queue.is_empty())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.size())
queue.print()
print(queue.dequeue())
print(queue.peek())
queue.print()
