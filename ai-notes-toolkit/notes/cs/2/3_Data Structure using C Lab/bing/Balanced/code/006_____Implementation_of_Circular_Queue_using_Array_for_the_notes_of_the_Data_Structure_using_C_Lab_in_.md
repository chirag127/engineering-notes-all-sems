### Implementation of Circular Queue using Array

- A circular queue is a linear data structure that follows the FIFO (First In First Out) principle.
- A circular queue can be implemented using an array of fixed size, say `MAX`.
- A circular queue has two pointers, `front` and `rear`, that indicate the first and last elements of the queue respectively.
- Initially, both `front` and `rear` are set to `-1`, indicating an empty queue.
- To insert an element into the queue, we perform the following steps:
  - Check if the queue is full by using the condition `(rear + 1) % MAX == front`.
  - If the queue is full, display an error message and return.
  - If the queue is empty, set both `front` and `rear` to `0`.
  - Otherwise, increment `rear` by `1` modulo `MAX`.
  - Store the element at the `rear` index of the array.
- To delete an element from the queue, we perform the following steps:
  - Check if the queue is empty by using the condition `front == -1`.
  - If the queue is empty, display an error message and return.
  - If the queue has only one element, set both `front` and `rear` to `-1`.
  - Otherwise, increment `front` by `1` modulo `MAX`.
  - Return the element at the `front` index of the array.
- To display the elements of the queue, we perform the following steps:
  - Check if the queue is empty by using the condition `front == -1`.
  - If the queue is empty, display an error message and return.
  - Otherwise, initialize a variable `i` to `front`.
  - Loop from `i` to `rear`, incrementing `i` by `1` modulo `MAX` in each iteration.
  - Print the element at the `i` index of the array.
- The following is a sample C program that implements a circular queue using an array:

```c
#include <stdio.h>
#define MAX 5 // Maximum size of the queue

int queue[MAX]; // Array to store the queue elements
int front = -1; // Pointer to the first element of the queue
int rear = -1; // Pointer to the last element of the queue

// Function to insert an element into the queue
void enqueue(int x) {
  // Check if the queue is full
  if ((rear + 1) % MAX == front) {
    printf("Queue is full\n");
    return;
  }
  // Check if the queue is empty
  if (front == -1) {
    front = 0;
    rear = 0;
  }
  // Otherwise, increment rear by 1 modulo MAX
  else {
    rear = (rear + 1) % MAX;
  }
  // Store the element at the rear index of the array
  queue[rear] = x;
  printf("Inserted %d\n", x);
}

// Function to delete an element from the queue
int dequeue() {
  int x; // Variable to store the deleted element
  // Check if the queue is empty
  if (front == -1) {
    printf("Queue is empty\n");
    return -1;
  }
  // Store the element at the front index of the array
  x = queue[front];
  // Check if the queue has only one element
  if (front == rear) {
    front = -1;
    rear = -1;
  }
  // Otherwise, increment front by 1 modulo MAX
  else {
    front = (front + 1) % MAX;
  }
  // Return the deleted element
  return x;
}

// Function to display the elements of the queue
void display() {
  int i; // Loop variable
  // Check if the queue is empty
  if (front == -1) {
    printf("Queue is empty\n");
    return;
  }
  // Initialize i to front
  i = front;
  // Loop from i to rear, incrementing i by 1 modulo MAX in each iteration
  while (i != rear) {
    // Print the element at the i index of the array
    printf("%d ", queue[i]);
    // Increment i by 1 modulo MAX
    i = (i + 1) % MAX;
  }
  // Print the element at the rear index of the array
  printf("%d\n", queue[rear]);
}

// Main function
int main() {
  int choice, x; // Variables to store the user input
  // Loop until the user enters

```
