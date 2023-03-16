# Diagonalization

- Diagonalization is the process of finding a diagonal matrix that is similar to a given matrix. A diagonal matrix is a matrix that has non-zero entries only on its main diagonal.
- Diagonalization is useful because diagonal matrices are easier to work with than general matrices. For example, it is easy to compute the power of a diagonal matrix, or to find its inverse.
- Diagonalization is related to the concept of eigenvalues and eigenvectors of a matrix. An eigenvalue of a matrix A is a scalar λ such that there exists a non-zero vector v satisfying Av = λv. Such a vector v is called an eigenvector of A corresponding to the eigenvalue λ.
- A matrix A is diagonalizable if and only if it has n linearly independent eigenvectors, where n is the size of the matrix. In that case, we can form a matrix P whose columns are the eigenvectors of A, and a diagonal matrix D whose diagonal entries are the eigenvalues of A. Then, we have A = PDP^-1, where P^-1 is the inverse of P.
- To diagonalize a matrix A, we need to follow four steps:
  - Step 1: Find the eigenvalues of A by solving the characteristic equation det(A - λI) = 0, where I is the identity matrix.
  - Step 2: For each eigenvalue λ, find the eigenvectors of A by solving the system (A - λI)v = 0, where v is the eigenvector.
  - Step 3: Check that the eigenvectors are linearly independent. If not, then A is not diagonalizable.
  - Step 4: Construct the matrix P by putting the eigenvectors as columns, and the matrix D by putting the eigenvalues on the diagonal. Then, verify that A = PDP^-1.