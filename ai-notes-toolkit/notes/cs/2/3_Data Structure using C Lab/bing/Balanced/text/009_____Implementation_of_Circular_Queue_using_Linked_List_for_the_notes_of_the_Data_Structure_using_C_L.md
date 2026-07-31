### Implementation of Circular Queue using Linked List for the notes of the Data Structure using C Lab in the subject of Data Structure using C

- A circular queue is a linear data structure that follows the FIFO (First In First Out) principle.
- A circular queue can be implemented using a linked list, where each node contains a data element and a pointer to the next node.
- A circular queue has two pointers: front and rear, which point to the first and last nodes of the queue respectively.
- The front pointer is used to dequeue (remove) elements from the queue, and the rear pointer is used to enqueue (insert) elements to the queue.
- The queue is empty when front and rear are NULL, and the queue is full when rear points to the node before front.
- To implement a circular queue using a linked list, we need to define a structure for the node, and declare the front and rear pointers as global variables.

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
  - Assign the data element to the new node.
  - If the queue is empty, set front and rear to point to the new node, and make the next pointer of the new node point to itself.
  - Else, make the next pointer of the rear node point to the new node, update the rear pointer to point to the new node, and make the next pointer of the new node point to the front node.

```c
// Enqueue an element to the queue
void enqueue(int x) {
  // Create a new node and allocate memory for it
  struct node *new_node = (struct node *)malloc(sizeof(struct node));
  // Assign the data element to the new node
  new_node->data = x;
  // If the queue is empty, set front and rear to point to the new node, and make the next pointer of the new node point to itself
  if (front == NULL && rear == NULL) {
    front = rear = new_node;
    new_node->next = new_node;
  }
  // Else, make the next pointer of the rear node point to the new node, update the rear pointer to point to the new node, and make the next pointer of the new node point to the front node
  else {
    rear->next = new_node;
    rear = new_node;
    new_node->next = front;
  }
}
```

- To dequeue an element from the queue, we need to perform the following steps:
  - Check if the queue is empty, and if so, print an error message and return.
  - Else, store the data element of the front node in a variable, and update the front pointer to point to the next node of the front node.
  - If the queue has only one node, set front and rear to NULL.
  - Else, make the next pointer of the rear node point to the front node.
  - Free the memory of the deleted node, and return the data element.

```c
// Dequeue an element from the queue
int dequeue() {
  // Check if the queue is empty, and if so, print an error message and return
  if (front == NULL && rear == NULL) {
    printf("Queue is empty\n");
    return -1;
  }
  // Else, store the data element of the front node in a variable, and update the front pointer to point to the next node of the front node
  else {
    int x = front->data; // Data element to be returned
    struct node *temp = front; // Temporary pointer to the front node
    front = front->next; // Update the front pointer
    // If the queue has only one node, set front and rear to NULL
    if (front == rear) {
      front = rear = NULL;
    }
    // Else, make the next pointer of the rear node point to the front node
    else {
      rear->next = front;
    }
    // Free the memory of the deleted node, and return the data element
    free(temp);
    return x;
  }
}
```

- To display the elements of the queue, we need to perform the following steps:
  - Check if the queue is empty, and if so, print an error message and return.
  - Else, declare a temporary pointer and initialize it to the front