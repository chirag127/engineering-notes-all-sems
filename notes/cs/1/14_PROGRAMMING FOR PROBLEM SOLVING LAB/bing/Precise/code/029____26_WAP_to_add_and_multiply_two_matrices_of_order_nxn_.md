## 26. WAP to add and multiply two matrices of order nxn.

A matrix is a two-dimensional array of numbers. Two matrices can be added or multiplied if they have the same dimensions. Here is an example of how to add and multiply two matrices of order nxn in Python:

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

# Multiplying two matrices
result2 = [[0 for x in range(n)] for y in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            result2[i][j] += matrix1[i][k] * matrix2[k][j]

# Displaying the result
print("The sum of the two matrices is: ")
for r in result:
    print(r)

print("The product of the two matrices is: ")
for r in result2:
    print(r)
```

This code takes the value of n as input from the user and then takes the values for two matrices of order nxn. It then adds and multiplies the two matrices and displays the result.

- The first step is to take the value of n as input from the user.
- The next step is to take the values for the first and second matrices as input from the user.
- To add two matrices, we create a result matrix of the same dimensions and initialize all its elements to 0.
- We then use nested loops to iterate over the rows and columns of the matrices and add the corresponding elements of the two matrices and store the result in the result matrix.
- To multiply two matrices, we create another result matrix of the same dimensions and initialize all its elements to 0.
- We then use nested loops to iterate over the rows and columns of the matrices and multiply the corresponding elements of the two matrices and store the result in the result matrix.
- Finally, we display the result matrices.

This is how you can add and multiply two matrices of order nxn in Python. You can modify the code to suit your needs.