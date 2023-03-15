### Implementation of Circular Queue using Array

A circular queue is a type of queue data structure that uses an array to store the elements. A queue is a linear data structure that follows the First In First Out (FIFO) principle, meaning that the element that is inserted first is removed first. A circular queue overcomes the limitation of a normal queue, which is the wastage of space due to the empty slots that are left behind after some elements are dequeued.

To implement a circular queue using an array, we need to follow these steps:

- Initialize an array `queue` of size `n`, where `n` is the maximum number of elements that the queue can hold.
- Initialize two variables `front` and `rear` to `-1`, which indicate the index of the first and the last element in the queue respectively.
- To enqueue an element `x` onto the queue, do the following:
  - Increment `rear` by `1`.
  - If `rear` is equal to `n`, set `rear` to `0`. This wraps around the array and makes it circular.
  - If `front` is `-1`, set `front` to `0`. This means that the queue was empty before the insertion.
  - Check if `rear` is equal to `front`. If yes, then the queue is full and the insertion cannot be done. Display an overflow message and return.
  - Otherwise, store `x` at `queue[rear]`.
- To dequeue an element from the queue, do the following:
  - Check if `front` is `-1`. If yes, then the queue is empty and the deletion cannot be done. Display an underflow message and return.
  - Otherwise, store the element at `queue[front]` in a variable `y`.
  - Increment `front` by `1`.
  - If `front` is equal to `n`, set `front` to `0`. This wraps around the array and makes it circular.
  - If `front` is equal to `rear + 1`, set both `front` and `rear` to `-1`. This means that the queue is empty after the deletion.
  - Return `y` as the dequeued element.
- To display the elements of the queue, do the following:
  - Check if `front` is `-1`. If yes, then the queue is empty and there is nothing to display. Return.
  - Otherwise, initialize a variable `i` to `front`.
  - Loop from `i` to `rear`, incrementing `i` by `1` in each iteration.
  - If `i` is equal to `n`, set `i` to `0`. This wraps around the array and makes it circular.
  - Print the element at `queue[i]`.
  - Exit the loop when `i` is equal to `rear`.

Here is an example of a circular queue using an array in C:

```c
#include <stdio.h>
#define MAX 5 // maximum size of the queue

int queue[MAX]; // array to store the queue elements
int front = -1; // index of the first element
int rear = -1; // index of the last element

// function to enqueue an element into the queue
void enqueue(int x) {
  rear = (rear + 1) % MAX; // increment rear and wrap around if needed
  if (front == -1) { // if the queue was empty
    front = 0; // set front to 0
  }
  if (rear == front) { // if the queue is full
    printf("Queue overflow\n"); // display an error message
    if (rear == 0) { // reset rear to the previous position
      rear = MAX - 1;
    } else {
      rear = rear - 1;
    }
    return;
  }
  queue[rear] = x; // store x at the rear position
}

// function to dequeue an element from the queue
int dequeue() {
  if (front == -1) { // if the queue is empty
    printf("Queue underflow\n"); // display an error message
    return -1;
  }
  int y = queue[front]; // store the front element in y
  front = (front + 1) % MAX; // increment front and wrap around if needed
  if (front == (rear + 1) % MAX) { // if the queue is empty after the deletion
    front = -1; // reset front