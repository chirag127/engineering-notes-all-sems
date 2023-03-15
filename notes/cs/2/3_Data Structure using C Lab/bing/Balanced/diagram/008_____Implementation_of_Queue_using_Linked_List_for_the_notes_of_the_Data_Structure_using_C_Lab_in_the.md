### Implementation of Queue using Linked List

A queue is a linear data structure that follows the First In First Out (FIFO) principle. It means that the element that is inserted first is removed first. A queue has two operations: enqueue and dequeue. Enqueue is the process of adding an element at the rear end of the queue. Dequeue is the process of removing an element from the front end of the queue.

A linked list is a dynamic data structure that consists of a sequence of nodes. Each node has two fields: data and next. Data stores the value of the node and next stores the address of the next node in the list. A linked list has a pointer called head that points to the first node of the list.

We can implement a queue using a linked list by maintaining two pointers: front and rear. Front points to the first node of the list and rear points to the last node of the list. To enqueue an element, we create a new node and insert it at the end of the list. To dequeue an element, we delete the first node of the list and update the front pointer.

The following are the steps to implement a queue using a linked list in C:

- Define a structure for the node of the linked list. It should have two fields: data and next.
- Declare two global pointers: front and rear. Initialize them to NULL.
- Define a function to create a new node. It should take the data value as a parameter and return a pointer to the new node. It should allocate memory for the node using malloc and assign the data and next fields.
- Define a function to enqueue an element. It should take the data value as a parameter and return nothing. It should call the create node function and insert the new node at the end of the list. It should update the rear pointer and check if the queue is empty. If the queue is empty, it should also update the front pointer.
- Define a function to dequeue an element. It should take no parameters and return the data value of the deleted node. It should check if the queue is empty. If the queue is empty, it should print an error message and return -1. Otherwise, it should store the data value of the first node in a temporary variable and delete the first node. It should update the front pointer and check if the queue is empty. If the queue is empty, it should also update the rear pointer. It should return the temporary variable.
- Define a function to display the elements of the queue. It should take no parameters and return nothing. It should check if the queue is empty. If the queue is empty, it should print a message and return. Otherwise, it should declare a pointer to traverse the list and print the data values of the nodes until it reaches the rear node.
- Define a function to check if the queue is empty. It should take no parameters and return a boolean value. It should return true if the front pointer is NULL and false otherwise.
- Define a main function to test the queue operations. It should declare a variable to store the user's choice and a loop to repeat the menu until the user exits. It should display the menu options and ask the user to enter their choice. It should use a switch case to perform the corresponding operation based on the user's choice. It should also declare a variable to store the data value for enqueue and dequeue operations.

The following is the code for the implementation of queue using linked list in C:

```c
#include <stdio.h>
#include <stdlib.h>

// Define a structure for the node of the linked list
struct node {
  int data; // To store the data value
  struct node *next; // To store the address of the next node
};

// Declare two global pointers: front and rear
struct node *front = NULL;
struct node *rear = NULL;

// Define a function to create a new node
struct node *create_node(int data) {
  // Allocate memory for the node using malloc
  struct node *new_node = (struct node *)malloc(sizeof(struct node));
  // Assign the data and next fields
  new_node->data = data;
  new_node->next = NULL;
  // Return the pointer to the new node
  return new_node;
}

// Define a function to enqueue an element
void enqueue(int data) {
  // Call the create node function and insert the new node at the end of the list
  struct node *new_node = create_node(data);
  if (rear == NULL) {
    // If the queue is empty, update the front and rear pointers
    front = rear = new_node;
  } else {
    // If the queue is not empty, update the next field of the rear node and the rear pointer
    rear