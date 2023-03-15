# Unit 2 - Arrays and Linked Lists

## Arrays

### Definition
An array is a collection of elements of the same data type, stored in contiguous memory locations. Each element can be accessed by its index, which is an integer value representing its position in the array.

### Single and Multidimensional Arrays
Arrays can have one or more dimensions. A one-dimensional array is a list of elements, while a two-dimensional array can be thought of as a table, with rows and columns. Arrays can have any number of dimensions, but the most common are one-dimensional and two-dimensional arrays.

### Representation of Arrays: Row Major Order and Column Major Order
Arrays can be stored in memory in two ways: row-major order and column-major order. In row-major order, the elements of an array are stored row by row, while in column-major order, the elements are stored column by column.

### Derivation of Index Formulae for 1-D, 2-D, 3-D and n-D Array
The formula for calculating the memory address of an element in an array depends on the number of dimensions of the array and the way it is stored in memory (row-major or column-major order). For a one-dimensional array, the formula is simply the base address of the array plus the index of the element multiplied by the size of each element. For a two-dimensional array, the formula is more complex and depends on the number of columns (for row-major order) or rows (for column-major order) in the array.

### Application of Arrays
Arrays are used in many different applications, including sorting, searching, and storing data in a structured way. They are also used in mathematical operations, such as matrix multiplication.

### Sparse Matrices and their Representations
A sparse matrix is a matrix in which most of the elements are zero. Storing a sparse matrix as a regular array would waste a lot of memory, so special data structures are used to represent sparse matrices in a more efficient way.

## Linked Lists

### Array Implementation and Pointer Implementation of Singly Linked Lists
A linked list is a data structure that consists of a sequence of nodes, each containing data and a reference to the next node in the list. Linked lists can be implemented using arrays or pointers. In an array implementation, each node is stored in an element of an array, while in a pointer implementation, each node is a separate object in memory, with a pointer to the next node.

### Doubly Linked List
A doubly linked list is a linked list in which each node has a reference to both the next and the previous node in the list. This allows for more efficient traversal of the list in both directions.

### Circularly Linked List
A circularly linked list is a linked list in which the last node in the list points back to the first node, forming a loop.

### Operations on a Linked List
Common operations on a linked list include insertion, deletion, and traversal. Insertion involves adding a new node to the list, while deletion involves removing a node from the list. Traversal involves visiting each node in the list in order.

### Polynomial Representation and Addition, Subtraction, and Multiplication of Single Variable and Two Variable Polynomials
Polynomials can be represented using linked lists, with each node representing a term in the polynomial. Operations such as addition, subtraction, and multiplication can be performed on polynomials represented in this way.