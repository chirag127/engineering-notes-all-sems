### Implementation of Circular Queue using Array

A circular queue is a linear data structure that follows the First In First Out (FIFO) principle. The difference between a regular queue and a circular queue is that in a circular queue, the last position is connected back to the first position to make a circle.

Here are the steps to implement a circular queue using an array:

1. **Initialize** the queue: Set the values of the front and rear pointers to -1, and create an array of a fixed size.

2. **Enqueue** operation: To add an element to the queue, first check if the queue is full. If the queue is full, display an error message. If the queue is not full, increment the rear pointer and add the element to the queue. If the rear pointer reaches the end of the array, set it to 0.

3. **Dequeue** operation: To remove an element from the queue, first check if the queue is empty. If the queue is empty, display an error message. If the queue is not empty, increment the front pointer and remove the element from the queue. If the front pointer reaches the end of the array, set it to 0.

4. **Display** the queue: To display the elements of the queue, start from the front pointer and traverse the queue until the rear pointer is reached.

Here is an example of a circular queue implemented using an array in C:

```c
#include <stdio.h>
#define SIZE 5

int items[SIZE];
int front = -1, rear = -1;

int isFull() {
  if ((front == rear + 1) || (front == 0 && rear == SIZE - 1)) return 1;
  return 0;
}

int isEmpty() {
  if (front == -1) return 1;
  return 0;
}

void enQueue(int element) {
  if (isFull())
    printf("\n Queue is full!! \n");
  else {
    if (front == -1) front = 0;
    rear = (rear + 1) % SIZE;
    items[rear] = element;
    printf("\n Inserted -> %d", element);
  }
}

int deQueue() {
  int element;
  if (isEmpty()) {
    printf("\n Queue is empty !! \n");
    return (-1);
  } else {
    element = items[front];
    if (front == rear) {
      front = -1;
      rear = -1;
    } else {
      front = (front + 1) % SIZE;
    }
    printf("\n Deleted element -> %d \n", element);
    return (element);
  }
}

void display() {
  int i;
  if (isEmpty())
    printf(" \n Empty Queue\n");
  else {
    printf("\n Front -> %d ", front);
    printf("\n Items -> ");
    for (i = front; i != rear; i = (i + 1) % SIZE) {
      printf("%d ", items[i]);
    }
    printf("%d ", items[i]);
    printf("\n Rear -> %d \n", rear);
  }
}

int main() {
  deQueue();

  enQueue(1);
  enQueue(2);
  enQueue(3);
  enQueue(4);
  enQueue(5);

  enQueue(6);

  display();
  deQueue();

  display();

  enQueue(7);
  display();

  enQueue(8);

  return 0;
}
```

This code creates a circular queue of size 5 and performs various operations such as enqueue, dequeue, and display. The `isFull` and `isEmpty` functions are used to check if the queue is full or empty, respectively.