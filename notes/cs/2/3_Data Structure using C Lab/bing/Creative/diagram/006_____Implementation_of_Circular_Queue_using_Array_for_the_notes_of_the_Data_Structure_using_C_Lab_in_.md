### Implementation of Circular Queue using Array

A circular queue is a type of queue that uses an array to store the elements. Unlike a normal queue, where the front and rear pointers move linearly, a circular queue allows the rear pointer to wrap around to the beginning of the array when it reaches the end. This way, the queue can utilize the empty spaces left by the deleted elements.

The main advantage of a circular queue is that it avoids the wastage of space that occurs in a normal queue. The main disadvantage is that it has a fixed size and cannot grow dynamically.

The following are the steps to implement a circular queue using an array in C:

- Declare an array of size n, where n is the maximum number of elements that the queue can hold. This array will be used to store the queue elements.
- Declare two variables front and rear to keep track of the front and rear positions of the queue. Initialize them to -1, indicating that the queue is empty.
- To enqueue an element x onto the queue, do the following:
  - Increment rear by 1. If rear is equal to n, set rear to 0. This ensures that the rear pointer wraps around to the beginning of the array when it reaches the end.
  - If front is -1, set front to 0. This indicates that the queue is no longer empty.
  - Check if front is equal to rear. If yes, then the queue is full and cannot insert any more elements. Display an overflow message and return.
  - Otherwise, store x at the rear position of the array.
- To dequeue an element from the queue, do the following:
  - Check if front is -1. If yes, then the queue is empty and cannot delete any elements. Display an underflow message and return.
  - Otherwise, store the element at the front position of the array in a variable and return it.
  - Increment front by 1. If front is equal to n, set front to 0. This ensures that the front pointer wraps around to the beginning of the array when it reaches the end.
  - Check if front is equal to rear + 1. If yes, then the queue is empty and set front and rear to -1.

The following is a diagram that illustrates the circular queue using an array:

```
  0   1   2   3   4   5   6   7
+---+---+---+---+---+---+---+---+
| 5 | 6 | 7 |   |   | 1 | 2 | 3 |  <- queue elements
+---+---+---+---+---+---+---+---+
  ^               ^   ^
  |               |   |
 rear            front |
                      rear + 1
```

In this example, the queue has a size of 8 and can hold up to 7 elements. The front pointer is at index 5 and the rear pointer is at index 1. The queue contains 5 elements: 1, 2, 3, 5, and 6. The empty spaces are at indexes 3 and 4. The rear pointer has wrapped around to the beginning of the array after inserting 3. The front pointer has wrapped around to the beginning of the array after deleting 4 and 7. The queue is not full and not empty.