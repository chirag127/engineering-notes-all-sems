### Implementation of Queue using Array

A queue is a linear data structure that follows the First In First Out (FIFO) principle. This means that the element that is inserted first will be removed first. A queue can be implemented using an array by keeping track of two indices, front and rear.

1. **Initialization**: To initialize a queue, we need to set the value of front and rear to -1. This indicates that the queue is empty.

2. **Enqueue**: To insert an element into the queue, we first need to check if the queue is full. This can be done by checking if the rear index is equal to the size of the array minus one. If the queue is full, we cannot insert any more elements. If the queue is not full, we increment the rear index and insert the element at the rear index.

3. **Dequeue**: To remove an element from the queue, we first need to check if the queue is empty. This can be done by checking if the front index is equal to -1. If the queue is empty, there are no elements to remove. If the queue is not empty, we increment the front index and return the element at the front index.

4. **Peek**: To view the element at the front of the queue without removing it, we can simply return the element at the front index.

Here is an example implementation of a queue using an array in C:

```c
#include <stdio.h>
#define SIZE 5

int queue[SIZE];
int front = -1;
int rear = -1;

void enqueue(int element) {
    if (rear == SIZE - 1) {
        printf("Queue is full\n");
    } else {
        if (front == -1) {
            front = 0;
        }
        rear++;
        queue[rear] = element;
        printf("Inserted element: %d\n", element);
    }
}

void dequeue() {
    if (front == -1) {
        printf("Queue is empty\n");
    } else {
        printf("Removed element: %d\n", queue[front]);
        front++;
        if (front > rear) {
            front = rear = -1;
        }
    }
}

void peek() {
    if (front == -1) {
        printf("Queue is empty\n");
    } else {
        printf("Element at front: %d\n", queue[front]);
    }
}

int main() {
    enqueue(1);
    enqueue(2);
    enqueue(3);
    enqueue(4);
    enqueue(5);
    enqueue(6);
    peek();
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    return 0;
}
```

This code implements a queue using an array of size 5. It has functions for enqueue, dequeue, and peek operations. The main function demonstrates how these functions can be used to insert and remove elements from the queue.