# Single and Multidimensional Arrays

## Definition

- An array is a data structure that stores a collection of elements of the same type in a contiguous block of memory.
- Each element in an array can be accessed by its index, which is a non-negative integer that represents its position in the array.
- An array can have one or more dimensions, depending on how many indices are needed to specify an element.

## Single and Multidimensional Arrays

- A single-dimensional array, or 1D array, is an array that has only one dimension, meaning that it can be represented as a row or a column of elements.
- A multidimensional array, or nD array, is an array that has more than one dimension, meaning that it can be represented as a matrix or a table of elements, or a higher-dimensional structure.
- A two-dimensional array, or 2D array, is a special case of a multidimensional array that has two dimensions, meaning that it can be represented as a matrix or a table of elements, with rows and columns.
- A three-dimensional array, or 3D array, is another special case of a multidimensional array that has three dimensions, meaning that it can be represented as a cube or a stack of matrices, with rows, columns, and layers.

## Representation of Arrays

- Arrays are stored in memory in a linear fashion, meaning that the elements are placed one after another in a sequential order.
- The way that the elements of an array are mapped to the memory locations is called the array representation or the array layout.
- There are two main ways to represent arrays in memory: row-major order and column-major order.

### Row-major order

- In row-major order, the elements of an array are stored row by row, meaning that the elements of the first row are stored first, followed by the elements of the second row, and so on.
- Row-major order is also called row-wise order or lexicographic order.
- Row-major order is the default way of representing arrays in many programming languages, such as C, C++, Java, and Python.

### Column-major order

- In column-major order, the elements of an array are stored column by column, meaning that the elements of the first column are stored first, followed by the elements of the second column, and so on.
- Column-major order is also called column-wise order or colexicographic order.
- Column-major order is the default way of representing arrays in some programming languages, such as Fortran, MATLAB, and R.

## Derivation of Index Formulae

- To access an element of an array, we need to know its index or indices, which are the numbers that specify its position in the array.
- To compute the index or indices of an element, we need to know the array representation, the array dimensions, and the array base address.
- The array base address is the memory location of the first element of the array.
- The index formulae are the mathematical expressions that relate the index or indices of an element to its memory location.

### Index formula for 1D array

- For a 1D array of size n, the index formula for row-major order is:

  - Memory location of A[i] = Base address + i * size of each element

- For a 1D array of size n, the index formula for column-major order is:

  - Memory location of A[i] = Base address + i * size of each element

- Note that the index formula for 1D array is the same for both row-major and column-major order, because there is only one dimension.

### Index formula for 2D array

- For a 2D array of size m x n, the index formula for row-major order is:

  - Memory location of A[i][j] = Base address + (i * n + j) * size of each element

- For a 2D array of size m x n, the index formula for column-major order is:

  - Memory location of A[i][j] = Base address + (j * m + i) * size of each element

- Note that the index formula for 2D array differs for row-major and column-major order, because the order of the indices matters.

### Index