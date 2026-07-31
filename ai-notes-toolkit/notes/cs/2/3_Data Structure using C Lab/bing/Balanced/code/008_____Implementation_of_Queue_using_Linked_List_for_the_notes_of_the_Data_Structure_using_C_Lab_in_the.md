### Implementation of Queue using Linked List

- A queue is a linear data structure that follows the FIFO (First In First Out) principle, meaning that the element that is inserted first is removed first.
- A linked list is a dynamic data structure that consists of a sequence of nodes, each node having a data field and a pointer field that points to the next node in the list.
- A queue can be implemented using a linked list by maintaining two pointers: front and rear. The front pointer points to the first node of the list, which is the head of the queue. The rear pointer points to the last node of the list, which is the tail of the queue.
- To implement a queue using a linked list, we need to perform the following operations:

  - **Enqueue**: This operation inserts a new node at the end of the list, which becomes the new rear of the queue. To do this, we need to allocate memory for the new node, assign the data value to it, and link it to the previous rear node. If the queue is empty, we also need to update the front pointer to point to the new node.
  - **Dequeue**: This operation removes the first node from the list, which is the front of the queue. To do this, we need to check if the queue is empty, and if not, we need to update the front pointer to point to the next node in the list, and free the memory of the removed node. If the queue becomes empty after this operation, we also need to update the rear pointer to NULL.
  - **Peek**: This operation returns the data value of the front node of the queue, without removing it. To do this, we need to check if the queue is empty, and if not, we need to return the data field of the front node.
  - **IsEmpty**: This operation checks if the queue is empty or not. To do this, we need to check if the front pointer is NULL or not, and return true or false accordingly.
  - **Display**: This operation prints the data values of all the nodes in the queue, from front to rear. To do this, we need to traverse the list using a temporary pointer, and print the data field of each node.

- The following is an example of C code that implements a queue using a linked list:

```c
// Define a structure for a node
struct node {
  int data; // Data field
  struct node *next; // Pointer field
};

// Define a structure for a queue
struct queue {
  struct node *front; // Front pointer
  struct node *rear; // Rear pointer
};

// Create a new node with a given data value
struct node* createNode(int data) {
  struct node *newNode = (struct node*)malloc(sizeof(struct node)); // Allocate memory
  newNode->data = data; // Assign data
  newNode->next = NULL; // Assign next to NULL
  return newNode; // Return the new node
}

// Create an empty queue
struct queue* createQueue() {
  struct queue *newQueue = (struct queue*)malloc(sizeof(struct queue)); // Allocate memory
  newQueue->front = NULL; // Assign front to NULL
  newQueue->rear = NULL; // Assign rear to NULL
  return newQueue; // Return the new queue
}

// Enqueue a node to the queue
void enqueue(struct queue *q, int data) {
  struct node *newNode = createNode(data); // Create a new node
  if (q->rear == NULL) { // If the queue is empty
    q->front = newNode; // Update the front pointer
    q->rear = newNode; // Update the rear pointer
  } else { // If the queue is not empty
    q->rear->next = newNode; // Link the new node to the previous rear node
    q->rear = newNode; // Update the rear pointer
  }
}

// Dequeue a node from the queue
int dequeue(struct queue *q) {
  if (q->front == NULL) { // If the queue is empty
    printf("Queue is empty.\n"); // Print an error message
    return -1; // Return an invalid value
  } else { // If the queue is not empty
    struct node *temp = q->front; // Store the front node in a temporary variable
    int data = temp->data; // Store the data value of the front node
    q->front = q->front->next; // Update the front pointer
    free(temp); // Free the memory of the removed node
    if (q->front == NULL) { // If the queue becomes

```
