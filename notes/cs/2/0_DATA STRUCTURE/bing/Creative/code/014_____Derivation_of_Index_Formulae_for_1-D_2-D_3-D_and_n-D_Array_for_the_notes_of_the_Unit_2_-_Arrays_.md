# Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

## 1-D Array

A one-dimensional array is a linear collection of elements that are stored in contiguous memory locations. The elements of a one-dimensional array can be accessed by using an index that specifies the position of the element in the array. The index usually starts from 0 or 1, depending on the programming language or the convention used.

To calculate the address of any element in a one-dimensional array, we need to know the following information:

- The base address of the array, which is the address of the first element of the array.
- The size of each element of the array, which is usually measured in bytes.
- The index of the element, which is an integer value that indicates the position of the element in the array.

The formula for calculating the address of any element in a one-dimensional array is:

**Address of A[i] = Base address of A + Size of each element * Index of the element**

For example, if we have an array A of integers that has a base address of 1000 and each integer occupies 4 bytes, then the address of A[3] is:

**Address of A[3] = 1000 + 4 * 3 = 1012**

## 2-D Array

A two-dimensional array is a collection of elements that are arranged in rows and columns, forming a matrix or a table. The elements of a two-dimensional array can be accessed by using two indices that specify the row and the column of the element in the array. The indices usually start from 0 or 1, depending on the programming language or the convention used.

To calculate the address of any element in a two-dimensional array, we need to know the following information:

- The base address of the array, which is the address of the first element of the array.
- The size of each element of the array, which is usually measured in bytes.
- The number of columns in the array, which is the total number of elements in each row of the array.
- The row index and the column index of the element, which are integer values that indicate the position of the element in the array.

There are two ways to store the elements of a two-dimensional array in memory: row-major order and column-major order.

### Row-major order

In row-major order, the elements of a two-dimensional array are stored row by row, meaning that the elements of the first row are stored first, followed by the elements of the second row, and so on. The formula for calculating the address of any element in a two-dimensional array in row-major order is:

**Address of A[i][j] = Base address of A + Size of each element * (Number of columns * Row index + Column index)**

For example, if we have an array A of integers that has a base address of 1000 and each integer occupies 4 bytes, and the array has 3 rows and 4 columns, then the address of A[1][2] in row-major order is:

**Address of A[1][2] = 1000 + 4 * (4 * 1 + 2) = 1020**

### Column-major order

In column-major order, the elements of a two-dimensional array are stored column by column, meaning that the elements of the first column are stored first, followed by the elements of the second column, and so on. The formula for calculating the address of any element in a two-dimensional array in column-major order is:

**Address of A[i][j] = Base address of A + Size of each element * (Number of rows * Column index + Row index)**

For example, if we have an array A of integers that has a base address of 1000 and each integer occupies 4 bytes, and the array has 3 rows and 4 columns, then the address of A[1][2] in column-major order is:

**Address of A[1][2] = 1000 + 4 * (3 * 2 + 1) = 1036**

## 3-D Array

A three-dimensional array is a collection of elements that are arranged in layers, rows and columns, forming a cube or a box. The elements of a three-dimensional array can be accessed by using three indices that specify the layer, the row and the column of the element in the array. The indices usually start from 0 or 1, depending on the programming language or the convention used.

To calculate the address of any element in a