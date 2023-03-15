### Implementation of Queue using Array

- A queue is a linear data structure that follows the **FIFO** (First In First Out) principle, meaning that the element that is inserted first is removed first.
- A queue can be implemented using an array by maintaining two variables: **front** and **rear**. The front variable points to the index of the first element in the queue, and the rear variable points to the index of the last element in the queue.
- To insert an element into the queue, we need to check if the queue is full or not. If the queue is full, we cannot insert any more elements and we display an error message. If the queue is not full, we increment the rear variable by one and store the element at the rear index of the array.
- To delete an element from the queue, we need to check if the queue is empty or not. If the queue is empty, we cannot delete any element and we display an error message. If the queue is not empty, we store the element at the front index of the array in a temporary variable, and then increment the front variable by one. We return the temporary variable as the deleted element.
- To display the elements of the queue, we need to iterate from the front index to the rear index of the array and print the elements.

- The following diagram shows an example of a queue implemented using an array of size 5:

```
| 10 | 20 | 30 | 40 | 50 |
  ^    ^              ^
  |    |              |
front  |            rear
       |
    deleted element
```

- In this example, the front variable is 1 and the rear variable is 4. The queue is not empty and not full. The element 10 is deleted from the queue and returned. The front variable is incremented to 2. The element 60 is inserted into the queue at the rear index of the array. The rear variable is incremented to 5. The queue is now full.

```
| 10 | 20 | 30 | 40 | 50 | 60 |
       ^                   ^
       |                   |
     front               rear
```

- The following is a sample C program that implements a queue using an array:

```c
#include <stdio.h>
#define MAX 5 // maximum size of the array

int queue[MAX]; // array to store the queue elements
int front = -1; // variable to point to the front of the queue
int rear = -1; // variable to point to the rear of the queue

// function to check if the queue is empty
int isEmpty() {
  if (front == -1 || front > rear) {
    return 1; // queue is empty
  }
  else {
    return 0; // queue is not empty
  }
}

// function to check if the queue is full
int isFull() {
  if (rear == MAX - 1) {
    return 1; // queue is full
  }
  else {
    return 0; // queue is not full
  }
}

// function to insert an element into the queue
void enqueue(int x) {
  if (isFull()) {
    printf("Queue is full. Cannot insert %d.\n", x);
  }
  else {
    if (front == -1) {
      front = 0; // initialize front to 0 if queue is empty
    }
    rear++; // increment rear by 1
    queue[rear] = x; // store the element at the rear index of the array
    printf("%d is inserted into the queue.\n", x);
  }
}

// function to delete an element from the queue
int dequeue() {
  int x;
  if (isEmpty()) {
    printf("Queue is empty. Cannot delete.\n");
    return -1; // return -1 as an error value
  }
  else {
    x = queue[front]; // store the element at the front index of the array in a temporary variable
    front++; // increment front by 1
    printf("%d is deleted from the queue.\n", x);
    return x; // return the deleted element
  }
}

// function to display the elements of the queue
void display() {
  int i;
  if (isEmpty()) {
    printf("Queue is empty. Nothing to display.\n");
  }
  else {
    printf("The elements of the queue are:\n");
    for (i = front; i <= rear; i++) {
      printf("%d ", queue[i]); // print the element at the current index of the array
    }
    printf("\n");
  }
}

// main