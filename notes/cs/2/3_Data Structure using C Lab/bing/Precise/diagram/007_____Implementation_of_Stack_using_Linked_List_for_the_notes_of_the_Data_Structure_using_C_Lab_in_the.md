### Implementation of Stack using Linked List

A stack is a linear data structure that follows the Last In First Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. A stack can be implemented using an array or a linked list. In this section, we will discuss the implementation of a stack using a linked list.

#### Advantages of using a linked list to implement a stack
- Dynamic size: The size of the stack can change during runtime, as opposed to an array implementation where the size is fixed.
- Ease of insertion and deletion: Insertion and deletion of elements in a linked list is easier compared to an array.

#### Steps to implement a stack using a linked list
1. Define a `Node` structure with two members: `data` and `next`. The `data` member will store the value of the node, and the `next` member will store the address of the next node in the list.
2. Define a `Stack` structure with one member: `top`. The `top` member will store the address of the top element of the stack.
3. Initialize the `top` member of the `Stack` structure to `NULL` to create an empty stack.
4. To push an element onto the stack, create a new node with the given value and make its `next` member point to the current `top` of the stack. Then, update the `top` member of the `Stack` structure to point to the new node.
5. To pop an element from the stack, check if the stack is empty. If it is not empty, store the value of the `top` element in a temporary variable, update the `top` member of the `Stack` structure to point to the `next` member of the current `top` element, and delete the current `top` element. Return the value stored in the temporary variable.
6. To check if the stack is empty, check if the `top` member of the `Stack` structure is `NULL`.

Here is an example implementation of a stack using a linked list in C:

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

void init(Stack *s) {
    s->top = NULL;
}

void push(Stack *s, int value) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = value;
    newNode->next = s->top;
    s->top = newNode;
}

int pop(Stack *s) {
    if (s->top == NULL) {
        printf("Stack is empty.\n");
        return -1;
    }
    int value = s->top->data;
    Node *temp = s->top;
    s->top = s->top->next;
    free(temp);
    return value;
}

int isEmpty(Stack *s) {
    return s->top == NULL;
}

int main() {
    Stack s;
    init(&s);
    push(&s, 1);
    push(&s, 2);
    push(&s, 3);
    while (!isEmpty(&s)) {
        printf("%d\n", pop(&s));
    }
    return 0;
}
```

This code creates a stack and pushes the values 1, 2, and 3 onto it. Then, it pops the elements from the stack until it is empty, printing the values 3, 2, and 1 in that order. This demonstrates the LIFO behavior of the stack.