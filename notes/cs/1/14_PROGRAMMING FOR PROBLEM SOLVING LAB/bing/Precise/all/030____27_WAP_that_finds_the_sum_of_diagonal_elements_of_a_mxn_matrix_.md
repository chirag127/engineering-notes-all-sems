## 27. WAP that finds the sum of diagonal elements of a mxn matrix

A matrix is a two-dimensional array of numbers. A diagonal of a matrix is a set of elements that run from one corner of the matrix to the opposite corner. In a square matrix, there are two diagonals: the main diagonal and the secondary diagonal. The main diagonal runs from the top-left corner to the bottom-right corner, while the secondary diagonal runs from the top-right corner to the bottom-left corner.

Here is an example of a program that finds the sum of the diagonal elements of a mxn matrix:

```python
def diagonal_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sum = 0
    for i in range(rows):
        for j in range(cols):
            if i == j:
                sum += matrix[i][j]
    return sum
```

This program defines a function called `diagonal_sum` that takes a matrix as an input. The function first determines the number of rows and columns in the matrix. Then, it initializes a variable called `sum` to 0. The function then uses two nested for loops to iterate over the elements of the matrix. If the row index and the column index are the same, the element is on the main diagonal, and its value is added to the `sum`. Finally, the function returns the value of `sum`.

Here is an example of how to use this function:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = diagonal_sum(matrix)
print(result) # 15
```

In this example, we define a 3x3 matrix and pass it to the `diagonal_sum` function. The function returns the sum of the diagonal elements, which is 15. This value is then printed to the screen.