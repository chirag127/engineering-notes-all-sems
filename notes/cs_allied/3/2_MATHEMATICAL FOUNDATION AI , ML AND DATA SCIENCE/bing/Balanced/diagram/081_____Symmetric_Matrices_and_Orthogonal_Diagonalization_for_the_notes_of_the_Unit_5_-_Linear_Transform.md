### Symmetric Matrices and Orthogonal Diagonalization

- A symmetric matrix is a square matrix that is equal to its transpose, i.e., A = A^T^.
- A symmetric matrix has real eigenvalues and orthogonal eigenvectors.
- An orthogonal matrix is a square matrix whose columns (or rows) are orthonormal, i.e., Q^T^Q = QQ^T^ = I.
- An orthogonal matrix preserves the length and angle of vectors, i.e., ||Qx|| = ||x|| and <Qx, Qy> = <x, y>.
- An orthogonal matrix has determinant 1 or -1 and inverse Q^T^.
- A matrix A is orthogonally diagonalizable if there exists an orthogonal matrix P and a diagonal matrix D such that A = PDP^T^.
- A symmetric matrix is orthogonally diagonalizable by the spectral theorem.
- To orthogonally diagonalize a symmetric matrix A, we need to find an orthonormal basis of eigenvectors of A and form the matrix P with these eigenvectors as columns. Then D is the diagonal matrix with the corresponding eigenvalues of A on the diagonal.
- Orthogonal diagonalization simplifies the computation of powers of a matrix, i.e., A^k^ = PD^k^P^T^.
- Orthogonal diagonalization also allows us to write a quadratic form as a sum of squares, i.e., x^T^Ax = y^T^Dy, where y = P^T^x and D is the diagonal matrix of eigenvalues of A.