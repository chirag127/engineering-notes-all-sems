## 27. WAP that finds the sum of diagonal elements of a mxn matrix.

A matrix is a two-dimensional array of numbers. A diagonal of a matrix is a set of elements that run from one corner of the matrix to the opposite corner. In a square matrix, there are two diagonals: the main diagonal and the secondary diagonal. The main diagonal runs from the top-left corner to the bottom-right corner, while the secondary diagonal runs from the top-right corner to the bottom-left corner.

Here is an example of a program that finds the sum of the diagonal elements of a mxn matrix in Python:

```python
def diagonal_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    for i in range(rows):
        for j in range(cols):
            if i == j:
                main_diagonal_sum += matrix[i][j]
            if i + j == cols - 1:
                secondary_diagonal_sum += matrix[i][j]
    return main_diagonal_sum, secondary_diagonal_sum
```

This program defines a function `diagonal_sum` that takes a matrix as an input and returns the sum of the main diagonal and the secondary diagonal. The function iterates over the rows and columns of the matrix using two nested for loops. If the row and column indices are equal, the element is on the main diagonal and is added to the `main_diagonal_sum`. If the sum of the row and column indices is equal to the number of columns minus one, the element is on the secondary diagonal and is added to the `secondary_diagonal_sum`. Finally, the function returns the sum of the main and secondary diagonals.

Here is an example of how to use the `diagonal_sum` function:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
main_diagonal_sum, secondary_diagonal_sum = diagonal_sum(matrix)
print(f"Main diagonal sum: {main_diagonal_sum}")
print(f"Secondary diagonal sum: {secondary_diagonal_sum}")
```

This code creates a 3x3 matrix and passes it to the `diagonal_sum` function. The function returns the sum of the main and secondary diagonals, which are printed to the console. The output of this code is:

```
Main diagonal sum: 15
Secondary diagonal sum: 15
```

This shows that the sum of the main diagonal is 15 and the sum of the secondary diagonal is also 15.