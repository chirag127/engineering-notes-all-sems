### Implementation of Circular Queue using Array

Circular Queue is a data structure that represents a queue in a circular manner. It has a front and a rear end, and items are enqueued at the rear end and dequeued from the front end. Once the rear end reaches the end of the array, it wraps around to the beginning of the array. Similarly, when the front end reaches the end of the array, it also wraps around to the beginning of the array.

The implementation of Circular Queue using an array involves the following steps:

1. Declare an array of a fixed size to hold the elements of the queue.
2. Initialize the front and rear pointers to -1, indicating an empty queue.
3. Define functions for enqueue and dequeue operations.
4. Implement the enqueue operation as follows:
   * Check if the queue is full by checking if the rear pointer is at the end of the array.
   * If the queue is full, display an overflow message and return.
   * If the queue is not full, increment the rear pointer and add the new element to the rear of the queue.
5. Implement the dequeue operation as follows:
   * Check if the queue is empty by checking if the front pointer is equal to -1.
   * If the queue is empty, display an underflow message and return.
   * If the queue is not empty, remove the element from the front of the queue and increment the front pointer.
6. Define a function to display the contents of the queue.
7. Implement the main function to test the enqueue, dequeue, and display functions.

Below is the C code for the implementation of Circular Queue using an array:

```
#define SIZE 5
int queue[SIZE];
int front = -1, rear = -1;

void enqueue(int value) {
    if ((front == 0 && rear == SIZE-1) || (rear == front-1)) {
        printf("Overflow\n");
        return;
    }
    else if (front == -1 && rear == -1) {
        front = rear = 0;
        queue[rear] = value;
    }
    else if (rear == SIZE-1 && front != 0) {
        rear = 0;
        queue[rear] = value;
    }
    else {
        rear++;
        queue[rear] = value;
    }
}

void dequeue() {
    if (front == -1) {
        printf("Underflow\n");
        return;
    }
    else if (front == rear) {
        front = rear = -1;
    }
    else if (front == SIZE-1) {
        front = 0;
    }
    else {
        front++;
    }
}

void display() {
    int i;
    if (front == -1) {
        printf("Queue is empty\n");
        return;
    }
    printf("Queue elements are:\n");
    if (rear >= front) {
        for (i = front; i <= rear; i++)
            printf("%d ", queue[i]);
    }
    else {
        for (i = front; i < SIZE; i++)
            printf("%d ", queue[i]);
        for (i = 0; i <= rear; i++)
            printf("%d ", queue[i]);
    }
    printf("\n");
}

int main() {
    enqueue(10);
    enqueue(20);
    enqueue(30);
    enqueue(40);
    display();
    dequeue();
    dequeue();
    display();
    enqueue(50);
    enqueue(60);
    display();
    dequeue();
    display();

    return 0;
}
```

In conclusion, the circular queue is a data structure that is efficient in managing data in a circular manner. The implementation of circular queue using an array is straightforward and can be easily implemented in C language.