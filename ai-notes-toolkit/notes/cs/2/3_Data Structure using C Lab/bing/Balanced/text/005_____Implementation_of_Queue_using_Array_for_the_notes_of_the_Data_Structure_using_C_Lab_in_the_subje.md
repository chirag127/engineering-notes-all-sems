### Implementation of Queue using Array

- A queue is a linear data structure that follows the First In First Out (FIFO) principle, meaning that the element that is inserted first is removed first.
- A queue can be implemented using an array by maintaining two variables: front and rear, that point to the first and last element of the queue respectively.
- To insert an element into the queue, we check if the queue is full by comparing the rear index with the size of the array. If the queue is full, we display an error message. Otherwise, we increment the rear index by one and store the element at that position in the array.
- To delete an element from the queue, we check if the queue is empty by comparing the front index with the rear index. If the queue is empty, we display an error message. Otherwise, we return the element at the front index and increment the front index by one.
- To display the elements of the queue, we use a loop to traverse the array from the front index to the rear index and print each element.
- The following is an example of a C program that implements a queue using an array:

```c
#include <stdio.h>
#define MAX 10 // maximum size of the array

int queue[MAX]; // array to store the queue elements
int front = -1; // index of the first element of the queue
int rear = -1; // index of the last element of the queue

// function to insert an element into the queue
void enqueue(int x) {
  if (rear == MAX - 1) { // check if the queue is full
    printf("Queue is full\n");
  } else {
    if (front == -1) { // check if the queue is empty
      front = 0; // set the front index to 0
    }
    rear++; // increment the rear index by 1
    queue[rear] = x; // store the element at the rear index
    printf("Inserted %d\n", x);
  }
}

// function to delete an element from the queue
int dequeue() {
  int x;
  if (front == -1 || front > rear) { // check if the queue is empty
    printf("Queue is empty\n");
    return -1;
  } else {
    x = queue[front]; // get the element at the front index
    front++; // increment the front index by 1
    printf("Deleted %d\n", x);
    return x;
  }
}

// function to display the elements of the queue
void display() {
  int i;
  if (front == -1 || front > rear) { // check if the queue is empty
    printf("Queue is empty\n");
  } else {
    printf("Queue elements are:\n");
    for (i = front; i <= rear; i++) { // loop from the front index to the rear index
      printf("%d ", queue[i]); // print the element at the current index
    }
    printf("\n");
  }
}

// main function to test the queue operations
int main() {
  int choice, x;
  while (1) {
    printf("1. Enqueue\n");
    printf("2. Dequeue\n");
    printf("3. Display\n");
    printf("4. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);
    switch (choice) {
      case 1:
        printf("Enter the element to be inserted: ");
        scanf("%d", &x);
        enqueue(x); // call the enqueue function
        break;
      case 2:
        x = dequeue(); // call the dequeue function
        break;
      case 3:
        display(); // call the display function
        break;
      case 4:
        return 0; // exit the program
      default:
        printf("Invalid choice\n");
    }
  }
  return 0;
}
```