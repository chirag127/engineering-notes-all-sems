## Unit 1 - Matrices

A matrix is a rectangular array of numbers, symbols, or expressions, arranged in rows and columns. For example, the following is a matrix:

```
| 1  2  3 |
| 4  5  6 |
| 7  8  9 |
```

The dimensions of a matrix are the number of rows and columns it has. For example, the matrix above has 3 rows and 3 columns, so its dimensions are 3 x 3.

Some important types of matrices are:

- A square matrix is a matrix that has the same number of rows and columns. For example, the matrix above is a square matrix.
- A diagonal matrix is a square matrix that has nonzero entries only on the main diagonal (from the top left to the bottom right). For example, the following is a diagonal matrix:

```
| 1  0  0 |
| 0  2  0 |
| 0  0  3 |
```

- An identity matrix is a diagonal matrix that has 1s on the main diagonal and 0s elsewhere. For example, the following is an identity matrix:

```
| 1  0  0 |
| 0  1  0 |
| 0  0  1 |
```

- A zero matrix is a matrix that has all entries equal to zero. For example, the following is a zero matrix:

```
| 0  0  0 |
| 0  0  0 |
| 0  0  0 |
```

- A row matrix is a matrix that has only one row. For example, the following is a row matrix:

```
| 1  2  3 |
```

- A column matrix is a matrix that has only one column. For example, the following is a column matrix:

```
| 1 |
| 2 |
| 3 |
```

- A scalar matrix is a diagonal matrix that has the same nonzero entry on the main diagonal. For example, the following is a scalar matrix:

```
| 2  0  0 |
| 0  2  0 |
| 0  0  2 |
```

- A symmetric matrix is a square matrix that is equal to its transpose. The transpose of a matrix is obtained by swapping the rows and columns. For example, the following is a symmetric matrix:

```
| 1  2  3 |
| 2  4  5 |
| 3  5  6 |
```

- A skew-symmetric matrix is a square matrix that is equal to the negative of its transpose. For example, the following is a skew-symmetric matrix:

```
| 0  2 -3 |
|-2  0  5 |
| 3 -5  0 |
```

Some basic operations on matrices are:

- Addition: Two matrices can be added if they have the same dimensions. The sum of two matrices is obtained by adding the corresponding entries. For example:

```
| 1  2  3 |   | 4  5  6 |   | 1+4  2+5  3+6 |
| 4  5  6 | + | 7  8  9 | = | 4+7  5+8  6+9 |
| 7  8  9 |   | 1  2  3 |   | 7+1  8+2  9+3 |
```

- Subtraction: Two matrices can be subtracted if they have the same dimensions. The difference of two matrices is obtained by subtracting the corresponding entries. For example:

```
| 1  2  3 |   | 4  5  6 |   | 1-4  2-5  3-6 |
| 4  5  6 | - | 7  8  9 | = | 4-7  5-8  6-9 |
| 7  8  9 |   | 1  2  3 |   | 7-1  8-2  9-3 |
```

- Scalar multiplication: A matrix can be multiplied by a scalar (a number). The product of a scalar and a matrix is obtained by multiplying each entry of the matrix by the scalar. For example:

```
2 x | 1  2