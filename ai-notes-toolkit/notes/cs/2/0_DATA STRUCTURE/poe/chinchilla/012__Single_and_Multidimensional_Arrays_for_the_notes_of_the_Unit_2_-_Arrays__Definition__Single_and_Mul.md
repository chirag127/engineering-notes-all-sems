### Single and Multidimensional Arrays

Arrays are data structures that store a collection of elements of the same data type. They can be either single-dimensional (1D) or multidimensional (2D, 3D, nD), depending on the number of indices needed to access the elements. Here are some key points to remember about arrays:

- Definition: An array is a collection of elements of the same data type, which are stored in contiguous memory locations.
- Single-dimensional arrays: Also known as vectors, 1D arrays are accessed using a single index or subscript. The elements are arranged in a linear sequence.
- Multidimensional arrays: These are arrays with more than one dimension. For example, a 2D array has rows and columns, while a 3D array has rows, columns, and depth.
- Representation of arrays: There are two common ways to represent arrays in memory: row major order and column major order. In row major order, the elements of each row are stored together in contiguous memory locations, while in column major order, the elements of each column are stored together.
- Derivation of index formulae: The index formula for accessing an element in a 1D array is straightforward: index = base_address + (element_size * (index - lower_bound)). For 2D arrays, the formula is index = base_address + (element_size * ((row_index - lower_row_bound) * num_columns + (column_index - lower_column_bound))). Similar formulas can be derived for higher-dimensional arrays.
- Application of arrays: Arrays are used in many applications, including sorting, searching, and matrix operations.
- Sparse matrices: Sparse matrices are matrices with a large number of zero elements. They can be represented in various ways, such as linked lists or arrays of tuples.

### Linked Lists

Linked lists are another type of data structure that can be used to store a collection of elements. Unlike arrays, linked lists are not stored in contiguous memory locations. Instead, each element is stored in a separate node that contains a pointer to the next node in the list. Here are some key points to remember about linked lists:

- Array implementation: Linked lists can be implemented using arrays, where each node contains the element and an index to the next node in the list.
- Pointer implementation: This is the most common way to implement linked lists. Each node contains the element and a pointer to the next node in the list.
- Singly linked list: In a singly linked list, each node has a pointer to the next node in the list, but not to the previous node.
- Doubly linked list: In a doubly linked list, each node has a pointer to both the next and previous nodes in the list.
- Circularly linked list: In a circularly linked list, the last node points to the first node in the list, creating a circular structure.
- Operations on a linked list: The basic operations on a linked list include insertion, deletion, and traversal.
- Polynomial representation: Linked lists can be used to represent polynomials, where each node contains a coefficient and an exponent.
- Addition, subtraction, and multiplication of polynomials: These operations can be performed on linked lists by traversing the lists and combining like terms.