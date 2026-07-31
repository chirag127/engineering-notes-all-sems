### Implementation of Stack using Linked List

- A stack is a linear data structure that follows the LIFO (Last In First Out) principle, meaning that the last element inserted is the first one to be removed.
- A linked list is a dynamic data structure that consists of a sequence of nodes, each node having a data field and a pointer field that points to the next node in the list.
- A stack can be implemented using a linked list by maintaining a pointer to the top node of the list, which represents the top of the stack.
- To perform the basic operations of a stack, such as push, pop, peek, and isEmpty, using a linked list, the following steps are required:

  - Push: To insert an element at the top of the stack, a new node is created with the given data and its pointer field is set to point to the current top node. Then, the top pointer is updated to point to the new node.
  - Pop: To remove an element from the top of the stack, the data of the top node is returned and the top pointer is updated to point to the next node in the list. Then, the top node is deleted from the memory.
  - Peek: To return the data of the top element of the stack without removing it, the data of the top node is returned.
  - isEmpty: To check if the stack is empty or not, the top pointer is checked for null value. If it is null, the stack is empty, otherwise it is not.

- The following is an example of C code that implements a stack using a linked list:

```c
// Define a structure for a node of the linked list
struct node {
  int data; // Data field
  struct node *next; // Pointer field
};

// Define a structure for a stack
struct stack {
  struct node *top; // Pointer to the top node of the list
};

// Create a new stack and initialize its top pointer to null
struct stack *createStack() {
  struct stack *s = (struct stack *)malloc(sizeof(struct stack)); // Allocate memory for the stack
  s->top = NULL; // Set the top pointer to null
  return s; // Return the stack
}

// Push an element at the top of the stack
void push(struct stack *s, int data) {
  struct node *newNode = (struct node *)malloc(sizeof(struct node)); // Allocate memory for the new node
  newNode->data = data; // Set the data field of the new node
  newNode->next = s->top; // Set the pointer field of the new node to point to the current top node
  s->top = newNode; // Update the top pointer to point to the new node
}

// Pop an element from the top of the stack
int pop(struct stack *s) {
  if (s->top == NULL) { // Check if the stack is empty
    printf("Stack is empty.\n"); // Print an error message
    return -1; // Return an invalid value
  }
  else {
    int data = s->top->data; // Store the data of the top node
    struct node *temp = s->top; // Store the address of the top node
    s->top = s->top->next; // Update the top pointer to point to the next node
    free(temp); // Free the memory of the top node
    return data; // Return the data of the popped element
  }
}

// Peek the top element of the stack
int peek(struct stack *s) {
  if (s->top == NULL) { // Check if the stack is empty
    printf("Stack is empty.\n"); // Print an error message
    return -1; // Return an invalid value
  }
  else {
    return s->top->data; // Return the data of the top node
  }
}

// Check if the stack is empty
int isEmpty(struct stack *s) {
  return (s->top == NULL); // Return 1 if the top pointer is null, 0 otherwise
}

// Display the elements of the stack
void display(struct stack *s) {
  struct node *temp = s->top; // Create a temporary pointer to traverse the list
  printf("Stack: ");
  while (temp != NULL) { // Loop until the end of the list
    printf("%d ", temp->data); // Print the data of the current node
    temp = temp->next; // Move the pointer to the next node
  }
  printf("\n");
}

// Main function to test the stack implementation
int main() {
  struct stack *s = createStack();

```
