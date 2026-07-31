### Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by their indices.
- The index formula is a mathematical expression that calculates the address of any element in an array, given its base address, size, and dimensions.
- The index formula depends on the order of storing the array elements in memory, which can be either row major or column major.
- In row major order, the elements of a row are stored together, followed by the elements of the next row, and so on. In column major order, the elements of a column are stored together, followed by the elements of the next column, and so on.
- The index formula for a 1-D array is:

  - LOC(A[i]) = B + W * (i - LB), where
    - LOC(A[i]) is the address of the ith element of the array A
    - B is the base address of the array A
    - W is the size of each element of the array A
    - i is the index of the element to be accessed
    - LB is the lower bound of the index range of the array A
  - This formula is the same for both row major and column major order, since a 1-D array has only one dimension.

- The index formula for a 2-D array is:

  - LOC(A[i][j]) = B + W * (i * C + j - LB1 * C - LB2), where
    - LOC(A[i][j]) is the address of the element in the ith row and jth column of the array A
    - B is the base address of the array A
    - W is the size of each element of the array A
    - i and j are the indices of the element to be accessed
    - C is the number of columns in the array A
    - LB1 and LB2 are the lower bounds of the index ranges of the array A for rows and columns, respectively
  - This formula is for row major order. For column major order, the formula is:

    - LOC(A[i][j]) = B + W * (j * R + i - LB1 - LB2 * R), where
      - R is the number of rows in the array A.

- The index formula for a 3-D array is:

  - LOC(A[i][j][k]) = B + W * (i * C * D + j * D + k - LB1 * C * D - LB2 * D - LB3), where
    - LOC(A[i][j][k]) is the address of the element in the ith plane, jth row, and kth column of the array A
    - B is the base address of the array A
    - W is the size of each element of the array A
    - i, j, and k are the indices of the element to be accessed
    - C is the number of columns in each plane of the array A
    - D is the number of planes in the array A
    - LB1, LB2, and LB3 are the lower bounds of the index ranges of the array A for planes, rows, and columns, respectively
  - This formula is for row major order. For column major order, the formula is:

    - LOC(A[i][j][k]) = B + W * (k * R * C + j * R + i - LB1 - LB2 * R - LB3 * R * C), where
      - R is the number of rows in each plane of the array A.

- The index formula for an n-D array is:

  - LOC(A[i1][i2]...[in]) = B + W * (i1 * S2 * S3 * ... * Sn + i2 * S3 * S4 * ... * Sn + ... + in - LB1 * S2 * S3 * ... * Sn - LB2 * S3 * S4 * ... * Sn - ... - LBn), where
    - LOC(A[i1][i2]...[in]) is the address of the element in the i1th dimension, i2th dimension, ..., and inth dimension of the array A
    - B is the base address of the array A
    - W is the size of each element of the array A