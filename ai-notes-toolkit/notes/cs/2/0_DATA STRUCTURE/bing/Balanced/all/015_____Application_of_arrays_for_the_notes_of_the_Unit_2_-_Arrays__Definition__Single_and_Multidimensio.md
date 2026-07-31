# Application of arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by an index.
- Arrays can be used to store and manipulate various kinds of data, such as numbers, characters, strings, matrices, graphs, images, etc.
- Arrays can be classified into single and multidimensional arrays, depending on the number of dimensions or subscripts required to access an element.
- A single-dimensional array is a linear array, where each element is identified by a single index. For example, `A[5]` is a single-dimensional array of size 5, and `A[3]` refers to the fourth element of the array.
- A multidimensional array is an array of arrays, where each element is identified by two or more indices. For example, `B[3][4]` is a two-dimensional array of size 3 by 4, and `B[2][1]` refers to the second element of the third row of the array.
- The representation of arrays in memory depends on the order in which the elements are stored. There are two common ways of storing multidimensional arrays: row major order and column major order.
- In row major order, the elements of an array are stored row by row, starting from the first row. For example, the elements of the array `B[3][4]` are stored as `B[0][0], B[0][1], B[0][2], B[0][3], B[1][0], B[1][1], B[1][2], B[1][3], B[2][0], B[2][1], B[2][2], B[2][3]`.
- In column major order, the elements of an array are stored column by column, starting from the first column. For example, the elements of the array `B[3][4]` are stored as `B[0][0], B[1][0], B[2][0], B[0][1], B[1][1], B[2][1], B[0][2], B[1][2], B[2][2], B[0][3], B[1][3], B[2][3]`.
- The index formulae for accessing an element of an array depend on the order of storage, the base address of the array, the size of each element, and the number of dimensions. For example, the general formula for accessing an element of a n-dimensional array `A[d1][d2]...[dn]` stored in row major order is:

`LOC(A[i1][i2]...[in]) = BA + size * (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in-1 * dn + in)`

where LOC is the location of the element, BA is the base address of the array, size is the size of each element, and i1, i2, ..., in are the indices of the element.

- The application of arrays can be seen in various domains, such as:

  - Mathematics: Arrays can be used to represent and perform operations on matrices, vectors, polynomials, etc. For example, a matrix can be stored as a two-dimensional array, and matrix multiplication can be done by using nested loops and array operations.
  - Computer graphics: Arrays can be used to store and manipulate images, pixels, colors, etc. For example, an image can be stored as a two-dimensional array of pixels, and image processing techniques can be applied by using array operations.
  - Data structures: Arrays can be used to implement various data structures, such as stacks, queues, heaps, hash tables, etc. For example, a stack can be implemented as a one-dimensional array, where the top element is stored at the end of the array, and push and pop operations can be done by using array operations.
  - Algorithms: Arrays can be used to store and sort data, search for elements, perform pattern matching, etc. For example, a sorting algorithm can be implemented by using an array, where the elements are compared and swapped by using array operations.

# Sparse matrices and their representations

- A sparse matrix is a matrix that has a large number of zero elements, and only a few non-zero elements. For example, the following matrix is a sparse matrix:

```
0 0 0 0 0
0 5 0 0 0
0 0 0 2 0
0 0 0 0 0
0 0 0 0 0

```
