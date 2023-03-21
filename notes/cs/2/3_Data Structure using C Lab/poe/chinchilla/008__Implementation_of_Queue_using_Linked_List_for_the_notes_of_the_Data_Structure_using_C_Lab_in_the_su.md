### Implementation of Queue using Linked List

In the Lab of Data Structure using C, you will learn about the implementation of Queue using Linked List. Here are some key points that will help you understand the concept better:

- Queue is a data structure in which the first element added is the first element to be removed. It follows the First-In-First-Out (FIFO) principle.
- Linked List is a data structure that consists of a sequence of nodes, where each node contains a value and a pointer to the next node.
- To implement Queue using Linked List, we create a new node every time an element is added to the Queue. The new node is then added to the end of the Linked List.
- To remove an element from the Queue, we remove the first node from the Linked List. This node becomes the front of the Queue.
- We maintain two pointers, front and rear, to keep track of the front and the end of the Queue, respectively.
- Initially, both pointers point to NULL, which indicates that the Queue is empty.
- When the first element is added to the Queue, the front and the rear pointers both point to the new node.
- When an element is added to the Queue, we create a new node and set its value. We then set its next pointer to NULL and the next pointer of the previous node to the new node. Finally, we update the rear pointer to point to the new node.
- When an element is removed from the Queue, we set the front pointer to the next node and free the memory of the removed node.

Here is the C code to implement Queue using Linked List:

```c
#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node* next;
};

struct node* front = NULL;
struct node* rear = NULL;

void enqueue(int x) {
    struct node* newnode = (struct node*) malloc(sizeof(struct node));
    newnode->data = x;
    newnode->next = NULL;
    if (front == NULL && rear == NULL) {
        front = rear = newnode;
        return;
    }
    rear->next = newnode;
    rear = newnode;
}

void dequeue() {
    struct node* temp = front;
    if (front == NULL) {
        printf("Queue is empty\n");
        return;
    }
    if (front == rear) {
        front = rear = NULL;
    } else {
        front = front->next;
    }
    free(temp);
}

void display() {
    struct node* temp = front;
    if (front == NULL && rear == NULL) {
        printf("Queue is empty\n");
        return;
    }
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    enqueue(2);
    enqueue(4);
    enqueue(6);
    display();
    dequeue();
    display();
    return 0;
}
```

In conclusion, understanding the implementation of Queue using Linked List is essential for your understanding of the Data Structure using C Lab. Follow the above key points and the provided code to master this concept.