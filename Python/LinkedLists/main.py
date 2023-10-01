class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        self.tail = self.tail if self.tail else new_node

        return self

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def traverse(self):
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def find(self, value):
        current_node = self.head

        while current_node:
            if current_node.data == value:
                return current_node

            current_node = current_node.next

        return None

    def deleteHead(self):
        if not self.head:
            return

        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None

    def to_array(self):
        items = []
        current_node = self.head

        while current_node:
            items.append(current_node.data)
            current_node = current_node.next

        return items


# Usage example
list = LinkedList()

list.append(4)
list.append(6)
list.append(2)

print(list.to_array())

list.prepend(1)
print(list.to_array())

list.find(6)
list.deleteHead()
