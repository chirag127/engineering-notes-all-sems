### Implementation of Queue using Array

A queue is a linear data structure that follows the principle of First In First Out (FIFO). This means that the element that is inserted first in the queue is the one that is deleted first. A queue has two operations: enqueue and dequeue. Enqueue is the process of adding an element at the rear end of the queue, and dequeue is the process of removing an element from the front end of the queue.

To implement a queue using an array, we need to declare an array of a fixed size and two variables to keep track of the front and rear indices of the queue. The front variable points to the first element of the queue, and the rear variable points to the last element of the queue. Initially, both front and rear are set to -1, indicating that the queue is empty.

The following are the steps to perform the enqueue and dequeue operations on a queue using an array:

- Enqueue: To add an element x to the queue, we first check if the queue is full or not. The queue is full if the rear index is equal to the size of the array minus one. If the queue is full, we display an error message and return. Otherwise, we increment the rear index by one and assign x to the array element at the rear index. If the queue was empty before, we also increment the front index by one.

- Dequeue: To remove an element from the queue, we first check if the queue is empty or not. The queue is empty if the front index is equal to -1 or if the front index is greater than the rear index. If the queue is empty, we display an error message and return. Otherwise, we store the array element at the front index in a variable and return it. We also increment the front index by one. If the queue becomes empty after the dequeue operation, we reset both front and rear to -1.

The following is an example of a C program that implements a queue using an array:

```c
#include <stdio.h>
#define MAXSIZE 10 // define the maximum size of the queue

// declare the queue array and the front and rear variables
int queue[MAXSIZE];
int front = -1;
int rear = -1;

// function to check if the queue is full
int isFull() {
  if (rear == MAXSIZE - 1) {
    return 1; // queue is full
  } else {
    return 0; // queue is not full
  }
}

// function to check if the queue is empty
int isEmpty() {
  if (front == -1 || front > rear) {
    return 1; // queue is empty
  } else {
    return 0; // queue is not empty
  }
}

// function to add an element to the queue
void enqueue(int x) {
  if (isFull()) {
    printf("Queue is full\n"); // display error message
    return;
  } else {
    rear++; // increment rear index
    queue[rear] = x; // assign x to the queue element at rear index
    if (front == -1) {
      front++; // increment front index if the queue was empty
    }
    printf("Enqueued %d\n", x); // display success message
  }
}

// function to remove an element from the queue
int dequeue() {
  int x;
  if (isEmpty()) {
    printf("Queue is empty\n"); // display error message
    return -1;
  } else {
    x = queue[front]; // store the queue element at front index in x
    front++; // increment front index
    if (front > rear) {
      front = rear = -1; // reset front and rear if the queue becomes empty
    }
    printf("Dequeued %d\n", x); // display success message
    return x;
  }
}

// function to display the queue elements
void display() {
  int i;
  if (isEmpty()) {
    printf("Queue is empty\n"); // display error message
    return;
  } else {
    printf("Queue elements are:\n");
    for (i = front; i <= rear; i++) {
      printf("%d ", queue[i]); // print the queue element at index i
    }
    printf("\n");
  }
}

// main function to test the queue implementation
int main() {
  // perform some enqueue and dequeue operations
  enqueue(10);
  enqueue(20);
  enqueue(30);
  display();
  dequeue();
  dequeue();
  display();