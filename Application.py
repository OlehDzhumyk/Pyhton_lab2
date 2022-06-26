from Transistor import Transistor
from Transistor_linked_list import TransistorLinkedList

if __name__ == "__main__":
    tr_list = TransistorLinkedList()
    tr_list.add(Transistor("pnp", "oleh", 2, 100))
    tr_list.add(Transistor("pnp", "oleh", 3, 100))
    tr_list.add(Transistor("pnp", "oleh", 4, 100))
    tr_list.add(Transistor("pnp", "oleh", 1, 100))
    tr_list.add(Transistor("pnp", "oleh", 0, 100))
    tr_list.add(Transistor("pnp", "oleh", 5, 100))

    tr_list.sort_by_max_current()

    tr_list.print_all_with_brand("oleh")
