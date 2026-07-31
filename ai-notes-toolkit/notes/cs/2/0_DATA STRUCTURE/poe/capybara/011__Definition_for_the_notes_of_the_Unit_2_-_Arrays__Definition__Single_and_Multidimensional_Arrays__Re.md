### Definition for the notes of the Unit 2 - Arrays: 

Arrays are a type of data structure that can store a fixed number of elements of the same data type. They are used to store collections of data that are all of the same type, such as integers, characters, or strings. 

### Single and Multidimensional Arrays: 

- Single-dimensional arrays are the most common type of array that contains a single row of elements.
- Multidimensional arrays are arrays that have more than one dimension. They can be thought of as arrays of arrays, where each element of the main array is itself an array. 

### Representation of Arrays: Row Major Order, and Column Major Order: 

- In row major order, the elements of each row are stored one after another in memory, followed by the next row, and so on.
- In column major order, the elements of each column are stored one after another in memory, followed by the next column, and so on.

### Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array: 

- The index formula for a one-dimensional array is simply the index of the element we want to access.
- For a two-dimensional array, the index formula is `(row * number of columns) + column`.
- For a three-dimensional array, the index formula is `(plane * number of rows * number of columns) + (row * number of columns) + column`.
- For an n-dimensional array, the index formula is a recursive formula that depends on the number of dimensions.

### Application of arrays: 

Arrays are used in various applications, such as:

- Sorting algorithms 
- Searching algorithms 
- Image processing 
- Scientific simulations 
- Database management systems 

### Sparse Matrices and their representations: 

Sparse matrices are matrices that contain mostly zero elements. They can be represented in various ways, including:

- Compressed row format (CRF)
- Compressed column format (CCF)
- Coordinate list (COO) format

### Linked lists: 

Linked lists are a type of data structure that consists of a sequence of nodes, where each node contains a value and a pointer to the next node. 

### Array Implementation and Pointer Implementation of Singly Linked Lists: 

- In array implementation, the linked list is represented as an array where each element of the array contains the value and the index of the next element.
- In pointer implementation, each node of the linked list contains a value and a pointer to the next node.

### Doubly Linked List: 

A doubly linked list is a type of linked list where each node contains a value, a pointer to the next node, and a pointer to the previous node.

### Circularly Linked List: 

A circularly linked list is a type of linked list where the last node points to the first node, forming a circle.

### Operations on a Linked List: 

Operations that can be performed on a linked list include:

- Insertion 
- Deletion 
- Traversal 

### Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial: 

Polynomials can be represented using linked lists, where each node of the linked list contains the coefficient and the exponent of each term. Addition, subtraction, and multiplication of single-variable and two-variable polynomials can be performed using linked lists.