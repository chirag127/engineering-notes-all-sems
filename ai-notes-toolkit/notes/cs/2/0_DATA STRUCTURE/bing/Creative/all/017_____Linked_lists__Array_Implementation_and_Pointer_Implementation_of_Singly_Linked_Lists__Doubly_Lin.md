# Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial.

## Linked lists

- A linked list is a linear data structure that consists of a sequence of nodes, each containing some data and a pointer to the next node in the list.
- A linked list can be used to store any type of data, such as numbers, characters, strings, etc.
- A linked list can grow or shrink dynamically, depending on the insertion and deletion operations performed on it.
- A linked list does not require a contiguous block of memory, unlike an array. It can utilize the available memory space efficiently.
- A linked list can be classified into different types, such as singly linked list, doubly linked list, circularly linked list, etc., based on the number and direction of pointers in each node.

## Array Implementation of Singly Linked Lists

- A singly linked list can be implemented using an array, where each element of the array represents a node of the list.
- The array should have two fields for each element: one to store the data and one to store the index of the next element in the list.
- The first element of the array is the head of the list, and the last element is the tail of the list.
- A special value, such as -1, can be used to indicate the end of the list or an empty list.
- For example, the following array represents a singly linked list of three nodes, containing the data 10, 20, and 30:

| Data | Next |
|------|------|
| 10   | 1    |
| 20   | 2    |
| 30   | -1   |

- The advantages of using an array to implement a singly linked list are:
  - It is easy to access any element of the list by its index.
  - It is easy to implement the basic operations, such as insertion, deletion, and traversal, using simple array operations.
- The disadvantages of using an array to implement a singly linked list are:
  - It requires a fixed size of memory, which may not be available or may be wasted if the list size changes frequently.
  - It is difficult to insert or delete an element at the beginning or in the middle of the list, as it requires shifting the subsequent elements in the array.

## Pointer Implementation of Singly Linked Lists

- A singly linked list can also be implemented using pointers, where each node of the list is a dynamic memory allocation that contains two fields: one to store the data and one to store the pointer to the next node in the list.
- The head of the list is a pointer that points to the first node of the list, and the tail of the list is a pointer that points to the last node of the list.
- A null pointer can be used to indicate the end of the list or an empty list.
- For example, the following diagram represents a singly linked list of three nodes, containing the data 10, 20, and 30:

![singly linked list pointer](https://i.imgur.com/0lZ1Z0t.png)

- The advantages of using pointers to implement a singly linked list are:
  - It does not require a fixed size of memory, as the nodes can be allocated and deallocated dynamically as per the list size.
  - It is easy to insert or delete an element at any position of the list, as it only requires updating the pointers of the adjacent nodes.
- The disadvantages of using pointers to implement a singly linked list are:
  - It requires extra space for storing the pointers in each node, which may increase the memory overhead.
  - It is difficult to access any element of the list by its index, as it requires traversing the list from the head until the desired node is reached.

## Doubly Linked List

- A doubly linked list is a linear data structure that consists of a sequence of nodes, each containing some data and two pointers: one to the previous node and one to the next node in the list.
- A doubly linked list can be used to store any type of data, such as numbers, characters, strings, etc.
- A doubly linked list can grow or shrink dynamically, depending on the insertion and deletion operations performed on it.
- A doubly linked list does not require a contiguous block of memory, unlike an array. It can utilize the available memory space efficiently.
- A doubly linked list can be traversed in both forward and backward directions, unlike a singly linked list that can only be traversed in one direction.
- A doubly linked list can be