# Implementation of Queue using Array

A queue is a linear data structure that follows the principle of First In First Out (FIFO). This means that the element that is inserted first in the queue is the one that is deleted first. A queue has two ends: the front and the rear. The front is where the elements are removed and the rear is where the elements are inserted.

To implement a queue using an array, we need to declare an array of a fixed size and two variables to keep track of the front and rear indices. The front and rear variables are initialized to -1, indicating that the queue is empty. The following diagram shows the structure of a queue using an array:

![queue using array](https://www.digitalocean.com/community/tutorials/queue-in-c/queue-array.png)

To perform the basic operations of a queue, such as enqueue (insert), dequeue (remove), peek (view the front element), and isEmpty (check if the queue is empty), we need to follow some rules:

- To enqueue an element, we need to check if the queue is full or not. The queue is full if the rear index is equal to the size of the array minus one. If the queue is not full, we increment the rear index by one and store the element at that position in the array.
- To dequeue an element, we need to check if the queue is empty or not. The queue is empty if the front index is equal to -1 or if the front index is greater than the rear index. If the queue is not empty, we return the element at the front index and increment the front index by one.
- To peek an element, we need to check if the queue is empty or not. If the queue is not empty, we return the element at the front index without modifying the queue.
- To check if the queue is empty, we compare the front and rear indices. If the front index is equal to -1 or if the front index is greater than the rear index, the queue is empty. Otherwise, the queue is not empty.

The following is a C program that implements a queue using an array and performs the basic operations:

```c
#include <stdio.h>
#include <stdlib.h>

#define MAXSIZE 10 // the maximum size of the queue

// declare the queue array and the front and rear variables
int queue[MAXSIZE];
int front = -1;
int rear = -1;

// function to check if the queue is full
int isFull()
{
    if (rear == MAXSIZE - 1)
    {
        return 1; // the queue is full
    }
    else
    {
        return 0; // the queue is not full
    }
}

// function to check if the queue is empty
int isEmpty()
{
    if (front == -1 || front > rear)
    {
        return 1; // the queue is empty
    }
    else
    {
        return 0; // the queue is not empty
    }
}

// function to insert an element at the rear of the queue
void enqueue(int x)
{
    if (isFull())
    {
        printf("Queue is full. Cannot insert %d.\n", x);
    }
    else
    {
        if (front == -1) // if the queue is initially empty
        {
            front = 0; // set the front index to 0
        }
        rear++; // increment the rear index
        queue[rear] = x; // store the element at the rear index
        printf("Inserted %d at the rear of the queue.\n", x);
    }
}

// function to remove and return an element from the front of the queue
int dequeue()
{
    int x;
    if (isEmpty())
    {
        printf("Queue is empty. Cannot dequeue.\n");
        return -1; // return -1 to indicate an error
    }
    else
    {
        x = queue[front]; // store the element at the front index
        front++; // increment the front index
        printf("Removed %d from the front of the queue.\n", x);
        return x; // return the removed element
    }
}

// function to return an element from the front of the queue without removing it
int peek()
{
    int x;
    if (isEmpty())
    {
        printf("Queue is empty. Cannot peek.\n");
        return -1; // return -1 to indicate an error
    }
    else
    {
        x = queue[front]; // store the element at the front index

```
