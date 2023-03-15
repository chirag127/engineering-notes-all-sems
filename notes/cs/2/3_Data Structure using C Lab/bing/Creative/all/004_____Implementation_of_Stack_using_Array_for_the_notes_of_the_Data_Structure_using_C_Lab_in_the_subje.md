# Implementation of Stack using Array

- A stack is a linear data structure that follows the principle of Last In First Out (LIFO).
- This means that the element that is inserted last will be removed first.
- A stack can be implemented using an array or a linked list.
- In this topic, we will see how to implement a stack using an array in C language.
- To implement a stack using an array, we need to declare an array of a fixed size, a variable to store the top index of the stack, and some functions to perform the operations on the stack.
- The top index of the stack is initially set to -1, indicating that the stack is empty.
- The functions that we need to implement are:

  - push(): This function takes an element as a parameter and inserts it into the stack. It also increments the top index by one. If the stack is full, it prints an error message and returns.
  - pop(): This function removes and returns the element at the top of the stack. It also decrements the top index by one. If the stack is empty, it prints an error message and returns.
  - peek(): This function returns the element at the top of the stack without removing it. If the stack is empty, it prints an error message and returns.
  - isEmpty(): This function returns true if the stack is empty, and false otherwise.
  - isFull(): This function returns true if the stack is full, and false otherwise.
  - display(): This function prints all the elements of the stack from top to bottom.

- The following is the C code for implementing a stack using an array:

```c
#include <stdio.h>
#define MAX 10 // Define the maximum size of the stack

int stack[MAX]; // Declare an array of size MAX to store the stack elements
int top = -1; // Declare a variable to store the top index of the stack

// Function to insert an element into the stack
void push(int x)
{
  if (isFull()) // Check if the stack is full
  {
    printf("Stack overflow\n"); // Print an error message
    return; // Return from the function
  }
  top++; // Increment the top index by one
  stack[top] = x; // Store the element at the top of the stack
  printf("Pushed %d into the stack\n", x); // Print a success message
}

// Function to remove and return an element from the stack
int pop()
{
  if (isEmpty()) // Check if the stack is empty
  {
    printf("Stack underflow\n"); // Print an error message
    return -1; // Return an invalid value
  }
  int x = stack[top]; // Store the element at the top of the stack
  top--; // Decrement the top index by one
  printf("Popped %d from the stack\n", x); // Print a success message
  return x; // Return the element
}

// Function to return the element at the top of the stack
int peek()
{
  if (isEmpty()) // Check if the stack is empty
  {
    printf("Stack is empty\n"); // Print an error message
    return -1; // Return an invalid value
  }
  int x = stack[top]; // Store the element at the top of the stack
  printf("The top element is %d\n", x); // Print the element
  return x; // Return the element
}

// Function to check if the stack is empty
int isEmpty()
{
  if (top == -1) // Check if the top index is -1
  {
    return 1; // Return true
  }
  else
  {
    return 0; // Return false
  }
}

// Function to check if the stack is full
int isFull()
{
  if (top == MAX - 1) // Check if the top index is MAX - 1
  {
    return 1; // Return true
  }
  else
  {
    return 0; // Return false
  }
}

// Function to display the stack elements
void display()
{
  if (isEmpty()) // Check if the stack is empty
  {
    printf("Stack is empty\n"); // Print an error message
    return; // Return from the function
  }
  printf("The stack elements are:\n"); // Print a message
  for (int i = top; i >= 0; i--) // Loop from the top index to the bottom index
  {
    printf("%d\n", stack[i]); // Print the element at the current index
  }
}

// Main function to test the stack implementation