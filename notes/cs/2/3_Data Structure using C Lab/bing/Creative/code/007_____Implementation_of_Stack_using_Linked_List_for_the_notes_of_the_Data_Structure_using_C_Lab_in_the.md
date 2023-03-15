### Implementation of Stack using Linked List

A stack is a linear data structure that follows the LIFO (Last In First Out) principle. It means that the element that is inserted last is removed first. A stack has two basic operations: push and pop. Push adds an element to the top of the stack, and pop removes and returns the element from the top of the stack.

A linked list is a dynamic data structure that consists of a sequence of nodes. Each node has two fields: data and next. Data stores the value of the node, and next stores the address of the next node in the list. The first node is called the head, and the last node is called the tail. The tail node has a null value in its next field.

We can implement a stack using a linked list by using the head node as the top of the stack. To push an element, we create a new node with the given value and make it the new head of the list. To pop an element, we delete the head node and return its value. We also need to check if the stack is empty before performing any operation.

The following are the steps to implement a stack using a linked list in C:

- Define a structure for the node with data and next fields.
- Declare a global pointer variable for the head of the list, and initialize it to NULL.
- Define a function to create a new node with a given value and return its address.
- Define a function to check if the stack is empty by checking if the head pointer is NULL.
- Define a function to push an element to the stack by creating a new node and making it the new head of the list.
- Define a function to pop an element from the stack by deleting the head node and returning its value. Also check if the stack is empty before popping.
- Define a function to display the elements of the stack by traversing the list from head to tail and printing the data values.
- Define a main function to test the stack operations by using a switch case and a loop.

The following is the code for the implementation of stack using linked list in C:

```c
#include <stdio.h>
#include <stdlib.h>

// Define a structure for the node
struct node {
    int data; // Data field
    struct node *next; // Next field
};

// Declare a global pointer for the head of the list
struct node *head = NULL;

// Function to create a new node with a given value and return its address
struct node *createNode(int value) {
    // Allocate memory for the node
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    // Check if memory allocation is successful
    if (newNode == NULL) {
        printf("Memory allocation failed.\n");
        exit(1);
    }
    // Assign the value to the data field
    newNode->data = value;
    // Assign NULL to the next field
    newNode->next = NULL;
    // Return the address of the node
    return newNode;
}

// Function to check if the stack is empty
int isEmpty() {
    // Return 1 if the head pointer is NULL, 0 otherwise
    return head == NULL;
}

// Function to push an element to the stack
void push(int value) {
    // Create a new node with the given value
    struct node *newNode = createNode(value);
    // Make the new node the new head of the list
    newNode->next = head;
    head = newNode;
    // Print a message
    printf("Pushed %d to the stack.\n", value);
}

// Function to pop an element from the stack
int pop() {
    // Check if the stack is empty
    if (isEmpty()) {
        printf("Stack is empty.\n");
        return -1;
    }
    // Store the value of the head node
    int value = head->data;
    // Store the address of the head node
    struct node *temp = head;
    // Make the next node the new head of the list
    head = head->next;
    // Free the memory of the head node
    free(temp);
    // Return the value of the popped element
    return value;
}

// Function to display the elements of the stack
void display() {
    // Check if the stack is empty
    if (isEmpty()) {
        printf("Stack is empty.\n");
        return;
    }
    // Declare a pointer to traverse the list
    struct node *ptr = head;
    // Print a message
    printf("Stack: ");
    // Traverse the list from head to tail and print the data values
    while (ptr != NULL) {
        printf("%d ",