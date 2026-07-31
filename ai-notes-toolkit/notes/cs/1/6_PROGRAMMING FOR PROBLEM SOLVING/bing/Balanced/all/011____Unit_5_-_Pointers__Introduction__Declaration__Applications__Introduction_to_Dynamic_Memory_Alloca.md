# Unit 5 - Pointers

## Introduction

- A pointer is a variable that stores the memory address of another variable as its value.
- Pointers are one of the things that make C stand out from other programming languages, like Python and Java.
- Pointers are important in C, because they allow us to manipulate the data in the computer's memory. This can reduce the code and improve the performance.

## Declaration

- To declare a pointer, we use the * operator followed by the data type and the variable name .
- The syntax is: `type *variable_name;` .
- For example: `int *p;` declares a pointer named p that can point to an int variable .

## Applications

- Some of the applications of pointers in C are:
  - Dynamic memory allocation: Pointers can be used to allocate memory at run time using functions like malloc, calloc, realloc and free.
  - Arrays, strings and functions: Pointers can be used to access and modify the elements of arrays and strings, and to pass and return functions as arguments.
  - Linked lists, trees and graphs: Pointers can be used to create and traverse data structures like linked lists, trees and graphs, which are based on self-referential structures.

## Introduction to Dynamic Memory Allocation

- Dynamic memory allocation is the process of allocating and deallocating memory at run time according to the program's needs.
- In C, we can use four functions to perform dynamic memory allocation:
  - malloc: This function allocates a block of memory of a given size and returns a pointer to the beginning of the block.
  - calloc: This function allocates a block of memory for an array of a given number of elements, each of a given size, and initializes all the bytes to zero. It returns a pointer to the beginning of the block.
  - realloc: This function reallocates a block of memory that was previously allocated by malloc or calloc, and changes its size to a new value. It returns a pointer to the beginning of the new block, or NULL if the allocation fails.
  - free: This function deallocates a block of memory that was previously allocated by malloc, calloc or realloc, and frees up the space for other uses.

## String and String functions

- A string is a sequence of characters terminated by a null character (\0).
- In C, we can declare a string as an array of char type, or as a pointer to char type.
- For example: `char str1[10] = "Hello";` or `char *str2 = "World";` are two ways of declaring strings.
- C provides several functions to manipulate strings, which are defined in the string.h header file.
- Some of the common string functions are:
  - strlen: This function returns the length of a string, excluding the null character.
  - strcpy: This function copies the contents of one string to another.
  - strcat: This function concatenates two strings, that is, appends one string to the end of another.
  - strcmp: This function compares two strings lexicographically, that is, based on the ASCII values of their characters.
  - strchr: This function returns a pointer to the first occurrence of a given character in a string, or NULL if the character is not found.
  - strstr: This function returns a pointer to the first occurrence of a given substring in a string, or NULL if the substring is not found.

## Use of Pointers in Self-Referential Structures

- A self-referential structure is a structure that contains a pointer to another variable of the same structure type.
- For example: `struct node { int data; struct node *next; };` is a self-referential structure that can be used to create a linked list.
- A self-referential structure can be used to create dynamic data structures that can grow or shrink at run time, such as linked lists, trees and graphs.
- To access the members of a self-referential structure, we can use the -> operator, which is a shorthand for dereferencing the pointer and