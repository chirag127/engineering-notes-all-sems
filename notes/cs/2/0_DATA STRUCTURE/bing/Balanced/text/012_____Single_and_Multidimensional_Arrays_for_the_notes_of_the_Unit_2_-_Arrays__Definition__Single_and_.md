### Single and Multidimensional Arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index.
- A single-dimensional array is an array with one dimension, meaning that it can store a fixed number of elements of the same type in a linear sequence.
- A multidimensional array is an array with more than one dimension, meaning that it can store a fixed number of elements of the same type in a rectangular or higher-dimensional grid.
- The representation of arrays in memory depends on the order in which the elements are stored. There are two common orders: row-major order and column-major order.
- In row-major order, the elements of an array are stored row by row, meaning that the elements of the first row are stored first, followed by the elements of the second row, and so on.
- In column-major order, the elements of an array are stored column by column, meaning that the elements of the first column are stored first, followed by the elements of the second column, and so on.
- The index formulae for accessing the elements of an array depend on the order, the number of dimensions, and the size of each dimension of the array.
- For a one-dimensional array A of size n, the index formula for accessing the element A[i] in row-major order or column-major order is the same: i.
- For a two-dimensional array A of size m x n, the index formula for accessing the element A[i][j] in row-major order is i * n + j, and in column-major order is i + j * m.
- For a three-dimensional array A of size l x m x n, the index formula for accessing the element A[i][j][k] in row-major order is i * m * n + j * n + k, and in column-major order is i + j * l + k * l * m.
- For an n-dimensional array A of size d1 x d2 x ... x dn, the index formula for accessing the element A[i1][i2]...[in] in row-major order is i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in, and in column-major order is i1 + i2 * d1 + i3 * d1 * d2 + ... + in * d1 * d2 * ... * dn-1.
- Arrays are useful for storing and manipulating data that have a fixed and regular structure, such as matrices, vectors, images, etc.
- Sparse matrices are matrices that have a large number of zero elements and a small number of non-zero elements. Storing sparse matrices as arrays can waste a lot of memory space and computation time.
- There are different ways of representing sparse matrices, such as using linked lists, arrays of lists, hash tables, etc. One common representation is using a triplet (row, column, value) to store each non-zero element of the matrix.