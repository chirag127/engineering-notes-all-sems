### Eigenvalues and Eigenvectors

- Eigenvalues and eigenvectors are concepts related to linear transformations of vector spaces.
- A linear transformation is a function that maps vectors from one vector space to another, preserving the operations of vector addition and scalar multiplication.
- A matrix is a rectangular array of numbers that can represent a linear transformation by multiplying it with a vector.
- An eigenvector of a matrix is a nonzero vector that does not change its direction when multiplied by the matrix. It may only change its length or sign.
- An eigenvalue of a matrix is a scalar that corresponds to an eigenvector. It is the factor by which the eigenvector is scaled when multiplied by the matrix.
- Geometrically, an eigenvector points in a direction that is stretched or shrunk by the matrix, and the eigenvalue is the amount of stretching or shrinking.
- Mathematically, an eigenvector **x** and an eigenvalue **λ** of a matrix **A** satisfy the equation **Ax = λx**.
- To find the eigenvalues of a matrix, we need to solve the characteristic equation **det(A - λI) = 0**, where **det** is the determinant and **I** is the identity matrix.
- To find the eigenvectors of a matrix, we need to find the null space of **A - λI** for each eigenvalue **λ**, where the null space is the set of vectors that are mapped to the zero vector by the matrix.
- Some properties of eigenvalues and eigenvectors are:
  - If **A** is a triangular matrix, then the diagonal elements of **A** are the eigenvalues of **A**.
  - If **λ** is an eigenvalue of **A** with eigenvector **x**, then **1/λ** is an eigenvalue of **A**<sup>-1</sup> with eigenvector **x**.
  - If **λ** is an eigenvalue of **A**, then **λ** is an eigenvalue of **A**<sup>T</sup>, where **T** denotes the transpose of the matrix.
  - The sum of the eigenvalues of **A** is equal to the trace of **A**, which is the sum of the diagonal elements of **A**.
  - The product of the eigenvalues of **A** is equal to the determinant of **A**.
  - The number of linearly independent eigenvectors of **A** is equal to the rank of **A**, which is the dimension of the column space of **A**.
  - If **A** has **n** distinct eigenvalues, then **A** has **n** linearly independent eigenvectors, and **A** is diagonalizable, meaning that it can be written as **A = PDP**<sup>-1</sup>, where **P** is a matrix whose columns are the eigenvectors of **A**, and **D** is a diagonal matrix whose diagonal elements are the eigenvalues of **A**.