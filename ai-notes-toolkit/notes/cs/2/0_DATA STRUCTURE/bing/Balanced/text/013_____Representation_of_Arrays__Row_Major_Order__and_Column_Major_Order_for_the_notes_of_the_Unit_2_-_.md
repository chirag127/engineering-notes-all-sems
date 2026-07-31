### Representation of Arrays: Row Major Order, and Column Major Order

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by their indices.
- A single-dimensional array is a linear array, where each element has a unique index.
- A multi-dimensional array is an array of arrays, where each element is another array of one lower dimension.
- The representation of arrays in memory depends on the order in which the elements are stored, which can be either row major order or column major order.
- In row major order, the elements of an array are stored row by row, i.e., the elements of the first row are stored first, followed by the elements of the second row, and so on.
- In column major order, the elements of an array are stored column by column, i.e., the elements of the first column are stored first, followed by the elements of the second column, and so on.
- The index formulae for accessing the elements of an array depend on the order of storage and the dimensions of the array.
- For a one-dimensional array A of size n, the index formula is:

  - A[i] = base address + i * size of element, where i is the index of the element, 0 <= i < n.

- For a two-dimensional array A of size m x n, the index formulae are:

  - A[i][j] = base address + (i * n + j) * size of element, for row major order, where i is the row index and j is the column index, 0 <= i < m, 0 <= j < n.
  - A[i][j] = base address + (j * m + i) * size of element, for column major order, where i is the row index and j is the column index, 0 <= i < m, 0 <= j < n.

- For a three-dimensional array A of size m x n x p, the index formulae are:

  - A[i][j][k] = base address + (i * n * p + j * p + k) * size of element, for row major order, where i is the first dimension index, j is the second dimension index, and k is the third dimension index, 0 <= i < m, 0 <= j < n, 0 <= k < p.
  - A[i][j][k] = base address + (k * m * n + j * m + i) * size of element, for column major order, where i is the first dimension index, j is the second dimension index, and k is the third dimension index, 0 <= i < m, 0 <= j < n, 0 <= k < p.

- For an n-dimensional array A of size d1 x d2 x ... x dn, the index formulae are:

  - A[i1][i2]...[in] = base address + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * size of element, for row major order, where i1, i2, ..., in are the indices of the n dimensions, 0 <= i1 < d1, 0 <= i2 < d2, ..., 0 <= in < dn.
  - A[i1][i2]...[in] = base address + (in * d1 * d2 * ... * dn-1 + in-1 * d1 * d2 * ... * dn-2 + ... + i1) * size of element, for column major order, where i1, i2, ..., in are the indices of the n dimensions, 0 <= i1 < d1, 0 <= i2 < d2, ..., 0 <= in < dn.

- The application of arrays can be seen in various domains, such as mathematics, science, engineering, computer science, etc. Some examples are:

  - Matrices and vectors, which are used for linear algebra, numerical analysis, differential equations, etc.
  - Images and graphics, which are represented as arrays of pixels or colors.
  - Strings and text, which are arrays of characters or symbols.
  - Tables and databases, which are arrays of records or fields.
  - Sorting and searching algorithms, which operate on arrays of data.

- A sparse matrix is a matrix that has a large number of zero elements, compared to the non-zero elements. Storing a sparse matrix as a regular array would waste a lot of memory space, so different representations are used to store only the non-zero elements and their positions.
- Some common