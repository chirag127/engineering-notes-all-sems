### Implementation of Stack using Linked List for the notes of the Data Structure using C Lab in the subject of Data Structure using C

A stack is a linear data structure that follows the Last In First Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. A stack can be implemented using an array or a linked list. In this section, we will discuss the implementation of a stack using a linked list.

1. **Node Structure**: The first step in implementing a stack using a linked list is to define the structure of a node. A node in a linked list contains two fields: data and a pointer to the next node. The data field stores the value of the node and the next field stores the address of the next node in the list.

```c
struct Node {
    int data;
    struct Node* next;
};
```

2. **Push Operation**: The push operation adds a new element to the top of the stack. In a linked list implementation, this is done by inserting a new node at the beginning of the list. The new node becomes the new head of the list.

```c
void push(struct Node** head, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = *head;
    *head = newNode;
}
```

3. **Pop Operation**: The pop operation removes the top element from the stack. In a linked list implementation, this is done by removing the first node from the list. The head of the list is updated to point to the next node.

```c
int pop(struct Node** head) {
    if (*head == NULL) {
        printf("Stack is empty\n");
        return INT_MIN;
    }
    struct Node* temp = *head;
    *head = (*head)->next;
    int popped = temp->data;
    free(temp);
    return popped;
}
```

4. **Peek Operation**: The peek operation returns the value of the top element of the stack without removing it. In a linked list implementation, this is done by returning the value of the first node in the list.

```c
int peek(struct Node* head) {
    if (head == NULL) {
        printf("Stack is empty\n");
        return INT_MIN;
    }
    return head->data;
}
```

5. **isEmpty Operation**: The isEmpty operation checks if the stack is empty. In a linked list implementation, this is done by checking if the head of the list is NULL.

```c
int isEmpty(struct Node* head) {
    return head == NULL;
}
```

This is a brief overview of how a stack can be implemented using a linked list in C. The push, pop, peek, and isEmpty operations can be performed in constant time, making this implementation efficient. Additionally, a linked list implementation of a stack does not have a fixed size, allowing it to grow and shrink dynamically as elements are added and removed.