### Implementation of Stack using Array

- A stack is a linear data structure that follows the LIFO (Last In First Out) principle, meaning that the last element inserted is the first one to be removed.
- A stack can be implemented using an array, which is a fixed-size collection of elements of the same data type, stored in contiguous memory locations.
- To implement a stack using an array, we need to keep track of two variables: the size of the array (capacity) and the index of the top element (top).
- The capacity of the array determines how many elements can be stored in the stack. The top of the stack is the index of the last element inserted, or -1 if the stack is empty.
- The basic operations on a stack are push, pop, peek, and isEmpty.
- Push operation adds a new element to the top of the stack, if there is space available. It increments the top variable by one and assigns the element to the array at that index.
- Pop operation removes and returns the top element of the stack, if the stack is not empty. It decrements the top variable by one and returns the element at that index.
- Peek operation returns the top element of the stack, without removing it, if the stack is not empty. It returns the element at the top index.
- IsEmpty operation checks if the stack is empty or not. It returns true if the top variable is -1, and false otherwise.
- The following is a possible C code for implementing a stack using an array:

```c
// Define the maximum capacity of the stack
#define MAX 10

// Declare a global array and a top variable
int stack[MAX];
int top = -1;

// Push operation
void push(int x) {
  // Check if the stack is full
  if (top == MAX - 1) {
    printf("Stack overflow\n");
    return;
  }
  // Increment the top and insert the element
  top++;
  stack[top] = x;
}

// Pop operation
int pop() {
  // Check if the stack is empty
  if (top == -1) {
    printf("Stack underflow\n");
    return -1;
  }
  // Return the top element and decrement the top
  int x = stack[top];
  top--;
  return x;
}

// Peek operation
int peek() {
  // Check if the stack is empty
  if (top == -1) {
    printf("Stack is empty\n");
    return -1;
  }
  // Return the top element
  return stack[top];
}

// IsEmpty operation
bool isEmpty() {
  // Return true if the top is -1, false otherwise
  return top == -1;
}
```