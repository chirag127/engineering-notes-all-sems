### Diagonalization

- Diagonalization is the process of finding a diagonal matrix that is similar to a given matrix. A diagonal matrix is a matrix that has non-zero entries only on its main diagonal.
- Diagonalization is useful because diagonal matrices are easier to work with than general matrices. For example, it is easy to compute the power of a diagonal matrix, or to find its inverse.
- Diagonalization is related to the concept of eigenvalues and eigenvectors of a matrix. An eigenvalue of a matrix A is a scalar λ such that there exists a non-zero vector v satisfying Av = λv. Such a vector v is called an eigenvector of A corresponding to the eigenvalue λ.
- A matrix A is diagonalizable if and only if it has n linearly independent eigenvectors, where n is the size of the matrix. In that case, there exists a matrix P such that P^-1AP is a diagonal matrix D, where the diagonal entries of D are the eigenvalues of A, and the columns of P are the eigenvectors of A.
- The steps to diagonalize a matrix A are as follows :
  - Step 1: Find the eigenvalues of A by solving the characteristic equation det(A - λI) = 0, where I is the identity matrix.
  - Step 2: For each eigenvalue λ, find a basis for the eigenspace of A, which is the set of all eigenvectors of A corresponding to λ. The eigenspace of A has dimension equal to the multiplicity of λ, which is the number of times λ appears as a root of the characteristic equation.
  - Step 3: Construct a matrix P whose columns are the eigenvectors of A, arranged in the same order as the corresponding eigenvalues. Make sure that the eigenvectors are linearly independent and normalized (i.e., have unit length).
  - Step 4: Compute the inverse of P and multiply it by A and P to obtain the diagonal matrix D = P^-1AP. The diagonal entries of D are the eigenvalues of A, and the columns of P are the eigenvectors of A.