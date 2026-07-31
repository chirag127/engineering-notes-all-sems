## 27.WAP that finds the sum of diagonal elements of a mxn matrix.

- A matrix is a rectangular array of numbers arranged in rows and columns.
- A diagonal element of a matrix is an element that lies on the diagonal line that connects the top left corner and the bottom right corner of the matrix.
- A mxn matrix has m rows and n columns, where m and n are positive integers.
- To find the sum of diagonal elements of a mxn matrix, we need to loop through the matrix and add the elements that have the same row and column index, i.e., the elements at positions (i, i) where i ranges from 0 to min(m, n) - 1.
- The following is a pseudocode for a program that finds the sum of diagonal elements of a mxn matrix:

```
// Assume that matrix is a mxn matrix that is given as input
sum = 0 // Initialize the sum to zero
for i = 0 to min(m, n) - 1 // Loop through the diagonal elements
    sum = sum + matrix[i][i] // Add the current element to the sum
end for
print sum // Print the sum
```