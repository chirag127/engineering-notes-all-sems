### Characteristic equation

- The characteristic equation of a square matrix A is the equation that is solved to find the eigenvalues of A, also called the characteristic roots or the latent roots of A   .
- The characteristic equation of A is obtained by subtracting a scalar x from the diagonal elements of A and then finding the determinant of the resulting matrix. This determinant is called the characteristic polynomial of A  .
- The characteristic equation of A can be written as:

det(A - xI) = 0

where I is the identity matrix of the same order as A and det is the determinant function    .

- The characteristic polynomial of A is a polynomial of degree n, where n is the order of A. It can be written as:

p(x) = det(A - xI) = a0 + a1x + a2x^2 + ... + an-1x^(n-1) + anx^n

where a0, a1, ..., an are the coefficients of the polynomial  .

- The eigenvalues of A are the roots of the characteristic equation, or equivalently, the zeros of the characteristic polynomial. They are the values of x that satisfy:

p(x) = det(A - xI) = 0

There are at most n distinct eigenvalues for an n x n matrix A  .

- The characteristic equation and the characteristic polynomial are invariant under matrix similarity, meaning that if A and B are similar matrices, then they have the same characteristic equation and the same characteristic polynomial .

- The characteristic equation and the characteristic polynomial can be used to find various properties of a matrix, such as its rank, trace, determinant, and inverse  .

- Example: Find the characteristic equation and the characteristic polynomial of the matrix A = [[1, 2], [3, 4]].

Solution: To find the characteristic equation, we subtract x from the diagonal elements of A and then find the determinant of the resulting matrix:

det(A - xI) = det([[1 - x, 2], [3, 4 - x]]) = (1 - x)(4 - x) - 6 = x^2 - 5x - 2

To find the characteristic polynomial, we equate the determinant to zero:

p(x) = det(A - xI) = x^2 - 5x - 2 = 0

The eigenvalues of A are the roots of the characteristic equation, or the zeros of the characteristic polynomial. They can be found by using the quadratic formula:

x = (5 ± √(25 + 8))/2 = (5 ± √33)/2

Therefore, the eigenvalues of A are (5 + √33)/2 and (5 - √33)/2.