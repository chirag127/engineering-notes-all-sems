## 27. WAP that finds the sum of diagonal elements of a mxn matrix.

A matrix is a rectangular array of numbers arranged in rows and columns. The diagonal of a matrix is a straight line that connects the upper left corner to the lower right corner, or the upper right corner to the lower left corner. The diagonal elements of a matrix are the elements that lie on this line.

In this program, we will write a Python code to find the sum of diagonal elements of a mxn matrix. Here are the steps to do this:

1. Create a matrix of size mxn using nested lists or NumPy library.
2. Initialize a variable `sum` to 0.
3. Use nested loops to iterate through each element of the matrix.
4. For each element, check if it lies on the diagonal by comparing its row index with its column index.
5. If it lies on the diagonal, add its value to the variable `sum`.
6. After iterating through all elements, print the value of `sum`.

Here's the Python code for the above steps:

```python
# Using nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            sum += matrix[i][j]

print("Sum of diagonal elements:", sum)

# Using NumPy library
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sum = np.trace(matrix)

print("Sum of diagonal elements:", sum)
```

In the above code, we have used two methods to create a matrix - one using nested lists and the other using the NumPy library. The first method is suitable for small matrices, while the second method is more efficient for large matrices.

In the first method, we have used nested loops to iterate through each element of the matrix. We have checked if an element lies on the diagonal by comparing its row index with its column index. If it lies on the diagonal, we have added its value to the variable `sum`. Finally, we have printed the value of `sum`.

In the second method, we have used the `trace` function of the NumPy library to find the sum of diagonal elements. The `trace` function returns the sum of diagonal elements of a matrix. We have assigned the value of `trace` function to the variable `sum` and printed its value.

In conclusion, we have learned how to write a Python program to find the sum of diagonal elements of a mxn matrix. We have used nested lists and the NumPy library to create a matrix and used nested loops and the `trace` function to find the sum of diagonal elements.