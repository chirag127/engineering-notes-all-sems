# Single and Multidimensional Arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by an index.
- An array can have one or more dimensions, depending on the number of subscripts used to specify the position of an element.
- A single-dimensional array (or 1-D array) is a linear array that has only one subscript, representing the row number of the element. For example, `A[5]` is a 1-D array of size 5, and `A[3]` is the element at the third row.
- A multidimensional array (or n-D array) is an array that has more than one subscript, representing the row, column, and other dimensions of the element. For example, `B[3][4]` is a 2-D array of size 3 by 4, and `B[2][3]` is the element at the second row and third column.
- The representation of arrays in memory depends on the order of storing the elements, which can be either row major order or column major order.
- In row major order, the elements of an array are stored row by row, starting from the first row. For example, the 2-D array `B[3][4]` is stored as `B[0][0], B[0][1], B[0][2], B[0][3], B[1][0], B[1][1], B[1][2], B[1][3], B[2][0], B[2][1], B[2][2], B[2][3]`.
- In column major order, the elements of an array are stored column by column, starting from the first column. For example, the 2-D array `B[3][4]` is stored as `B[0][0], B[1][0], B[2][0], B[0][1], B[1][1], B[2][1], B[0][2], B[1][2], B[2][2], B[0][3], B[1][3], B[2][3]`.
- The index formulae for 1-D, 2-D, 3-D and n-D arrays are derived based on the size of each dimension, the base address of the array, and the order of storing the elements.
- For a 1-D array `A[n]` with base address `BA` and element size `ES`, the address of `A[i]` is given by `BA + i * ES`.
- For a 2-D array `B[m][n]` with base address `BA` and element size `ES`, the address of `B[i][j]` is given by `BA + (i * n + j) * ES` in row major order, and `BA + (j * m + i) * ES` in column major order.
- For a 3-D array `C[p][q][r]` with base address `BA` and element size `ES`, the address of `C[i][j][k]` is given by `BA + (i * q * r + j * r + k) * ES` in row major order, and `BA + (k * p * q + j * p + i) * ES` in column major order.
- For an n-D array `D[d1][d2]...[dn]` with base address `BA` and element size `ES`, the address of `D[i1][i2]...[in]` is given by `BA + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * ES` in row major order, and `BA + (in * d1 * d2 * ... * d(n-1) + i(n-1) * d1 * d2 * ... * d(n-2) + ... + i1) * ES` in column major order.
- Arrays are used to store and manipulate data in various applications, such as matrices, vectors, polynomials, strings, graphs, images, etc.
- Sparse matrices are matrices that have a large number of zero elements, and only a few non-zero elements. Storing sparse matrices as arrays can waste a lot of memory space and computation time.
- Sparse matrices can be represented more efficiently by using different methods, such as linked lists, arrays of lists, arrays of arrays, etc. These methods store only the non-zero elements and their positions, and use pointers