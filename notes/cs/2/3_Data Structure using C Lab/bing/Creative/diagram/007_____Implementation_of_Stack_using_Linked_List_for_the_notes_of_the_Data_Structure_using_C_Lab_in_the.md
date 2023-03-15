### Implementation of Stack using Linked List

- A stack is a linear data structure that follows the LIFO (Last In First Out) principle, meaning that the last element inserted is the first one to be removed.
- A linked list is a dynamic data structure that consists of a sequence of nodes, each node having a data field and a pointer field that points to the next node in the list.
- A stack can be implemented using a linked list by maintaining a pointer to the top node of the list, which represents the top of the stack.
- To perform the basic operations of a stack using a linked list, we need to define the following functions:

  - `push()`: This function inserts a new node at the beginning of the list, and updates the top pointer to point to the new node. The time complexity of this operation is O(1), as it does not depend on the size of the list.
  - `pop()`: This function deletes the first node of the list, and updates the top pointer to point to the next node. It also returns the data of the deleted node. The time complexity of this operation is also O(1), as it does not depend on the size of the list.
  - `peek()`: This function returns the data of the top node of the list, without deleting it. The time complexity of this operation is O(1), as it does not depend on the size of the list.
  - `isEmpty()`: This function checks if the list is empty or not, by checking if the top pointer is NULL or not. The time complexity of this operation is O(1), as it does not depend on the size of the list.
  - `display()`: This function prints the data of all the nodes in the list, starting from the top node. The time complexity of this operation is O(n), where n is the number of nodes in the list, as it depends on the size of the list.

- The following is an example of the C code for implementing a stack using a linked list:

```c
// Define a structure for the node
struct node {
  int data; // Data field
  struct node *next; // Pointer field
};

// Define a global pointer for the top of the stack
struct node *top = NULL;

// Define a function to push a new node to the stack
void push(int x) {
  // Allocate memory for the new node
  struct node *newNode = (struct node *)malloc(sizeof(struct node));
  // Check if memory allocation is successful
  if (newNode == NULL) {
    printf("Stack overflow\n");
    return;
  }
  // Assign the data to the new node
  newNode->data = x;
  // Link the new node to the top of the stack
  newNode->next = top;
  // Update the top pointer
  top = newNode;
  printf("Pushed %d to the stack\n", x);
}

// Define a function to pop a node from the stack
int pop() {
  // Check if the stack is empty
  if (top == NULL) {
    printf("Stack underflow\n");
    return -1;
  }
  // Store the data of the top node
  int x = top->data;
  // Store the address of the top node
  struct node *temp = top;
  // Update the top pointer
  top = top->next;
  // Free the memory of the deleted node
  free(temp);
  printf("Popped %d from the stack\n", x);
  // Return the data of the deleted node
  return x;
}

// Define a function to peek the top node of the stack
int peek() {
  // Check if the stack is empty
  if (top == NULL) {
    printf("Stack is empty\n");
    return -1;
  }
  // Return the data of the top node
  return top->data;
}

// Define a function to check if the stack is empty
int isEmpty() {
  // Check if the top pointer is NULL
  if (top == NULL) {
    // Return 1 if true
    return 1;
  }
  // Return 0 if false
  return 0;
}

// Define a function to display the stack
void display() {
  // Check if the stack is empty
  if (top == NULL) {
    printf("Stack is empty\n");
    return;
  }
  // Create a temporary pointer to traverse the stack
  struct node *temp = top;
  // Print the data of each node
  printf("Stack: ");
  while (temp != NULL) {
    printf("%d ", temp->data);
    temp =