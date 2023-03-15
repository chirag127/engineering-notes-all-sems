# Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by a common name.
- The index formula is a mathematical expression that calculates the address of any element in an array, given its base address, size, and dimensions.
- The index formula depends on the order of storing the array elements in memory, which can be either row major order or column major order.
- In row major order, the elements of a row are stored together, followed by the elements of the next row, and so on. In column major order, the elements of a column are stored together, followed by the elements of the next column, and so on.
- The index formula also depends on the lower and upper bounds of the array dimensions, which can be either zero-based or arbitrary.

## Index Formula for 1-D Array

- A 1-D array is a linear array that has only one dimension, such as A[10] or B[5..14].
- The index formula for a 1-D array in row major order is:

  - LOC(A[i]) = BA + w * (i - LB)

  - where LOC(A[i]) is the address of the ith element of the array A, BA is the base address of the array, w is the size of each element, i is the index of the element, and LB is the lower bound of the array.

- The index formula for a 1-D array in column major order is the same as the row major order, since there is only one dimension.

## Index Formula for 2-D Array

- A 2-D array is a rectangular array that has two dimensions, such as A[3][4] or B[1..5][2..6].
- The index formula for a 2-D array in row major order is:

  - LOC(A[i][j]) = BA + w * [(i - LB1) * n + (j - LB2)]

  - where LOC(A[i][j]) is the address of the element in the ith row and jth column of the array A, BA is the base address of the array, w is the size of each element, i and j are the indices of the element, LB1 and LB2 are the lower bounds of the row and column dimensions, and n is the number of columns in the array.

- The index formula for a 2-D array in column major order is:

  - LOC(A[i][j]) = BA + w * [(j - LB2) * m + (i - LB1)]

  - where LOC(A[i][j]) is the address of the element in the ith row and jth column of the array A, BA is the base address of the array, w is the size of each element, i and j are the indices of the element, LB1 and LB2 are the lower bounds of the row and column dimensions, and m is the number of rows in the array.

## Index Formula for 3-D Array

- A 3-D array is a cuboidal array that has three dimensions, such as A[2][3][4] or B[1..2][2..4][3..6].
- The index formula for a 3-D array in row major order is:

  - LOC(A[i][j][k]) = BA + w * [(i - LB1) * n * p + (j - LB2) * p + (k - LB3)]

  - where LOC(A[i][j][k]) is the address of the element in the ith plane, jth row, and kth column of the array A, BA is the base address of the array, w is the size of each element, i, j, and k are the indices of the element, LB1, LB2, and LB3 are the lower bounds of the plane, row, and column dimensions, n is the number of rows in each plane, and p is the number of columns in each row.

- The index formula for a 3-D array in column major order is:

  - LOC(A[i][j][k]) = BA + w * [(k - LB3) * m * n + (j - LB2) * m + (i - LB1)]

  - where LOC(A[i][j][k]) is the address of the element in the ith plane, jth row, and kth column of the array A, BA is the base