### Implementation of Stack using Array

A stack is a linear data structure that follows the Last In First Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. A stack can be implemented using an array in the following way:

1. **Initialize** the stack: To implement a stack using an array, we first need to initialize the stack. This involves setting the top of the stack to -1, indicating that the stack is empty. We also need to allocate memory for the array that will be used to store the elements of the stack.

2. **Push** operation: To add an element to the stack, we need to perform the push operation. This involves checking if the stack is full. If the stack is full, we cannot add any more elements to it. If the stack is not full, we increment the top of the stack and add the element to the array at the new top position.

3. **Pop** operation: To remove an element from the stack, we need to perform the pop operation. This involves checking if the stack is empty. If the stack is empty, we cannot remove any elements from it. If the stack is not empty, we remove the element from the array at the top position and decrement the top of the stack.

4. **Peek** operation: The peek operation allows us to view the top element of the stack without removing it. This involves checking if the stack is empty. If the stack is empty, we cannot view any elements. If the stack is not empty, we return the element at the top position of the array.

5. **IsFull** and **IsEmpty** operations: The IsFull and IsEmpty operations allow us to check if the stack is full or empty, respectively. The IsFull operation returns true if the top of the stack is equal to the maximum size of the array minus one. The IsEmpty operation returns true if the top of the stack is equal to -1.

Here is an example of a stack implementation using an array in C:

```c
#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 10

struct Stack {
    int top;
    int arr[MAXSIZE];
};

void initStack(struct Stack *s) {
    s->top = -1;
}

int isFull(struct Stack *s) {
    return s->top == MAXSIZE - 1;
}

int isEmpty(struct Stack *s) {
    return s->top == -1;
}

void push(struct Stack *s, int x) {
    if (isFull(s)) {
        printf("Stack is full\n");
        return;
    }
    s->top++;
    s->arr[s->top] = x;
}

int pop(struct Stack *s) {
    if (isEmpty(s)) {
        printf("Stack is empty\n");
        return -1;
    }
    int x = s->arr[s->top];
    s->top--;
    return x;
}

int peek(struct Stack *s) {
    if (isEmpty(s)) {
        printf("Stack is empty\n");
        return -1;
    }
    return s->arr[s->top];
}

int main() {
    struct Stack s;
    initStack(&s);
    push(&s, 1);
    push(&s, 2);
    push(&s, 3);
    printf("%d\n", pop(&s));
    printf("%d\n", peek(&s));
    return 0;
}
```