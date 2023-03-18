### Implementation of Queue using Linked List

- Queue is a linear data structure that follows the First In First Out (FIFO) principle.
- In a queue, elements are added at the rear end and removed from the front end.
- Linked List is a dynamic data structure that can be used to implement a queue.
- The linked list implementation of a queue is efficient for operations involving insertion and deletion of elements.
- The following steps can be followed to implement a queue using linked list:

1. Define a structure to represent a node of the linked list. The structure should contain two fields - data and a pointer to the next node.
2. Define a structure to represent the queue. The structure should contain two pointers - front and rear. The front pointer points to the first node of the queue and the rear pointer points to the last node of the queue.
3. Initialize the front and rear pointers to NULL to indicate an empty queue.
4. To add an element to the queue, create a new node and insert it at the rear end of the queue. Update the rear pointer to point to the newly added node.
5. To remove an element from the queue, delete the node at the front end of the queue. Update the front pointer to point to the next node in the queue.
6. Implement functions to perform enqueue and dequeue operations on the queue. The enqueue function should take an element as input and add it to the queue. The dequeue function should remove the element at the front end of the queue and return it.
7. Implement a function to check if the queue is empty. The function should return true if the front pointer is NULL and false otherwise.
8. Implement a function to display the elements in the queue. The function should traverse the linked list from the front end to the rear end and print the data of each node.

- The linked list implementation of a queue can be used in various applications like job scheduling, printer queue, etc.