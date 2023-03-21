### Implementation of Circular Queue using Linked List

Circular Queue is a data structure that follows the FIFO (First In First Out) principle. It is similar to a regular queue, but the last element is connected to the first element to form a circular structure. In this lab, we will be implementing a Circular Queue using Linked List in the C programming language.

#### Linked List Implementation of Circular Queue

1. Define a structure for the Circular Queue node that contains two members: data and a pointer to the next node.

   ```c
   struct node {
       int data;
       struct node *next;
   };
   ```

2. Define a structure for the Circular Queue that contains two members: front and rear.

   ```c
   struct queue {
       struct node *front;
       struct node *rear;
   };
   ```

3. Initialize the Circular Queue by setting both front and rear to NULL.

   ```c
   struct queue *q;
   q->front = NULL;
   q->rear = NULL;
   ```

4. Implement the enqueue operation to insert an element at the rear of the Circular Queue.

   ```c
   void enqueue(struct queue *q, int data) {
       struct node *new_node = (struct node*)malloc(sizeof(struct node));
       new_node->data = data;
       new_node->next = NULL;
       if (q->front == NULL) {
           q->front = new_node;
       } else {
           q->rear->next = new_node;
       }
       q->rear = new_node;
       q->rear->next = q->front;
   }
   ```

5. Implement the dequeue operation to remove an element from the front of the Circular Queue.

   ```c
   int dequeue(struct queue *q) {
       if (q->front == NULL) {
           printf("Circular Queue is empty!\n");
           return -1;
       }
       int data = q->front->data;
       struct node *temp = q->front;
       if (q->front == q->rear) {
           q->front = NULL;
           q->rear = NULL;
       } else {
           q->front = q->front->next;
           q->rear->next = q->front;
       }
       free(temp);
       return data;
   }
   ```

6. Implement the display operation to print all the elements in the Circular Queue.

   ```c
   void display(struct queue *q) {
       if (q->front == NULL) {
           printf("Circular Queue is empty!\n");
           return;
       }
       struct node *temp = q->front;
       printf("Circular Queue: ");
       do {
           printf("%d ", temp->data);
           temp = temp->next;
       } while (temp != q->front);
       printf("\n");
   }
   ```

7. Test the Circular Queue implementation by calling the enqueue, dequeue, and display operations.

   ```c
   int main() {
       struct queue q;
       q.front = NULL;
       q.rear = NULL;
       enqueue(&q, 10);
       enqueue(&q, 20);
       enqueue(&q, 30);
       display(&q);
       printf("Dequeued element: %d\n", dequeue(&q));
       display(&q);
       return 0;
   }
   ```

   Output:
   ```
   Circular Queue: 10 20 30
   Dequeued element: 10
   Circular Queue: 20 30
   ```

#### Conclusion

In this lab, we have learned how to implement a Circular Queue using Linked List in the C programming language. Circular Queue is a useful data structure for applications that require data to be processed in a circular manner. By implementing a Circular Queue using Linked List, we can efficiently insert and remove elements from the queue without having to shift the entire queue.