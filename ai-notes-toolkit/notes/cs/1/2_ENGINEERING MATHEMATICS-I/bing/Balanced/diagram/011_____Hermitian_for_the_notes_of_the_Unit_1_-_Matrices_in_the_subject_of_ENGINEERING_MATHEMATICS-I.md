### Hermitian Matrix

- A hermitian matrix is a complex square matrix that is equal to its own conjugate transpose .
- The conjugate transpose of a matrix is obtained by taking the complex conjugate of each element and then transposing the matrix.
- The complex conjugate of a complex number `a + ib` is `a - ib`, where `a` is the real part and `b` is the imaginary part.
- The diagonal elements of a hermitian matrix are always real numbers, while the non-diagonal elements are complex numbers .
- The complex numbers in a hermitian matrix are such that the element of the `i`th row and `j`th column is the complex conjugate of the element of the `j`th row and `i`th column, for all indices `i` and `j` .
- A hermitian matrix can be written in the form `A = A*`, where `A*` denotes the conjugate transpose of `A`.
- A hermitian matrix has some important properties, such as :
  - It has only real eigenvalues.
  - It has orthogonal eigenvectors, which can form an orthonormal basis for the vector space.
  - It is diagonalizable by a unitary matrix, which means `A = UDU*`, where `U` is a unitary matrix and `D` is a diagonal matrix with the eigenvalues of `A` on the diagonal.
  - It is positive definite if all its eigenvalues are positive, and positive semidefinite if all its eigenvalues are non-negative.
- An example of a hermitian matrix is:

```
A = [2  1+i  4-i]
    [1-i  3  0  ]
    [4+i  0  5  ]
```

- The conjugate transpose of `A` is:

```
A* = [2  1-i  4+i]
     [1+i  3  0  ]
     [4-i  0  5  ]
```

- We can see that `A = A*`, so `A` is a hermitian matrix. The diagonal elements of `A` are real numbers, and the non-diagonal elements are complex numbers that are conjugate to each other. The eigenvalues of `A` are `9.4142`, `2.5858`, and `-2`, which are all real numbers. The eigenvectors of `A` are orthogonal to each other, and can be normalized to form an orthonormal basis.