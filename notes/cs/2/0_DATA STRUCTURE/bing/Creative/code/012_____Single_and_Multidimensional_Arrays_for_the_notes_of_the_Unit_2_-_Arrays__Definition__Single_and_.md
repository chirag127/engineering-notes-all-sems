```markdown
# Single and Multidimensional Arrays

## Definition
- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by an index.
- An array can have one or more dimensions, depending on the number of subscripts used to specify the position of an element.
- A single-dimensional array is also called a vector or a list, and has one subscript that ranges from 0 to n-1, where n is the size of the array.
- A multidimensional array is also called a matrix or a table, and has two or more subscripts that range from 0 to m-1 and 0 to p-1, where m and p are the sizes of the respective dimensions.
- For example, a two-dimensional array of integers can be declared as int A[3][4], which means that A has 3 rows and 4 columns, and each element is an integer.

## Representation of Arrays
- Arrays are stored in memory in either row-major order or column-major order, depending on the programming language or the convention used.
- In row-major order, the elements of an array are stored row by row, starting from the first row and ending with the last row. The elements of each row are stored in consecutive memory locations.
- In column-major order, the elements of an array are stored column by column, starting from the first column and ending with the last column. The elements of each column are stored in consecutive memory locations.
- For example, consider the following two-dimensional array of integers:

| A[0][0] | A[0][1] | A[0][2] | A[0][3] |
|---------|---------|---------|---------|
| A[1][0] | A[1][1] | A[1][2] | A[1][3] |
| A[2][0] | A[2][1] | A[2][2] | A[2][3] |

- In row-major order, the elements are stored as:

| A[0][0] | A[0][1] | A[0][2] | A[0][3] | A[1][0] | A[1][1] | A[1][2] | A[1][3] | A[2][0] | A[2][1] | A[2][2] | A[2][3] |

- In column-major order, the elements are stored as:

| A[0][0] | A[1][0] | A[2][0] | A[0][1] | A[1][1] | A[2][1] | A[0][2] | A[1][2] | A[2][2] | A[0][3] | A[1][3] | A[2][3] |

## Derivation of Index Formulae
- To access an element of an array, we need to calculate its address in memory, based on the base address of the array, the size of each element, and the subscripts of the element.
- The formula for calculating the address of an element depends on whether the array is stored in row-major order or column-major order, and on the number of dimensions of the array.
- For a single-dimensional array A of size n, stored in row-major order, the address of A[i] is given by:

`address(A[i]) = base(A) + i * size(A[0])`

- where base(A) is the base address of the array, and size(A[0]) is the size of each element.
- For a two-dimensional array A of size m x p, stored in row-major order, the address of A[i][j] is given by:

`address(A[i][j]) = base(A) + (i * p + j) * size(A[0][0])`

- where base(A) is the base address of the array, and size(A[0][0]) is the size of each element.
- For a two-dimensional array A of size m x p, stored in column-major order, the address of A[i][j] is given by:

`address(A[i][j]) = base(A) + (j * m + i) * size(A[0][0])`

- where base(A) is the base address of the array, and size(A[0][0]) is the size of each element.
- For a three-dimensional array A of size m x p x q, stored in row-major order, the address of A[i][j][k] is given by:

`address(A