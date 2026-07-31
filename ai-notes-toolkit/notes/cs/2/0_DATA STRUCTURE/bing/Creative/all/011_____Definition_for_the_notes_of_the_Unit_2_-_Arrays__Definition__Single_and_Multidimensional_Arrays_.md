# Unit 2 - Arrays: Definition, Single and Multidimensional Arrays, Representation of Arrays: Row Major Order, and Column Major Order, Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array Application of arrays, Sparse Matrices and their representations. Linked lists: Array Implementation and Pointer Implementation of Singly Linked Lists, Doubly Linked List, Circularly Linked List, Operations on a Linked List. Insertion, Deletion, Traversal, Polynomial Representation and Addition Subtraction & Multiplications of Single variable & Two variables Polynomial.

## Arrays: Definition, Single and Multidimensional Arrays

- An array is a collection of homogeneous elements stored in a contiguous memory location for better access and easier calculation by the system.
- An array is a data structure consisting of a collection of elements, each identified by at least one array index or key.
- An array is an assortment of similar types of data, while a list can include dissimilar data values.
- An array can be of any type, including an array type.
- An array can be single-dimensional or multidimensional, depending on the number of dimensions or indices it has.
- A single-dimensional array is a linear array that has one index or key for each element. It can be represented as a row or a column of elements.
- A multidimensional array is an array that has more than one index or key for each element. It can be represented as a matrix or a table of elements, or a higher-dimensional structure.
- The number of dimensions or indices of an array is also called its rank or order.
- The size or length of an array is the number of elements it can hold.
- The position of each element in an array can be computed from its index or key by a mathematical formula.
- An array can be declared, initialized, accessed, modified, and iterated using different syntaxes and methods depending on the programming language.

## Representation of Arrays: Row Major Order, and Column Major Order

- Row major order and column major order are two ways of storing multidimensional arrays in linear memory.
- Row major order means that the elements of a multidimensional array are stored row by row, or that the row index varies faster than the column index.
- Column major order means that the elements of a multidimensional array are stored column by column, or that the column index varies faster than the row index.
- The choice of row major order or column major order affects the computation of the memory address of an element in a multidimensional array, as well as the traversal order of the array.
- Different programming languages use different conventions for the representation of arrays. For example, C and C++ use row major order, while Fortran and MATLAB use column major order.

## Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

- The index formula is the mathematical expression that calculates the memory address of an element in an array, given its index or key and the base address of the array.
- The index formula depends on the representation of the array, the size of each dimension, and the size of each element.
- For a single-dimensional array A of size n and element size s, the index formula for row major order is:

  - `address(A[i]) = base(A) + i * s`

  - where i is the index of the element, base(A) is the base address of the array, and address(A[i]) is the memory address of the element.

- For a two-dimensional array A of size m x n and element size s, the index formula for row major order is:

  - `address(A[i][j]) = base(A) + (i * n + j) * s`

  - where i and j are the row and column indices of the element, respectively.

- For a two-dimensional array A of size m x n and element size s, the index formula for column major order is:

  - `address(A[i][j]) = base(A) + (j * m + i) * s`

  - where i and j are the row and column indices of the element, respectively.

- For a three-dimensional array A of size l x m x n and element size s, the index formula for row major order is:

  - `address(A[i][j][k]) = base(A) + (i * m * n + j * n + k) * s`

  - where i, j, and k are the indices of the element along the three dimensions, respectively