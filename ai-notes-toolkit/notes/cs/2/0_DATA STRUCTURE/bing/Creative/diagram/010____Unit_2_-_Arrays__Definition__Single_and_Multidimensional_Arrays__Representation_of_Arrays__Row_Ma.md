## Unit 2 - Arrays and Linked Lists

### Arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by an index.
- An array can have one or more dimensions, depending on the number of subscripts used to specify an element.
- A one-dimensional array (1-D array) is a linear array, where elements are stored in a single row or column.
- A two-dimensional array (2-D array) is a rectangular array, where elements are stored in rows and columns, forming a matrix.
- A three-dimensional array (3-D array) is a cubic array, where elements are stored in layers of matrices, forming a cube.
- An n-dimensional array (n-D array) is a generalization of the above arrays, where elements are stored in n subscripts, forming a hypercube.

#### Representation of Arrays

- Arrays can be represented in two ways: row major order and column major order.
- In row major order, the elements of an array are stored row by row, starting from the first row. The elements of each row are stored in consecutive memory locations.
- In column major order, the elements of an array are stored column by column, starting from the first column. The elements of each column are stored in consecutive memory locations.
- The choice of representation depends on the programming language and the application of the array.

#### Derivation of Index Formulae

- To access an element of an array, we need to calculate its memory address using an index formula.
- The index formula depends on the representation, the base address, the size of each element, and the dimensions of the array.
- For a 1-D array A of size n, the index formula for row major order is:

  - `address(A[i]) = base(A) + i * size(A)`
  - where `base(A)` is the base address of the array, `i` is the index of the element, and `size(A)` is the size of each element.

- The index formula for column major order is:

  - `address(A[i]) = base(A) + i * size(A)`
  - which is the same as row major order for 1-D arrays.

- For a 2-D array A of size m x n, the index formula for row major order is:

  - `address(A[i][j]) = base(A) + (i * n + j) * size(A)`
  - where `i` and `j` are the row and column indices of the element, respectively.

- The index formula for column major order is:

  - `address(A[i][j]) = base(A) + (j * m + i) * size(A)`
  - where `i` and `j` are the row and column indices of the element, respectively.

- For a 3-D array A of size l x m x n, the index formula for row major order is:

  - `address(A[i][j][k]) = base(A) + (i * m * n + j * n + k) * size(A)`
  - where `i`, `j`, and `k` are the layer, row, and column indices of the element, respectively.

- The index formula for column major order is:

  - `address(A[i][j][k]) = base(A) + (k * l * m + j * l + i) * size(A)`
  - where `i`, `j`, and `k` are the layer, row, and column indices of the element, respectively.

- For an n-D array A of size d1 x d2 x ... x dn, the index formula for row major order is:

  - `address(A[i1][i2]...[in]) = base(A) + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * size(A)`
  - where `i1`, `i2`, ..., `in` are the indices of the element along each dimension, respectively.

- The index formula for column major order is:

  - `address(A[i1][i2]...[in]) = base(A) + (in * d1 * d2 * ... * d(n-1) + i(n-1) * d1 * d2 * ... * d(n-2) + ... + i1) * size(A)`
  - where `i1`, `i2`, ..., `in` are the indices of the element along each dimension, respectively.

#### Application of Arrays

- Arrays are widely used in various fields of computer science and engineering, such as: