## Unit 5 - Pointers: Introduction, Declaration, Applications, Introduction to Dynamic Memory Allocation (Malloc, Calloc, Realloc, Free), String and String functions , Use of Pointers in Self-Referential Structures, Notion of Linked List (No Implementation)

- A pointer is a variable that stores the address of another variable in memory.
- A pointer can be declared using the * operator followed by the data type and the pointer name, for example: `int *p;`
- A pointer can be assigned the address of another variable using the & operator, for example: `p = &x;`
- A pointer can be dereferenced using the * operator to access or modify the value of the variable it points to, for example: `*p = 10;`
- Pointers can be used for various applications, such as:
  - Passing arguments by reference to functions, which allows the function to modify the original variables.
  - Returning multiple values from a function, by using pointers as output parameters.
  - Creating dynamic data structures, such as arrays, linked lists, trees, etc.
  - Implementing low-level operations, such as memory management, file handling, etc.
- Dynamic memory allocation is the process of allocating and deallocating memory at runtime, as per the program's needs.
- Dynamic memory allocation can be done using the following functions in C:
  - `malloc` - allocates a block of memory of a given size and returns a pointer to it.
  - `calloc` - allocates a block of memory for an array of a given number of elements, each of a given size, and initializes all the bytes to zero. It also returns a pointer to the allocated memory.
  - `realloc` - changes the size of an existing block of memory, either by expanding or shrinking it, and returns a pointer to the new memory. It may also move the memory to a new location, if necessary.
  - `free` - deallocates a block of memory that was previously allocated by `malloc`, `calloc`, or `realloc`, and frees up the memory for other uses.
- A string is a sequence of characters terminated by a null character (\0).
- A string can be declared as an array of characters, for example: `char str[10];`
- A string can be initialized using double quotes, for example: `char str[10] = "Hello";`
- A string can be manipulated using various string functions defined in the string.h header file, such as:
  - `strlen` - returns the length of a string, excluding the null character.
  - `strcpy` - copies one string to another.
  - `strcat` - concatenates two strings.
  - `strcmp` - compares two strings lexicographically and returns a positive, negative, or zero value depending on the result.
  - `strchr` - returns a pointer to the first occurrence of a character in a string, or NULL if not found.
  - `strstr` - returns a pointer to the first occurrence of a substring in a string, or NULL if not found.
- A self-referential structure is a structure that contains a pointer to another variable of the same structure type.
- A self-referential structure can be used to create linked data structures, such as linked lists, trees, graphs, etc.
- A linked list is a linear data structure that consists of a sequence of nodes, each containing some data and a pointer to the next node in the list.
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
temp = (struct node *)malloc(sizeof(struct node)); // Allocate memory for a new node
temp->data = 10; // Assign data
temp->next = NULL; // Set next pointer to NULL
if (head == NULL) { // If the list is empty
  head = temp; // Set head to the new node
  tail = temp; // Set tail to the new node
} else { // If the list is not empty
  tail->next = temp; // Set the next pointer of the last node to the new node
  tail = temp; // Set tail to the new node
}
```
- A linked list can be traversed, searched, inserted, deleted, sorted,