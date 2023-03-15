## 26. WAP to add and multiply two matrices of order nxn.

### Matrix Addition
To add two matrices of order nxn, we follow these steps:
1. Create a new matrix of order nxn to store the result.
2. Loop through each element of both matrices using nested loops.
3. For each element, add the corresponding elements of both matrices and store the result in the new matrix.
4. Return the resulting matrix.

### Matrix Multiplication
To multiply two matrices of order nxn, we follow these steps:
1. Create a new matrix of order nxn to store the result.
2. Loop through each row of the first matrix using the outer loop.
3. Loop through each column of the second matrix using the second loop.
4. Loop through each element of the current row of the first matrix and the current column of the second matrix using the innermost loop.
5. Multiply the corresponding elements and add the result to a variable.
6. Store the final result in the current element of the resulting matrix.
7. Return the resulting matrix.

Here is an example code in Python that adds and multiplies two matrices of order nxn:

```python
def add_matrices(mat1, mat2, n):
    result = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result

def multiply_matrices(mat1, mat2, n):
    result = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result
```

This code defines two functions, `add_matrices` and `multiply_matrices`, that take as input two matrices of order nxn and the order n, and return the resulting matrix after performing the respective operation. The functions use nested loops to iterate over the elements of the matrices and perform the required operations. The resulting matrix is then returned.