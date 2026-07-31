## 26. WAP to add and multiply two matrices of order nxn

In linear algebra, a matrix is a rectangular array of numbers, symbols, or expressions arranged in rows and columns. Matrices are essential tools in many fields, including engineering, physics, computer graphics, and economics. In this topic, we will discuss how to add and multiply two matrices of order nxn.

### Matrix Addition

Matrix addition is the process of adding two matrices of the same order. The order of a matrix is defined as the number of rows and columns it contains. To add two matrices, we add the corresponding elements of the two matrices.

The steps to add two matrices of order nxn are as follows:

1. Create two matrices of the same order, say A and B.
2. Create a new matrix, say C, of the same order as A and B.
3. For each element in the matrices A and B, add the corresponding elements and store the result in the corresponding element of matrix C.
4. The resulting matrix C is the sum of matrices A and B.

Example:

Let A and B be two matrices of order 2x2.

```
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]
```

To find the sum of matrices A and B, we add the corresponding elements of A and B.

```
C = [[A[0][0] + B[0][0], A[0][1] + B[0][1]],
     [A[1][0] + B[1][0], A[1][1] + B[1][1]]]

C = [[6, 8],
     [10, 12]]
```

Therefore, the sum of matrices A and B is `[[6, 8], [10, 12]]`.

### Matrix Multiplication

Matrix multiplication is the process of multiplying two matrices to produce a third matrix. The resulting matrix has the same number of rows as the first matrix and the same number of columns as the second matrix.

The steps to multiply two matrices of order nxn are as follows:

1. Create two matrices of the same order, say A and B.
2. Create a new matrix, say C, of the same order as A and B.
3. For each element in the resulting matrix C, calculate the dot product of the corresponding row of matrix A and column of matrix B.
4. Store the resulting dot product in the corresponding element of matrix C.
5. The resulting matrix C is the product of matrices A and B.

Example:

Let A and B be two matrices of order 2x2.

```
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]
```

To find the product of matrices A and B, we calculate the dot product of the corresponding row of matrix A and column of matrix B.

```
C = [[A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
     [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]]

C = [[19, 22],
     [43, 50]]
```

Therefore, the product of matrices A and B is `[[19, 22], [43, 50]]`.

In conclusion, adding and multiplying two matrices of order nxn is an essential operation in linear algebra. These operations have numerous applications in various fields, including engineering, physics, computer graphics, and economics.