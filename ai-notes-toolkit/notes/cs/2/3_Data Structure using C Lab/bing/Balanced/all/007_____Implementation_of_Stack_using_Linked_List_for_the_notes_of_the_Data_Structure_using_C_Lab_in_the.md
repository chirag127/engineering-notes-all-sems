# Implementation of Stack using Linked List

- A stack is a linear data structure that follows the LIFO (Last In First Out) principle, meaning that the element that is inserted last is removed first.
- A linked list is a dynamic data structure that consists of a sequence of nodes, each node having a data field and a pointer field that points to the next node in the list.
- A stack can be implemented using a linked list by maintaining a pointer to the top node of the list, and performing the following operations:

  - Push: To insert a new element at the top of the stack, create a new node with the given data, point its next field to the current top node, and update the top pointer to the new node.
  - Pop: To remove the element at the top of the stack, check if the stack is empty, if not, store the data of the top node, update the top pointer to the next node, and delete the previous top node. Return the stored data or an error message if the stack is empty.
  - Peek: To return the element at the top of the stack without removing it, check if the stack is empty, if not, return the data of the top node or an error message if the stack is empty.
  - IsEmpty: To check if the stack is empty, return true if the top pointer is null, or false otherwise.
  - Display: To print the elements of the stack from top to bottom, traverse the linked list from the top node to the end, and print the data of each node.

- The advantages of implementing a stack using a linked list are:

  - The size of the stack is not fixed and can grow or shrink as needed.
  - The memory allocation and deallocation are done at runtime, so there is no wastage of memory or overflow.
  - The insertion and deletion operations are done in constant time, as only the top node is affected.

- The disadvantages of implementing a stack using a linked list are:

  - The extra space is required for the pointer field of each node, which increases the memory usage.
  - The access to the elements of the stack is sequential, not random, which may affect the performance in some applications.