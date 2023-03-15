### Implementation of Circular Queue using Linked List for the notes of the Data Structure using C Lab in the subject of Data Structure using C

- A circular queue is a linear data structure that follows the FIFO (First In First Out) principle.
- A circular queue can be implemented using a linked list, where each node contains a data element and a pointer to the next node.
- A circular queue has two pointers, front and rear, that point to the first and last nodes of the queue respectively.
- The front pointer is used to dequeue (remove) elements from the queue, and the rear pointer is used to enqueue (insert) elements to the queue.
- The queue is empty when front and rear are NULL, and the queue is full when rear points to the node before front.
- To implement a circular queue using a linked list, we need to define a structure for the node and declare the front and rear pointers as global variables.

```c
// Define the structure for the node
struct node {
  int data; // Data element
  struct node *next; // Pointer to the next node
};

// Declare the front and rear pointers as global variables
struct node *front = NULL;
struct node *rear = NULL;
```

- To enqueue an element to the queue, we need to perform the following steps:
  - Create a new node and allocate memory for it.
  - Assign the data element to the new node and set its next pointer to NULL.
  - If the queue is empty, set both front and rear to point to the new node.
  - Else, set the next pointer of the rear node to point to the new node, and update the rear pointer to point to the new node.
  - Display a message that the element is enqueued.

```c
// Function to enqueue an element to the queue
void enqueue(int x) {
  // Create a new node and allocate memory for it
  struct node *newnode = (struct node *)malloc(sizeof(struct node));
  // Assign the data element to the new node and set its next pointer to NULL
  newnode->data = x;
  newnode->next = NULL;
  // If the queue is empty, set both front and rear to point to the new node
  if (front == NULL && rear == NULL) {
    front = rear = newnode;
  }
  // Else, set the next pointer of the rear node to point to the new node, and update the rear pointer to point to the new node
  else {
    rear->next = newnode;
    rear = newnode;
  }
  // Display a message that the element is enqueued
  printf("%d is enqueued to the queue.\n", x);
}
```

- To dequeue an element from the queue, we need to perform the following steps:
  - Check if the queue is empty. If yes, display a message that the queue is underflow and return.
  - Else, store the data element of the front node in a variable and display it.
  - If the queue has only one node, set both front and rear to NULL and free the node.
  - Else, update the front pointer to point to the next node of the front node and free the node.
  - Display a message that the element is dequeued.

```c
// Function to dequeue an element from the queue
void dequeue() {
  // Check if the queue is empty. If yes, display a message that the queue is underflow and return
  if (front == NULL && rear == NULL) {
    printf("The queue is underflow.\n");
    return;
  }
  // Else, store the data element of the front node in a variable and display it
  int x = front->data;
  printf("%d is dequeued from the queue.\n", x);
  // If the queue has only one node, set both front and rear to NULL and free the node
  if (front == rear) {
    free(front);
    front = rear = NULL;
  }
  // Else, update the front pointer to point to the next node of the front node and free the node
  else {
    struct node *temp = front;
    front = front->next;
    free(temp);
  }
}
```

- To display the elements of the queue, we need to perform the following steps:
  - Check if the queue is empty. If yes, display a message that the queue is empty and return.
  - Else, declare a pointer to traverse the queue from front to rear and display the data elements of each node.
  - Display a newline character at the end.

```c
// Function to display the elements of the queue
void display() {