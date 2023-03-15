### Implementation of Stack using Array

A stack is a linear data structure that follows the Last In First Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. A stack can be implemented using an array in the following way:

1. **Define the maximum size of the stack:** The maximum size of the stack is defined by the size of the array used to implement it.

2. **Initialize the stack:** The stack is initialized by setting the top variable to -1. This indicates that the stack is empty.

3. **Push operation:** To add an element to the stack, the top variable is incremented by 1 and the element is added to the array at the position indicated by the top variable.

4. **Pop operation:** To remove an element from the stack, the element at the position indicated by the top variable is removed and the top variable is decremented by 1.

5. **Peek operation:** To view the top element of the stack without removing it, the element at the position indicated by the top variable is returned.

6. **Check if the stack is full:** The stack is considered full if the top variable is equal to the maximum size of the stack minus 1.

7. **Check if the stack is empty:** The stack is considered empty if the top variable is equal to -1.

Here is an example of a stack implementation using an array in C:

```c
#include <stdio.h>
#define MAXSIZE 10

int stack[MAXSIZE];
int top = -1;

int isFull() {
    if (top == MAXSIZE - 1)
        return 1;
    else
        return 0;
}

int isEmpty() {
    if (top == -1)
        return 1;
    else
        return 0;
}

int peek() {
    return stack[top];
}

int pop() {
    int data;
    if (!isEmpty()) {
        data = stack[top];
        top = top - 1;
        return data;
    } else {
        printf("Stack is empty.\n");
    }
}

int push(int data) {
    if (!isFull()) {
        top = top + 1;
        stack[top] = data;
    } else {
        printf("Stack is full.\n");
    }
}

int main() {
    push(3);
    push(5);
    push(9);
    push(1);
    push(12);
    push(15);

    printf("Element at top of the stack: %d\n" ,peek());
    printf("Elements: \n");

    while (!isEmpty()) {
        int data = pop();
        printf("%d\n",data);
    }

    printf("Stack full: %s\n" , isFull()?"true":"false");
    printf("Stack empty: %s\n" , isEmpty()?"true":"false");

    return 0;
}
```

This code defines a stack of maximum size 10 and implements the push, pop, peek, isFull, and isEmpty operations. The main function demonstrates how these operations can be used to add and remove elements from the stack.
