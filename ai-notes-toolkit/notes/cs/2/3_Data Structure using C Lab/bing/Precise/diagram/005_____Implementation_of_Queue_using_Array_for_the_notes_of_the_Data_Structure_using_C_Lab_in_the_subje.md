### Implementation of Queue using Array

A queue is a linear data structure that follows the First In First Out (FIFO) principle. This means that the element that is inserted first will be removed first. A queue can be implemented using an array by maintaining two variables, `front` and `rear`. The `front` variable points to the first element in the queue, while the `rear` variable points to the last element in the queue.

Here are the steps to implement a queue using an array:

1. Initialize the `front` and `rear` variables to -1.
2. To insert an element into the queue, first check if the queue is full by checking if `rear` is equal to the size of the array minus 1. If the queue is full, display an error message. Otherwise, increment the `rear` variable and insert the element at the `rear` position in the array.
3. To remove an element from the queue, first check if the queue is empty by checking if `front` is equal to -1. If the queue is empty, display an error message. Otherwise, increment the `front` variable and return the element at the `front` position in the array.
4. To check if the queue is empty, check if `front` is equal to -1.
5. To check if the queue is full, check if `rear` is equal to the size of the array minus 1.

Here is an example of a queue implemented using an array in C:

```c
#include <stdio.h>
#define SIZE 5

int queue[SIZE];
int front = -1;
int rear = -1;

void enqueue(int item) {
    if (rear == SIZE - 1) {
        printf("Queue is full\n");
    } else {
        if (front == -1) {
            front = 0;
        }
        rear++;
        queue[rear] = item;
        printf("Inserted %d\n", item);
    }
}

int dequeue() {
    int item;
    if (front == -1 || front > rear) {
        printf("Queue is empty\n");
        return -1;
    } else {
        item = queue[front];
        front++;
        printf("Removed %d\n", item);
        return item;
    }
}

int main() {
    enqueue(1);
    enqueue(2);
    enqueue(3);
    enqueue(4);
    enqueue(5);
    enqueue(6);
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    return 0;
}
```

This code creates a queue of size 5 and inserts 6 elements into it. Since the queue can only hold 5 elements, an error message is displayed when trying to insert the 6th element. The code then removes all the elements from the queue and displays an error message when trying to remove an element from an empty queue.