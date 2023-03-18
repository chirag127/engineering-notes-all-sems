### Implementation of Stack using Linked List

The stack is a data structure that follows the Last In First Out (LIFO) principle. In this lab, we will be implementing the stack using a linked list in the C programming language. This will help us to understand the concept of linked lists and how they can be used to implement a stack.

Here are the steps to implement a stack using a linked list:

1. Define a structure for the stack node that will contain the data and a pointer to the next node.
```c
struct stackNode {
    int data;
    struct stackNode* next;
};
```

2. Define a structure for the stack that will contain the top pointer.
```c
struct stack {
    struct stackNode* top;
};
```

3. Create a function to initialize the stack by setting the top pointer to NULL.
```c
void initializeStack(struct stack* s) {
    s->top = NULL;
}
```

4. Create a function to push an element onto the stack by creating a new node and setting its data and next pointers. Then, set the top pointer to the new node.
```c
void push(struct stack* s, int data) {
    struct stackNode* newNode = (struct stackNode*)malloc(sizeof(struct stackNode));
    newNode->data = data;
    newNode->next = s->top;
    s->top = newNode;
}
```

5. Create a function to pop an element from the stack by freeing the top node and setting the top pointer to the next node.
```c
int pop(struct stack* s) {
    if (s->top == NULL) {
        printf("Stack is empty");
        return -1;
    }
    int data = s->top->data;
    struct stackNode* temp = s->top;
    s->top = s->top->next;
    free(temp);
    return data;
}
```

6. Create a function to display the elements in the stack by traversing the linked list and printing the data.
```c
void display(struct stack* s) {
    if (s->top == NULL) {
        printf("Stack is empty");
        return;
    }
    struct stackNode* temp = s->top;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
}
```

By following these steps, we can implement a stack using a linked list in the C programming language. This will help us to understand the concept of linked lists and how they can be used to implement other data structures as well.