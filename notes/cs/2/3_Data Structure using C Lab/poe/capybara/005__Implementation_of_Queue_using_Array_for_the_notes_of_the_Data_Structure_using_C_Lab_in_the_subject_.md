### Implementation of Queue using Array

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. It means that the element that enters the queue first will leave the queue first. The implementation of the queue can be done using an array.

Here are the steps to implement a queue using an array in C:

1. Declare an array of a fixed size that will act as a queue.

2. Initialize two variables, `front` and `rear`. `front` will point to the first element in the queue, and `rear` will point to the last element in the queue. Initially, set both the variables to -1.

3. Define the `enqueue()` function to insert elements into the queue. The function will take an element as a parameter and increment the value of `rear` by 1. Then, it will insert the element at the `rear` index of the array.

4. Define the `dequeue()` function to remove elements from the queue. The function will remove the element at the `front` index of the array and increment the value of `front` by 1.

5. Define the `isEmpty()` function to check if the queue is empty. It will return 1 if the queue is empty, and 0 if it is not empty.

6. Define the `isFull()` function to check if the queue is full. It will return 1 if the queue is full, and 0 if it is not full.

7. Define the `display()` function to display all the elements in the queue.

Here is the implementation of the queue using an array in C:

```c
#include<stdio.h>
#define MAX_SIZE 5

int queue[MAX_SIZE];
int front = -1, rear = -1;

void enqueue(int element){
    if(rear == MAX_SIZE-1){
        printf("Queue is full.\n");
    }
    else{
        rear++;
        queue[rear] = element;
    }
}

void dequeue(){
    if(front == rear){
        printf("Queue is empty.\n");
    }
    else{
        front++;
        printf("The dequeued element is %d.\n", queue[front]);
    }
}

int isEmpty(){
    if(front == rear){
        return 1;
    }
    else{
        return 0;
    }
}

int isFull(){
    if(rear == MAX_SIZE-1){
        return 1;
    }
    else{
        return 0;
    }
}

void display(){
    if(front == rear){
        printf("Queue is empty.\n");
    }
    else{
        printf("The elements in the queue are:\n");
        for(int i=front+1; i<=rear; i++){
            printf("%d\n", queue[i]);
        }
    }
}

int main(){
    enqueue(10);
    enqueue(20);
    enqueue(30);
    display();
    dequeue();
    display();
    return 0;
}
```

In this implementation, the `MAX_SIZE` macro is used to define the maximum size of the queue. The `enqueue()` function inserts elements into the queue, the `dequeue()` function removes elements from the queue, the `isEmpty()` function checks if the queue is empty, the `isFull()` function checks if the queue is full, and the `display()` function displays all the elements in the queue. The `main()` function is used to test the implementation.

In conclusion, the implementation of the queue using an array is a simple and efficient way to implement a queue in C. By following the above steps and implementing the necessary functions, one can easily create a queue using an array.