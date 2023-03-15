### Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

The index formulae for arrays are used to calculate the memory address of an element in an array. The formulae vary depending on the dimension of the array and the order in which the elements are stored.

#### 1-D Array

A one-dimensional array is a linear data structure where elements are stored in contiguous memory locations. The index formula for a 1-D array is given by:

`Address of A[i] = Base address of A + (i * size of data type)`

where `A` is the name of the array, `i` is the index of the element, and `size of data type` is the number of bytes required to store one element of the array.

#### 2-D Array

A two-dimensional array is a data structure where elements are stored in a matrix form. The index formula for a 2-D array depends on the order in which the elements are stored.

##### Row Major Order

In row major order, the elements are stored row by row. The index formula for a 2-D array in row major order is given by:

`Address of A[i][j] = Base address of A + ((i * number of columns) + j) * size of data type`

where `A` is the name of the array, `i` and `j` are the row and column indices of the element, `number of columns` is the number of columns in the array, and `size of data type` is the number of bytes required to store one element of the array.

##### Column Major Order

In column major order, the elements are stored column by column. The index formula for a 2-D array in column major order is given by:

`Address of A[i][j] = Base address of A + ((j * number of rows) + i) * size of data type`

where `A` is the name of the array, `i` and `j` are the row and column indices of the element, `number of rows` is the number of rows in the array, and `size of data type` is the number of bytes required to store one element of the array.

#### 3-D Array

A three-dimensional array is a data structure where elements are stored in a cube form. The index formula for a 3-D array depends on the order in which the elements are stored.

##### Row Major Order

In row major order, the elements are stored plane by plane, row by row, and column by column. The index formula for a 3-D array in row major order is given by:

`Address of A[i][j][k] = Base address of A + (((i * number of rows * number of columns) + (j * number of columns) + k) * size of data type)`

where `A` is the name of the array, `i`, `j`, and `k` are the indices of the element, `number of rows` and `number of columns` are the number of rows and columns in each plane of the array, and `size of data type` is the number of bytes required to store one element of the array.

##### Column Major Order

In column major order, the elements are stored plane by plane, column by column, and row by row. The index formula for a 3-D array in column major order is given by:

`Address of A[i][j][k] = Base address of A + (((k * number of columns * number of rows) + (j * number of rows) + i) * size of data type)`

where `A` is the name of the array, `i`, `j`, and `k` are the indices of the element, `number of rows` and `number of columns` are the number of rows and columns in each plane of the array, and `size of data type` is the number of bytes required to store one element of the array.

#### n-D Array

The index formula for an n-dimensional array can be derived using the same principles as for 2-D and 3-D arrays. The formula depends on the order in which the elements are stored and the dimensions of the array.