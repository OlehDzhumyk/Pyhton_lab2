from Transistor import Transistor


class Node:
    def __init__(self, transistor: Transistor, previous_node, next_node):
        self.transistor = transistor
        self.previous_node = previous_node
        self.next_node = next_node

    def print_transistor(self):
        print(self.transistor.brand, self.transistor.type, self.transistor.maximum_current, self.transistor.maximum_voltage)
        return True
