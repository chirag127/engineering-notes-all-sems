### Implementation of Queue using Array for the notes of the Data Structure using C Lab in the subject of Data Structure using C

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle, where the first element added to the queue is the first one to be removed. In other words, elements are added to the back of the queue and removed from the front of the queue.

One way to implement a queue using an array is to use two pointers, front and rear, to keep track of the front and rear of the queue. The front pointer points to the first element in the queue, while the rear pointer points to the next available position in the queue. When an element is added to the queue, the rear pointer is incremented, and when an element is removed from the queue, the front pointer is incremented.

The implementation of a queue using an array requires the following steps:

1. Declare an array of a fixed size to store the elements in the queue.

2. Initialize the front and rear pointers to 0.

3. To add an element to the queue, check if the rear pointer is equal to the size of the array. If it is, the queue is full and no more elements can be added. If it is not, increment the rear pointer and insert the new element at that position.

4. To remove an element from the queue, check if the front pointer is equal to the rear pointer. If it is, the queue is empty and no elements can be removed. If it is not, increment the front pointer and return the element at that position.

In this unit, we will study the implementation of a queue using an array in the C programming language. We will examine the algorithms for adding and removing elements from the queue, and study the performance of the queue in terms of time and space complexity. We will also study the relationship between queues and other data structures, such as stacks and linked lists.
