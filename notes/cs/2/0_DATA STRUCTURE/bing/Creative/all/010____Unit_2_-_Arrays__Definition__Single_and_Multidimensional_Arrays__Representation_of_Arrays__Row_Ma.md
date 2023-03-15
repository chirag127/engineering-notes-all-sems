# Unit 2 - Arrays and Linked Lists

## Arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by an index.
- An array can be single-dimensional or multi-dimensional, depending on the number of dimensions or subscripts used to specify an element.
- A single-dimensional array is a linear array, where each element is identified by a single index. For example, `A[5]` is a single-dimensional array of size 5, and `A[3]` refers to the fourth element of the array.
- A multi-dimensional array is an array of arrays, where each element is identified by a combination of indices. For example, `B[3][4]` is a two-dimensional array of size 3 by 4, and `B[2][1]` refers to the second element of the third row of the array.
- The representation of arrays in memory depends on the order of storing the elements, which can be either row major order or column major order.
- In row major order, the elements of an array are stored row by row, starting from the first row. For example, the two-dimensional array `B[3][4]` is stored as `B[0][0], B[0][1], B[0][2], B[0][3], B[1][0], B[1][1], B[1][2], B[1][3], B[2][0], B[2][1], B[2][2], B[2][3]`.
- In column major order, the elements of an array are stored column by column, starting from the first column. For example, the two-dimensional array `B[3][4]` is stored as `B[0][0], B[1][0], B[2][0], B[0][1], B[1][1], B[2][1], B[0][2], B[1][2], B[2][2], B[0][3], B[1][3], B[2][3]`.
- The index formulae for accessing an element of an array depend on the order of storage, the base address of the array, the size of each element, and the number of dimensions.
- For a single-dimensional array `A[n]` stored in row major order, with base address `BA` and element size `ES`, the address of `A[i]` is given by `BA + i * ES`.
- For a two-dimensional array `B[m][n]` stored in row major order, with base address `BA` and element size `ES`, the address of `B[i][j]` is given by `BA + (i * n + j) * ES`.
- For a three-dimensional array `C[p][q][r]` stored in row major order, with base address `BA` and element size `ES`, the address of `C[i][j][k]` is given by `BA + (i * q * r + j * r + k) * ES`.
- For an n-dimensional array `D[d1][d2]...[dn]` stored in row major order, with base address `BA` and element size `ES`, the address of `D[i1][i2]...[in]` is given by `BA + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in-1 * dn + in) * ES`.
- The index formulae for accessing an element of an array stored in column major order can be derived by reversing the order of the indices and the dimensions in the formulae for row major order.
- Arrays are used to store and manipulate data in various applications, such as matrices, vectors, tables, lists, strings, etc.
- Sparse matrices are matrices that have a large number of zero elements, and only a few non-zero elements. Storing sparse matrices as arrays can waste a lot of memory space and computation time.
- Sparse matrices can be represented more efficiently by using different techniques, such as linked lists, arrays of lists, coordinate lists, compressed row storage, compressed column storage, etc.

## Linked Lists

- A linked list is a linear data structure, where each element is a separate object that contains a data field and a pointer field that links to the next element.
- A linked list can be implemented using either an array or a pointer.
- An array implementation of a linked list uses a fixed-size array to store the data and the next index of each element. For example, the linked list `