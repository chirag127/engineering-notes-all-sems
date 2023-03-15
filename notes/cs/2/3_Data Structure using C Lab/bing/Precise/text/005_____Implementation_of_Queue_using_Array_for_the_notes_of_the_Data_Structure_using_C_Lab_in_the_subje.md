### Implementation of Queue using Array

A queue is a linear data structure that follows the First In First Out (FIFO) principle. This means that the element that is inserted first will be removed first. A queue can be implemented using an array by maintaining two variables, `front` and `rear`. The `front` variable points to the first element in the queue, while the `rear` variable points to the last element in the queue.

Here are the steps to implement a queue using an array:

1. **Initialize** the `front` and `rear` variables to -1, indicating that the queue is empty.
2. To **enqueue** an element, first check if the queue is full by comparing the `rear` variable with the size of the array. If the queue is full, display an error message. Otherwise, increment the `rear` variable and insert the element at the `rear` position in the array.
3. To **dequeue** an element, first check if the queue is empty by comparing the `front` variable with the `rear` variable. If the queue is empty, display an error message. Otherwise, increment the `front` variable and return the element at the `front` position in the array.
4. To **display** the elements in the queue, start from the `front` position and iterate until the `rear` position, displaying each element in the array.

Here is an example of a queue implemented using an array in C:

```c
#include <stdio.h>
#define SIZE 5

int queue[SIZE];
int front = -1, rear = -1;

void enqueue(int item) {
    if (rear == SIZE - 1) {
        printf("Queue is full\n");
    } else {
        if (front == -1)
            front = 0;
        rear++;
        queue[rear] = item;
        printf("Inserted -> %d\n", item);
    }
}

void dequeue() {
    if (front == -1) {
        printf("Queue is empty\n");
    } else {
        printf("Deleted : %d\n", queue[front]);
        front++;
        if (front > rear)
            front = rear = -1;
    }
}

void display() {
    if (rear == -1) {
        printf("Queue is empty\n");
    } else {
        int i;
        printf("Queue elements are:\n");
        for (i = front; i <= rear; i++)
            printf("%d ", queue[i]);
        printf("\n");
    }
}

int main() {
    dequeue();
    enqueue(1);
    enqueue(2);
    enqueue(3);
    enqueue(4);
    enqueue(5);
    enqueue(6);
    display();
    dequeue();
    display();

    return 0;
}
```

This code creates a queue of size 5 and performs various operations such as enqueue, dequeue, and display. The output of this code will be:

```
Queue is empty
Inserted -> 1
Inserted -> 2
Inserted -> 3
Inserted -> 4
Inserted -> 5
Queue is full
Queue elements are:
1 2 3 4 5
Deleted : 1
Queue elements are:
2 3 4 5
```

This is how a queue can be implemented using an array in C. It is important to note that this implementation has a limitation in that the size of the queue is fixed and cannot be changed dynamically. A more flexible implementation can be achieved using a linked list.