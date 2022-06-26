from Node import Node
from Transistor import Transistor


class TransistorLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, transistor: Transistor):
        if self.head:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = Node(transistor, current_node, None)
            self.tail = current_node.next_node
            self.length += 1
        else:
            self.head = Node(transistor, None, None)
            self.tail = self.head
            self.length += 1
        return True

    def add_at_the_end(self, transistor: Transistor):
        if self.tail:
            self.tail.next_node = Node(transistor, self.tail, None)
            self.tail = self.tail.next_node
            self.length += 1
        else:
            self.head = Node(transistor, None, None)
            self.tail = self.head
            self.length += 1
        return True

    def remove(self, transistor: Transistor):
        node_to_delete = self.search(transistor)
        if node_to_delete:
            if node_to_delete.previous_node is None:
                self.head = node_to_delete.next_node
                self.length -= 1
                return True
            if node_to_delete.next_node is None:
                self.tail = node_to_delete.previous_node
                self.length -= 1
                return True
            node_to_delete.previous_node.next_node = node_to_delete.next_node
            node_to_delete.next_node = node_to_delete.previous_node
            self.length -= 1

    def search(self, transistor):
        if self.head:
            current_node = self.head
            while current_node.transistor != transistor and current_node:
                current_node = current_node.next_node
            return current_node

    def remove_all(self):
        self.tail = None
        self.head = None
        self.length = 0

    def get(self, index: int):
        if index > self.length - 1 or index < 0:
            raise Exception(f"Out of range. Get {index} form {self.length - 1}")

        current_node = self.head
        for i in range(index):
            current_node = current_node.next_node
        return current_node.transistor

    def set(self, index: int, transistor: Transistor):
        if index > self.length - 1 or index < 0:
            raise Exception(f"Out of range. Get {index} form {self.length - 1}")

        current_node = self.head
        for i in range(index):
            current_node = current_node.next_node
        current_node.transistor = transistor

    def sort_by_max_current(self):
        for i in range(self.length):
            x = self.get(i)
            j = i
            while j > 0 and self.get(j - 1).maximum_current > x.maximum_current:
                self.set(j, self.get(j - 1))
                j = j - 1
            self.set(j, x)

    def print_all_with_brand(self, brand: str):
        current_node = self.head
        for i in range(self.length):
            if current_node.transistor.brand == brand:
                current_node.print_transistor()
            current_node = current_node.next_node
