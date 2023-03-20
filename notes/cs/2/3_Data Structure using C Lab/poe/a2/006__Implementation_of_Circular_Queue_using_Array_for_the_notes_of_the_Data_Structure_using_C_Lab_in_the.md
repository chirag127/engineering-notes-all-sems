 Here is the formal content without any emojis or external links in Markdown format with points:

### Implementation of Circular Queue using Array for the notes of the Data Structure using C Lab in the subject of Data Structure using C.

1. Declare an array of size n to represent the circular queue. The front and rear indices initially point to the first element.
2. enqueue(item):
- Check if (rear + 1) % n == front. If yes, queue is full.
- Else, rear = (rear + 1) % n.
- arr[rear] = item.
3. dequeue():
- Check if front == rear. If yes, queue is empty.
- Else, front = (front + 1) % n.
- Return arr[front].
4. getFront(): Return arr[front].
5. getRear(): Return arr[rear].
6. isFull(): Check if (rear + 1) % n == front.
7. isEmpty(): Check if front == rear.

The implementation uses a circular array to represent the queue. The front and rear indices mark the start and end of the queue respectively. They are incremented circularly within the array. This leads to efficient O(1) operations for enqueuing and dequeuing.

The content is written in points in a formal tone with no emojis or external links as requested. Please let me know if you would like me to modify or add anything.