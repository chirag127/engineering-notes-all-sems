## Unit 5 - Pointers: Introduction, Declaration, Applications, Introduction to Dynamic Memory Allocation (Malloc, Calloc, Realloc, Free), String and String functions , Use of Pointers in Self-Referential Structures, Notion of Linked List (No Implementation)

- A pointer is a variable that stores the address of another variable in memory.
- A pointer can be declared using the * operator followed by the data type and the pointer name, for example: `int *p;`
- A pointer can be assigned the address of another variable using the & operator, for example: `p = &x;`
- A pointer can be dereferenced using the * operator to access or modify the value of the variable it points to, for example: `*p = 10;`
- Pointers can be used for various applications, such as:
  - Passing arguments by reference to functions, which allows the function to modify the original variables.
  - Returning multiple values from a function, by using pointers as output parameters.
  - Creating dynamic data structures, such as arrays, lists, trees, etc., by using pointers to link the nodes.
  - Implementing generic functions, by using void pointers that can point to any data type.
  - Improving the performance and efficiency of the program, by reducing the memory usage and copying overhead.
- Dynamic memory allocation is the process of allocating and deallocating memory at run time, as per the program's needs.
- Dynamic memory allocation can be done using the following functions from the stdlib.h header file:
  - `malloc(size_t n)` - allocates n bytes of memory and returns a pointer to the first byte, or NULL if the allocation fails.
  - `calloc(size_t n, size_t m)` - allocates n * m bytes of memory, initializes all the bytes to zero, and returns a pointer to the first byte, or NULL if the allocation fails.
  - `realloc(void *p, size_t n)` - reallocates the memory pointed by p to n bytes, copies the existing data, and returns a pointer to the new memory, or NULL if the allocation fails. If p is NULL, it behaves like malloc. If n is zero, it behaves like free.
  - `free(void *p)` - deallocates the memory pointed by p and returns it to the system. If p is NULL, it does nothing.
- A string is a sequence of characters terminated by a null character (\0).
- A string can be declared using an array of char, for example: `char str[10];`
- A string can be initialized using double quotes, for example: `char str[] = "Hello";`
- A string can be manipulated using various functions from the string.h header file, such as:
  - `strlen(char *s)` - returns the length of the string s, excluding the null character.
  - `strcpy(char *d, char *s)` - copies the string s to the string d, including the null character.
  - `strcat(char *d, char *s)` - appends the string s to the end of the string d, including the null character.
  - `strcmp(char *s1, char *s2)` - compares the strings s1 and s2 lexicographically, and returns a negative, zero, or positive value if s1 is less than, equal to, or greater than s2, respectively.
  - `strchr(char *s, char c)` - returns a pointer to the first occurrence of the character c in the string s, or NULL if not found.
  - `strstr(char *s1, char *s2)` - returns a pointer to the first occurrence of the string s2 in the string s1, or NULL if not found.
- A self-referential structure is a structure that contains a pointer to another variable of the same structure type.
- A self-referential structure can be used to create linked data structures, such as linked lists, trees, graphs, etc.
- A linked list is a linear data structure that consists of a sequence of nodes, each node containing some data and a pointer to the next node in the list.
- A linked list can be created using a self-referential structure, for example:

```c
// Define a node structure
struct node {
  int data; // Data part
  struct node *next; // Pointer to the next node
};

// Create a linked list
struct node *head = NULL; // Pointer to the first node
struct node *tail = NULL; // Pointer to the last node
struct node *temp = NULL; // Temporary pointer

// Add a node at the end of the list
temp = (struct node *)