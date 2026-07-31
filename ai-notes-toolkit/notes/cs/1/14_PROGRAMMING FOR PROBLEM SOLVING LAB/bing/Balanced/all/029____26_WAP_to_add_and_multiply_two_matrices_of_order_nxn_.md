## 26.WAP to add and multiply two matrices of order nxn.

- A matrix is a rectangular array of numbers arranged in rows and columns.
- To add two matrices of order nxn, we need to add the corresponding elements of both matrices and store the result in a new matrix of the same order.
- To multiply two matrices of order nxn, we need to multiply each row of the first matrix with each column of the second matrix and sum up the products to get the elements of the new matrix.
- The following is a pseudocode for adding and multiplying two matrices of order nxn:

```
// Declare three matrices A, B and C of order nxn
matrix A[n][n], B[n][n], C[n][n]

// Input the elements of matrix A
for i = 0 to n-1
  for j = 0 to n-1
    input A[i][j]

// Input the elements of matrix B
for i = 0 to n-1
  for j = 0 to n-1
    input B[i][j]

// Add matrix A and B and store the result in matrix C
for i = 0 to n-1
  for j = 0 to n-1
    C[i][j] = A[i][j] + B[i][j]

// Display the result of matrix addition
print "The sum of matrix A and B is:"
for i = 0 to n-1
  for j = 0 to n-1
    print C[i][j]
  print newline

// Multiply matrix A and B and store the result in matrix C
for i = 0 to n-1
  for j = 0 to n-1
    C[i][j] = 0 // Initialize the element to zero
    for k = 0 to n-1
      C[i][j] = C[i][j] + A[i][k] * B[k][j] // Multiply and add the products

// Display the result of matrix multiplication
print "The product of matrix A and B is:"
for i = 0 to n-1
  for j = 0 to n-1
    print C[i][j]
  print newline
```