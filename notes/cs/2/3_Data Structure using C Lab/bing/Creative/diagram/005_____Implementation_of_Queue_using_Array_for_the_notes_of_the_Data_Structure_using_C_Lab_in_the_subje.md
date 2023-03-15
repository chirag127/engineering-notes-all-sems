### Implementation of Queue using Array

A queue is a linear data structure that follows the **First In First Out (FIFO)** principle. It means that the element that is inserted first in the queue is the one that is deleted first. A queue has two ends: the **front** and the **rear**. The front is where the elements are removed, and the rear is where the elements are inserted.

An array is a collection of elements of the same data type that are stored in contiguous memory locations. An array has a fixed size that is declared at compile time.

To implement a queue using an array, we need to:

- Declare an array of a fixed size, say MAXSIZE, to store the queue elements.
- Declare two variables, front and rear, to keep track of the first and last element of the queue. Initially, both front and rear are set to -1, indicating that the queue is empty.
- Define the following operations on the queue:
  - **enqueue(x)**: This operation inserts an element x at the rear end of the queue. To do this, we need to check if the queue is full or not. The queue is full if rear == MAXSIZE - 1. If the queue is full, we cannot insert any more elements and we display an error message. Otherwise, we increment rear by 1 and assign x to queue[rear].
  - **dequeue()**: This operation removes and returns the element at the front end of the queue. To do this, we need to check if the queue is empty or not. The queue is empty if front == -1 or front > rear. If the queue is empty, we cannot remove any elements and we display an error message. Otherwise, we return queue[front] and increment front by 1.
  - **display()**: This operation displays all the elements of the queue from front to rear. To do this, we need to check if the queue is empty or not. If the queue is empty, we display a message saying that the queue is empty. Otherwise, we use a loop to print the elements of the queue from queue[front] to queue[rear].

The following is a possible C program to implement a queue using an array:

```c
#include <stdio.h>
#define MAXSIZE 10

int queue[MAXSIZE]; // array to store the queue elements
int front = -1; // variable to mark the front of the queue
int rear = -1; // variable to mark the rear of the queue

// function to insert an element at the rear of the queue
void enqueue(int x)
{
    if (rear == MAXSIZE - 1) // check if the queue is full
    {
        printf("Queue is full\n");
    }
    else
    {
        rear++; // increment rear
        queue[rear] = x; // assign x to queue[rear]
        printf("Inserted %d\n", x);
    }
}

// function to remove and return the element at the front of the queue
int dequeue()
{
    if (front == -1 || front > rear) // check if the queue is empty
    {
        printf("Queue is empty\n");
        return -1;
    }
    else
    {
        int x = queue[front]; // store the front element in x
        front++; // increment front
        printf("Removed %d\n", x);
        return x; // return x
    }
}

// function to display the elements of the queue from front to rear
void display()
{
    if (front == -1 || front > rear) // check if the queue is empty
    {
        printf("Queue is empty\n");
    }
    else
    {
        printf("Queue elements are:\n");
        for (int i = front; i <= rear; i++) // loop from front to rear
        {
            printf("%d ", queue[i]); // print queue[i]
        }
        printf("\n");
    }
}

// main function to test the queue operations
int main()
{
    enqueue(10); // insert 10
    enqueue(20); // insert 20
    enqueue(30); // insert 30
    display(); // display the queue
    dequeue(); // remove the front element
    display(); // display the queue
    enqueue(40); // insert 40
    display(); // display the queue
    return 0;
}
```

The output of the program is:

```
Inserted 10
Inserted 20
Inserted 30
Queue elements are:
10 20 30