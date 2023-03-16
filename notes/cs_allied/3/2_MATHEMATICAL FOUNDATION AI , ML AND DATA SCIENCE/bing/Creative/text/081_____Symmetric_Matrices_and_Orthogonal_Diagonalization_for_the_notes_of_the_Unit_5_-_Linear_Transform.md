### Symmetric Matrices and Orthogonal Diagonalization

- A **symmetric matrix** is a square matrix that is equal to its transpose, i.e., A = A^T.
- A symmetric matrix has **real eigenvalues** and **orthogonal eigenvectors**.
- An **orthogonal matrix** is a square matrix whose columns (and rows) are **orthonormal vectors**, i.e., Q^T Q = I.
- An **orthonormal basis** is a basis whose vectors are orthogonal and have unit length.
- The **Gram-Schmidt process** is a method to obtain an orthonormal basis from a linearly independent set of vectors.
- The **orthogonal projection** of a vector onto a subspace is the sum of the scalar projections of the vector onto the orthonormal basis vectors of the subspace.
- The **orthogonal complement** of a subspace W is the set of all vectors that are orthogonal to every vector in W, denoted by W^⊥.
- A **diagonal matrix** is a square matrix whose only nonzero entries are on the main diagonal.
- A matrix is **diagonalizable** if it is similar to a diagonal matrix, i.e., there exists an invertible matrix P such that P^-1 A P = D, where D is a diagonal matrix.
- A matrix is **orthogonally diagonalizable** if it is similar to a diagonal matrix by an orthogonal matrix, i.e., there exists an orthogonal matrix Q such that Q^T A Q = D, where D is a diagonal matrix.
- A **spectral theorem** is a result that relates the properties of a matrix to its eigenvalues and eigenvectors.
- The **spectral theorem for symmetric matrices** states that a matrix A is symmetric if and only if it is orthogonally diagonalizable, i.e., there exists an orthogonal matrix Q such that Q^T A Q = D, where D is a diagonal matrix with the eigenvalues of A on the main diagonal.
- The **spectral theorem for normal matrices** states that a matrix A is normal (i.e., A A^T = A^T A) if and only if it is unitarily diagonalizable, i.e., there exists a unitary matrix U (i.e., U^* U = I, where U^* is the conjugate transpose of U) such that U^* A U = D, where D is a diagonal matrix with the eigenvalues of A on the main diagonal.