### Implementation of Circular Queue using Array

A circular queue is a type of queue data structure in which the last position is connected back to the first position to make a circle. It is also known as a ring buffer. A circular queue can be implemented using an array.

Here are the steps to implement a circular queue using an array:

1. **Initialize** the queue: Set the values of the front and rear pointers to -1, and create an array of a fixed size to store the elements of the queue.

2. **Enqueue** operation: To add an element to the queue, first check if the queue is full. If the queue is full, display an error message. If the queue is not full, increment the rear pointer and add the element to the queue. If the rear pointer reaches the end of the array, set it to 0.

3. **Dequeue** operation: To remove an element from the queue, first check if the queue is empty. If the queue is empty, display an error message. If the queue is not empty, increment the front pointer and remove the element from the queue. If the front pointer reaches the end of the array, set it to 0.

4. **Check if the queue is full**: The queue is full if the rear pointer is one less than the front pointer, or if the rear pointer is at the end of the array and the front pointer is at the beginning of the array.

5. **Check if the queue is empty**: The queue is empty if the front and rear pointers are both -1.
