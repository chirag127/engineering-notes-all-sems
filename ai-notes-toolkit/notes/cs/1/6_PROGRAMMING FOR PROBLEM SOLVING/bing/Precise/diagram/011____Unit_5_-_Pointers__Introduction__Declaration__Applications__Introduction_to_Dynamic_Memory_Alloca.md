## Unit 5 - Pointers

### Introduction
- A pointer is a variable that stores the memory address of another variable.
- Pointers allow for indirect access to the value of a variable.
- The `&` operator is used to obtain the memory address of a variable.
- The `*` operator is used to access the value stored at a memory address.

### Declaration
- Pointers are declared using the `*` operator.
- The syntax for declaring a pointer is `data_type *pointer_name;`.
- For example, to declare a pointer to an integer, the syntax would be `int *p;`.

### Applications
- Pointers can be used to pass variables by reference to functions.
- Pointers can be used to dynamically allocate memory.
- Pointers can be used to create and manipulate complex data structures such as linked lists and trees.

### Introduction to Dynamic Memory Allocation
- Dynamic memory allocation allows for the allocation of memory at runtime.
- The `malloc`, `calloc`, `realloc`, and `free` functions are used for dynamic memory allocation.
- `malloc` allocates a block of memory of a specified size.
- `calloc` allocates a block of memory for an array of a specified number of elements, each of a specified size, and initializes all bytes to zero.
- `realloc` changes the size of a previously allocated block of memory.
- `free` deallocates a previously allocated block of memory.

### String and String functions
- A string is an array of characters.
- The `string.h` header file contains several functions for manipulating strings.
- Some common string functions include `strlen`, `strcpy`, `strcat`, and `strcmp`.

### Use of Pointers in Self-Referential Structures
- A self-referential structure is a structure that contains a pointer to an instance of the same structure type.
- Self-referential structures are commonly used to implement linked lists and trees.

### Notion of Linked List
- A linked list is a data structure that consists of a sequence of nodes, each containing data and a pointer to the next node in the list.
- Linked lists allow for efficient insertion and deletion of elements.
- The implementation of a linked list is not covered in this unit.