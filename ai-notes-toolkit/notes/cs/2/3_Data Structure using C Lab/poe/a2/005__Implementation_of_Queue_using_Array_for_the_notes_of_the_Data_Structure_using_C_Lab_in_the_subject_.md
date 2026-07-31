 Here is the formal notes on the given topic:

### Implementation of Queue using Array

1. Queue is an abstract data type which is like a list in which the additions are made at one end called REAR and deletions are made at the other end called FRONT.
2. The queue follows the First In First Out (FIFO) principle, i.e. the element which is entered first in the queue is dequeued first.
3. We can implement a queue using an array. In this, we specify the size of the array (lets say n). We define two variables:
- FRONT: Points to the front element of the queue
- REAR: Points to the last element of the queue
4. Initially, FRONT = -1 and REAR = -1 (Empty queue)
5. When an element is enqueued, REAR is incremented and the element is added at the REAR index. If REAR = n-1, it is wrapped around to 0 as the queue is implemented using a circular array.
6. When an element is dequeued, FRONT is incremented. If FRONT = n-1, it is wrapped around to 0.
7. The queue is full when REAR = (FRONT + 1) % n and empty when FRONT = REAR.

The above points cover the major steps to implement a queue using an array. The implementation can be done in C/C++/Java, etc. The program should handle cases of queue full and queue empty appropriately.