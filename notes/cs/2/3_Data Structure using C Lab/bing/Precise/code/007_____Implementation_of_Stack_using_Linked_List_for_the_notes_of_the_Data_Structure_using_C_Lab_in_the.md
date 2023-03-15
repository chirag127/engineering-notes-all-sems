### Implementation of Stack using Linked List

A stack is a linear data structure that follows the Last In First Out (LIFO) principle. It means that the last element added to the stack will be the first one to be removed. A stack can be implemented using an array or a linked list. In this section, we will discuss the implementation of a stack using a linked list.

#### Advantages of using a linked list to implement a stack
- Dynamic size: The size of the stack can grow or shrink as needed.
- Ease of insertion and deletion: Insertion and deletion of elements in a stack implemented using a linked list are easier as compared to an array.

#### Steps to implement a stack using a linked list
1. Define a `Node` structure to represent a node in the linked list. The `Node` structure should have two members: `data` to store the value and `next` to store the address of the next node.
2. Define a `Stack` structure to represent the stack. The `Stack` structure should have one member: `top` to store the address of the top element of the stack.
3. Implement the `push` operation to add an element to the stack. To push an element, create a new node, set its `data` member to the value to be pushed, set its `next` member to the current `top` of the stack, and update the `top` of the stack to the new node.
4. Implement the `pop` operation to remove the top element from the stack. To pop an element, check if the stack is empty. If the stack is not empty, store the value of the `top` element, update the `top` of the stack to the `next` of the current `top`, and return the stored value.
5. Implement the `peek` operation to return the value of the top element of the stack without removing it. To peek, check if the stack is empty. If the stack is not empty, return the value of the `top` element.
6. Implement the `isEmpty` operation to check if the stack is empty. To check if the stack is empty, check if the `top` of the stack is `NULL`.

#### Example code in C
```c
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

typedef struct Stack {
    Node *top;
} Stack;

void push(Stack *stack, int value) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = stack->top;
    stack->top = newNode;
}

int pop(Stack *stack) {
    if (stack->top == NULL) {
        printf("Stack is empty.\n");
        return -1;
    }
    int value = stack->top->data;
    Node *temp = stack->top;
    stack->top = stack->top->next;
    free(temp);
    return value;
}

int peek(Stack *stack) {
    if (stack->top == NULL) {
        printf("Stack is empty.\n");
        return -1;
    }
    return stack->top->data;
}

int isEmpty(Stack *stack) {
    return stack->top == NULL;
}

int main() {
    Stack stack;
    stack.top = NULL;

    push(&stack, 1);
    push(&stack, 2);
    push(&stack, 3);

    printf("Top element: %d\n", peek(&stack));

    printf("Elements: ");
    while (!isEmpty(&stack)) {
        printf("%d ", pop(&stack));
    }
    printf("\n");

    return 0;
}
```