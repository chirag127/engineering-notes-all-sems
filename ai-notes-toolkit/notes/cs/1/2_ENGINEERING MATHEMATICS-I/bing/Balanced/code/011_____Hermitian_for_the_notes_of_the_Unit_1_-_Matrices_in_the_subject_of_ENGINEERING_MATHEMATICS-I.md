### Hermitian Matrix

- A **Hermitian matrix** is a complex square matrix that is equal to its own conjugate transpose .
- The **conjugate transpose** of a matrix is obtained by taking the complex conjugate of each element and then transposing the matrix.
- The **complex conjugate** of a complex number `a + ib` is `a - ib`, where `a` is the real part and `b` is the imaginary part.
- The **diagonal elements** of a Hermitian matrix are always **real numbers** .
- The **non-diagonal elements** of a Hermitian matrix are all **complex numbers**.
- The complex numbers in a Hermitian matrix are such that the element of the `i`th row and `j`th column is the complex conjugate of the element of the `j`th row and `i`th column, for all indices `i` and `j` .
- A Hermitian matrix can be written as `A = A*`, where `A*` denotes the conjugate transpose of `A`.
- A Hermitian matrix has the following properties:
  - It is **symmetric**, meaning `A = A^T`, where `A^T` denotes the transpose of `A`.
  - It is **normal**, meaning `AA* = A*A`, where `A*` denotes the conjugate transpose of `A`.
  - It has **real eigenvalues** and **orthonormal eigenvectors**.
  - It is **diagonalizable** by a unitary matrix, meaning `A = UDU*`, where `U` is a unitary matrix, `D` is a diagonal matrix, and `U*` is the conjugate transpose of `U`.
- An example of a Hermitian matrix is:

```
A = | 2  1+i |
    | 1-i 3  |
```

where `i` is the imaginary unit. We can verify that `A = A*` by computing the conjugate transpose of `A`:

```
A* = | 2  1-i |
     | 1+i 3  |
```

which is equal to `A`.