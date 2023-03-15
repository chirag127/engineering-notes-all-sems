# Implementation of Stack using Linked List

- A stack is a linear data structure that follows the **LIFO (Last In First Out)** principle, meaning that the last element inserted into the stack is the first one to be removed.
- A stack supports various operations like **push**, **pop**, **peek**, **empty**, and **size**.
- A stack can be implemented using an array or a linked list. The benefit of implementing a stack using a linked list over arrays is that it allows the stack to grow or shrink as per the requirements, i.e., memory can be allocated or deallocated dynamically .
- A linked list is a collection of nodes, where each node contains some data and a pointer to the next node in the list. The first node is called the **head** and the last node is called the **tail**. The tail node points to **NULL** to indicate the end of the list.
- To implement a stack using a linked list, we need to maintain a pointer to the top of the stack, which is the head of the linked list. The push operation will insert a new node at the beginning of the list, and the pop operation will delete the first node from the list. The peek operation will return the data of the first node without deleting it. The empty operation will check if the list is empty or not, and the size operation will count the number of nodes in the list.

## Pseudocode for stack operations using linked list

- Define a structure for a node, which contains a data field and a next pointer field.
- Define a global variable for the top pointer, which points to the head of the linked list.
- Define a function to create a new node, which takes a data value as a parameter and returns a pointer to the node.
- Define a function to push a data value into the stack, which takes a data value as a parameter and returns nothing.
  - Create a new node using the create node function and assign the data value to it.
  - If the top pointer is NULL, then the stack is empty and the new node is the first node in the list. Set the top pointer to point to the new node and set the next pointer of the new node to NULL.
  - Else, the stack is not empty and the new node is inserted at the beginning of the list. Set the next pointer of the new node to point to the node pointed by the top pointer and set the top pointer to point to the new node.
- Define a function to pop a data value from the stack, which takes no parameters and returns the data value of the popped node.
  - If the top pointer is NULL, then the stack is empty and there is nothing to pop. Print an error message and return -1.
  - Else, the stack is not empty and the first node is popped from the list. Store the data value of the node pointed by the top pointer in a temporary variable. Set the top pointer to point to the next node in the list and free the memory of the popped node. Return the temporary variable.
- Define a function to peek the data value at the top of the stack, which takes no parameters and returns the data value of the top node.
  - If the top pointer is NULL, then the stack is empty and there is nothing to peek. Print an error message and return -1.
  - Else, the stack is not empty and the first node is the top node. Return the data value of the node pointed by the top pointer.
- Define a function to check if the stack is empty, which takes no parameters and returns a boolean value.
  - If the top pointer is NULL, then the stack is empty and return true.
  - Else, the stack is not empty and return false.
- Define a function to get the size of the stack, which takes no parameters and returns an integer value.
  - Initialize a counter variable to zero.
  - Initialize a temporary pointer to point to the node pointed by the top pointer.
  - Loop through the list until the temporary pointer is NULL, incrementing the counter and moving the temporary pointer to the next node in each iteration.
  - Return the counter value.

## C code for stack operations using linked list

```c
// Define a structure for a node
struct node {
  int data; // data field
  struct node *next; // next pointer field
};

// Define a global variable for the top pointer
struct node *top = NULL;

// Define a function to create a new node
struct node *create_node(int data) {