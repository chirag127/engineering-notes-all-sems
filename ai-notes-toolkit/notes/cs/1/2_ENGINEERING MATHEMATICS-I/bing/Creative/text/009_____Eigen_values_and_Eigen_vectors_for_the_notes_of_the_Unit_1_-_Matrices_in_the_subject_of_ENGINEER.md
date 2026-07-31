### Eigenvalues and Eigenvectors

- Eigenvalues and eigenvectors are concepts related to linear transformations of vector spaces.
- A linear transformation is a function that maps vectors to vectors, such that the sum and scalar multiples of vectors are preserved.
- A matrix is a rectangular array of numbers that can represent a linear transformation by multiplying it with a vector.
- An eigenvector of a matrix is a nonzero vector that does not change its direction when multiplied by the matrix. It may only change its length or sign.
- An eigenvalue of a matrix is a scalar that corresponds to an eigenvector, such that multiplying the matrix by the eigenvector gives the same result as multiplying the eigenvector by the eigenvalue.
- Mathematically, if A is a matrix, x is an eigenvector, and λ is an eigenvalue, then Ax = λx.
- Geometrically, an eigenvector is a direction in which the matrix acts as a scaling transformation, and the eigenvalue is the factor by which the vector is scaled.
- To find the eigenvalues and eigenvectors of a matrix, one has to solve the characteristic equation, which is given by det(A - λI) = 0, where I is the identity matrix and det is the determinant function.
- The characteristic equation is a polynomial of degree n, where n is the size of the matrix. The roots of the polynomial are the eigenvalues, and the corresponding eigenvectors can be found by plugging the eigenvalues into the equation A - λI = 0 and solving for x.
- Some properties of eigenvalues and eigenvectors are:

  - If A is triangular, then the diagonal elements of A are the eigenvalues of A.
  - If λ is an eigenvalue of A with eigenvector x, then 1/λ is an eigenvalue of A^-1 with eigenvector x.
  - If λ is an eigenvalue of A then λ is an eigenvalue of A^T.
  - The sum of the eigenvalues of A is equal to the trace of A, which is the sum of the diagonal elements of A.
  - The product of the eigenvalues of A is equal to the determinant of A.
  - If A and B are similar matrices, meaning that A = PBP^-1 for some invertible matrix P, then they have the same eigenvalues.
  - If A is diagonalizable, meaning that it can be written as A = PDP^-1 for some diagonal matrix D and some invertible matrix P, then the columns of P are the eigenvectors of A and the diagonal elements of D are the eigenvalues of A.