## Unit 1 - Matrices

A matrix is a rectangular array of numbers, symbols, or expressions, arranged in rows and columns. For example, the following is a matrix with 2 rows and 3 columns:

```
| 1  2  3 |
| 4  5  6 |
```

The numbers, symbols, or expressions in a matrix are called its elements or entries. The horizontal lines of elements are called rows and the vertical lines of elements are called columns. The size or order of a matrix is given by the number of rows and columns it has. For example, the matrix above has size 2 x 3.

Some important types of matrices are:

- A square matrix is a matrix with the same number of rows and columns. For example, the following is a square matrix of size 3 x 3:

```
| 1  2  3 |
| 4  5  6 |
| 7  8  9 |
```

- A diagonal matrix is a square matrix in which all the elements outside the main diagonal are zero. The main diagonal is the line of elements from the top left to the bottom right of the matrix. For example, the following is a diagonal matrix of size 3 x 3:

```
| 1  0  0 |
| 0  2  0 |
| 0  0  3 |
```

- An identity matrix is a diagonal matrix in which all the elements on the main diagonal are one. It is denoted by I or I_n, where n is the size of the matrix. For example, the following is the identity matrix of size 3 x 3:

```
| 1  0  0 |
| 0  1  0 |
| 0  0  1 |
```

- A zero matrix is a matrix in which all the elements are zero. It is denoted by O or O_mn, where m and n are the number of rows and columns of the matrix. For example, the following is the zero matrix of size 2 x 3:

```
| 0  0  0 |
| 0  0  0 |
```

- A row matrix is a matrix with only one row. For example, the following is a row matrix of size 1 x 3:

```
| 1  2  3 |
```

- A column matrix is a matrix with only one column. For example, the following is a column matrix of size 3 x 1:

```
| 1 |
| 2 |
| 3 |
```

- A scalar matrix is a diagonal matrix in which all the elements on the main diagonal are the same. For example, the following is a scalar matrix of size 3 x 3 with the scalar value 4:

```
| 4  0  0 |
| 0  4  0 |
| 0  0  4 |
```

- A triangular matrix is a square matrix in which all the elements above or below the main diagonal are zero. A triangular matrix can be either upper triangular or lower triangular. For example, the following is an upper triangular matrix of size 3 x 3:

```
| 1  2  3 |
| 0  4  5 |
| 0  0  6 |
```

And the following is a lower triangular matrix of size 3 x 3:

```
| 1  0  0 |
| 2  3  0 |
| 4  5  6 |
```

- A symmetric matrix is a square matrix that is equal to its transpose. The transpose of a matrix is obtained by interchanging the rows and columns of the matrix. For example, the following is a symmetric matrix of size 3 x 3:

```
| 1  2  3 |
| 2  4  5 |
| 3  5  6 |
```

Its transpose is also the same:

```
| 1  2  3 |
| 2  4  5 |
| 3  5  6 |
```

- A skew-symmetric matrix is a square matrix that is equal to the negative of its transpose. For example, the following is a skew-symmetric matrix of size 3 x 3:

```
| 0  2 -3 |
|-2  0  4 |
| 3 -4  0 |
```

Its transpose is the negative of