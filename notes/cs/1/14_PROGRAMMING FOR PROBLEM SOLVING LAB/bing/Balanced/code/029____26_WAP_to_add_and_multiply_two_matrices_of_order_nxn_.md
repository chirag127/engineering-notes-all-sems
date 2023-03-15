Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write a program to add and multiply two matrices of order nxn. Here is the content in markdown format:

## 26.WAP to add and multiply two matrices of order nxn.

A matrix is a rectangular array of numbers arranged in rows and columns. The order of a matrix is the number of rows and columns it has. For example, a matrix of order 3x3 has 3 rows and 3 columns.

To add two matrices of the same order, we simply add the corresponding elements of the matrices and store the result in a new matrix. For example, if A and B are two matrices of order 3x3, then their sum C is given by:

```
C[0][0] = A[0][0] + B[0][0]
C[0][1] = A[0][1] + B[0][1]
C[0][2] = A[0][2] + B[0][2]
C[1][0] = A[1][0] + B[1][0]
C[1][1] = A[1][1] + B[1][1]
C[1][2] = A[1][2] + B[1][2]
C[2][0] = A[2][0] + B[2][0]
C[2][1] = A[2][1] + B[2][1]
C[2][2] = A[2][2] + B[2][2]
```

To multiply two matrices of order nxn, we use the following formula:

```
C[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j] + ... + A[i][n-1] * B[n-1][j]
```

where C is the product matrix, A is the first matrix, B is the second matrix, i is the row index, and j is the column index. We repeat this formula for every element of C.

Here is a sample program in Python that can add and multiply two matrices of order nxn:

```python
# Define the order of the matrices
n = 3

# Initialize the matrices with some values
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

# Create empty matrices for the sum and product
C = [[0 for j in range(n)] for i in range(n)]
D = [[0 for j in range(n)] for i in range(n)]

# Add the matrices
for i in range(n):
  for j in range(n):
    C[i][j] = A[i][j] + B[i][j]

# Multiply the matrices
for i in range(n):
  for j in range(n):
    for k in range(n):
      D[i][j] += A[i][k] * B[k][j]

# Print the matrices
print("Matrix A:")
for row in A:
  print(row)

print("Matrix B:")
for row in B:
  print(row)

print("Sum of A and B:")
for row in C:
  print(row)

print("Product of A and B:")
for row in D:
  print(row)
```

The output of this program is:

```
Matrix A:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
Matrix B:
[9, 8, 7]
[6, 5, 4]
[3, 2, 1]
Sum of A and B:
[10, 10, 10]
[10, 10, 10]
[10, 10, 10]
Product of A and B:
[30, 24, 18]
[84, 69, 54]
[138, 114, 90]
```
