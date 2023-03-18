### Implementation of Stack using Array

In this lab, we will learn about the implementation of a Stack using an Array in the Data Structure using C. A Stack is a linear data structure that follows the Last In First Out (LIFO) concept. The element which is inserted last is the first one to be removed.

#### Steps for Implementing Stack using Array

1. Start by defining the maximum size of the stack and initializing the top of the stack to -1.
2. Declare an array of the defined size to store the elements of the stack.
3. Push operation: To insert an element into the stack, check if the stack is full or not by comparing the top of the stack with the maximum size. If the stack is not full, increment the top of the stack and insert the element at the top position.
4. Pop operation: To remove an element from the stack, check if the stack is empty or not by comparing the top of the stack with -1. If the stack is not empty, remove the element at the top position and decrement the top of the stack.
5. Peek operation: To get the topmost element of the stack without actually removing it, simply return the element at the top position of the stack.
6. Display operation: To display all the elements of the stack, start from the top of the stack and print all the elements until the bottom of the stack is reached.

#### Advantages of using an Array to implement Stack

1. Arrays provide fast access to elements using an index.
2. Arrays have a fixed size that can be easily defined.
3. Arrays can be easily traversed.

#### Disadvantages of using an Array to implement Stack

1. The size of the array needs to be defined before use, making it difficult to change the size of the stack dynamically.
2. If the stack is not full, the array still occupies the same amount of memory, leading to memory wastage.
3. Insertion and deletion of elements in the middle of the stack is not possible.

By implementing a Stack using an Array, we can easily manipulate data in a LIFO manner. In this lab, we learned about the steps to implement a Stack using an Array and the advantages and disadvantages of using an Array to implement a Stack.