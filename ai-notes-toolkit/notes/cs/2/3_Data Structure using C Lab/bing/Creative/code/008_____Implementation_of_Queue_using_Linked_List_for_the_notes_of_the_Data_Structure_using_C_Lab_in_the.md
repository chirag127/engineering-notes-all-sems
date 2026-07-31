### Implementation of Queue using Linked List

- A queue is a linear data structure that follows the FIFO (First In First Out) principle, meaning that the element that is inserted first is removed first.
- A linked list is a dynamic data structure that consists of a sequence of nodes, each node having a data field and a pointer field that points to the next node in the list.
- A queue can be implemented using a linked list by maintaining two pointers, one for the front of the queue and one for the rear of the queue.
- The front pointer points to the node that is at the head of the linked list, and the rear pointer points to the node that is at the tail of the linked list.
- To enqueue an element, a new node is created with the given data and the pointer field set to NULL. The new node is then inserted at the end of the linked list, and the rear pointer is updated to point to the new node.
- To dequeue an element, the node that is pointed by the front pointer is removed from the beginning of the linked list, and the front pointer is updated to point to the next node. The data of the removed node is returned and the node is freed from memory.
- To check if the queue is empty, the front pointer is compared with NULL. If the front pointer is NULL, then the queue is empty, otherwise it is not.
- To check if the queue is full, the memory allocation for the new node is checked. If the memory allocation fails, then the queue is full, otherwise it is not.
- To display the elements of the queue, the linked list is traversed from the front pointer to the rear pointer, and the data of each node is printed.