### Implementation of Stack using Array

A stack is a linear data structure that follows the Last In First Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. A stack can be implemented using an array in the following way:

1. Define a fixed size for the stack and create an array of that size.
2. Initialize a variable `top` to -1 to keep track of the top element of the stack.
3. To push an element onto the stack, first check if the stack is full by comparing the value of `top` with the size of the array. If the stack is full, display an error message. Otherwise, increment the value of `top` and add the element to the array at the `top` index.
4. To pop an element from the stack, first check if the stack is empty by comparing the value of `top` with -1. If the stack is empty, display an error message. Otherwise, remove the element from the array at the `top` index and decrement the value of `top`.
5. To check if the stack is empty, compare the value of `top` with -1. If `top` is equal to -1, the stack is empty.
6. To check if the stack is full, compare the value of `top` with the size of the array. If `top` is equal to the size of the array, the stack is full.
7. To display the elements of the stack, iterate from the `top` index to 0 and display the elements of the array.

Here is an example of a stack implementation using an array in C:

```c
#include <stdio.h>
#define MAXSIZE 10

int stack[MAXSIZE];
int top = -1;

void push(int data) {
    if (top == MAXSIZE - 1) {
        printf("Stack is full\n");
    } else {
        top++;
        stack[top] = data;
    }
}

int pop() {
    if (top == -1) {
        printf("Stack is empty\n");
        return -1;
    } else {
        int data = stack[top];
        top--;
        return data;
    }
}

int is_empty() {
    if (top == -1) {
        return 1;
    } else {
        return 0;
    }
}

int is_full() {
    if (top == MAXSIZE - 1) {
        return 1;
    } else {
        return 0;
    }
}

void display() {
    for (int i = top; i >= 0; i--) {
        printf("%d ", stack[i]);
    }
    printf("\n");
}

int main() {
    push(1);
    push(2);
    push(3);
    display();
    pop();
    display();
    return 0;
}
```

This code creates a stack of size 10 and defines functions to push, pop, check if the stack is empty or full, and display the elements of the stack. In the `main` function, the stack is used to push and pop elements and display the contents of the stack. The output of this code will be:

```
3 2 1
2 1
```

This is an example of how a stack can be implemented using an array in C. It is important to note that the size of the stack is fixed and cannot be changed once it is defined. If a dynamic size stack is needed, a linked list can be used to implement the stack instead of an array.