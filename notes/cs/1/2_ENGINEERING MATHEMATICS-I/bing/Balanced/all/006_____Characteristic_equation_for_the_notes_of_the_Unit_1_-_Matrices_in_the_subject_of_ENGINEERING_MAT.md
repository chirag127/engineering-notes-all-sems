# Characteristic equation

- The characteristic equation of a square matrix A is the equation that is solved to find the eigenvalues of A. It is also called the characteristic polynomial of A.
- The characteristic equation of A in variable x is defined by

  `det(A - xI) = 0`

  where I is the identity matrix of the same size as A and det is the determinant of a matrix.
- The characteristic equation is a polynomial equation of degree n, where n is the order of A. The roots of the characteristic equation are the eigenvalues of A.
- The characteristic equation can be written explicitly as

  `a_0 + a_1x + a_2x^2 + ... + a_nx^n = 0`

  where a_0 = det(A), a_1 = -tr(A), a_2, ..., a_n are coefficients that depend on the entries of A, and tr(A) is the trace of A, which is the sum of the diagonal elements of A.
- The characteristic equation can be used to find the eigenvectors of A by plugging in each eigenvalue into the equation

  `(A - xI)v = 0`

  and solving for the nonzero vector v. The eigenvectors are the vectors that span the null space of A - xI for each eigenvalue x.