
### Implementation of Stack using Array

1. Stack is a linear data structure which follows a particular order in which the operations are performed. 
2. The order may be LIFO(Last In First Out) or FILO(First In Last Out). 
3. Stack is a collection of elements, with two principal operations: 
    * push, which adds an element to the collection, and 
    * pop, which removes the most recently added element that was not yet removed.
4. The implementation of a stack using an array is easy. 
5. The array has two parts: one part is used to store the elements of the stack and the other part is used to keep track of the top element of the stack.
6. The top element is the element that was added last.
7. The push operation adds an element to the top of the stack and increments the top index.
8. The pop operation removes the top element of the stack and decrements the top index.
9. In the implementation of stack using an array, the size of the array must be pre-defined.
10. If the stack is full, then the push operation will not be allowed.
11. Similarly, if the stack is empty, then the pop operation will not be allowed.