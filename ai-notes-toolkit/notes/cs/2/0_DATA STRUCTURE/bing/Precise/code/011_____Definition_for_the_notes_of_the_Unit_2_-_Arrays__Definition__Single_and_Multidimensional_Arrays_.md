### Unit 2 - Arrays and Linked Lists

#### Arrays: Definition, Single and Multidimensional Arrays
- An array is a collection of elements of the same data type, stored in contiguous memory locations.
- Each element in an array can be accessed by its index, which is an integer value representing its position in the array.
- Arrays can be single-dimensional (1D) or multidimensional (2D, 3D, nD).
- A single-dimensional array is a list of elements, while a multidimensional array is an array of arrays.

#### Representation of Arrays: Row Major Order and Column Major Order
- Arrays can be represented in memory in two ways: row-major order and column-major order.
- In row-major order, the elements of an array are stored row by row, while in column-major order, the elements are stored column by column.
- The index formula for a 1D array is `index = base_address + (element_size * index)`.
- The index formula for a 2D array in row-major order is `index = base_address + (element_size * (row_index * number_of_columns + column_index))`.
- The index formula for a 2D array in column-major order is `index = base_address + (element_size * (column_index * number_of_rows + row_index))`.
- The index formulae for 3D and nD arrays can be derived similarly.

#### Application of Arrays
- Arrays are used in various applications, such as storing and processing data, implementing data structures like stacks and queues, and representing mathematical concepts like matrices and vectors.

#### Sparse Matrices and their Representations
- A sparse matrix is a matrix in which most of the elements are zero.
- Sparse matrices can be represented using various data structures, such as arrays, linked lists, and trees, to save memory and improve the efficiency of operations.

#### Linked Lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List
- A linked list is a data structure in which elements are stored in nodes, and each node points to the next node in the list.
- Linked lists can be implemented using arrays or pointers.
- A singly linked list is a linked list in which each node has a pointer to the next node.
- A doubly linked list is a linked list in which each node has a pointer to the next node and the previous node.
- A circularly linked list is a linked list in which the last node points to the first node.

#### Operations on a Linked List: Insertion, Deletion, Traversal
- Common operations on a linked list include insertion, deletion, and traversal.
- Insertion involves adding a new node to the list at a specific position.
- Deletion involves removing a node from the list.
- Traversal involves visiting each node in the list and performing some operation on the data stored in the node.

#### Polynomial Representation and Addition, Subtraction, and Multiplication of Single Variable and Two Variables Polynomial
- A polynomial can be represented using an array or a linked list.
- The addition, subtraction, and multiplication of polynomials can be performed using algorithms that operate on the data structures used to represent the polynomials.