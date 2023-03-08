### Implementation of Stack using Linked List in C

A stack is a linear data structure that follows the LIFO (Last In First Out) principle. It means that the element that is inserted last will be removed first. A stack supports various operations like push, pop, peek, empty, and size.

A stack can be implemented using an array or a linked list. The benefit of implementing a stack using a linked list over arrays is that it allows the stack to grow or shrink as per the requirements, i.e., memory can be allocated dynamically. Using an array will put a restriction on the maximum capacity of the array which can lead to stack overflow.

To implement a stack using a linked list, we need to define a node structure that will store the data and a pointer to the next node. The node structure can be defined as:

```c
struct node {
    int data; // data field
    struct node *next; // pointer to the next node
};
```

We also need to maintain a pointer to the top of the stack, which will be initialized to NULL. The top pointer will point to the node that is at the top of the stack. The top pointer can be declared as:

```c
struct node *top = NULL; // pointer to the top of the stack
```

The following are the main operations that can be performed on a stack using a linked list:

- Push: This operation inserts a new node at the top of the stack. To perform this operation, we need to allocate memory for the new node, assign the data to the node, and make the node point to the current top of the stack. Then, we update the top pointer to point to the new node. The push operation can be implemented as:

```c
void push(int data) {
    // allocate memory for the new node
    struct node *new_node = (struct node *)malloc(sizeof(struct node));
    // check if memory allocation is successful
    if (new_node == NULL) {
        printf("Stack overflow\n");
        return;
    }
    // assign the data to the node
    new_node->data = data;
    // make the node point to the current top of the stack
    new_node->next = top;
    // update the top pointer to point to the new node
    top = new_node;
}
```

- Pop: This operation removes the node that is at the top of the stack and returns its data. To perform this operation, we need to check if the stack is empty or not. If the stack is empty, we print an error message and return. Otherwise, we store the data of the top node in a variable, update the top pointer to point to the next node, and free the memory of the removed node. The pop operation can be implemented as:

```c
int pop() {
    // check if the stack is empty or not
    if (top == NULL) {
        printf("Stack underflow\n");
        return -1;
    }
    // store the data of the top node in a variable
    int data = top->data;
    // update the top pointer to point to the next node
    struct node *temp = top;
    top = top->next;
    // free the memory of the removed node
    free(temp);
    // return the data of the removed node
    return data;
}
```

- Peek: This operation returns the data of the node that is at the top of the stack without removing it. To perform this operation, we need to check if the stack is empty or not. If the stack is empty, we print an error message and return. Otherwise, we return the data of the top node. The peek operation can be implemented as:

```c
int peek() {
    // check if the stack is empty or not
    if (top == NULL) {
        printf("Stack is empty\n");
        return -1;
    }
    // return the data of the top node
    return top->data;
}
```

- Empty: This operation checks if the stack is empty or not. To perform this operation, we need to check if the top pointer is NULL or not. If the top pointer is NULL, we return true. Otherwise, we return false. The empty operation can be implemented as:

```c
bool empty() {
    // check if the top pointer is NULL or not
    if (top == NULL) {
        return true;
    }
    else {
        return false;
    }
}
```

- Size: This operation returns the number of nodes in the stack. To perform

this operation, we need to traverse the linked list from the top to the bottom and count the number of nodes. The size operation can be implemented as:

```c
int size() {
    // initialize a counter variable
    int count = 0;
    // traverse the linked list from the top to the bottom
    struct node *temp = top;
    while (temp != NULL) {
        // increment the counter for each node
        count++;
        // move to the next node
        temp = temp->next;
    }
    // return the counter value
    return count;
}
```

Some mnemonics and learning tricks for the topic are:

- To remember the LIFO principle of stack, think of a stack of plates or books. The plate or book that is placed last will be taken out first.
- To remember the push and pop operations of stack, think of pushing and popping a balloon. Pushing a balloon means adding air to it, while popping a balloon means releasing air from it.
- To remember the difference between stack overflow and stack underflow, think of a glass of water. Stack overflow means the glass is full and cannot hold more water, while stack underflow means the glass is empty and cannot release more water.