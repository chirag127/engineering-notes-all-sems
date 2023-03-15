Hello, I am Sydney, your AI assistant. I can help you with your topic of derivation of index formulae for arrays. Here is some information that I found from the web:

### Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index.
- The index formula is a mathematical expression that calculates the address of any element in the array, given the base address, the size of each element, and the index of the element.
- The index formula depends on the order of storing the array elements in the memory, which can be either row major order or column major order.

#### Row Major Order

- In row major order, the elements of the array are stored row by row, starting from the first row and moving to the next row after filling the previous one.
- The index formula for a 1-D array in row major order is:

  - LOC(A[i]) = BA + W * (i - LB)

  - Where LOC(A[i]) is the address of the ith element, BA is the base address, W is the size of each element, and LB is the lower bound of the index.

- The index formula for a 2-D array in row major order is:

  - LOC(A[i][j]) = BA + W * (n * (i - LBR) + (j - LBC))

  - Where LOC(A[i][j]) is the address of the element in the ith row and jth column, BA is the base address, W is the size of each element, n is the number of columns, LBR is the lower bound of the row index, and LBC is the lower bound of the column index.

- The index formula for a 3-D array in row major order is:

  - LOC(A[i][j][k]) = BA + W * (p * n * (i - LBR) + n * (j - LBC) + (k - LBK))

  - Where LOC(A[i][j][k]) is the address of the element in the ith plane, jth row, and kth column, BA is the base address, W is the size of each element, p is the number of planes, n is the number of rows, LBR is the lower bound of the plane index, LBC is the lower bound of the row index, and LBK is the lower bound of the column index.

- The index formula for an n-D array in row major order is:

  - LOC(A[i1][i2]...[in]) = BA + W * (S1 * S2 * ... * Sn-1 * (i1 - LB1) + S2 * S3 * ... * Sn-1 * (i2 - LB2) + ... + Sn-1 * (in-1 - LBn-1) + (in - LBn))

  - Where LOC(A[i1][i2]...[in]) is the address of the element with the indices i1, i2, ..., in, BA is the base address, W is the size of each element, Sj is the size of the jth dimension, LBj is the lower bound of the jth index.

#### Column Major Order

- In column major order, the elements of the array are stored column by column, starting from the first column and moving to the next column after filling the previous one.
- The index formula for a 1-D array in column major order is the same as in row major order:

  - LOC(A[i]) = BA + W * (i - LB)

- The index formula for a 2-D array in column major order is:

  - LOC(A[i][j]) = BA + W * (m * (j - LBC) + (i - LBR))

  - Where LOC(A[i][j]) is the address of the element in the ith row and jth column, BA is the base address, W is the size of each element, m is the number of rows, LBR is the lower bound of the row index, and LBC is the lower bound of the column index.

- The index formula for a 3-D array in column major order is:

  - LOC(A[i][j][k]) = BA + W * (p * m * (k - LBK) + m * (j - LBC) + (i - LBR))

  - Where LOC(A