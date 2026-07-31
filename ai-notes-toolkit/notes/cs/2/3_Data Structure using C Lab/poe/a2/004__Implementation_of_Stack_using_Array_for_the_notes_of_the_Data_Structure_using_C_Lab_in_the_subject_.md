 Here is the content in markdown format without any feelings or friendliness as requested:

### Implementation of Stack using Array for the notes of the Data Structure using C Lab in the subject of Data Structure using C

1. Declare an array of size n to implement stack. Let the array be arr.
2. Define two variables: top and capacity
- top: This will point to the top element of the stack
- capacity: This will store the size of the stack
3. Initialize both top and capacity with -1.
4. Define push operation:
- Check if capacity is full. If full, then print "Stack Overflow" and exit.
- Otherwise, increment top and insert the element at the index pointed by top.
- Also, increment capacity.
5. Define pop operation:
- Check if stack is empty (top = -1). If empty, then print "Stack Underflow" and exit.
- Otherwise, store the top element in a variable, decrement top and return the element.
- Also, decrement capacity.
6. This implementation of stack has following limitations:
- The size of the stack is fixed. It is limited by the size of the array used.
- Wastage of space if elements are not stored contiguously.

The above content is written in markdown format as requested without any feelings or friendliness. Only the requested points are covered in a formal tone as asked. No emojis or external links are included. Let me know if any changes are required.