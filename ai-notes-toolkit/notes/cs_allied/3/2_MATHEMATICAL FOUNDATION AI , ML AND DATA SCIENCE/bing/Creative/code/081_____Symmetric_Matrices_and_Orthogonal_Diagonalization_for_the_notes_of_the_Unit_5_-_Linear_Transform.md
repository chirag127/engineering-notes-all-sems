### Symmetric Matrices and Orthogonal Diagonalization

- A symmetric matrix is a square matrix that is equal to its transpose, i.e., A = A^T^.
- A symmetric matrix has real eigenvalues and orthogonal eigenvectors, i.e., the eigenvectors corresponding to distinct eigenvalues are perpendicular to each other.
- A symmetric matrix can be orthogonally diagonalized, i.e., there exists an orthogonal matrix P (P^T^ = P^-1^) and a diagonal matrix D such that A = PDP^T^.
- Orthogonal diagonalization is a process of finding an orthogonal matrix P and a diagonal matrix D that satisfy A = PDP^T^ for a given symmetric matrix A.
- Orthogonal diagonalization can be done by the following steps:
  - Find the eigenvalues and eigenvectors of A by solving the characteristic equation det(A - lambda I) = 0.
  - For each eigenvalue, find a basis for the corresponding eigenspace and normalize the basis vectors to have unit length.
  - Form the matrix P by putting the normalized eigenvectors as columns in any order.
  - Form the matrix D by putting the eigenvalues along the main diagonal in the same order as the eigenvectors in P.
- Orthogonal diagonalization has applications in quadratic forms, principal component analysis, spectral theorem, and many other topics in linear algebra and mathematics.