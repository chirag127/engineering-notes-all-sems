# Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial.

## Linked lists
- A linked list is a linear data structure that stores a collection of data elements dynamically .
- Nodes represent those data elements, and links or pointers connect each node .
- Each node consists of two fields, the information stored in a linked list and a pointer that stores the address of its next node .
- Linked lists are not stored at contiguous memory locations, unlike arrays .
- Linked lists can grow and shrink in size during execution, unlike arrays .
- Linked lists can be classified into different types based on the number and direction of links between nodes .

## Array Implementation of Singly Linked Lists
- A singly linked list is a type of linked list that has only one link or pointer for each node .
- The link points to the next node in the list, and the last node has a null pointer .
- An array implementation of a singly linked list uses a fixed-size array to store the nodes of the list .
- The array has two columns, one for the data field and one for the link field .
- The link field stores the index of the next node in the array, or -1 if there is no next node .
- The array implementation of a singly linked list has some advantages and disadvantages over the pointer implementation .
  - Advantages:
    - It is easy to access any node by its index in the array .
    - It does not require dynamic memory allocation .
  - Disadvantages:
    - It has a fixed size and cannot grow or shrink dynamically .
    - It may waste space if the array is larger than the number of nodes in the list .
    - It may not have enough space if the array is smaller than the number of nodes in the list .
    - It requires shifting of elements when inserting or deleting nodes .

## Pointer Implementation of Singly Linked Lists
- A pointer implementation of a singly linked list uses dynamic memory allocation to create nodes as needed .
- The nodes are not stored in a fixed order in memory, but are linked by pointers .
- The pointer field of each node stores the address of the next node in memory, or null if there is no next node .
- The pointer implementation of a singly linked list has some advantages and disadvantages over the array implementation .
  - Advantages:
    - It can grow and shrink dynamically according to the number of nodes in the list .
    - It does not waste space as it only allocates memory for the nodes that are needed .
    - It does not require shifting of elements when inserting or deleting nodes .
  - Disadvantages:
    - It is difficult to access any node by its index as it requires traversing the list from the beginning .
    - It requires dynamic memory allocation and deallocation, which may be costly and prone to errors .

## Doubly Linked List
- A doubly linked list is a type of linked list that has two links or pointers for each node .
- The links point to the previous and the next node in the list, and the first and the last node have null pointers for the previous and the next node respectively .
- A doubly linked list allows traversal in both directions, forward and backward .
- A doubly linked list can be implemented using arrays or pointers, similar to a singly linked list