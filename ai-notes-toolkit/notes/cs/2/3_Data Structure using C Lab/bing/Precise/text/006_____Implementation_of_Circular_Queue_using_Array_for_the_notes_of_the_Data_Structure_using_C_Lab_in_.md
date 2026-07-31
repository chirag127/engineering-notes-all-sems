### Implementation of Circular Queue using Array

A circular queue is a linear data structure that follows the First In First Out (FIFO) principle. The difference between a regular queue and a circular queue is that in a circular queue, the last position is connected back to the first position to make a circle. This can be implemented using an array.

Here are the steps to implement a circular queue using an array:

1. **Initialize** the queue: Set the front and rear pointers to -1 and create an array of a fixed size.

2. **Enqueue** operation: To add an element to the queue, first check if the queue is full. If the queue is full, print an error message. If the queue is not full, increment the rear pointer and add the element to the array at the rear pointer's index. If this is the first element being added, set the front pointer to 0.

3. **Dequeue** operation: To remove an element from the queue, first check if the queue is empty. If the queue is empty, print an error message. If the queue is not empty, remove the element at the front pointer's index and increment the front pointer. If the front pointer becomes equal to the size of the array, set it back to 0.

4. **Check if the queue is full**: The queue is full if the rear pointer is one less than the front pointer or if the rear pointer is at the last index of the array and the front pointer is at the first index.

5. **Check if the queue is empty**: The queue is empty if the front and rear pointers are both -1.

This is a basic implementation of a circular queue using an array in the C programming language. It can be used as a reference for the Data Structure using C Lab in the subject of Data Structure using C.