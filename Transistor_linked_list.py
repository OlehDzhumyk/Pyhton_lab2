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
        current_node = self.head
        for i in range(index):
            current_node = current_node.next_node
        return current_node

    def set(self, index: int, node_path: Node):
        if index > self.length - 1:
            print("йой")

        if index == 0:
            node = Node(node_path.transistor, None, self.head.next_node)
            self.head.next_node.previous_node = node
            self.head = node
            return True

        elif index == self.length - 1:
            node = Node(node_path.transistor, self.tail.previous_node, None)
            self.tail.previous_node.next_node = node
            self.tail = node
            return True
        else:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next_node

            node = Node(node_path.transistor, current_node.previous_node, current_node.next_node)

            current_node.previous_node.next_node = node
            current_node.next_node.previous_node = node

    def sort_by_max_current(self):
        for i in range(self.length):
            x = self.get(i)
            j = i
            while j > 0 and self.get(j - 1).transistor.maximum_current > x.transistor.maximum_current:
                self.set(j, self.get(j - 1))
                j = j - 1
            self.set(j, x)

    def print_all_with_brand(self, brand: str):
        for i in range(self.length):
            if self.get(i).transistor.brand == brand:
                self.get(i).print_transistor()
