### Implementation of Circular Queue using Linked List

A circular queue is a type of queue data structure that stores elements in a circular fashion. Unlike a linear queue, which has a fixed size and can cause overflow or underflow, a circular queue can utilize the empty spaces left by the deleted elements. A circular queue can be implemented using an array or a linked list. In this section, we will discuss how to implement a circular queue using a linked list in C.

A linked list is a data structure that consists of nodes, each containing some data and a pointer to the next node. A circular linked list is a special case of a linked list, where the last node points to the first node, forming a loop. A circular linked list can be used to implement a circular queue by maintaining two pointers: front and rear. The front pointer points to the first node of the queue, and the rear pointer points to the last node of the queue. The following diagram illustrates the structure of a circular queue using a linked list:

![Circular queue using linked list](https://i.imgur.com/1xwZ8wL.png)

To implement a circular queue using a linked list in C, we need to define a node structure and a queue structure. The node structure contains an integer data field and a pointer to the next node. The queue structure contains two pointers: front and rear, which point to the first and last nodes of the queue, respectively. The queue structure also contains a function pointer to display the queue elements. The following code snippet shows the definition of the node and queue structures:

```c
// Node structure
struct node {
    int data; // data field
    struct node *next; // pointer to the next node
};

// Queue structure
struct queue {
    struct node *front; // pointer to the first node
    struct node *rear; // pointer to the last node
    void (*display)(struct queue *); // function pointer to display the queue elements
};
```

To perform the basic operations on a circular queue, such as enqueue, dequeue, peek, and display, we need to write the corresponding functions. The following code snippet shows the implementation of these functions:

```c
// Function to create a new node with given data and return its pointer
struct node *newNode(int data) {
    struct node *temp = (struct node *)malloc(sizeof(struct node)); // allocate memory for the node
    temp->data = data; // assign data to the node
    temp->next = NULL; // initialize next pointer to NULL
    return temp; // return the node pointer
}

// Function to create an empty queue and return its pointer
struct queue *createQueue() {
    struct queue *q = (struct queue *)malloc(sizeof(struct queue)); // allocate memory for the queue
    q->front = NULL; // initialize front pointer to NULL
    q->rear = NULL; // initialize rear pointer to NULL
    q->display = displayQueue; // assign display function to the function pointer
    return q; // return the queue pointer
}

// Function to check if a queue is empty or not
int isEmpty(struct queue *q) {
    return (q->front == NULL); // return true if front pointer is NULL, false otherwise
}

// Function to enqueue an element to the rear of the queue
void enqueue(struct queue *q, int data) {
    struct node *temp = newNode(data); // create a new node with the given data
    if (isEmpty(q)) { // if the queue is empty
        q->front = temp; // assign the new node to the front pointer
        q->rear = temp; // assign the new node to the rear pointer
        temp->next = temp; // make the new node point to itself
    } else { // if the queue is not empty
        temp->next = q->front; // make the new node point to the front node
        q->rear->next = temp; // make the rear node point to the new node
        q->rear = temp; // assign the new node to the rear pointer
    }
}

// Function to dequeue an element from the front of the queue and return its data
int dequeue(struct queue *q) {
    if (isEmpty(q)) { // if the queue is empty
        printf("Queue is empty.\n"); // print an error message
        return -1; // return -1 as an invalid value
    } else { // if the queue is not empty
        struct node *temp = q->front; // store the front node