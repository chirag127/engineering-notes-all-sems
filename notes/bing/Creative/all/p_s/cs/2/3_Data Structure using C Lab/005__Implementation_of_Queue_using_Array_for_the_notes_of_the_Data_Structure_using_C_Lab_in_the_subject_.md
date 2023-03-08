### Implementation of Queue using Array in C

- A queue is a linear data structure that follows the **FIFO (First In First Out)** principle, meaning that the element that is inserted first is removed first.
- A queue has two operations: **enqueue** and **dequeue**. Enqueue adds an element at the rear end of the queue, and dequeue removes an element from the front end of the queue.
- A queue can be implemented using an array in C, but there are some limitations and challenges to consider.
- One limitation is that the size of the array must be fixed at compile time, and cannot be changed at run time. Therefore, the queue can only store a limited number of elements, and may cause overflow or underflow errors if the queue is full or empty.
- Another challenge is that the array must be shifted every time an element is dequeued, which is a costly operation in terms of time and space complexity. To avoid this, a circular queue can be used, which uses a modulo operation to wrap around the array indices.
- A queue using an array in C can be implemented using the following steps:

  - Declare an array of a fixed size, and two variables to store the front and rear indices of the queue. Initialize both indices to -1, indicating that the queue is empty.
  - To enqueue an element, check if the queue is full by comparing the rear index with the size of the array. If the queue is full, display an error message and return. Otherwise, increment the rear index by one, and store the element at that index in the array.
  - To dequeue an element, check if the queue is empty by comparing the front and rear indices. If the queue is empty, display an error message and return. Otherwise, increment the front index by one, and return the element at that index in the array.
  - To display the queue, iterate from the front index to the rear index, and print the elements in the array.

- Here is an example of a queue using an array in C:

```c
#include <stdio.h>
#define SIZE 5 // size of the array

// global variables
int queue[SIZE]; // array to store the queue elements
int front = -1; // index of the front element
int rear = -1; // index of the rear element

// function prototypes
void enqueue(int x); // to add an element at the rear end
int dequeue(); // to remove an element from the front end
void display(); // to display the queue elements

int main()
{
    // some sample operations
    enqueue(10);
    enqueue(20);
    enqueue(30);
    display();
    printf("Dequeued element: %d\n", dequeue());
    display();
    enqueue(40);
    enqueue(50);
    enqueue(60); // overflow error
    display();
    return 0;
}

// function to add an element at the rear end
void enqueue(int x)
{
    // check if the queue is full
    if (rear == SIZE - 1)
    {
        printf("Queue overflow\n");
        return;
    }
    // increment the rear index and store the element
    rear++;
    queue[rear] = x;
    // if the queue was empty, update the front index
    if (front == -1)
    {
        front = 0;
    }
}

// function to remove an element from the front end
int dequeue()
{
    // check if the queue is empty
    if (front == -1 || front > rear)
    {
        printf("Queue underflow\n");
        return -1;
    }
    // return the element and increment the front index
    int x = queue[front];
    front++;
    // if the queue becomes empty, reset the indices
    if (front > rear)
    {
        front = -1;
        rear = -1;
    }
    return x;
}

// function to display the queue elements
void display()
{
    // check if the queue is empty
    if (front == -1 || front > rear)
    {
        printf("Queue is empty\n");
        return;
    }
    // print the elements from front to rear
    printf("Queue elements: ");
    for (int i = front; i <= rear; i++)
    {
        printf("%d ", queue[i]);
    }
    printf("\n");
}
```

- The output of the program is:

```
Queue elements: 10 20 30
Dequeued element: 10
Queue elements: 20 30

Some possible mnemonics and learning tricks for the topic are:

- To remember the order of enqueue and dequeue operations, think of a queue as a line of people waiting to enter a movie theater. The first person to enter the line is the first person to enter the theater, and the last person to enter the line is the last person to enter the theater. This is the FIFO principle.
- To remember the initial values of the front and rear indices, think of them as pointers that point to nothing when the queue is empty. Therefore, they are set to -1, which is an invalid index in the array.
- To remember the condition for queue overflow, think of the rear index reaching the end of the array. Therefore, the condition is rear == SIZE - 1, where SIZE is the size of the array.
- To remember the condition for queue underflow, think of the front index exceeding the rear index. Therefore, the condition is front == -1 or front > rear.