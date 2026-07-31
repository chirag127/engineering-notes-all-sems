### Symmetric Matrices and Orthogonal Diagonalization

- A symmetric matrix is a square matrix that is equal to its transpose, i.e., A = A^T^.
- A symmetric matrix has real eigenvalues and orthogonal eigenvectors.
- An orthogonal matrix is a square matrix whose columns (or rows) are orthonormal vectors, i.e., Q^T^Q = QQ^T^ = I.
- An orthogonal matrix preserves the length and angle of vectors, i.e., ||Qx|| = ||x|| and <Qx, Qy> = <x, y>.
- An orthogonal matrix has determinant 1 or -1 and inverse Q^T^.
- A matrix A is orthogonally diagonalizable if there exists an orthogonal matrix P and a diagonal matrix D such that A = PDP^T^.
- A matrix A is orthogonally diagonalizable if and only if A is symmetric.
- The orthogonal diagonalization of a symmetric matrix A can be obtained by finding the eigenvalues and eigenvectors of A, and forming P as the matrix whose columns are the normalized eigenvectors of A, and D as the matrix whose diagonal entries are the corresponding eigenvalues of A.
- The orthogonal diagonalization of a symmetric matrix A can be used to simplify quadratic forms, such as x^T^Ax, by changing variables to y = P^T^x, where P is the orthogonal matrix that diagonalizes A. Then x^T^Ax = y^T^Dy, where D is the diagonal matrix of eigenvalues of A.