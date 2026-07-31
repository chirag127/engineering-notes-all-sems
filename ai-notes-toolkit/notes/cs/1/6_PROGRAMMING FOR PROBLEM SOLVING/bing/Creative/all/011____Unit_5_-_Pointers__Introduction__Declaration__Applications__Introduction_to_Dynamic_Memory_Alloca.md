# Unit 5 - Pointers: Introduction, Declaration, Applications, Introduction to Dynamic Memory Allocation (Malloc, Calloc, Realloc, Free), String and String functions , Use of Pointers in Self-Referential Structures, Notion of Linked List (No Implementation)

## Introduction to Pointers
- A pointer is a variable that stores the address of another variable in memory.
- Pointers allow us to access and manipulate the data stored at a specific memory location using indirection operator (*).
- Pointers can also be used to pass data by reference to functions, create dynamic data structures, and implement low-level operations.

## Declaration of Pointers
- To declare a pointer, we need to specify the data type of the variable that it points to, followed by an asterisk (*) and the pointer name.
- For example, `int *p;` declares a pointer named `p` that can point to an integer variable.
- To assign the address of a variable to a pointer, we use the address-of operator (&) before the variable name.
- For example, `p = &x;` assigns the address of the variable `x` to the pointer `p`.
- To access the value stored at the address pointed by a pointer, we use the indirection operator (*) before the pointer name.
- For example, `*p` returns the value of the variable `x` that `p` points to.

## Applications of Pointers
- Pointers can be used for various purposes, such as:
  - Passing data by reference: Pointers allow us to pass the address of a variable to a function, instead of passing a copy of its value. This way, the function can modify the original variable without returning it.
  - Creating dynamic data structures: Pointers allow us to allocate memory dynamically at run time, and create data structures that can grow or shrink as needed, such as linked lists, trees, graphs, etc.
  - Implementing low-level operations: Pointers allow us to access and manipulate the memory directly, and perform operations that are not possible with normal variables, such as pointer arithmetic, casting, etc.

## Introduction to Dynamic Memory Allocation
- Dynamic memory allocation is the process of allocating and deallocating memory at run time, as per the program's requirements.
- Dynamic memory allocation allows us to create data structures that are not fixed in size or type, and can be modified during the program execution.
- Dynamic memory allocation is done using four functions in C: `malloc`, `calloc`, `realloc`, and `free`.
- `malloc` is a function that allocates a block of memory of a given size in bytes, and returns a pointer to the beginning of the block. The memory is not initialized, and may contain garbage values.
- `calloc` is a function that allocates a block of memory for an array of a given number of elements, each of a given size in bytes, and returns a pointer to the beginning of the block. The memory is initialized to zero.
- `realloc` is a function that changes the size of a previously allocated block of memory, and returns a pointer to the new block. The contents of the old block are copied to the new block, and the old block is freed. The memory may not be contiguous, and may contain garbage values.
- `free` is a function that deallocates a previously allocated block of memory, and returns the memory to the system. The pointer to the block becomes invalid, and should not be used again.

## String and String functions
- A string is a sequence of characters terminated by a null character ('\0').
- A string can be declared as an array of characters, or as a pointer to a character.
- For example, `char str[10] = "Hello";` or `char *str = "Hello";` declare a string of 5 characters and a null character.
- C provides various functions to manipulate strings, such as:
  - `strlen` is a function that returns the length of a string, excluding the null character.
  - `strcpy` is a function that copies a string from one array to another.
  - `strcat` is a function that concatenates two strings, and appends the second string to the end of the first string.
  - `strcmp` is a function that compares two strings lexicographically, and returns a positive, negative, or zero value depending on whether the first string is greater than, less than, or equal to the second string.
  - `strchr` is a function that returns a pointer to the first occurrence of a given character in a string, or NULL if the character is not found.
  - `strstr` is a function that returns a pointer to the first occurrence of a given substring in a string