# Second Python lab2
## Task: Implement open bidirectional linked list:

There is a class `Transistor_linked`.
Each list has two attributes:
`head` and `tail`
which are pointers for the first and the last node of the list.
Each node has three attributes:
1. Object type `Transistor` `transistor`    
   * Each `Transistor`'s has:
       * `type`: String
       * `brand`: String
       * `maximum_current`: float
       * `maximum_voltage`: float
2. Pointer for the previous node `previous_node`;
3. Pointer for the next node  `next_node`

## Function

- Adding an item to the list;  
`.add(Transistor)` -> Boolean Type


- Add transistor at the end;  
`.add_at_the_end(Transistor)` -> Boolean Type


- Searching for an item by key;  
`.search(Transistor)` -> Node


- Outputting item data;  
`.print_transistor(Node)` -> Boolean Type


Removing an item from the list;  
`.remove(Transistor)` -> Boolean Type


- Removing all items from the list;  
`.remove_all()` -> Boolean Type

  
- Sort the list by maximum current by selection method;  
`.sort()` -> Boolean Type


- Output information about the transistor of a given brand;  
`.print_all_with_brand(brand: String)` -> Boolean Type
***

![Screenshot](https://user-images.githubusercontent.com/93152974/171742422-27b37e05-acfa-453e-a0fa-a651587e401d.png)




