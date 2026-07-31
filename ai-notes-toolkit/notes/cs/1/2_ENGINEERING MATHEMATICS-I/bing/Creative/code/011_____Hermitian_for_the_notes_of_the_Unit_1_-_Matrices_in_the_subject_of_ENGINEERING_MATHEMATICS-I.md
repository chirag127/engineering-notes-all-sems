### Hermitian Matrix

- A hermitian matrix is a complex square matrix that is equal to its own conjugate transpose .
- The conjugate transpose of a matrix is obtained by taking the complex conjugate of each element and then transposing the matrix.
- The complex conjugate of a complex number is obtained by changing the sign of the imaginary part.
- The diagonal elements of a hermitian matrix are always real numbers   .
- The non-diagonal elements of a hermitian matrix are complex numbers that satisfy the property that the element in the i-th row and j-th column is the complex conjugate of the element in the j-th row and i-th column .
- A hermitian matrix can be written in the form A = A* where A* denotes the conjugate transpose of A .
- A hermitian matrix has some important properties, such as :
  - It has real eigenvalues.
  - It has orthogonal eigenvectors.
  - It is diagonalizable by a unitary matrix.
  - It is positive definite if and only if all its eigenvalues are positive.
  - It is negative definite if and only if all its eigenvalues are negative.
  - It is indefinite if it has both positive and negative eigenvalues.
- An example of a hermitian matrix is:

```
A = [2  1+i  4-i]
    [1-i  3  0  ]
    [4+i  0  1  ]
```

- The conjugate transpose of A is:

```
A* = [2  1-i  4+i]
     [1+i  3  0  ]
     [4-i  0  1  ]
```

- We can see that A = A*, so A is a hermitian matrix.