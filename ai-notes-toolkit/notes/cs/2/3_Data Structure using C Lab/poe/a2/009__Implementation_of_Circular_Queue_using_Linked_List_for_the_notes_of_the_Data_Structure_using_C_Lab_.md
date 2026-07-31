 Here is the formal notes on the topic -

### Implementation of Circular Queue using Linked List

1. A Circular Queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle.
2. A Linked List is a collection of nodes where each node has a data field and a reference (link) to the next node in the list.
3. To implement a Circular Queue using Linked List:
- Declare a Node which has two attributes - data and next.
- Create a Linked List of nodes and refer to the head and tail of the list.
- perform Enqueue operation by:
-- checking if the queue is full
-- inserting the node at the tail and updating the tail to point to the new node
- perform Dequeue operation by:
-- checking if the queue is empty
-- accessing the head node, storing its data and then incrementing the head to point to the next node
- The queue is full when tail = (head + 1) % queueSize and empty when head = tail.
4. The main advantages of Circular Queue are -
- The last position is connected to the first position, hence no extra space is required.
- The effective usage of space.
- The overflow and underflow situations are easily handled.

The above notes cover the key points to understand the Implementation of Circular Queue using Linked List. The points are written in a formal manner with no emojis or external links as requested. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.