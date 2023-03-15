### Implementation of Circular Queue using Linked List

A circular queue is a linear data structure that follows the First In First Out (FIFO) principle. The difference between a linear queue and a circular queue is that in a circular queue, the last element is connected to the first element, forming a circle.

A linked list is a data structure that consists of a sequence of nodes, where each node contains data and a reference to the next node in the sequence.

A circular queue can be implemented using a linked list by maintaining a reference to the front and rear of the queue. The front of the queue is the first element, and the rear of the queue is the last element.

Here are the steps to implement a circular queue using a linked list:

1. Define a node structure that contains data and a reference to the next node.
2. Initialize the front and rear of the queue to NULL.
3. To enqueue an element, create a new node and add it to the rear of the queue. If the queue is empty, set the front and rear to the new node. Otherwise, set the next reference of the rear node to the new node and update the rear to the new node.
4. To dequeue an element, remove the front node from the queue and update the front to the next node. If the queue becomes empty, set the front and rear to NULL.
5. To check if the queue is empty, check if the front is NULL.
6. To check if the queue is full, check if the next reference of the rear node is the front node.
