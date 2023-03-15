### Unit 2 - Arrays and Linked Lists

#### Arrays: Definition, Single and Multidimensional Arrays
- An array is a collection of elements of the same data type, stored in contiguous memory locations.
- Each element in an array can be accessed by its index, which is an integer value representing its position in the array.
- Arrays can be single-dimensional (1D) or multidimensional (2D, 3D, nD).
- A single-dimensional array is a list of elements, while a multidimensional array is an array of arrays.

#### Representation of Arrays: Row Major Order and Column Major Order
- Arrays can be represented in memory in two ways: row-major order and column-major order.
- In row-major order, the elements of an array are stored row by row. The first row is stored first, followed by the second row, and so on.
- In column-major order, the elements of an array are stored column by column. The first column is stored first, followed by the second column, and so on.

#### Derivation of Index Formulae for 1D, 2D, 3D, and nD Arrays
- The formula for calculating the memory address of an element in a 1D array is `base_address + (index * size_of_element)`.
- The formula for calculating the memory address of an element in a 2D array in row-major order is `base_address + ((row_index * number_of_columns) + column_index) * size_of_element`.
- The formula for calculating the memory address of an element in a 2D array in column-major order is `base_address + ((column_index * number_of_rows) + row_index) * size_of_element`.
- The formulae for calculating the memory address of an element in 3D and nD arrays can be derived similarly.

#### Application of Arrays
- Arrays are used in various applications, such as storing and processing data in a structured manner.
- They are commonly used in computer programming to implement data structures such as lists, stacks, queues, and hash tables.

#### Sparse Matrices and their Representations
- A sparse matrix is a matrix in which most of the elements are zero.
- Storing a sparse matrix as a regular 2D array would be inefficient, as it would require a large amount of memory to store many zero values.
- Sparse matrices can be represented more efficiently using data structures such as linked lists, arrays of arrays, or hash tables.

#### Linked Lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List
- A linked list is a data structure in which elements are stored in nodes, and each node points to the next node in the list.
- Linked lists can be implemented using arrays or pointers.
- In an array implementation of a linked list, each element is stored in an array, and the index of the next element is stored in the same array.
- In a pointer implementation of a linked list, each node contains a pointer to the next node in the list.
- Linked lists can be singly linked, doubly linked, or circularly linked.
- In a singly linked list, each node points to the next node in the list.
- In a doubly linked list, each node points to both the next and the previous nodes in the list.
- In a circularly linked list, the last node points back to the first node in the list.

#### Operations on a Linked List: Insertion, Deletion, Traversal
- Common operations on a linked list include insertion, deletion, and traversal.
- To insert an element into a linked list, a new node is created and inserted at the desired position in the list.
- To delete an element from a linked list, the node containing the element is removed from the list.
- To traverse a linked list, the list is iterated from the first node to the last node, visiting each node in turn.

#### Polynomial Representation and Addition, Subtraction, and Multiplication of Single Variable and Two Variable Polynomials
- A polynomial can be represented as a linked list, where each node contains the coefficient and exponent of a term in the polynomial.
- Polynomial addition, subtraction, and multiplication can be performed by manipulating the linked lists representing the polynomials.
- For example, to add two polynomials, the corresponding terms in the two linked lists are added together to create a new linked list representing the sum of the polynomials.
- Similarly, subtraction and multiplication of polynomials can be performed by manipulating the linked lists representing the polynomials.