# Unit 2 - Arrays and Linked Lists

## Arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index.
- An array can be single-dimensional or multidimensional, depending on the number of dimensions or subscripts used to specify an element.
- A single-dimensional array is a linear array, where each element is identified by a single index. For example, `A[5]` is a single-dimensional array of size 5, and `A[3]` is the element at index 3.
- A multidimensional array is an array of arrays, where each element is identified by a tuple of indices. For example, `A[3][4]` is a two-dimensional array of size 3x4, and `A[2][1]` is the element at row 2 and column 1.
- The representation of arrays in memory depends on the order of storing the elements, which can be either row major order or column major order.
- In row major order, the elements of an array are stored row by row, starting from the first row. For example, the elements of `A[3][4]` are stored as `A[0][0], A[0][1], A[0][2], A[0][3], A[1][0], A[1][1], A[1][2], A[1][3], A[2][0], A[2][1], A[2][2], A[2][3]`.
- In column major order, the elements of an array are stored column by column, starting from the first column. For example, the elements of `A[3][4]` are stored as `A[0][0], A[1][0], A[2][0], A[0][1], A[1][1], A[2][1], A[0][2], A[1][2], A[2][2], A[0][3], A[1][3], A[2][3]`.
- The index formulae for 1-D, 2-D, 3-D and n-D arrays are derived by using the base address, the size of each element, and the order of storing the elements.
- For a 1-D array `A[n]`, the address of `A[i]` is given by `base + i * size`, where `base` is the address of `A[0]` and `size` is the size of each element.
- For a 2-D array `A[m][n]`, the address of `A[i][j]` in row major order is given by `base + (i * n + j) * size`, and in column major order is given by `base + (j * m + i) * size`.
- For a 3-D array `A[l][m][n]`, the address of `A[i][j][k]` in row major order is given by `base + (i * m * n + j * n + k) * size`, and in column major order is given by `base + (k * m * l + j * l + i) * size`.
- For an n-D array `A[d1][d2]...[dn]`, the address of `A[i1][i2]...[in]` in row major order is given by `base + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * size`, and in column major order is given by `base + (in * d1 * d2 * ... * d(n-1) + i(n-1) * d1 * d2 * ... * d(n-2) + ... + i1) * size`.
- Arrays are used to store and manipulate data in various applications, such as matrices, vectors, tables, lists, stacks, queues, etc.
- Sparse matrices are matrices that have a large number of zero elements, and storing them as arrays would waste a lot of memory space. Therefore, sparse matrices are represented using different techniques, such as linked lists, arrays of lists, coordinate lists, compressed sparse row, compressed sparse column, etc.

## Linked Lists

- A linked list is a linear data structure, where each element is a node that contains data and a pointer to the next node.
- A linked list can be implemented using either an array or a pointer.
- In array implementation, a fixed-size array is used to store the nodes, and each node has an index that