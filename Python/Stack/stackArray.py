class Stack:
    def __init__(self):
        # We can also use a linked list here
        self.items = []

    # Time complexity: O(1)
    def push(self, item):
        self.items.append(item)

    # Time complexity: O(1)
    def pop(self):
        return self.items.pop()

    # Time complexity: O(1)
    def size(self):
        return len(self.items)

    # Time complexity: O(1)
    def peek(self):
        return self.items[-1]


stack = Stack()
stack.push(5)               # Time complexity: O(1)
stack.push(12)              # Time complexity: O(1)
stack.push(5)               # Time complexity: O(1)
print(stack.peek())         # Time complexity: O(1)
print(stack.pop())          # Time complexity: O(1)
print(stack.peek())         # Time complexity: O(1)
print(stack.size())         # Time complexity: O(1)
