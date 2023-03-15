Hello, I am Sydney, your AI assistant. I can help you with your study material for the Data Structure using C Lab. Here is the content for the topic of Implementation of Stack using Linked List.

### Implementation of Stack using Linked List

- A stack is a linear data structure that follows the LIFO (Last In First Out) principle, meaning that the last element inserted is the first one to be removed.
- A linked list is a dynamic data structure that consists of a sequence of nodes, each containing some data and a pointer to the next node in the list.
- A stack can be implemented using a linked list by maintaining a pointer to the top node of the list, which represents the top of the stack.
- To perform the basic operations of a stack, such as push, pop, peek, and isEmpty, we can use the following algorithms:

  - Push: To insert an element at the top of the stack, we can create a new node with the given data and make it point to the current top node. Then, we can update the top pointer to point to the new node.
  - Pop: To remove an element from the top of the stack, we can check if the stack is empty. If not, we can store the data of the top node in a temporary variable and update the top pointer to point to the next node in the list. Then, we can delete the top node and return the data stored in the temporary variable.
  - Peek: To return the element at the top of the stack without removing it, we can check if the stack is empty. If not, we can return the data of the top node.
  - IsEmpty: To check if the stack is empty, we can simply check if the top pointer is NULL or not.

- The following diagram illustrates the implementation of a stack using a linked list:

```
    top
     |
     v
+----+----+     +----+----+     +----+----+
| 10 | --+----> | 20 | --+----> | 30 |NULL|
+----+----+     +----+----+     +----+----+
```

- The following code snippet shows the implementation of a stack using a linked list in C:

```c
// A node structure for the linked list
struct node {
  int data; // data field
  struct node* next; // pointer to the next node
};

// A stack structure with a pointer to the top node
struct stack {
  struct node* top; // pointer to the top node
};

// A function to create a new node with the given data
struct node* createNode(int data) {
  // allocate memory for the node
  struct node* newNode = (struct node*)malloc(sizeof(struct node));
  // check if memory allocation is successful
  if (newNode == NULL) {
    printf("Memory allocation failed.\n");
    exit(1);
  }
  // assign the data and the next pointer
  newNode->data = data;
  newNode->next = NULL;
  // return the new node
  return newNode;
}

// A function to create an empty stack
struct stack* createStack() {
  // allocate memory for the stack
  struct stack* newStack = (struct stack*)malloc(sizeof(struct stack));
  // check if memory allocation is successful
  if (newStack == NULL) {
    printf("Memory allocation failed.\n");
    exit(1);
  }
  // initialize the top pointer to NULL
  newStack->top = NULL;
  // return the new stack
  return newStack;
}

// A function to push an element to the top of the stack
void push(struct stack* s, int data) {
  // create a new node with the given data
  struct node* newNode = createNode(data);
  // make the new node point to the current top node
  newNode->next = s->top;
  // update the top pointer to point to the new node
  s->top = newNode;
  // print a message
  printf("Pushed %d to the stack.\n", data);
}

// A function to pop an element from the top of the stack
int pop(struct stack* s) {
  // check if the stack is empty
  if (s->top == NULL) {
    printf("Stack is empty.\n");
    return -1;
  }
  // store the data of the top node in a temporary variable
  int data = s->top->data;
  // update the top pointer to point to the next node in the list
  struct node* temp = s->top;
  s->top = s->top->next;