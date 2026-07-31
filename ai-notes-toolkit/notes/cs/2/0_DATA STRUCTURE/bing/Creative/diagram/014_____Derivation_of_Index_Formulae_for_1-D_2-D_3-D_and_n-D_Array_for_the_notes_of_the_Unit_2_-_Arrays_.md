### Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index. The index formula is a mathematical expression that calculates the address of any element in the array, given its base address, size, and dimensions.

#### 1-D Array

A one-dimensional array is a linear array of elements, such as A[1..n], where n is the number of elements. The index formula for a 1-D array is:

`LOC(A[i]) = BA + W * (i - LB)`

where:

- LOC(A[i]) is the address of the ith element of the array A
- BA is the base address of the array A
- W is the size of each element of the array A
- i is the index of the element of the array A
- LB is the lower bound of the index of the array A

For example, if A is an array of integers (W = 4 bytes) with LB = 1 and BA = 1000, then the address of A[5] is:

`LOC(A[5]) = 1000 + 4 * (5 - 1) = 1016`

#### 2-D Array

A two-dimensional array is an array of arrays, such as A[1..m, 1..n], where m and n are the number of rows and columns, respectively. The index formula for a 2-D array depends on the order of storing the elements: row-major or column-major.

- Row-major order: The elements of the array are stored row by row, such that the elements of the first row are stored first, followed by the elements of the second row, and so on. The index formula for a 2-D array in row-major order is:

  `LOC(A[i, j]) = BA + W * (n * (i - LBR) + (j - LBC))`

  where:

  - LOC(A[i, j]) is the address of the element in the ith row and jth column of the array A
  - BA is the base address of the array A
  - W is the size of each element of the array A
  - n is the number of columns of the array A
  - i and j are the indices of the row and column of the element of the array A
  - LBR and LBC are the lower bounds of the indices of the rows and columns of the array A

  For example, if A is an array of integers (W = 4 bytes) with LBR = 1, LBC = 1, and BA = 1000, then the address of A[3, 4] is:

  `LOC(A[3, 4]) = 1000 + 4 * (n * (3 - 1) + (4 - 1)) = 1000 + 4 * (n * 2 + 3)`

  If n = 5, then LOC(A[3, 4]) = 1048.

- Column-major order: The elements of the array are stored column by column, such that the elements of the first column are stored first, followed by the elements of the second column, and so on. The index formula for a 2-D array in column-major order is:

  `LOC(A[i, j]) = BA + W * (m * (j - LBC) + (i - LBR))`

  where:

  - LOC(A[i, j]) is the address of the element in the ith row and jth column of the array A
  - BA is the base address of the array A
  - W is the size of each element of the array A
  - m is the number of rows of the array A
  - i and j are the indices of the row and column of the element of the array A
  - LBR and LBC are the lower bounds of the indices of the rows and columns of the array A

  For example, if A is an array of integers (W = 4 bytes) with LBR = 1, LBC = 1, and BA = 1000, then the address of A[3, 4] is:

  `LOC(A[3, 4]) = 1000 + 4 * (m * (4 - 1) + (3 - 1)) =