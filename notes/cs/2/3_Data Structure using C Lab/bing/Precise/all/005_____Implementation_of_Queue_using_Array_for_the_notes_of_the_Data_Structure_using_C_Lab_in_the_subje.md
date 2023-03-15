### Implementation of Queue using Array

A queue is a linear data structure that follows the First In First Out (FIFO) principle. This means that the element that is inserted first will be removed first. A queue can be implemented using an array by maintaining two variables, front and rear, to keep track of the first and last elements in the queue.

Here are the steps to implement a queue using an array:

1. Initialize the front and rear variables to -1, indicating that the queue is empty.
2. To insert an element into the queue, first check if the queue is full by comparing the rear variable with the size of the array. If the queue is full, display an error message. Otherwise, increment the rear variable and insert the element at the rear position in the array.
3. To remove an element from the queue, first check if the queue is empty by comparing the front and rear variables. If the queue is empty, display an error message. Otherwise, increment the front variable and return the element at the front position in the array.
4. To display the elements in the queue, iterate from the front to the rear position in the array and print the elements.

This is a basic implementation of a queue using an array in the C programming language for the Data Structure using C Lab in the subject of Data Structure using C. It is important to note that this implementation has a limitation in that the size of the queue is fixed and cannot be changed dynamically. A more advanced implementation using a dynamic array or linked list can overcome this limitation.