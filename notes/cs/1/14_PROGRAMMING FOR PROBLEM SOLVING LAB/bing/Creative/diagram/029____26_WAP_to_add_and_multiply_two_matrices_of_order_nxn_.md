Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write a program to add and multiply two matrices of order nxn. Here is the content in markdown format:

## 26.WAP to add and multiply two matrices of order nxn.

A matrix is a rectangular array of numbers arranged in rows and columns. The order of a matrix is the number of rows and columns it has. For example, a matrix of order 3x3 has 3 rows and 3 columns.

To add two matrices of the same order, we simply add the corresponding elements of the matrices and store the result in a new matrix. For example, if A and B are two matrices of order 3x3, then their sum C is given by:

```
C = A + B
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

To multiply two matrices of order nxn, we need to perform a series of dot products between the rows of the first matrix and the columns of the second matrix. The dot product of two vectors is the sum of the products of their corresponding elements. For example, if A and B are two matrices of order 3x3, then their product C is given by:

```
C = A x B
C[0][0] = A[0][0] x B[0][0] + A[0][1] x B[1][0] + A[0][2] x B[2][0]
C[0][1] = A[0][0] x B[0][1] + A[0][1] x B[1][1] + A[0][2] x B[2][1]
C[0][2] = A[0][0] x B[0][2] + A[0][1] x B[1][2] + A[0][2] x B[2][2]
C[1][0] = A[1][0] x B[0][0] + A[1][1] x B[1][0] + A[1][2] x B[2][0]
C[1][1] = A[1][0] x B[0][1] + A[1][1] x B[1][1] + A[1][2] x B[2][1]
C[1][2] = A[1][0] x B[0][2] + A[1][1] x B[1][2] + A[1][2] x B[2][2]
C[2][0] = A[2][0] x B[0][0] + A[2][1] x B[1][0] + A[2][2] x B[2][0]
C[2][1] = A[2][0] x B[0][1] + A[2][1] x B[1][1] + A[2][2] x B[2][1]
C[2][2] = A[2][0] x B[0][2] + A[2][1] x B[1][2] + A[2][2] x B[2][2]
```

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

# Create empty

```
