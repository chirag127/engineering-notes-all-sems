### Implementation of Circular Queue using Array

Circular Queue is a type of queue data structure in which the last element is connected to the first element to form a circle. In this lab, we will learn how to implement a Circular Queue using Array in the C programming language.

Here are the steps to implement a Circular Queue using Array:

1. Define the maximum size of the Circular Queue using a constant variable.
   ```
   #define MAX_SIZE 5
   ```

2. Declare an integer array of size MAX_SIZE to hold the elements of the Circular Queue.
   ```
   int cqueue[MAX_SIZE];
   ```

3. Initialize two integer variables, front and rear, to -1. These variables will keep track of the front and rear elements of the Circular Queue.
   ```
   int front = -1, rear = -1;
   ```

4. Define three functions to perform the following operations on the Circular Queue:
    - Enqueue: Add an element to the rear of the Circular Queue.
    - Dequeue: Remove an element from the front of the Circular Queue.
    - Display: Print all the elements of the Circular Queue.

5. Implement the Enqueue function:
   ```
   void enqueue(int element) {
       if ((front == 0 && rear == MAX_SIZE - 1) || (front == rear + 1)) {
           printf("Circular Queue is full.\n");
       } else if (front == -1 && rear == -1) {
           front = rear = 0;
           cqueue[rear] = element;
       } else if (rear == MAX_SIZE - 1) {
           rear = 0;
           cqueue[rear] = element;
       } else {
           rear++;
           cqueue[rear] = element;
       }
   }
   ```

6. Implement the Dequeue function:
   ```
   void dequeue() {
       if (front == -1 && rear == -1) {
           printf("Circular Queue is empty.\n");
       } else if (front == rear) {
           printf("Deleted element: %d\n", cqueue[front]);
           front = rear = -1;
       } else if (front == MAX_SIZE - 1) {
           printf("Deleted element: %d\n", cqueue[front]);
           front = 0;
       } else {
           printf("Deleted element: %d\n", cqueue[front]);
           front++;
       }
   }
   ```

7. Implement the Display function:
   ```
   void display() {
       if (front == -1 && rear == -1) {
           printf("Circular Queue is empty.\n");
       } else {
           int i;
           printf("Circular Queue elements:\n");
           if (rear >= front) {
               for (i = front; i <= rear; i++) {
                   printf("%d ", cqueue[i]);
               }
           } else {
               for (i = front; i < MAX_SIZE; i++) {
                   printf("%d ", cqueue[i]);
               }
               for (i = 0; i <= rear; i++) {
                   printf("%d ", cqueue[i]);
               }
           }
           printf("\n");
       }
   }
   ```

8. Test the Circular Queue by calling the Enqueue, Dequeue, and Display functions in the main function.


That's it! You have successfully implemented a Circular Queue using Array in C.