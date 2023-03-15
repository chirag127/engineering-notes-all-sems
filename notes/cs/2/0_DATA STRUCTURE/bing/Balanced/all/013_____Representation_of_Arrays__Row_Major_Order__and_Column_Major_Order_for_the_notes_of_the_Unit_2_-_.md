# Representation of Arrays: Row Major Order, and Column Major Order

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by their indices.
- A single-dimensional array is a linear array, where each element has a unique index.
- A multi-dimensional array is an array of arrays, where each element is itself an array and has a tuple of indices.
- The representation of arrays in memory depends on the order in which the elements are stored, which can be either row major order or column major order.
- In row major order, the elements of an array are stored row by row, i.e., the elements of the first row are stored first, followed by the elements of the second row, and so on.
- In column major order, the elements of an array are stored column by column, i.e., the elements of the first column are stored first, followed by the elements of the second column, and so on.
- The index formulae for accessing the elements of an array in memory depend on the order of storage, the number of dimensions, the base address, and the size of each element and dimension.
- For a one-dimensional array A of size n, the index formula is:

  - In row major order: `address(A[i]) = base(A) + i * size(A)`
  - In column major order: `address(A[i]) = base(A) + i * size(A)`

- For a two-dimensional array A of size m x n, the index formula is:

  - In row major order: `address(A[i][j]) = base(A) + (i * n + j) * size(A)`
  - In column major order: `address(A[i][j]) = base(A) + (j * m + i) * size(A)`

- For a three-dimensional array A of size l x m x n, the index formula is:

  - In row major order: `address(A[i][j][k]) = base(A) + (i * m * n + j * n + k) * size(A)`
  - In column major order: `address(A[i][j][k]) = base(A) + (k * l * m + j * l + i) * size(A)`

- For an n-dimensional array A of size d1 x d2 x ... x dn, the index formula is:

  - In row major order: `address(A[i1][i2]...[in]) = base(A) + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * size(A)`
  - In column major order: `address(A[i1][i2]...[in]) = base(A) + (in * d1 * d2 * ... * dn-1 + in-1 * d1 * d2 * ... * dn-2 + ... + i1) * size(A)`

- The choice of row major order or column major order depends on the programming language, the data structure, and the application of the array.
- Some advantages of row major order are:

  - It is easier to implement and understand, as it follows the natural order of reading and writing data.
  - It is more efficient for accessing rows or sub-arrays of an array, as they are stored contiguously in memory.
  - It is compatible with most programming languages, such as C, C++, Java, Python, etc.

- Some advantages of column major order are:

  - It is more efficient for accessing columns or transposed arrays, as they are stored contiguously in memory.
  - It is compatible with some programming languages, such as Fortran, MATLAB, R, etc.
  - It is more suitable for some mathematical operations, such as matrix multiplication, inversion, etc.