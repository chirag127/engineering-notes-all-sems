### Implementation of Circular Queue using Linked List

- A circular queue is a linear data structure that follows the FIFO (First In First Out) principle.
- A circular queue can be implemented using a linked list, where each node contains a data element and a pointer to the next node.
- A circular queue has two pointers: front and rear, which point to the first and last nodes of the queue respectively.
- The front pointer is used to dequeue (remove) elements from the queue, and the rear pointer is used to enqueue (insert) elements to the queue.
- The queue is empty when both front and rear are NULL, and the queue is full when the rear pointer points to the front node.
- To implement a circular queue using a linked list, we need to perform the following operations:

  - Create: To create an empty circular queue, we initialize both front and rear pointers to NULL.
  - Enqueue: To enqueue an element to the queue, we create a new node with the given data and link it to the rear node. Then, we update the rear pointer to point to the new node. If the queue is empty, we also update the front pointer to point to the new node. Finally, we link the new node to the front node to make the queue circular.
  - Dequeue: To dequeue an element from the queue, we check if the queue is empty. If not, we store the data of the front node and unlink it from the queue. Then, we update the front pointer to point to the next node. If the queue becomes empty, we also update the rear pointer to NULL. Finally, we return the stored data.
  - Display: To display the elements of the queue, we check if the queue is empty. If not, we traverse the queue from the front node to the rear node using a temporary pointer and print the data of each node. We stop the traversal when the temporary pointer reaches the front node again.

- The following is a possible C code for implementing a circular queue using a linked list:

```c
// A structure to represent a node of the queue
struct node {
  int data; // data element
  struct node *next; // pointer to the next node
};

// A structure to represent a circular queue
struct queue {
  struct node *front; // pointer to the front node
  struct node *rear; // pointer to the rear node
};

// A function to create an empty circular queue
struct queue *create() {
  struct queue *q = (struct queue *)malloc(sizeof(struct queue)); // allocate memory for the queue
  q->front = NULL; // initialize front pointer to NULL
  q->rear = NULL; // initialize rear pointer to NULL
  return q; // return the queue
}

// A function to enqueue an element to the queue
void enqueue(struct queue *q, int x) {
  struct node *newnode = (struct node *)malloc(sizeof(struct node)); // allocate memory for the new node
  newnode->data = x; // assign data to the new node
  newnode->next = NULL; // initialize next pointer to NULL
  if (q->rear == NULL) { // if the queue is empty
    q->front = newnode; // update front pointer to the new node
    q->rear = newnode; // update rear pointer to the new node
  } else { // if the queue is not empty
    q->rear->next = newnode; // link the new node to the rear node
    q->rear = newnode; // update rear pointer to the new node
  }
  q->rear->next = q->front; // link the rear node to the front node to make the queue circular
}

// A function to dequeue an element from the queue
int dequeue(struct queue *q) {
  if (q->front == NULL) { // if the queue is empty
    printf("Queue is empty.\n"); // print an error message
    return -1; // return an invalid value
  } else { // if the queue is not empty
    int x = q->front->data; // store the data of the front node
    struct node *temp = q->front; // store the front node in a temporary pointer
    if (q->front == q->rear) { // if the queue has only one node
      q->front = NULL; // update front pointer to NULL
      q->rear = NULL; // update rear pointer to NULL
    } else { // if the queue has more than one node
      q->front = q->front->next; // update front pointer to the next node
      q->rear