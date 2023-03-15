## 27. WAP that finds the sum of diagonal elements of a mxn matrix

A matrix is a rectangular array of numbers arranged in rows and columns. The diagonal elements of a matrix are the elements that lie on the line that runs from the top left corner to the bottom right corner of the matrix. The sum of the diagonal elements of a matrix can be found by iterating over the elements of the matrix and adding the elements that lie on the diagonal.

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

This program defines a function `diagonal_sum` that takes a matrix as an argument. The function initializes a variable `sum` to 0, which will be used to keep track of the sum of the diagonal elements. The function then iterates over the elements of the matrix using two nested for loops. The outer loop iterates over the rows of the matrix, while the inner loop iterates over the columns. If the row index `i` is equal to the column index `j`, then the element `matrix[i][j]` lies on the diagonal, and its value is added to the `sum`. Finally, the function returns the value of `sum`.

This program can be used to find the sum of the diagonal elements of any mxn matrix. For example, if we have the following matrix:

```
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
```

We can find the sum of its diagonal elements by calling the `diagonal_sum` function like this:

```python
result = diagonal_sum(matrix)
print(result)
```

This will output `15`, which is the sum of the diagonal elements `1`, `5`, and `9`.