### Implementation of Queue using Linked List for the notes of the Data Structure using C Lab in the subject of Data Structure using C

A queue is a linear data structure that follows the First In First Out (FIFO) order of operations. This means that the element that is inserted first is the first one to be removed. A queue can be implemented using an array, a linked list, or a dynamic array.

In this section, we will discuss the implementation of a queue using a linked list. A linked list is a data structure that consists of a group of nodes that represent a sequence. Each node contains a data element and a reference to the next node in the sequence.

Here are the steps to implement a queue using a linked list:

1. Define a `Node` structure with two members: `data` and `next`. The `data` member will store the element and the `next` member will store the reference to the next node in the sequence.

```c
struct Node {
    int data;
    struct Node* next;
};
```

2. Define a `Queue` structure with two members: `front` and `rear`. The `front` member will store the reference to the front node of the queue and the `rear` member will store the reference to the rear node of the queue.

```c
struct Queue {
    struct Node *front, *rear;
};
```

3. Initialize the `front` and `rear` members of the `Queue` structure to `NULL` in the `createQueue` function.

```c
struct Queue* createQueue() {
    struct Queue* q = (struct Queue*)malloc(sizeof(struct Queue));
    q->front = q->rear = NULL;
    return q;
}
```

4. To enqueue an element, create a new node with the given data and set its `next` member to `NULL`. If the queue is empty, set the `front` and `rear` members of the `Queue` structure to the new node. Otherwise, set the `next` member of the `rear` node to the new node and update the `rear` member of the `Queue` structure to the new node.

```c
void enqueue(struct Queue* q, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    if (q->rear == NULL) {
        q->front = q->rear = newNode;
        return;
    }
    q->rear->next = newNode;
    q->rear = newNode;
}
```

5. To dequeue an element, check if the queue is empty. If it is, return `INT_MIN`. Otherwise, store the `data` member of the `front` node in a temporary variable, update the `front` member of the `Queue` structure to the `next` member of the `front` node, and free the memory of the `front` node. If the `front` member of the `Queue` structure is `NULL` after the update, set the `rear` member of the `Queue` structure to `NULL` as well.

```c
int dequeue(struct Queue* q) {
    if (q->front == NULL)
        return INT_MIN;
    struct Node* temp = q->front;
    q->front = q->front->next;
    if (q->front == NULL)
        q->rear = NULL;
    int data = temp->data;
    free(temp);
    return data;
}
```

This is how a queue can be implemented using a linked list in the C programming language. This implementation allows for dynamic resizing of the queue and efficient enqueue and dequeue operations. However, it requires extra memory for the `next` member of each node and the `front` and `rear` members of the `Queue` structure.