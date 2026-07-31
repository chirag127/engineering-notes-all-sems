Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write a program to add and multiply two matrices of order nxn. Here is the content in markdown format:

## 26.WAP to add and multiply two matrices of order nxn.

A matrix is a rectangular array of numbers arranged in rows and columns. The order of a matrix is the number of rows and columns it has. For example, a matrix of order 3x3 has 3 rows and 3 columns.

To add two matrices of the same order, we simply add the corresponding elements of the matrices and store the result in a new matrix. For example, if A and B are two matrices of order 3x3, then their sum C is given by:

```
C = A + B
  = | a11 a12 a13 |   | b11 b12 b13 |   | a11 + b11 a12 + b12 a13 + b13 |
    | a21 a22 a23 | + | b21 b22 b23 | = | a21 + b21 a22 + b22 a23 + b23 |
    | a31 a32 a33 |   | b31 b32 b33 |   | a31 + b31 a32 + b32 a33 + b33 |
```

To multiply two matrices of order nxn, we use the following formula:

```
C = A x B
  = | a11 a12 ... a1n |   | b11 b12 ... b1n |   | c11 c12 ... c1n |
    | a21 a22 ... a2n | x | b21 b22 ... b2n | = | c21 c22 ... c2n |
    | ... ... ... ... |   | ... ... ... ... |   | ... ... ... ... |
    | an1 an2 ... ann |   | bn1 bn2 ... bnn |   | cn1 cn2 ... cnn |
```

where

```
cij = a1i x b1j + a2i x b2j + ... + ani x bnj
```

for i = 1, 2, ..., n and j = 1, 2, ..., n.

Here is a pseudocode for a program that can add and multiply two matrices of order nxn:

```
// Input the order of the matrices
n = input("Enter the order of the matrices: ")

// Declare two matrices A and B of order nxn
A = array[n][n]
B = array[n][n]

// Input the elements of matrix A
print("Enter the elements of matrix A: ")
for i = 0 to n-1
  for j = 0 to n-1
    A[i][j] = input()

// Input the elements of matrix B
print("Enter the elements of matrix B: ")
for i = 0 to n-1
  for j = 0 to n-1
    B[i][j] = input()

// Declare a matrix C to store the sum of A and B
C = array[n][n]

// Add A and B and store the result in C
for i = 0 to n-1
  for j = 0 to n-1
    C[i][j] = A[i][j] + B[i][j]

// Print the sum of A and B
print("The sum of A and B is: ")
for i = 0 to n-1
  for j = 0 to n-1
    print(C[i][j], end=" ")
  print()

// Declare a matrix D to store the product of A and B
D = array[n][n]

// Multiply A and B and store the result in D
for i = 0 to n-1
  for j = 0 to n-1
    D[i][j] = 0
    for k = 0 to n-1
      D[i][j] = D[i][j] + A[i][k] x B[k][j]

// Print the product of A and B
print("The product of A and B is: ")
for i = 0 to n-1
  for j = 0 to n-1
    print(D[i][j], end=" ")
  print()
```