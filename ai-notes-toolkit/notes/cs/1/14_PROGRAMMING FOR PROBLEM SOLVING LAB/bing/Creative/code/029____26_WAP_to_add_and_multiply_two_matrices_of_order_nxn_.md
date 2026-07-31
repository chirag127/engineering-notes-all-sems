## 26.WAP to add and multiply two matrices of order nxn.

A matrix is a rectangular array of numbers arranged in rows and columns. The order of a matrix is the number of rows and columns it has. For example, a matrix of order 3x3 has 3 rows and 3 columns.

To add two matrices of the same order, we simply add the corresponding elements of each matrix and place the result in a new matrix of the same order. For example, if A and B are two matrices of order 3x3, then their sum C is given by:

C = A + B

C = [[a11 + b11, a12 + b12, a13 + b13],
     [a21 + b21, a22 + b22, a23 + b23],
     [a31 + b31, a32 + b32, a33 + b33]]

To multiply two matrices, the number of columns of the first matrix must be equal to the number of rows of the second matrix. The product of two matrices A and B of order m x n and n x p respectively, is a matrix C of order m x p, where each element cij is given by:

cij = a1i * b1j + a2i * b2j + ... + ani * bnj

For example, if A and B are two matrices of order 2x3 and 3x2 respectively, then their product C is given by:

C = A * B

C = [[a11 * b11 + a12 * b21 + a13 * b31, a11 * b12 + a12 * b22 + a13 * b32],
     [a21 * b11 + a22 * b21 + a23 * b31, a21 * b12 + a22 * b22 + a23 * b32]]

A pseudocode to add and multiply two matrices of order nxn is given below:

```
# Input the order of the matrices
n = input("Enter the order of the matrices: ")

# Initialize the matrices A, B and C
A = [[0 for i in range(n)] for j in range(n)]
B = [[0 for i in range(n)] for j in range(n)]
C = [[0 for i in range(n)] for j in range(n)]

# Input the elements of matrix A
print("Enter the elements of matrix A: ")
for i in range(n):
  for j in range(n):
    A[i][j] = input()

# Input the elements of matrix B
print("Enter the elements of matrix B: ")
for i in range(n):
  for j in range(n):
    B[i][j] = input()

# Add the matrices A and B and store the result in C
for i in range(n):
  for j in range(n):
    C[i][j] = A[i][j] + B[i][j]

# Print the sum of the matrices
print("The sum of the matrices is: ")
for i in range(n):
  for j in range(n):
    print(C[i][j], end=" ")
  print()

# Multiply the matrices A and B and store the result in C
for i in range(n):
  for j in range(n):
    C[i][j] = 0 # Reset the element to zero
    for k in range(n):
      C[i][j] = C[i][j] + A[i][k] * B[k][j]

# Print the product of the matrices
print("The product of the matrices is: ")
for i in range(n):
  for j in range(n):
    print(C[i][j], end=" ")
  print()
```