class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    # Time complexity: O(1)
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    # Time complexity: O(1)
    def pop(self):
        if not self.top:
            return None  # Stack is empty
        removed_node = self.top
        self.top = self.top.next
        self.size -= 1
        return removed_node.value

    # Time complexity: O(1)
    def get_size(self):
        return self.size

    # Time complexity: O(1)
    def peek(self):
        if not self.top:
            return None  # Stack is empty
        return self.top.value


stack = Stack()
stack.push(5)               # Time complexity: O(1)
stack.push(12)              # Time complexity: O(1)
stack.push(5)               # Time complexity: O(1)
print(stack.peek())         # Time complexity: O(1)
print(stack.pop())          # Time complexity: O(1)
print(stack.peek())         # Time complexity: O(1)
print(stack.get_size())     # Time complexity: O(1)
