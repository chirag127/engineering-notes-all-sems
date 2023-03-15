### Implementation of Stack using Array

- A stack is a linear data structure that follows the LIFO (Last In First Out) principle, meaning that the last element inserted is the first one to be removed.
- A stack can be implemented using an array, which is a fixed-size collection of elements of the same data type, stored in contiguous memory locations.
- To implement a stack using an array, we need to keep track of two variables: the capacity of the array, which is the maximum number of elements that can be stored in the stack, and the top of the stack, which is the index of the last element inserted in the array.
- The basic operations on a stack are push, pop, peek, and isEmpty. Push adds an element to the top of the stack, pop removes and returns the element at the top of the stack, peek returns the element at the top of the stack without removing it, and isEmpty checks if the stack is empty or not.
- The pseudocode for implementing a stack using an array is as follows:

```
// Declare an array of size capacity and a variable top
array[capacity]
top = -1

// Push operation
push(element):
  // Check if the stack is full
  if top == capacity - 1:
    // Display an error message and return
    print("Stack overflow")
    return
  // Increment the top by 1
  top = top + 1
  // Store the element at the top of the array
  array[top] = element

// Pop operation
pop():
  // Check if the stack is empty
  if top == -1:
    // Display an error message and return
    print("Stack underflow")
    return
  // Store the element at the top of the array
  element = array[top]
  // Decrement the top by 1
  top = top - 1
  // Return the element
  return element

// Peek operation
peek():
  // Check if the stack is empty
  if top == -1:
    // Display an error message and return
    print("Stack is empty")
    return
  // Return the element at the top of the array
  return array[top]

// isEmpty operation
isEmpty():
  // Check if the top is -1
  if top == -1:
    // Return true
    return true
  // Return false
  return false
```