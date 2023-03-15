### Hermitian Matrix

- A hermitian matrix is a complex square matrix that is equal to its own conjugate transpose .
- The conjugate transpose of a matrix is obtained by taking the complex conjugate of each element and then transposing the matrix.
- The complex conjugate of a complex number a + ib is a - ib, where i is the imaginary unit.
- The diagonal elements of a hermitian matrix are always real numbers, while the non-diagonal elements are complex numbers .
- The element in the i-th row and j-th column of a hermitian matrix is equal to the complex conjugate of the element in the j-th row and i-th column, for all indices i and j .
- In matrix form, a hermitian matrix A satisfies the equation A = A^H, where A^H is the conjugate transpose of A.
- For example, the matrix

```
A = | 2  3 + i |
    | 3 - i  4 |
```

is a hermitian matrix, because

```
A^H = | 2  3 - i |
      | 3 + i  4 |
```

and A = A^H.

- Some properties of hermitian matrices are :

  - The sum of two hermitian matrices is also a hermitian matrix.
  - The product of two hermitian matrices is hermitian if and only if they commute, i.e., AB = BA.
  - The inverse of a hermitian matrix is also a hermitian matrix, if it exists.
  - The eigenvalues of a hermitian matrix are always real numbers.
  - The eigenvectors of a hermitian matrix corresponding to distinct eigenvalues are orthogonal to each other.
  - A hermitian matrix is positive definite if and only if all its eigenvalues are positive.