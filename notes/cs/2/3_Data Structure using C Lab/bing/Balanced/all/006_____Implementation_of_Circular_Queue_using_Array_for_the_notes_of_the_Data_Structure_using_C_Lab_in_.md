# Implementation of Circular Queue using Array

- A circular queue is a linear data structure that follows the FIFO (First In First Out) principle.
- A circular queue can be implemented using an array of fixed size, with two variables to keep track of the front and rear indices of the queue.
- The front index points to the first element of the queue, and the rear index points to the last element of the queue.
- The queue is empty when front and rear are equal, and the queue is full when rear is one position behind front (modulo the size of the array).
- To insert an element into the queue, we check if the queue is full, and if not, we increment the rear index (modulo the size of the array) and store the element at that position.
- To delete an element from the queue, we check if the queue is empty, and if not, we return the element at the front index and increment the front index (modulo the size of the array).
- To display the elements of the queue, we start from the front index and traverse the queue until we reach the rear index, printing the elements along the way.
- The advantage of using a circular queue over a linear queue is that it avoids the wastage of space that occurs when the front index moves forward in a linear queue, leaving empty spaces at the beginning of the array.
- The disadvantage of using a circular queue is that it has a fixed capacity and cannot grow dynamically as the number of elements increases.

The following is a sample code in C language to implement a circular queue using an array:

```c
#include <stdio.h>
#define MAXSIZE 10 // define the maximum size of the queue

int queue[MAXSIZE]; // declare the array to store the queue elements
int front = -1; // initialize the front index to -1
int rear = -1; // initialize the rear index to -1

// function to check if the queue is empty
int isEmpty()
{
    if (front == -1 && rear == -1)
        return 1; // return 1 if the queue is empty
    else
        return 0; // return 0 if the queue is not empty
}

// function to check if the queue is full
int isFull()
{
    if ((rear + 1) % MAXSIZE == front)
        return 1; // return 1 if the queue is full
    else
        return 0; // return 0 if the queue is not full
}

// function to insert an element into the queue
void enqueue(int x)
{
    if (isFull())
    {
        printf("Queue is full. Cannot insert %d.\n", x); // print an error message if the queue is full
        return;
    }
    else if (isEmpty())
    {
        front = 0; // set the front index to 0 if the queue is empty
        rear = 0; // set the rear index to 0 if the queue is empty
    }
    else
    {
        rear = (rear + 1) % MAXSIZE; // increment the rear index (modulo the size of the array) if the queue is not empty and not full
    }
    queue[rear] = x; // store the element at the rear index
    printf("Inserted %d into the queue.\n", x); // print a success message
}

// function to delete an element from the queue
int dequeue()
{
    int x; // declare a variable to store the deleted element
    if (isEmpty())
    {
        printf("Queue is empty. Cannot delete.\n"); // print an error message if the queue is empty
        return -1;
    }
    else if (front == rear)
    {
        x = queue[front]; // store the element at the front index
        front = -1; // set the front index to -1 if the queue has only one element
        rear = -1; // set the rear index to -1 if the queue has only one element
    }
    else
    {
        x = queue[front]; // store the element at the front index
        front = (front + 1) % MAXSIZE; // increment the front index (modulo the size of the array) if the queue has more than one element
    }
    printf("Deleted %d from the queue.\n", x); // print a success message
    return x; // return the deleted element
}

// function to display the elements of the queue
void display()
{
    int i; // declare a variable to loop through the queue
    if (isEmpty())
    {
        printf("Queue is empty. Nothing to display.\n"); //