## 26. WAP to add and multiply two matrices of order nxn.

A matrix is a two-dimensional array of numbers. Two matrices can be added or multiplied together if they have the same dimensions. Here is an example of how to add and multiply two matrices of order nxn in Python:

```python
n = int(input("Enter the value of n: "))
print("Enter the values for the first matrix: ")
matrix1 = [[int(input()) for x in range(n)] for y in range(n)]
print("Enter the values for the second matrix: ")
matrix2 = [[int(input()) for x in range(n)] for y in range(n)]

# Adding two matrices
result = [[0 for x in range(n)] for y in range(n)]
for i in range(n):
    for j in range(n):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

# Displaying the result
print("The sum of the two matrices is: ")
for r in result:
    print(r)

# Multiplying two matrices
result = [[0 for x in range(n)] for y in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

# Displaying the result
print("The product of the two matrices is: ")
for r in result:
    print(r)
```

This program first takes the value of n as input from the user, which represents the order of the matrices. Then, it takes the values for the first and second matrices as input from the user. The program then adds and multiplies the two matrices and displays the result.

- The addition of two matrices is performed by adding the corresponding elements of the two matrices.
- The multiplication of two matrices is performed by taking the dot product of the rows of the first matrix with the columns of the second matrix.
- The result of the multiplication is a new matrix where the element in the ith row and jth column is the dot product of the ith row of the first matrix and the jth column of the second matrix.
