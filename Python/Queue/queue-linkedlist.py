class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Time complexity: O(1)
    def enqueue(self, value): # adding element to end of queue aka push
        node = Node(value)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    # Time complexity: O(1)
    def dequeue(self): # removing first element of queue aka pop
        if self.is_empty():
            return None
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return value

    # Time complexity: O(1)
    def peek(self):
        if self.is_empty():
            return None
        return self.head.value

    # Time complexity: O(1)
    def is_empty(self):
        return self.size == 0

    # Time complexity: O(1)
    def get_size(self):
        return self.size

    # Time complexity: O(N)
    def print(self):
        if self.is_empty():
            print("List is empty")
        else:
            curr = self.head
            list = ""
            while curr:
                list += f"{curr.value} -> "
                curr = curr.next
            list += "None"
            print(list)


queue = LinkedListQueue()
print(queue.is_empty())     # True
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.get_size())     # 3
queue.print()               # 10 -> 20 -> 30 -> None
print(queue.dequeue())      # 10
queue.print()               # 20 -> 30 -> None
print(queue.peek())         # 20
