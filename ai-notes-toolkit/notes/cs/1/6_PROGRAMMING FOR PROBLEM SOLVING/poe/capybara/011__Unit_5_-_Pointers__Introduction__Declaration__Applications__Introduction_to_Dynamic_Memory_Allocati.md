## Unit 5 - Pointers: Introduction, Declaration, Applications, Introduction to Dynamic Memory Allocation (Malloc, Calloc, Realloc, Free), String and String functions , Use of Pointers in Self-Referential Structures, Notion of Linked List (No Implementation)

In this unit, we will cover the following topics related to pointers:

- Introduction to Pointers
- Declaration of Pointers
- Applications of Pointers
- Dynamic Memory Allocation
- String and String Functions
- Use of Pointers in Self-Referential Structures
- Notion of Linked List

### Introduction to Pointers

- A pointer is a variable that stores the memory address of another variable.
- Pointers are used to manipulate memory and to access data stored in memory.
- Pointers are useful for passing large data structures to functions efficiently.
- Pointers are also used to implement dynamic data structures such as linked lists and trees.

### Declaration of Pointers

- Pointers are declared using the * operator.
- The * operator is called the dereference operator when used to access the value stored at the address pointed to by a pointer.
- Pointers must be initialized before they can be used.
- Pointers can be assigned the address of another variable using the & operator.

### Applications of Pointers

- Pointers can be used to dynamically allocate memory.
- Pointers are used to implement data structures such as linked lists and trees.
- Pointers can be used to pass large data structures to functions efficiently.
- Pointers can be used to access hardware registers and memory-mapped I/O.

### Dynamic Memory Allocation

- Dynamic memory allocation allows programs to request memory from the operating system at runtime.
- There are four functions used for dynamic memory allocation: malloc, calloc, realloc, and free.
- malloc is used to allocate memory.
- calloc is used to allocate memory and initialize it to zero.
- realloc is used to change the size of a previously allocated block of memory.
- free is used to release previously allocated memory.

### String and String Functions

- In C, a string is a sequence of characters terminated by a null character (\0).
- Strings can be manipulated using functions such as strcpy, strcat, and strlen.
- Pointers are commonly used to manipulate strings.

### Use of Pointers in Self-Referential Structures

- Pointers can be used to implement self-referential structures.
- A self-referential structure is a structure that contains a pointer to another instance of the same structure type.
- Self-referential structures are used to implement linked lists, trees, and other dynamic data structures.

### Notion of Linked List

- A linked list is a dynamic data structure that consists of a sequence of nodes, each containing data and a pointer to the next node.
- Linked lists can be used to implement stacks, queues, and other data structures.
- The advantage of linked lists is that they can be dynamically resized, unlike arrays which have a fixed size.