### Inverse of a matrix

- The inverse of a matrix is a matrix that, when multiplied by the original matrix, results in the identity matrix.
- The inverse of a matrix A is denoted as A^-1^.
- Not all matrices have an inverse. A matrix must be square (i.e., have the same number of rows and columns) and have a non-zero determinant to have an inverse.
- The formula for finding the inverse of a 2x2 matrix is as follows:
  - If A = [a b; c d], then A^-1^ = (1/det(A)) * [d -b; -c a], where det(A) = ad - bc.
- For larger matrices, the inverse can be found using the adjugate (or classical adjoint) matrix and the determinant.
  - The formula is A^-1^ = (1/det(A)) * adj(A), where adj(A) is the adjugate matrix of A.
- The inverse of a matrix can be used to solve systems of linear equations.
- The inverse of a matrix has several properties, including:
  - (A^-1^)^-1^ = A
  - (kA)^-1^ = k^-1^A^-1^, where k is a scalar
  - (AB)^-1^ = B^-1^A^-1^
  - (A^T^)^-1^ = (A^-1^)^T^