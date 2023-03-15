## Unit 5 - Pointers

### Introduction
- A pointer is a variable that stores the memory address of another variable.
- Pointers allow for dynamic memory allocation and deallocation, as well as the ability to manipulate data in memory.

### Declaration
- Pointers are declared using the `*` symbol.
- The syntax for declaring a pointer is `data_type *pointer_name;`
- For example, to declare a pointer to an integer, the syntax would be `int *p;`

### Applications
- Pointers have many applications, including:
  - Dynamic memory allocation and deallocation
  - Manipulating data in memory
  - Passing arguments to functions by reference
  - Creating and manipulating complex data structures such as linked lists and trees

### Introduction to Dynamic Memory Allocation
- Dynamic memory allocation refers to the process of allocating and deallocating memory at runtime.
- In C, dynamic memory allocation is achieved using the `malloc`, `calloc`, `realloc`, and `free` functions.

#### Malloc
- `malloc` stands for "memory allocation".
- It is used to allocate a block of memory of a specified size.
- The syntax for `malloc` is `void *malloc(size_t size);`
- `malloc` returns a pointer to the allocated memory, or `NULL` if the allocation fails.

#### Calloc
- `calloc` stands for "clear allocation".
- It is similar to `malloc`, but it initializes the allocated memory to zero.
- The syntax for `calloc` is `void *calloc(size_t nmemb, size_t size);`
- `calloc` returns a pointer to the allocated memory, or `NULL` if the allocation fails.

#### Realloc
- `realloc` stands for "reallocate".
- It is used to change the size of a previously allocated block of memory.
- The syntax for `realloc` is `void *realloc(void *ptr, size_t size);`
- `realloc` returns a pointer to the newly allocated memory, or `NULL` if the reallocation fails.

#### Free
- `free` is used to deallocate memory that was previously allocated using `malloc`, `calloc`, or `realloc`.
- The syntax for `free` is `void free(void *ptr);`
- `free` does not return a value.

### String and String functions
- A string is an array of characters terminated by a null character (`'\0'`).
- C provides several functions for manipulating strings, including:
  - `strlen` - returns the length of a string
  - `strcpy` - copies one string to another
  - `strcat` - concatenates two strings
  - `strcmp` - compares two strings
  - `strchr` - finds the first occurrence of a character in a string
  - `strstr` - finds the first occurrence of a substring in a string

### Use of Pointers in Self-Referential Structures
- A self-referential structure is a data structure that contains a pointer to an instance of the same data structure.
- Pointers are used in self-referential structures to create complex data structures such as linked lists and trees.

### Notion of Linked List
- A linked list is a data structure that consists of a sequence of nodes, each containing data and a pointer to the next node in the list.
- Linked lists can be used to implement various data structures such as stacks, queues, and associative arrays.
- The implementation of linked lists is not covered in this unit.