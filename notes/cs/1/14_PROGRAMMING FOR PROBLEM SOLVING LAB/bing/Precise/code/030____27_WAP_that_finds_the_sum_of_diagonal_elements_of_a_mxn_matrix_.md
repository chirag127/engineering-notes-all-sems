## 27. WAP that finds the sum of diagonal elements of a mxn matrix.

A matrix is a two-dimensional array of numbers. The diagonal elements of a matrix are the elements that lie on the diagonal line from the top left corner to the bottom right corner of the matrix. The sum of the diagonal elements of a matrix can be found by iterating over the elements of the matrix and adding the elements that lie on the diagonal line.

Here is an example of a program that finds the sum of the diagonal elements of a mxn matrix:

```python
def diagonal_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                sum += matrix[i][j]
    return sum
```

This program defines a function `diagonal_sum` that takes a matrix as an input and returns the sum of its diagonal elements. The function iterates over the rows and columns of the matrix using two nested for loops. If the row index `i` is equal to the column index `j`, the element lies on the diagonal line and is added to the sum. Finally, the sum is returned.

Here is an example of how to use this function:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = diagonal_sum(matrix)
print(result) # 15
```

In this example, the `diagonal_sum` function is called with a 3x3 matrix as an input. The function returns the sum of the diagonal elements, which is 15 in this case. The result is printed to the console.