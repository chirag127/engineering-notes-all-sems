## 27.WAP that finds the sum of diagonal elements of a mxn matrix.

- A matrix is a rectangular array of numbers arranged in rows and columns.
- A diagonal element of a matrix is an element that lies on the diagonal line that connects the top left corner and the bottom right corner of the matrix.
- A mxn matrix has m rows and n columns. The diagonal elements of a mxn matrix are the elements with the same row and column index, i.e., a[i][i] for i = 0, 1, ..., min(m, n) - 1.
- To find the sum of diagonal elements of a mxn matrix, we need to loop through the diagonal elements and add them to a variable that stores the sum.
- The following is a pseudocode for finding the sum of diagonal elements of a mxn matrix:

```
// Declare a mxn matrix a and initialize it with some values
// Declare a variable sum and initialize it with zero
sum = 0
// Declare a variable min and assign it the minimum of m and n
min = min(m, n)
// Loop from i = 0 to i = min - 1
for i = 0 to min - 1
  // Add the diagonal element a[i][i] to sum
  sum = sum + a[i][i]
// End of loop
// Print the sum
print(sum)
```