
### Implementation of Circular Queue using Array

1. A circular queue is a type of data structure in which the last position is connected to the first position to make a circle.
2. The elements can be added at the end of the queue and removed from the beginning of the queue.
3. The size of the queue is fixed and it is declared at the time of creation.
4. The array is used to implement a circular queue.
5. The array is declared with the size of the queue and the two variables front and rear are used to keep track of the positions of the elements.
6. The front points to the first element of the queue and rear points to the last element of the queue.
7. When the queue is empty, both front and rear points to the same position.
8. When the queue is full, the next position of the rear is the front.
9. The enqueue operation adds an element at the rear of the queue and the dequeue operation removes an element from the front of the queue.
10. The overflow condition occurs when the rear reaches the end of the array and the underflow condition occurs when the queue is empty.