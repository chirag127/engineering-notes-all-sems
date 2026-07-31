### Implementation of Stack using Array

A stack is a linear data structure that follows the Last In First Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. A stack can be implemented using an array in the following way:

1. **Create an array:** Choose an appropriate size for the array based on the maximum number of elements that the stack is expected to hold. This array will be used to store the elements of the stack.

2. **Initialize a variable to keep track of the top of the stack:** The top of the stack is the index of the last element added to the stack. Initialize a variable `top` to -1 to indicate that the stack is empty.

3. **Push operation:** To add an element to the stack, first check if the stack is full by comparing the value of `top` with the maximum size of the array. If the stack is not full, increment the value of `top` and add the element to the array at the new `top` index.

4. **Pop operation:** To remove an element from the stack, first check if the stack is empty by checking the value of `top`. If the stack is not empty, remove the element from the array at the `top` index and decrement the value of `top`.

5. **Peek operation:** To view the top element of the stack without removing it, return the element at the `top` index of the array.

Here is an example implementation of a stack using an array in C:

```c
#include <stdio.h>
#define MAXSIZE 10

int stack[MAXSIZE];
int top = -1;

void push(int x) {
    if (top == MAXSIZE - 1) {
        printf("Stack is full\n");
        return;
    }
    top++;
    stack[top] = x;
}

int pop() {
    if (top == -1) {
        printf("Stack is empty\n");
        return -1;
    }
    int x = stack[top];
    top--;
    return x;
}

int peek() {
    if (top == -1) {
        printf("Stack is empty\n");
        return -1;
    }
    return stack[top];
}

int main() {
    push(1);
    push(2);
    push(3);
    printf("%d\n", pop());
    printf("%d\n", peek());
    printf("%d\n", pop());
    printf("%d\n", pop());
    printf("%d\n", pop());
    return 0;
}
```