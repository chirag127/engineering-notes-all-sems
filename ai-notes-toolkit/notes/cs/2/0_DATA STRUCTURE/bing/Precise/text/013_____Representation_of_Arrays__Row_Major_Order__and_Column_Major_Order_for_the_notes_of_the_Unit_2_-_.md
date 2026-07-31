### Representation of Arrays: Row Major Order, and Column Major Order

- Arrays can be stored in memory in two ways: row-major order and column-major order.
- In row-major order, the elements of an array are stored row by row. The first row is stored first, followed by the second row, and so on.
- In column-major order, the elements of an array are stored column by column. The first column is stored first, followed by the second column, and so on.
- The choice of row-major or column-major order depends on the programming language and the specific application.
- For example, in the C programming language, arrays are stored in row-major order, while in the Fortran programming language, arrays are stored in column-major order.
- The index formula for a 1-D array is `Index = Base + (i * w)`, where `Base` is the base address of the array, `i` is the index of the element, and `w` is the size of each element.
- The index formula for a 2-D array in row-major order is `Index = Base + ((i * n) + j) * w`, where `Base` is the base address of the array, `i` and `j` are the row and column indices of the element, `n` is the number of columns, and `w` is the size of each element.
- The index formula for a 2-D array in column-major order is `Index = Base + ((j * m) + i) * w`, where `Base` is the base address of the array, `i` and `j` are the row and column indices of the element, `m` is the number of rows, and `w` is the size of each element.
- These index formulae can be extended to n-D arrays.