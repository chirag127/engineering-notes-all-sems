### Diagonalization

- Diagonalization is the process of finding a diagonal matrix that is similar to a given matrix. A diagonal matrix is a matrix that has non-zero entries only on its main diagonal.
- Diagonalization is useful because diagonal matrices are easier to work with than general matrices. For example, it is easy to compute the power of a diagonal matrix, or to find its inverse.
- Diagonalization is related to the concept of eigenvalues and eigenvectors of a matrix. An eigenvalue of a matrix A is a scalar λ such that there exists a non-zero vector v satisfying Av = λv. Such a vector v is called an eigenvector of A corresponding to the eigenvalue λ.
- A matrix A is diagonalizable if and only if there exists a basis of the vector space consisting of eigenvectors of A. In other words, A is diagonalizable if and only if there are n linearly independent eigenvectors of A, where n is the dimension of the vector space.
- If A is diagonalizable, then there exists an invertible matrix P such that P^-1AP is a diagonal matrix D. The columns of P are the eigenvectors of A, and the diagonal entries of D are the eigenvalues of A. The matrix P is called the change of basis matrix, and the matrix D is called the diagonalized matrix.
- To diagonalize a matrix A, we need to follow four steps:
  - Step 1: Find the eigenvalues of A by solving the characteristic equation det(A - λI) = 0, where I is the identity matrix.
  - Step 2: For each eigenvalue λ, find the eigenvectors of A by solving the system (A - λI)v = 0.
  - Step 3: Check if there are n linearly independent eigenvectors of A. If not, then A is not diagonalizable. If yes, then form the matrix P by putting the eigenvectors as columns.
  - Step 4: Compute the matrix D by multiplying P^-1AP. The diagonal entries of D are the eigenvalues of A.