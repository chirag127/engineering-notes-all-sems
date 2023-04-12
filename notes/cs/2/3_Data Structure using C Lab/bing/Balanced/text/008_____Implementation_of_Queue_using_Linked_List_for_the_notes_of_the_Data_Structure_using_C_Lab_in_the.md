### Implementation of Queue using Linked List

- A queue is a linear data structure that follows the FIFO (First In First Out) principle, meaning that the first element inserted is the first one to be removed.
- A linked list is a dynamic data structure that consists of a sequence of nodes, each containing some data and a pointer to the next node.
- A queue can be implemented using a linked list by maintaining two pointers: front and rear. The front pointer points to the first node of the queue, and the rear pointer points to the last node of the queue.
- To insert an element into the queue, a new node is created and appended at the end of the linked list, and the rear pointer is updated to point to the new node.
- To delete an element from the queue, the first node of the linked list is removed and the front pointer is updated to point to the next node. If the queue becomes empty, both front and rear pointers are set to NULL.
- The main operations of a queue are enqueue (insert), dequeue (delete), peek (return the front element without deleting), and isEmpty (check if the queue is empty).
- The following is a possible C code for implementing a queue using a linked list:

```c
// Define a structure for a node of the linked list
struct node {
  int data; // data field
  struct node *next; // pointer to the next node
};

// Define a structure for a queue
struct queue {
  struct node *front; // pointer to the front node
  struct node *rear; // pointer to the rear node
};

// Create a new node with a given data value and return its pointer
struct node *createNode(int data) {
  struct node *newNode = (struct node *)malloc(sizeof(struct node)); // allocate memory for the node
  newNode->data = data; // assign the data value
  newNode->next = NULL; // set the next pointer to NULL
  return newNode; // return the pointer to the node
}

// Create an empty queue and return its pointer
struct queue *createQueue() {
  struct queue *newQueue = (struct queue *)malloc(sizeof(struct queue)); // allocate memory for the queue
  newQueue->front = NULL; // set the front pointer to NULL
  newQueue->rear = NULL; // set the rear pointer to NULL
  return newQueue; // return the pointer to the queue
}

// Insert an element at the rear of the queue
void enqueue(struct queue *q, int data) {
  struct node *newNode = createNode(data); // create a new node with the data value
  if (q->rear == NULL) { // if the queue is empty
    q->front = newNode; // set the front pointer to the new node
    q->rear = newNode; // set the rear pointer to the new node
  } else { // if the queue is not empty
    q->rear->next = newNode; // link the new node after the rear node
    q->rear = newNode; // update the rear pointer to the new node
  }
}

// Delete an element from the front of the queue and return its data value
int dequeue(struct queue *q) {
  if (q->front == NULL) { // if the queue is empty
    printf("Queue is empty.\n"); // print an error message
    return -1; // return an invalid value
  } else { // if the queue is not empty
    struct node *temp = q->front; // store the front node in a temporary variable
    int data = temp->data; // store the data value of the front node
    q->front = q->front->next; // update the front pointer to the next node
    if (q->front == NULL) { // if the queue becomes empty
      q->rear = NULL; // set the rear pointer to NULL
    }
    free(temp); // free the memory of the front node
    return data; // return the data value of the deleted node
  }
}

// Return the data value of the front element of the queue without deleting it
int peek(struct queue *q) {
  if (q->front == NULL) { // if the queue is empty
    printf("Queue is empty.\n"); // print an error message
    return -1; // return an invalid value
  } else { // if the queue is not empty
    return q->front->data; // return the data value of the front node
  }
}

// Check if the queue is empty
int isEmpty(struct queue *q) {
  return (q->front == NULL); // return

```
