### Implementation of Stack using Linked List

In this lab, we will learn how to implement a stack using a linked list in the C programming language. A stack is a data structure that follows the Last-In-First-Out (LIFO) principle, meaning the last item added to the stack is the first item to be removed. 

#### Linked List

A linked list is a dynamic data structure that consists of nodes, where each node contains data and a reference to the next node in the list. In a singly linked list, each node has only one reference, which points to the next node in the list. 

#### Stack using Linked List

To implement a stack using a linked list, we can use the following steps:

1. Define a structure for the node of the linked list, which should contain the data and a pointer to the next node.
2. Define a structure for the stack, which should have a pointer to the top node of the stack.
3. Implement the push operation, which adds an element to the top of the stack. This operation involves creating a new node with the given data and pointing it to the current top node of the stack.
4. Implement the pop operation, which removes the top element from the stack. This operation involves updating the top pointer of the stack to point to the next node in the list.
5. Implement the peek operation, which returns the top element of the stack without removing it. This operation involves accessing the data of the top node of the stack.
6. Implement the isEmpty operation, which checks if the stack is empty. This operation involves checking if the top pointer of the stack is NULL.

#### Code Implementation

```c
#include<stdio.h>
#include<stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Stack {
    struct Node* top;
};

void push(struct Stack* s, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = s->top;
    s->top = newNode;
}

int pop(struct Stack* s) {
    if(s->top == NULL) {
        printf("Stack is empty\n");
        return -1;
    }
    struct Node* temp = s->top;
    int data = s->top->data;
    s->top = s->top->next;
    free(temp);
    return data;
}

int peek(struct Stack* s) {
    if(s->top == NULL) {
        printf("Stack is empty\n");
        return -1;
    }
    return s->top->data;
}

int isEmpty(struct Stack* s) {
    return s->top == NULL;
}
```

#### Conclusion

In this lab, we learned how to implement a stack using a linked list in the C programming language. We defined the necessary structures and implemented the push, pop, peek, and isEmpty operations. By using a linked list, we were able to create a dynamic and efficient implementation of a stack.