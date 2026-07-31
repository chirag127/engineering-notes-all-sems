## 27. WAP that finds the sum of diagonal elements of a mxn matrix.

To find the sum of diagonal elements of a mxn matrix, we can follow the below steps:

1. Initialize the sum variable as 0.
2. Loop through each row and column of the matrix using nested loops.
3. Check if the current element is on the diagonal (i.e., if the row and column index are equal).
4. If the element is on the diagonal, add it to the sum variable.
5. After looping through all the elements, print the sum variable.

Here is the Python code for the same:

```python
# initialize a mxn matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# initialize sum variable
sum = 0

# loop through each row and column
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        # check if element is on diagonal
        if i == j:
            # add element to sum
            sum += matrix[i][j]

# print the sum of diagonal elements
print("Sum of diagonal elements:", sum)
```

It is important to note that this code assumes that the matrix is a square matrix (i.e., m = n). If the matrix is not square, we need to modify the code accordingly. Additionally, if the matrix contains non-numeric elements, we need to add error handling to handle such cases.