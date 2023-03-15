# Implementation of Circular Queue using Array

A circular queue is a type of queue data structure that uses an array to store the elements. A queue is a linear data structure that follows the FIFO (First In First Out) principle, meaning that the element that is inserted first is removed first. A circular queue overcomes the limitation of a normal queue, which is the wastage of space due to the empty slots that are left behind after some insertions and deletions.

To implement a circular queue using an array, we need to follow these steps:

- Initialize an array of size n, where n is the maximum number of elements that the queue can hold. This array will be used to store the elements of the queue.
- Initialize two variables front and rear to -1. These variables will keep track of the index of the first and the last element of the queue, respectively.
- To enqueue (insert) an element x onto the queue, do the following:
  - Increment rear by 1. If rear is equal to n, set rear to 0. This ensures that the rear index wraps around the array when it reaches the end.
  - If front is -1, set front to 0. This means that the queue was empty before the insertion, and now it has one element.
  - If front is equal to rear, then the queue is full and the insertion cannot be done. Display an overflow message and return.
  - Otherwise, store x at the rear index of the array.
- To dequeue (remove) an element from the queue, do the following:
  - If front is -1, then the queue is empty and the deletion cannot be done. Display an underflow message and return.
  - Otherwise, store the element at the front index of the array in a variable and return it.
  - Increment front by 1. If front is equal to n, set front to 0. This ensures that the front index wraps around the array when it reaches the end.
  - If front is equal to rear + 1, then the queue is empty after the deletion, and set both front and rear to -1. This resets the queue to its initial state.

Here is an example of a circular queue using an array in C:

```c
#include <stdio.h>
#define MAX 5 // maximum size of the queue

int cqueue_arr[MAX]; // array to store the elements of the queue
int front = -1; // index of the first element of the queue
int rear = -1; // index of the last element of the queue

void insert(int item); // function to enqueue an element
int del(); // function to dequeue an element
void display(); // function to display the elements of the queue

int main()
{
    int choice, item; // variables to store the user input
    while (1) // loop until the user exits
    {
        printf("1. Insert\n");
        printf("2. Delete\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice); // read the user choice
        switch (choice) // perform the corresponding operation
        {
        case 1:
            printf("Enter the element to be inserted: ");
            scanf("%d", &item); // read the element to be inserted
            insert(item); // call the insert function
            break;
        case 2:
            item = del(); // call the delete function and store the returned element
            if (item != -1) // if the element is valid, display it
                printf("The deleted element is: %d\n", item);
            break;
        case 3:
            display(); // call the display function
            break;
        case 4:
            exit(1); // exit the program
        default:
            printf("Invalid choice\n"); // display an error message for invalid choice
        }
    }
    return 0;
}

void insert(int item)
{
    if ((front == 0 && rear == MAX - 1) || (front == rear + 1)) // check if the queue is full
    {
        printf("Queue Overflow\n"); // display an overflow message
        return;
    }
    if (front == -1) // check if the queue is empty
        front = 0; // set front to 0
    if (rear == MAX - 1) // check if rear is at the end of the array
        rear = 0; // wrap around rear to 0