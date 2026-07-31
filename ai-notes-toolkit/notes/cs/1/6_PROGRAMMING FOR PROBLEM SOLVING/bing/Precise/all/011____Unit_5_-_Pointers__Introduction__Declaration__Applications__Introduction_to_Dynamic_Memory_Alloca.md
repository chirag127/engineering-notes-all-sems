## Unit 5 - Pointers

### Introduction
- A pointer is a variable that stores the memory address of another variable.
- Pointers allow for dynamic memory allocation and deallocation, and can be used to manipulate data in a more flexible and efficient manner.

### Declaration
- Pointers are declared using the `*` symbol, for example: `int *p;`
- The `*` symbol is used to dereference the pointer, i.e., to access the value stored at the memory address pointed to by the pointer.

### Applications
- Pointers can be used to pass variables by reference to functions, allowing the function to modify the value of the variable.
- Pointers can be used to create and manipulate dynamic data structures such as linked lists, trees, and graphs.
- Pointers can be used to improve the efficiency of certain algorithms by reducing the amount of data that needs to be copied.

### Introduction to Dynamic Memory Allocation
- Dynamic memory allocation refers to the process of allocating and deallocating memory at runtime.
- The functions `malloc`, `calloc`, `realloc`, and `free` are used to perform dynamic memory allocation in C.
- `malloc` is used to allocate a block of memory of a specified size.
- `calloc` is similar to `malloc`, but it also initializes the allocated memory to zero.
- `realloc` is used to resize a previously allocated block of memory.
- `free` is used to deallocate a previously allocated block of memory.

### String and String functions
- A string is an array of characters terminated by a null character (`\0`).
- Common string functions include `strlen`, `strcpy`, `strcat`, `strcmp`, and `strchr`.
- `strlen` returns the length of a string (not including the null terminator).
- `strcpy` copies a string from one location to another.
- `strcat` concatenates two strings.
- `strcmp` compares two strings and returns 0 if they are equal, a positive value if the first string is greater, and a negative value if the second string is greater.
- `strchr` returns a pointer to the first occurrence of a character in a string.

### Use of Pointers in Self-Referential Structures
- A self-referential structure is a data structure that contains a pointer to an instance of the same data structure.
- Linked lists, trees, and graphs are examples of self-referential structures.
- Pointers are used to link the nodes of the data structure together.

### Notion of Linked List
- A linked list is a data structure consisting of a sequence of nodes, each containing data and a pointer to the next node in the sequence.
- Linked lists can be used to implement stacks, queues, and other data structures.
- Linked lists allow for efficient insertion and deletion of elements, but do not provide constant-time access to individual elements.