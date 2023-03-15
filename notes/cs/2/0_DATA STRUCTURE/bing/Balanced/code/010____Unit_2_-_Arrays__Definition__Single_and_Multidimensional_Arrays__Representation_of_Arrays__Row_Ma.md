```markdown
# Unit 2 - Arrays and Linked Lists

## Arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by an index.
- An array can have one or more dimensions, depending on the number of subscripts used to specify an element.
- A one-dimensional array (1-D array) is a linear array, where elements are stored in a single row or column.
- A two-dimensional array (2-D array) is a rectangular array, where elements are stored in rows and columns, forming a matrix.
- A three-dimensional array (3-D array) is a cubic array, where elements are stored in layers of matrices, forming a cube.
- An n-dimensional array (n-D array) is a generalization of the above arrays, where elements are stored in n subscripts, forming a hypercube.

### Representation of Arrays

- Arrays are represented by their name and the number of dimensions in brackets, such as A[3] for a 1-D array, B[2][3] for a 2-D array, C[3][4][5] for a 3-D array, and D[2][3][4][5] for a 4-D array.
- The elements of an array are stored in a linear sequence of memory locations, called the base address of the array.
- The index of an element is the position of the element in the array, starting from zero.
- The address of an element is the memory location where the element is stored, calculated by adding the offset of the element to the base address of the array.
- The offset of an element is the distance of the element from the base address of the array, measured in the number of data elements.

### Row Major Order and Column Major Order

- Row major order and column major order are two ways of storing the elements of a multi-dimensional array in a linear sequence of memory locations.
- In row major order, the elements of a row are stored consecutively, followed by the elements of the next row, and so on. The last subscript of the array varies the fastest.
- In column major order, the elements of a column are stored consecutively, followed by the elements of the next column, and so on. The first subscript of the array varies the fastest.

### Derivation of Index Formulae

- The index formula is an expression that calculates the address of an element in an array, given the base address, the size of each data element, and the index of the element.
- The index formula depends on the number of dimensions, the order of storage, and the lower and upper bounds of each dimension of the array.
- For a 1-D array A[n], the index formula is:

  - Address(A[i]) = Base(A) + Size * (i - L), where L is the lower bound of the array.

- For a 2-D array B[m][n], the index formula is:

  - Address(B[i][j]) = Base(B) + Size * (i * n + j - L1 * n - L2), where L1 and L2 are the lower bounds of the first and second dimensions of the array, respectively, in row major order.
  - Address(B[i][j]) = Base(B) + Size * (i + j * m - L1 - L2 * m), where L1 and L2 are the lower bounds of the first and second dimensions of the array, respectively, in column major order.

- For a 3-D array C[p][q][r], the index formula is:

  - Address(C[i][j][k]) = Base(C) + Size * (i * q * r + j * r + k - L1 * q * r - L2 * r - L3), where L1, L2, and L3 are the lower bounds of the first, second, and third dimensions of the array, respectively, in row major order.
  - Address(C[i][j][k]) = Base(C) + Size * (i + j * p + k * p * q - L1 - L2 * p - L3 * p * q), where L1, L2, and L3 are the lower bounds of the first, second, and third dimensions of the array, respectively, in column major order.

- For an n-D array D[d1][d2]...[dn], the index formula is:

  - Address(D[i1][i2]...[in]) = Base(D) + Size * (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in