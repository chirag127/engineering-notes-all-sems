### Application of arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index.
- Arrays can be used to store and manipulate various kinds of data, such as numbers, characters, strings, matrices, graphs, images, etc.
- Arrays can be classified into single-dimensional and multi-dimensional arrays, depending on the number of indices required to access an element.
- Single-dimensional arrays are also called vectors or one-dimensional arrays. They have only one index that ranges from 0 to n-1, where n is the size of the array.
- Multi-dimensional arrays are also called matrices or n-dimensional arrays. They have more than one index that ranges from 0 to n-1, where n is the size of each dimension of the array.
- For example, a two-dimensional array can be represented as a table of rows and columns, where each element has two indices: row and column. A three-dimensional array can be represented as a cube of layers, where each element has three indices: layer, row and column.
- The representation of arrays in memory can be done in two ways: row major order and column major order.
- Row major order is a method of storing an array in memory where the elements of a row are stored consecutively, followed by the elements of the next row, and so on. For example, the two-dimensional array A[2][3] can be stored in row major order as follows:

| Memory Location | Element |
| --------------- | ------- |
| 100             | A[0][0] |
| 101             | A[0][1] |
| 102             | A[0][2] |
| 103             | A[1][0] |
| 104             | A[1][1] |
| 105             | A[1][2] |

- Column major order is a method of storing an array in memory where the elements of a column are stored consecutively, followed by the elements of the next column, and so on. For example, the two-dimensional array A[2][3] can be stored in column major order as follows:

| Memory Location | Element |
| --------------- | ------- |
| 100             | A[0][0] |
| 101             | A[1][0] |
| 102             | A[0][1] |
| 103             | A[1][1] |
| 104             | A[0][2] |
| 105             | A[1][2] |

- The index formulae for 1-D, 2-D, 3-D and n-D arrays are used to calculate the memory location of an element in an array, given its indices and the base address of the array.
- The index formula for a 1-D array A[n] in row major order is:

  - LOC(A[i]) = BA + i * size
  - where LOC(A[i]) is the memory location of A[i], BA is the base address of the array, i is the index of the element, and size is the size of each element in bytes.

- The index formula for a 2-D array A[m][n] in row major order is:

  - LOC(A[i][j]) = BA + (i * n + j) * size
  - where LOC(A[i][j]) is the memory location of A[i][j], BA is the base address of the array, i and j are the indices of the element, n is the number of columns in the array, and size is the size of each element in bytes.

- The index formula for a 2-D array A[m][n] in column major order is:

  - LOC(A[i][j]) = BA + (j * m + i) * size
  - where LOC(A[i][j]) is the memory location of A[i][j], BA is the base address of the array, i and j are the indices of the element, m is the number of rows in the array, and size is the size of each element in bytes.

- The index formula for a 3-D array A[l][m][n] in row major order is:

  - LOC(A[i][j][k]) = BA + (i * m * n + j * n + k) * size
  - where LOC(A[i][j][k]) is the memory location of A[i][j][k], BA is the base address of the array, i, j and k are the indices of the element, m and n are the number of rows and columns in each layer of the array, and size is the size of each element in