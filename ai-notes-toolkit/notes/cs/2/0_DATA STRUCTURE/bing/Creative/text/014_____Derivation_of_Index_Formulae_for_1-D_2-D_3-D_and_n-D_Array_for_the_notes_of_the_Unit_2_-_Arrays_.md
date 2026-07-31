### Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index.
- The index formula is a mathematical expression that calculates the address of any element in an array, given its base address, size, and dimensions.
- The index formula depends on the order of storing the array elements in memory, which can be either row major order or column major order.
- In row major order, the elements of an array are stored row by row, i.e., the elements of the first row are stored first, followed by the elements of the second row, and so on.
- In column major order, the elements of an array are stored column by column, i.e., the elements of the first column are stored first, followed by the elements of the second column, and so on.

#### Index Formula for 1-D Array

- A 1-D array is a linear array that has only one dimension, i.e., a single row or column of elements.
- The index formula for a 1-D array in row major order is:

  - `LOC(A[i]) = BA + W * (i - LB)`

  - where LOC(A[i]) is the address of the ith element of the array A, BA is the base address of the array, W is the size of each element, i is the index of the element, and LB is the lower bound of the index.

- The index formula for a 1-D array in column major order is the same as the row major order, since there is no difference in the order of storing the elements.

#### Index Formula for 2-D Array

- A 2-D array is a rectangular array that has two dimensions, i.e., rows and columns of elements.
- The index formula for a 2-D array in row major order is:

  - `LOC(A[i][j]) = BA + W * (n * (i - LBR) + (j - LBC))`

  - where LOC(A[i][j]) is the address of the element in the ith row and jth column of the array A, BA is the base address of the array, W is the size of each element, n is the number of columns in the array, i and j are the indices of the element, and LBR and LBC are the lower bounds of the row and column indices, respectively.

- The index formula for a 2-D array in column major order is:

  - `LOC(A[i][j]) = BA + W * (m * (j - LBC) + (i - LBR))`

  - where LOC(A[i][j]) is the address of the element in the ith row and jth column of the array A, BA is the base address of the array, W is the size of each element, m is the number of rows in the array, i and j are the indices of the element, and LBR and LBC are the lower bounds of the row and column indices, respectively.

#### Index Formula for 3-D Array

- A 3-D array is a cuboidal array that has three dimensions, i.e., rows, columns, and layers of elements.
- The index formula for a 3-D array in row major order is:

  - `LOC(A[i][j][k]) = BA + W * (n * p * (i - LBR) + p * (j - LBC) + (k - LBL))`

  - where LOC(A[i][j][k]) is the address of the element in the ith row, jth column, and kth layer of the array A, BA is the base address of the array, W is the size of each element, n and p are the number of columns and layers in the array, i, j, and k are the indices of the element, and LBR, LBC, and LBL are the lower bounds of the row, column, and layer indices, respectively.

- The index formula for a 3-D array in column major order is:

  - `LOC(A[i][j][k]) = BA + W * (m * p * (k - LBL) + m * (j - LBC) + (i - LBR))`

  - where LOC(A[i][j][k]) is the address of the element in the ith row, jth column, and kth layer of the array A, BA is the base