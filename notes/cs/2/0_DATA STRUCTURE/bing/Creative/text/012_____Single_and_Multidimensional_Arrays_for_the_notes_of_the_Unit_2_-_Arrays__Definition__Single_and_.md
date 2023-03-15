### Single and Multidimensional Arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by an index.
- A single-dimensional array is an array with one dimension, meaning that it can store a fixed number of elements of the same type in a linear sequence.
- A multidimensional array is an array with more than one dimension, meaning that it can store a fixed number of elements of the same type in a rectangular or higher-dimensional grid.
- The representation of arrays depends on the order in which the elements are stored in memory. There are two common orders: row-major order and column-major order.
- In row-major order, the elements of an array are stored row by row, meaning that the elements of the first row are stored first, followed by the elements of the second row, and so on.
- In column-major order, the elements of an array are stored column by column, meaning that the elements of the first column are stored first, followed by the elements of the second column, and so on.
- The index formulae for accessing the elements of an array depend on the order of storage and the number of dimensions. For a one-dimensional array A of size n, the index formula is:

  - A[i] = base address + i * size of element, where i is the index of the element, ranging from 0 to n-1.

- For a two-dimensional array A of size m x n, the index formulae are:

  - A[i][j] = base address + (i * n + j) * size of element, for row-major order, where i is the row index and j is the column index, ranging from 0 to m-1 and 0 to n-1, respectively.
  - A[i][j] = base address + (j * m + i) * size of element, for column-major order, where i is the row index and j is the column index, ranging from 0 to m-1 and 0 to n-1, respectively.

- For a three-dimensional array A of size l x m x n, the index formulae are:

  - A[i][j][k] = base address + (i * m * n + j * n + k) * size of element, for row-major order, where i is the first dimension index, j is the second dimension index, and k is the third dimension index, ranging from 0 to l-1, 0 to m-1, and 0 to n-1, respectively.
  - A[i][j][k] = base address + (k * m * l + j * l + i) * size of element, for column-major order, where i is the first dimension index, j is the second dimension index, and k is the third dimension index, ranging from 0 to l-1, 0 to m-1, and 0 to n-1, respectively.

- For an n-dimensional array A of size d1 x d2 x ... x dn, the index formulae are:

  - A[i1][i2]...[in] = base address + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * size of element, for row-major order, where i1, i2, ..., in are the indices of the elements, ranging from 0 to d1-1, 0 to d2-1, ..., and 0 to dn-1, respectively.
  - A[i1][i2]...[in] = base address + (in * d1 * d2 * ... * dn-1 + in-1 * d1 * d2 * ... * dn-2 + ... + i1) * size of element, for column-major order, where i1, i2, ..., in are the indices of the elements, ranging from 0 to d1-1, 0 to d2-1, ..., and 0 to dn-1, respectively.

- Arrays are useful for storing and manipulating data that have a fixed and regular structure, such as matrices, vectors, images, etc.
- Sparse matrices are matrices that have a large number of zero elements, and only a few non-zero elements. Storing sparse matrices as regular arrays can waste a lot of memory space and computation time.
- There are different ways of representing sparse matrices, such as:

  - Triplet representation: A sparse matrix is stored as a list of triplets, where each triplet consists of the row index, the column index, and the value of a non-zero element.
  - Compressed row