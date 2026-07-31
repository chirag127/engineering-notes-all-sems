 Here is the formal notes on the topic "Implementation of Queue using Linked List" without any emojis or external links in Markdown format:

### Implementation of Queue using Linked List

1. Queue is an abstract data type which demonstrates First In First Out (FIFO) behavior.
2. In a queue, the first element inserted is the first one to be removed.
3. One of the ways to implement a queue is using a linked list. In a linked list implementation of a queue:
- The front pointer points to the front element of the queue.
- The rear pointer points to the rear element of the queue.
- enqueue operation:
-- insert an element at the rear of the queue
-- increment rear and point it to the new rear element
- dequeue operation:
-- remove the front element and increment front to point to the next element.
-- if the queue is empty, front and rear would be equal.
4. The advantages of a linked list implementation are:
- Dynamic size
- Efficient enqueue and dequeue operations if we maintain front and rear pointers.
- The disadvantages are:
- Wastage of space as each element requires space for a pointer.
- Random access is not allowed. We have to access elements sequentially starting from the front pointer.

The above notes cover the key points on implementing a queue using a linked list. The points are written in a formal way with headings and without any emojis or external links as requested. Please let me know if you would like me to elaborate on any of the points or modify the content.