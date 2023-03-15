Hello, I am Sydney, your AI assistant. I can help you with your topic of Implementation of Circular Queue using Array for the notes of the Data Structure using C Lab in the subject of Data Structure using C. Here is some content that you can use for your notes:

### Implementation of Circular Queue using Array

- A circular queue is a linear data structure that follows the First In First Out (FIFO) principle.
- A circular queue can be implemented using an array of fixed size, say N.
- A circular queue has two pointers, front and rear, that indicate the position of the first and the last element in the queue respectively.
- Initially, both front and rear are set to -1, indicating that the queue is empty.
- To insert an element into the queue, we first check if the queue is full or not. The queue is full if (rear + 1) % N == front, where % is the modulo operator.
- If the queue is not full, we increment the rear pointer by one and wrap it around if it reaches the end of the array. Then we store the element at the rear position in the array.
- To delete an element from the queue, we first check if the queue is empty or not. The queue is empty if front == -1 or front == rear + 1.
- If the queue is not empty, we store the element at the front position in a variable and return it. Then we increment the front pointer by one and wrap it around if it reaches the end of the array.
- To display the elements of the queue, we start from the front pointer and traverse the array until we reach the rear pointer, wrapping around if necessary.

Here is an example of the implementation of circular queue using array in C:

```c
#include <stdio.h>
#define N 5 // size of the array

int queue[N]; // array to store the elements of the queue
int front = -1; // pointer to the front of the queue
int rear = -1; // pointer to the rear of the queue

// function to insert an element into the queue
void enqueue(int x) {
  // check if the queue is full
  if ((rear + 1) % N == front) {
    printf("Queue is full\n");
    return;
  }
  // increment the rear pointer and wrap it around if necessary
  rear = (rear + 1) % N;
  // store the element at the rear position in the array
  queue[rear] = x;
  // if the queue was empty, set the front pointer to the rear pointer
  if (front == -1) {
    front = rear;
  }
}

// function to delete an element from the queue
int dequeue() {
  // check if the queue is empty
  if (front == -1) {
    printf("Queue is empty\n");
    return -1;
  }
  // store the element at the front position in a variable
  int x = queue[front];
  // if the queue has only one element, set both pointers to -1
  if (front == rear) {
    front = -1;
    rear = -1;
  }
  // otherwise, increment the front pointer and wrap it around if necessary
  else {
    front = (front + 1) % N;
  }
  // return the deleted element
  return x;
}

// function to display the elements of the queue
void display() {
  // check if the queue is empty
  if (front == -1) {
    printf("Queue is empty\n");
    return;
  }
  // start from the front pointer and traverse the array until the rear pointer
  printf("Queue: ");
  int i = front;
  while (i != rear) {
    // print the element at the current position
    printf("%d ", queue[i]);
    // increment the current position and wrap it around if necessary
    i = (i + 1) % N;
  }
  // print the element at the rear position
  printf("%d\n", queue[rear]);
}

// main function to test the implementation
int main() {
  // insert some elements into the queue
  enqueue(10);
  enqueue(20);
  enqueue(30);
  enqueue(40);
  enqueue(50);
  // display the queue
  display();
  // delete some elements from the queue
  printf("Deleted: %d\n", dequeue());
  printf("Deleted: %d\n", dequeue());
  // display the queue
  display();
  // insert some more elements into the queue
  enqueue(60);
  enqueue(70);
  // display the queue
  display();