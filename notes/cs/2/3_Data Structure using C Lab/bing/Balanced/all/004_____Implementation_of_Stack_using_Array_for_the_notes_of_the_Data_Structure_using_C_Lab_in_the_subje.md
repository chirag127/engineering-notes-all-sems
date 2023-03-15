# Implementation of Stack using Array in C

A stack is a linear data structure that follows the LIFO (Last In First Out) principle. It means that the last element inserted into the stack is the first one to be removed. A stack has two basic operations: push and pop. Push adds an element to the top of the stack, and pop removes and returns the top element of the stack.

An array is a collection of elements of the same data type, stored in contiguous memory locations. An array can be used to implement a stack by using a variable called top to keep track of the index of the topmost element of the stack. The top variable is initialized to -1 when the stack is empty, and incremented by 1 when an element is pushed, and decremented by 1 when an element is popped.

The following are the steps to implement a stack using an array in C:

- Declare an array of a fixed size and a variable top to store the index of the top element of the stack.
- Define a function to check if the stack is empty by comparing the top variable with -1.
- Define a function to check if the stack is full by comparing the top variable with the size of the array minus 1.
- Define a function to push an element to the stack by checking if the stack is full, and if not, incrementing the top variable and assigning the element to the array at the top index.
- Define a function to pop an element from the stack by checking if the stack is empty, and if not, returning the element at the top index and decrementing the top variable.
- Define a function to display the elements of the stack by iterating from the top index to 0 and printing the array elements.

The following is an example of a C program that implements a stack using an array:

```c
#include <stdio.h>
#define MAX 10 // maximum size of the array

int stack[MAX]; // array to store the stack elements
int top = -1; // variable to store the index of the top element

// function to check if the stack is empty
int isEmpty()
{
    if (top == -1)
        return 1; // stack is empty
    else
        return 0; // stack is not empty
}

// function to check if the stack is full
int isFull()
{
    if (top == MAX - 1)
        return 1; // stack is full
    else
        return 0; // stack is not full
}

// function to push an element to the stack
void push(int x)
{
    if (isFull())
        printf("Stack overflow\n"); // stack is full, cannot push
    else
    {
        top++; // increment the top index
        stack[top] = x; // assign the element to the array at the top index
        printf("Pushed %d to the stack\n", x); // print the pushed element
    }
}

// function to pop an element from the stack
int pop()
{
    int x; // variable to store the popped element
    if (isEmpty())
    {
        printf("Stack underflow\n"); // stack is empty, cannot pop
        return -1; // return an invalid value
    }
    else
    {
        x = stack[top]; // assign the element at the top index to x
        top--; // decrement the top index
        printf("Popped %d from the stack\n", x); // print the popped element
        return x; // return the popped element
    }
}

// function to display the elements of the stack
void display()
{
    int i; // variable to iterate over the array
    if (isEmpty())
        printf("Stack is empty\n"); // stack is empty, nothing to display
    else
    {
        printf("Stack elements are:\n");
        for (i = top; i >= 0; i--) // iterate from the top index to 0
        {
            printf("%d\n", stack[i]); // print the array element
        }
    }
}

// main function to test the stack implementation
int main()
{
    int choice, x; // variables to store the user choice and input
    while (1) // loop until the user exits
    {
        printf("Enter your choice:\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        scanf("%d", &choice); // read the user choice
        switch (choice)