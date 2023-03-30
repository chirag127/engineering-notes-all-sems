
### Implementation of Simple Stack Allocation Scheme for Unit 4 - Symbol Tables in Compiler Design

1. Stack allocation is a memory management system used in compiler design that allocates memory to the variables used in a program. 
2. It uses a stack data structure to store the variables and their associated values. 
3. The stack is organized into frames, which are allocated and deallocated as needed. 
4. The frames contain the variables and their values, as well as any other data needed to execute the program, such as function parameters and return addresses. 
5. When a function is called, a new frame is allocated on the stack and the variables and values associated with that frame are stored in it. 
6. When the function returns, the frame is deallocated and the values are no longer accessible. 
7. Stack allocation is a simple and efficient way to manage memory, as it eliminates the need to manually allocate and deallocate memory. 
8. It is also easy to debug, as the frames can be easily inspected to see what variables are in scope and what values they contain. 
9. However, stack allocation can lead to stack overflow if the size of the stack exceeds the amount of memory available.