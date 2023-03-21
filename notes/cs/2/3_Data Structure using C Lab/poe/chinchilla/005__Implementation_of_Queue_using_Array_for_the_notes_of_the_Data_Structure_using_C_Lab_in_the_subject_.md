### Implementation of Queue using Array

In this lab, we will learn about the implementation of Queue using Array in the subject of Data Structure using C. Queue is a linear data structure that follows the FIFO (First-In-First-Out) principle. It is similar to a queue in real life, where the person who arrives first gets served first. In Queue, the insertion of elements takes place at the rear end, also called the tail, and deletion of elements from the front end, also called the head.

#### Why do we need Queue?

Queue is widely used in programming and computer science. Some of the applications of Queue are:

- Job scheduling
- CPU task scheduling 
- Traffic management
- Printer spooling
- Breadth-first search algorithm in Graph Theory

#### Implementation of Queue using Array

The implementation of Queue using Array involves the following operations:

- `enqueue():` Adds an element to the rear end of the Queue.
- `dequeue():` Removes an element from the front end of the Queue.
- `isFull():` Checks whether the Queue is full or not.
- `isEmpty():` Checks whether the Queue is empty or not.
- `front():` Returns the element at the front end of the Queue.
- `rear():` Returns the element at the rear end of the Queue.

To implement Queue using Array, we need to declare an array of a fixed size and two pointers, `front` and `rear`, pointing to the front and rear end of the Queue, respectively. Initially, both pointers are set to -1 to indicate that the Queue is empty.

The following steps are involved in implementing Queue using Array:

1. Declare an array of a fixed size, say `queue[]`.
2. Declare two pointers, `front` and `rear`, and initialize them to -1.
3. Implement the `enqueue()` function as follows:
   - If the Queue is full, display an error message.
   - If the Queue is empty, increment both `front` and `rear` pointers and add the element to the `queue[]`.
   - If the Queue is not empty, increment the `rear` pointer and add the element to the `queue[]`.
4. Implement the `dequeue()` function as follows:
   - If the Queue is empty, display an error message.
   - If the Queue is not empty, remove the element from the `queue[]` pointed by `front` and increment the `front` pointer.
5. Implement the `isFull()` function as follows:
   - If the `rear` pointer is equal to the size of the `queue[]`, return `true`.
   - Otherwise, return `false`.
6. Implement the `isEmpty()` function as follows:
   - If both `front` and `rear` pointers are -1, return `true`.
   - Otherwise, return `false`.
7. Implement the `front()` function as follows:
   - If the Queue is empty, display an error message.
   - Otherwise, return the element pointed by `front` in the `queue[]`.
8. Implement the `rear()` function as follows:
   - If the Queue is empty, display an error message.
   - Otherwise, return the element pointed by `rear` in the `queue[]`.

#### Conclusion

In conclusion, Queue is a crucial data structure used in various applications. The implementation of Queue using Array can be done with the help of the above steps. It is essential to understand the concept of Queue and its implementation in programming to develop efficient algorithms.