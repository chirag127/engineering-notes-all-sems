### Eigenvalues and Eigenvectors

- Eigenvalues and eigenvectors are concepts related to linear transformations of vector spaces.
- A linear transformation is a function that maps vectors from one vector space to another, preserving the operations of vector addition and scalar multiplication.
- A matrix is a rectangular array of numbers that can represent a linear transformation by multiplying it with a vector.
- An eigenvector of a matrix is a nonzero vector that does not change its direction when multiplied by the matrix. It may only change its length or sign.
- An eigenvalue of a matrix is a scalar that corresponds to an eigenvector. It is the factor by which the eigenvector is scaled when multiplied by the matrix.
- Geometrically, an eigenvector points in a direction that is stretched or shrunk by the matrix, and the eigenvalue is the amount of stretching or shrinking.
- Mathematically, an eigenvector and an eigenvalue of a matrix A satisfy the equation A**v** = λ**v**, where **v** is the eigenvector and λ is the eigenvalue.
- To find the eigenvalues and eigenvectors of a matrix, one can use the characteristic equation det(A - λI) = 0, where I is the identity matrix and det is the determinant function.
- The eigenvalues are the roots of the characteristic polynomial, which is obtained by expanding the determinant.
- The eigenvectors are the solutions of the system of linear equations (A - λI)**v** = 0, for each eigenvalue λ.
- Some properties of eigenvalues and eigenvectors are:
  - The sum of the eigenvalues of a matrix is equal to its trace, which is the sum of its diagonal elements.
  - The product of the eigenvalues of a matrix is equal to its determinant.
  - The eigenvalues of a triangular matrix are its diagonal elements.
  - The eigenvalues of a symmetric matrix are real numbers.
  - The eigenvalues of an invertible matrix are nonzero, and the inverse matrix has the reciprocal eigenvalues.
  - The eigenvalues of a matrix and its transpose are the same.
  - The eigenvectors corresponding to distinct eigenvalues of a matrix are linearly independent.