## Unit 2 - Arrays and Linked Lists

- Arrays are data structures that store a collection of elements of the same data type in contiguous memory locations.
- Arrays can be classified into single-dimensional and multi-dimensional arrays based on the number of indices required to access an element.
- Single-dimensional arrays are also called linear or one-dimensional arrays. They have only one index or subscript to access an element. For example, `int a[10]` is a single-dimensional array of 10 integers.
- Multi-dimensional arrays are also called rectangular or n-dimensional arrays. They have more than one index or subscript to access an element. For example, `int b[3][4]` is a two-dimensional array of 12 integers, arranged in 3 rows and 4 columns.
- Representation of arrays: Arrays can be stored in memory in two ways: row major order and column major order.
  - Row major order: In this method, the elements of an array are stored row by row, starting from the first row. The elements of each row are stored in consecutive memory locations. For example, the two-dimensional array `b[3][4]` is stored in row major order as follows:

    | Memory Address | Element |
    | -------------- | ------- |
    | 1000           | b[0][0] |
    | 1004           | b[0][1] |
    | 1008           | b[0][2] |
    | 1012           | b[0][3] |
    | 1016           | b[1][0] |
    | 1020           | b[1][1] |
    | 1024           | b[1][2] |
    | 1028           | b[1][3] |
    | 1032           | b[2][0] |
    | 1036           | b[2][1] |
    | 1040           | b[2][2] |
    | 1044           | b[2][3] |

  - Column major order: In this method, the elements of an array are stored column by column, starting from the first column. The elements of each column are stored in consecutive memory locations. For example, the two-dimensional array `b[3][4]` is stored in column major order as follows:

    | Memory Address | Element |
    | -------------- | ------- |
    | 1000           | b[0][0] |
    | 1004           | b[1][0] |
    | 1008           | b[2][0] |
    | 1012           | b[0][1] |
    | 1016           | b[1][1] |
    | 1020           | b[2][1] |
    | 1024           | b[0][2] |
    | 1028           | b[1][2] |
    | 1032           | b[2][2] |
    | 1036           | b[0][3] |
    | 1040           | b[1][3] |
    | 1044           | b[2][3] |

- Derivation of index formulae for 1-D, 2-D, 3-D and n-D arrays: To calculate the memory address of any element in an array, we need to know the base address of the array, the size of each element, the number of dimensions, the size of each dimension, and the index of the element. The formulae for different types of arrays are as follows:
  - For a single-dimensional array `a[n]` stored in row major order, the memory address of `a[i]` is given by:

    `address(a[i]) = base(a) + i * size(a)`

    where `base(a)` is the base address of the array, `i` is the index of the element, and `size(a)` is the size of each element.

  - For a two-dimensional array `a[m][n]` stored in row major order, the memory address of `a[i][j]` is given by:

    `address(a[i][j]) = base(a) + (i * n + j) * size(a)`

    where `base(a)` is the base address of the array, `i` and `j` are the indices of the element, `n` is the size of the second dimension, and `size(a)` is the size of each element.

  - For a three-dimensional array `a[l][m][n]` stored in row major order, the memory address of `a