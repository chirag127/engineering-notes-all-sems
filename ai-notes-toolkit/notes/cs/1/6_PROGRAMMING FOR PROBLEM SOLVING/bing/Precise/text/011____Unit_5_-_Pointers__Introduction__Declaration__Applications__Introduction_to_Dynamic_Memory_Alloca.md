## Unit 5 - Pointers: Introduction, Declaration, Applications, Introduction to Dynamic Memory Allocation (Malloc, Calloc, Realloc, Free), String and String functions , Use of Pointers in Self-Referential Structures, Notion of Linked List (No Implementation)

1. **Introduction to Pointers**: A pointer is a variable that stores the memory address of another variable. Pointers are used to indirectly access the value of a variable through its memory address.

2. **Declaration of Pointers**: Pointers are declared using the `*` symbol. For example, to declare a pointer to an integer variable, the syntax would be `int *ptr;`.

3. **Applications of Pointers**: Pointers have many applications in programming, including:
    - Accessing and modifying the value of a variable indirectly
    - Passing arguments to functions by reference
    - Dynamic memory allocation
    - Creating and manipulating complex data structures such as linked lists and trees

4. **Introduction to Dynamic Memory Allocation**: Dynamic memory allocation refers to the process of allocating memory during runtime. This is done using functions such as `malloc`, `calloc`, `realloc`, and `free`.

5. **Malloc**: `malloc` is a function that allocates a block of memory of a specified size and returns a pointer to the first byte of the allocated memory.

6. **Calloc**: `calloc` is similar to `malloc`, but it also initializes the allocated memory to zero.

7. **Realloc**: `realloc` is used to change the size of a previously allocated block of memory.

8. **Free**: `free` is used to deallocate memory that was previously allocated using `malloc`, `calloc`, or `realloc`.

9. **String and String functions**: A string is an array of characters. String functions are used to manipulate strings, such as finding the length of a string, concatenating two strings, or comparing two strings.

10. **Use of Pointers in Self-Referential Structures**: Self-referential structures are data structures that contain a pointer to an instance of the same data structure. Pointers are used to link the instances together, forming complex data structures such as linked lists and trees.

11. **Notion of Linked List**: A linked list is a data structure that consists of a sequence of nodes, each containing data and a pointer to the next node in the list. The first node is called the head, and the last node is called the tail. Linked lists can be used to implement various data structures such as stacks, queues, and associative arrays.