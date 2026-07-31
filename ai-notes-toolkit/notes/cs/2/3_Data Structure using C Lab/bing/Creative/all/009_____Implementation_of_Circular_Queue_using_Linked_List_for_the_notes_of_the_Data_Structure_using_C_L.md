# Implementation of Circular Queue using Linked List

- A circular queue is a type of queue data structure that stores elements in a circular manner.
- A circular queue can be implemented using a linked list, where each node contains a data element and a pointer to the next node.
- A circular queue has two pointers, front and rear, that point to the first and last nodes of the queue respectively.
- A circular queue is empty when front and rear are NULL, and full when rear->next is front.
- The main operations on a circular queue are enqueue (insert an element at the rear), dequeue (remove an element from the front), and display (print all the elements in the queue).

## Enqueue Operation

- To enqueue an element in a circular queue, we need to perform the following steps:
  - Create a new node and store the data element in it.
  - If the queue is empty, set both front and rear to the new node, and make the new node point to itself.
  - If the queue is not empty, set rear->next to the new node, update rear to the new node, and make the new node point to front.
  - Return the queue.

## Dequeue Operation

- To dequeue an element from a circular queue, we need to perform the following steps:
  - If the queue is empty, return NULL or an error message.
  - If the queue has only one element, store the data element in a temporary variable, free the node, and set both front and rear to NULL.
  - If the queue has more than one element, store the data element in a temporary variable, update front to front->next, free the node, and make rear point to the new front.
  - Return the data element or the queue.

## Display Operation

- To display the elements of a circular queue, we need to perform the following steps:
  - If the queue is empty, return NULL or an error message.
  - If the queue is not empty, initialize a pointer to the front node, and print its data element.
  - Traverse the queue by updating the pointer to the next node, until it reaches the rear node, and print its data element.
  - Return the queue.