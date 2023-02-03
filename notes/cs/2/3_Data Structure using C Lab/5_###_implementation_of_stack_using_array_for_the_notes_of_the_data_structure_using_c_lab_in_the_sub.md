### Implementation of Stack using Array for the notes of the Data Structure using C Lab in the subject of Data Structure using C

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle, meaning that the last element added to the stack is the first one to be removed. One way to implement a stack is using an array. In this implementation, an array is used to store the elements of the stack, and two variables are used to keep track of the top of the stack.

The first variable, called "top," keeps track of the index of the element at the top of the stack. Initially, the value of "top" is set to -1, which indicates that the stack is empty. When an element is added to the stack, the value of "top" is incremented, and the element is stored in the array at the index "top."

The second variable, called "capacity," keeps track of the maximum number of elements that the stack can hold. This value is set when the stack is created, and it cannot be exceeded.

To implement the push operation, which adds an element to the top of the stack, the following steps are taken:

1. Check if the stack is full. If it is, return an error message.
2. Increment the value of "top."
3. Store the element in the array at the index "top."

To implement the pop operation, which removes the element from the top of the stack, the following steps are taken:

1. Check if the stack is empty. If it is, return an error message.
2. Retrieve the element from the array at the index "top."
3. Decrement the value of "top."

In addition to push and pop operations, other operations, such as peek (returning the element at the top of the stack without removing it), and isEmpty (checking if the stack is empty), can also be implemented using the array implementation of a stack.

In summary, an array can be used to implement a stack data structure in C language. The implementation uses two variables, "top" and "capacity," to keep track of the top of the stack and the maximum number of elements that the stack can hold, respectively. The push and pop operations can be implemented using the array, and other operations, such as peek and isEmpty, can also be implemented.
