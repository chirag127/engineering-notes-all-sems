# Implementation of Queue using Linked List

- A queue is a linear data structure that follows the FIFO (First In First Out) principle, meaning that the first element inserted is the first one to be removed.
- A linked list is a dynamic data structure that consists of a sequence of nodes, each node having a data field and a pointer field that points to the next node in the list.
- A queue can be implemented using a linked list by maintaining two pointers: front and rear. The front pointer points to the first node of the list, which is the head of the queue. The rear pointer points to the last node of the list, which is the tail of the queue.
- To implement a queue using a linked list, we need to perform the following operations:

  - **Enqueue**: This operation inserts a new node at the end of the list, and updates the rear pointer to point to the new node. The time complexity of this operation is O(1), since we only need to change one pointer.
  - **Dequeue**: This operation removes the first node from the list, and updates the front pointer to point to the next node. The time complexity of this operation is also O(1), since we only need to change one pointer.
  - **IsEmpty**: This operation checks if the list is empty by comparing the front and rear pointers. If they are both NULL, then the list is empty. The time complexity of this operation is O(1), since we only need to compare two pointers.
  - **IsFull**: This operation checks if the list is full by comparing the available memory space with the size of a node. If there is not enough memory to allocate a new node, then the list is full. The time complexity of this operation is O(1), since we only need to compare two values.
  - **Peek**: This operation returns the data of the first node of the list, without removing it. The time complexity of this operation is O(1), since we only need to access one node.

- The following is an example of C code that implements a queue using a linked list:

```c
// Define a node structure
struct node {
  int data; // Data field
  struct node *next; // Pointer field
};

// Define a queue structure
struct queue {
  struct node *front; // Front pointer
  struct node *rear; // Rear pointer
};

// Create a new queue and initialize its pointers to NULL
struct queue *createQueue() {
  struct queue *q = (struct queue *)malloc(sizeof(struct queue)); // Allocate memory for the queue
  q->front = NULL; // Set front pointer to NULL
  q->rear = NULL; // Set rear pointer to NULL
  return q; // Return the queue
}

// Check if the queue is empty
int isEmpty(struct queue *q) {
  return (q->front == NULL); // Return true if front pointer is NULL, false otherwise
}

// Check if the queue is full
int isFull(struct queue *q) {
  struct node *temp = (struct node *)malloc(sizeof(struct node)); // Allocate memory for a temporary node
  if (temp == NULL) { // If memory allocation fails
    return 1; // Return true
  }
  else { // If memory allocation succeeds
    free(temp); // Free the temporary node
    return 0; // Return false
  }
}

// Insert a new node at the end of the queue
void enqueue(struct queue *q, int x) {
  if (isFull(q)) { // If the queue is full
    printf("Queue is full.\n"); // Print an error message
    return; // Exit the function
  }
  struct node *newNode = (struct node *)malloc(sizeof(struct node)); // Allocate memory for the new node
  newNode->data = x; // Set the data of the new node to x
  newNode->next = NULL; // Set the next pointer of the new node to NULL
  if (isEmpty(q)) { // If the queue is empty
    q->front = newNode; // Set the front pointer to the new node
  }
  else { // If the queue is not empty
    q->rear->next = newNode; // Set the next pointer of the last node to the new node
  }
  q->rear = newNode; // Set the rear pointer to the new node
  printf("Enqueued %d.\n", x); // Print a success message
}

// Remove the first node from the queue
int dequeue(struct queue *q) {
  if (isEmpty(q)) { // If the queue is empty
    printf("Queue is empty.\n

```
