# Diagonalization

- Diagonalization is a process of finding a diagonal matrix that is similar to a given square matrix. A diagonal matrix is a matrix that has nonzero entries only on the main diagonal.
- Diagonalization is useful because diagonal matrices are easier to work with than general matrices. For example, computing the power of a diagonal matrix is simply raising each diagonal entry to that power.
- Diagonalization is also related to the concept of eigenvalues and eigenvectors of a matrix. Eigenvalues are special scalars that satisfy the equation $Ax = \lambda x$ for some nonzero vector $x$, where $A$ is a square matrix. Eigenvectors are the nonzero vectors $x$ that satisfy this equation. Each eigenvalue has a corresponding eigenspace, which is the set of all eigenvectors with that eigenvalue, plus the zero vector.
- A square matrix $A$ is diagonalizable if and only if it has $n$ linearly independent eigenvectors, where $n$ is the size of the matrix. In that case, there exists a matrix $P$ whose columns are the eigenvectors of $A$, and a diagonal matrix $D$ whose diagonal entries are the eigenvalues of $A$, such that $A = PDP^{-1}$.
- The steps to diagonalize a matrix are as follows:

  1. Find the eigenvalues of the matrix by solving the characteristic equation $|A - \lambda I| = 0$, where $I$ is the identity matrix.
  2. For each eigenvalue, find a basis for the eigenspace by solving the system $(A - \lambda I)x = 0$.
  3. Form the matrix $P$ by arranging the eigenvectors as columns. Check that $P$ is invertible by computing its determinant or row reducing it to the identity matrix.
  4. Form the matrix $D$ by placing the eigenvalues along the main diagonal, in the same order as the corresponding eigenvectors in $P$.
  5. Verify that $A = PDP^{-1}$ by multiplying the matrices.