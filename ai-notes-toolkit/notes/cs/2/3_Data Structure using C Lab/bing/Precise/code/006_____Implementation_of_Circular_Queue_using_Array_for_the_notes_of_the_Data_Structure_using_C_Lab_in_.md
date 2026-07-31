### Implementation of Circular Queue using Array

A circular queue is a linear data structure that follows the First In First Out (FIFO) principle. The difference between a linear queue and a circular queue is that in a circular queue, the last position is connected to the first position, forming a circle.

Here are the steps to implement a circular queue using an array in the C programming language:

1. **Define the maximum size of the queue:** Define a constant variable to represent the maximum size of the queue.

```c
#define MAX_SIZE 5
```

2. **Declare the queue:** Declare an array to represent the queue and two variables to represent the front and rear of the queue.

```c
int queue[MAX_SIZE];
int front = -1;
int rear = -1;
```

3. **Enqueue operation:** To insert an element into the queue, first check if the queue is full. If the queue is full, display an error message. Otherwise, increment the rear variable and insert the element at the rear of the queue. If this is the first element being inserted, set the front variable to 0.

```c
void enqueue(int element) {
    if ((rear + 1) % MAX_SIZE == front) {
        printf("Queue is full\n");
    } else {
        rear = (rear + 1) % MAX_SIZE;
        queue[rear] = element;
        if (front == -1) {
            front = 0;
        }
    }
}
```

4. **Dequeue operation:** To remove an element from the queue, first check if the queue is empty. If the queue is empty, display an error message. Otherwise, remove the element at the front of the queue and increment the front variable. If the front and rear variables are equal after the increment, set them both to -1 to indicate that the queue is empty.

```c
int dequeue() {
    if (front == -1) {
        printf("Queue is empty\n");
        return -1;
    } else {
        int element = queue[front];
        if (front == rear) {
            front = -1;
            rear = -1;
        } else {
            front = (front + 1) % MAX_SIZE;
        }
        return element;
    }
}
```

5. **Display operation:** To display the elements in the queue, start from the front of the queue and move towards the rear, printing each element.

```c
void display() {
    if (front == -1) {
        printf("Queue is empty\n");
    } else {
        int i;
        for (i = front; i != rear; i = (i + 1) % MAX_SIZE) {
            printf("%d ", queue[i]);
        }
        printf("%d\n", queue[rear]);
    }
}
```

This is a basic implementation of a circular queue using an array in the C programming language. It can be further modified and improved according to the specific needs of the user.