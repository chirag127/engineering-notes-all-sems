### Implementation of Stack using Array

A stack is a linear data structure that follows the LIFO (Last In First Out) principle. It means that the last element inserted into the stack is the first one to be removed. A stack has two main operations: push and pop. Push adds an element to the top of the stack, and pop removes and returns the top element of the stack. A stack also has a property called top, which points to the index of the topmost element of the stack.

An array is a collection of elements of the same data type, stored in contiguous memory locations. An array can be used to implement a stack by using a fixed-size array and a variable to store the top index. The array will store the elements of the stack, and the top variable will indicate the position of the top element. The size of the array will determine the maximum capacity of the stack.

The implementation of stack using array in C can be done as follows:

- Declare a global array of a fixed size and a global variable to store the top index. Initialize the top variable to -1, indicating that the stack is empty.
- Define a function to check if the stack is empty. The function will return true if the top variable is -1, and false otherwise.
- Define a function to check if the stack is full. The function will return true if the top variable is equal to the size of the array minus one, and false otherwise.
- Define a function to push an element to the stack. The function will take an element as a parameter and check if the stack is full. If the stack is full, the function will print an error message and return. Otherwise, the function will increment the top variable by one and assign the element to the array at the top index.
- Define a function to pop an element from the stack. The function will check if the stack is empty. If the stack is empty, the function will print an error message and return. Otherwise, the function will store the element at the top index in a temporary variable, decrement the top variable by one, and return the temporary variable.
- Define a function to display the elements of the stack. The function will loop from the top index to zero and print the array elements at each index.

The following is an example of the C code for the implementation of stack using array:

```c
#include <stdio.h>
#define MAX 10 // Define the maximum size of the stack

int stack[MAX]; // Declare a global array to store the stack elements
int top = -1; // Declare a global variable to store the top index

// Function to check if the stack is empty
int isEmpty()
{
    if (top == -1)
        return 1; // Return true if the top is -1
    else
        return 0; // Return false otherwise
}

// Function to check if the stack is full
int isFull()
{
    if (top == MAX - 1)
        return 1; // Return true if the top is equal to the size of the array minus one
    else
        return 0; // Return false otherwise
}

// Function to push an element to the stack
void push(int x)
{
    if (isFull())
    {
        printf("Stack overflow\n"); // Print an error message if the stack is full
        return;
    }
    else
    {
        top++; // Increment the top by one
        stack[top] = x; // Assign the element to the array at the top index
    }
}

// Function to pop an element from the stack
int pop()
{
    int x;
    if (isEmpty())
    {
        printf("Stack underflow\n"); // Print an error message if the stack is empty
        return;
    }
    else
    {
        x = stack[top]; // Store the element at the top index in a temporary variable
        top--; // Decrement the top by one
        return x; // Return the temporary variable
    }
}

// Function to display the elements of the stack
void display()
{
    int i;
    if (isEmpty())
    {
        printf("Stack is empty\n"); // Print a message if the stack is empty
        return;
    }
    else
    {
        printf("Stack elements are:\n");
        for (i = top; i >= 0; i--) // Loop from the top index to zero
        {
            printf("%d\n", stack[i]); // Print the array element at each index
        }
    }
}

// Main function to test the stack operations
int main()

```
