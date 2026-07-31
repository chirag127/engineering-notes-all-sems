### Implementation of Stack using Array

- A stack is a linear data structure that follows the LIFO (Last In First Out) principle, meaning that the last element inserted is the first one to be removed.
- A stack can be implemented using an array, which is a fixed-size collection of elements of the same data type.
- To implement a stack using an array, we need to keep track of two variables: the size of the array and the top of the stack.
- The size of the array is the maximum number of elements that the stack can hold, and it is determined at the time of declaration.
- The top of the stack is the index of the array where the last element was inserted, and it is initialized to -1, indicating that the stack is empty.
- To perform the basic operations of a stack, such as push, pop, peek, and isEmpty, we need to use the following algorithms:

  - Push: To insert an element into the stack, we need to check if the stack is full or not. If the stack is full, we cannot insert any more elements and we display an error message. If the stack is not full, we increment the top variable by one and assign the element to the array at that index.
  - Pop: To remove an element from the stack, we need to check if the stack is empty or not. If the stack is empty, we cannot remove any elements and we display an error message. If the stack is not empty, we store the element at the top index in a temporary variable, decrement the top variable by one, and return the temporary variable.
  - Peek: To view the element at the top of the stack without removing it, we need to check if the stack is empty or not. If the stack is empty, we display an error message. If the stack is not empty, we return the element at the top index.
  - isEmpty: To check if the stack is empty or not, we need to compare the top variable with -1. If the top variable is equal to -1, the stack is empty and we return true. If the top variable is not equal to -1, the stack is not empty and we return false.

- Here is an example of how to implement a stack using an array in C:

```c
// Define the maximum size of the stack
#define MAX 10

// Declare the array and the top variable
int stack[MAX];
int top = -1;

// Push function
void push(int x)
{
  // Check if the stack is full
  if (top == MAX - 1)
  {
    printf("Stack overflow\n");
    return;
  }
  // Increment the top and insert the element
  top++;
  stack[top] = x;
}

// Pop function
int pop()
{
  // Check if the stack is empty
  if (top == -1)
  {
    printf("Stack underflow\n");
    return -1;
  }
  // Store the element and decrement the top
  int x = stack[top];
  top--;
  return x;
}

// Peek function
int peek()
{
  // Check if the stack is empty
  if (top == -1)
  {
    printf("Stack is empty\n");
    return -1;
  }
  // Return the element at the top
  return stack[top];
}

// isEmpty function
bool isEmpty()
{
  // Compare the top with -1
  if (top == -1)
  {
    return true;
  }
  else
  {
    return false;
  }
}
```