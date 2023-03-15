### Implementation of Queue using Linked List for the notes of the Data Structure using C Lab in the subject of Data Structure using C

A queue is a linear data structure that follows the First In First Out (FIFO) principle. This means that the element that is inserted first will be removed first. A queue can be implemented using an array or a linked list. In this section, we will discuss the implementation of a queue using a linked list.

1. **Node Structure**: The first step in implementing a queue using a linked list is to define the structure of a node. A node in a linked list contains two fields: data and a pointer to the next node. The data field stores the value of the element, while the next field stores the address of the next node in the list.

```c
struct Node {
    int data;
    struct Node* next;
};
```

2. **Enqueue Operation**: The enqueue operation is used to insert an element at the end of the queue. To implement this operation, we need to create a new node, assign the value to the data field, and set the next field to NULL. Then, we need to check if the queue is empty. If it is, we set the front and rear pointers to the new node. Otherwise, we set the next field of the rear node to the new node and update the rear pointer.

```c
void enqueue(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    if (front == NULL && rear == NULL) {
        front = rear = newNode;
    } else {
        rear->next = newNode;
        rear = newNode;
    }
}
```

3. **Dequeue Operation**: The dequeue operation is used to remove an element from the front of the queue. To implement this operation, we need to check if the queue is empty. If it is, we return an error message. Otherwise, we create a temporary pointer to the front node, update the front pointer to the next node, and free the memory occupied by the temporary node.

```c
void dequeue() {
    if (front == NULL) {
        printf("Queue is empty\n");
        return;
    }
    struct Node* temp = front;
    front = front->next;
    free(temp);
    if (front == NULL) {
        rear = NULL;
    }
}
```

4. **Display Operation**: The display operation is used to print the elements of the queue. To implement this operation, we need to create a temporary pointer to the front node and traverse the linked list until we reach the end. At each node, we print the value of the data field.

```c
void display() {
    struct Node* temp = front;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}
```

In conclusion, a queue can be easily implemented using a linked list. The enqueue, dequeue, and display operations can be performed in constant time, making it an efficient data structure for certain applications.