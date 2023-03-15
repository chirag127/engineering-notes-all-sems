# Implementation of Circular Queue using Linked List

- A circular queue is a linear data structure that follows the FIFO (First In First Out) principle.
- A circular queue can be implemented using a linked list, where each node contains a data element and a pointer to the next node.
- A circular queue has two pointers: front and rear, which point to the first and last nodes of the queue respectively.
- The front pointer is used to dequeue (remove) elements from the queue, and the rear pointer is used to enqueue (insert) elements to the queue.
- The queue is empty when both front and rear are NULL, and the queue is full when the rear pointer points to the front node.
- To implement a circular queue using a linked list, we need to define a structure for the node, and declare the front and rear pointers as global variables.

```c
// Define a structure for the node
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
  - If the queue is empty, set both front and rear pointers to the new node.
  - Else, set the next pointer of the rear node to the new node, and update the rear pointer to the new node.
  - Set the next pointer of the new node to the front node, to make the queue circular.

```c
// Enqueue an element to the queue
void enqueue(int x) {
  // Create a new node and allocate memory for it
  struct node *newnode = (struct node *)malloc(sizeof(struct node));
  // Assign the data element to the new node and set its next pointer to NULL
  newnode->data = x;
  newnode->next = NULL;
  // If the queue is empty, set both front and rear pointers to the new node
  if (front == NULL && rear == NULL) {
    front = rear = newnode;
  }
  // Else, set the next pointer of the rear node to the new node, and update the rear pointer to the new node
  else {
    rear->next = newnode;
    rear = newnode;
  }
  // Set the next pointer of the new node to the front node, to make the queue circular
  newnode->next = front;
}
```

- To dequeue an element from the queue, we need to perform the following steps:
  - Check if the queue is empty, and if so, print an error message and return.
  - Else, store the data element of the front node in a temporary variable, and update the front pointer to the next node of the front node.
  - If the front pointer becomes NULL, set the rear pointer to NULL as well, to indicate that the queue is empty.
  - Free the memory of the front node, and return the data element stored in the temporary variable.

```c
// Dequeue an element from the queue
int dequeue() {
  // Check if the queue is empty, and if so, print an error message and return
  if (front == NULL && rear == NULL) {
    printf("Queue is empty\n");
    return -1;
  }
  // Else, store the data element of the front node in a temporary variable, and update the front pointer to the next node of the front node
  int x = front->data;
  struct node *temp = front;
  front = front->next;
  // If the front pointer becomes NULL, set the rear pointer to NULL as well, to indicate that the queue is empty
  if (front == NULL) {
    rear = NULL;
  }
  // Free the memory of the front node, and return the data element stored in the temporary variable
  free(temp);
  return x;
}
```

- To display the elements of the queue, we need to perform the following steps:
  - Check if the queue is empty, and if so, print an error message and return.
  - Else, declare a pointer variable to traverse the queue, and initialize it with the front pointer.
  - Loop through the queue until the pointer variable reaches the rear node, and print the data element of each node.
  - Print the data element of the rear node as well, and print a newline character.

```c
// Display the elements of the queue
void display() {
  // Check if the queue