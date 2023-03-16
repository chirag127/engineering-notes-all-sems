### Symmetric Matrices and Orthogonal Diagonalization

#### Symmetric Matrices
- A square matrix is said to be symmetric if it is equal to its transpose.
- In other words, a matrix `A` is symmetric if `A = A^T`.
- The entries of a symmetric matrix are symmetric with respect to the main diagonal.
- For example, the matrix `A = [[1, 2], [2, 3]]` is symmetric because `A = A^T`.

#### Orthogonal Diagonalization
- A square matrix is said to be orthogonally diagonalizable if it is diagonalizable and its eigenvectors form an orthonormal set.
- In other words, a matrix `A` is orthogonally diagonalizable if there exists an orthogonal matrix `P` such that `P^TAP` is a diagonal matrix.
- Orthogonal diagonalization is a powerful tool for simplifying matrix computations, as it allows us to represent a matrix in terms of its eigenvalues and eigenvectors.
- For example, the matrix `A = [[1, 2], [2, 3]]` is orthogonally diagonalizable because it can be written as `A = PDP^T`, where `P = [[1/sqrt(2), -1/sqrt(2)], [1/sqrt(2), 1/sqrt(2)]]` is an orthogonal matrix and `D = [[-1, 0], [0, 5]]` is a diagonal matrix.
