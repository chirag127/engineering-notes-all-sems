### Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

An array is a data structure that stores a collection of elements, which can be of any data type, such as integers, characters, or strings. The elements are stored in contiguous memory locations and can be accessed using an index. The index formulae for 1-D, 2-D, 3-D, and n-D arrays are used to calculate the memory address of an element in the array.

#### 1-D Array

A 1-D array is a linear array, where the elements are stored in a single row. The index formula for a 1-D array is given by:

`Address of A[i] = Base address of A + (i * size of data type)`

where `A` is the name of the array, `i` is the index of the element, and `size of data type` is the number of bytes required to store a single element of the array.

#### 2-D Array

A 2-D array is a rectangular array, where the elements are stored in rows and columns. The index formula for a 2-D array is given by:

`Address of A[i][j] = Base address of A + ((i * number of columns + j) * size of data type)`

where `A` is the name of the array, `i` and `j` are the row and column indices of the element, `number of columns` is the number of columns in the array, and `size of data type` is the number of bytes required to store a single element of the array.

#### 3-D Array

A 3-D array is an array where the elements are stored in a three-dimensional grid. The index formula for a 3-D array is given by:

`Address of A[i][j][k] = Base address of A + (((i * number of rows + j) * number of columns + k) * size of data type)`

where `A` is the name of the array, `i`, `j`, and `k` are the indices of the element along the three dimensions, `number of rows` and `number of columns` are the number of rows and columns in the array, and `size of data type` is the number of bytes required to store a single element of the array.

#### n-D Array

An n-D array is an array where the elements are stored in an n-dimensional grid. The index formula for an n-D array is given by:

`Address of A[i1][i2]...[in] = Base address of A + (((...((i1 * size[i2] + i2) * size[i3] + i3)...)*size[in-1] + in-1)*size[in] + in) * size of data type)`

where `A` is the name of the array, `i1`, `i2`, ..., `in` are the indices of the element along the n dimensions, `size[i]` is the size of the `i-th` dimension, and `size of data type` is the number of bytes required to store a single element of the array.

These index formulae are used to calculate the memory address of an element in an array, which is useful for accessing and manipulating the elements of the array. They are derived based on the way the elements are stored in memory and the dimensions of the array.