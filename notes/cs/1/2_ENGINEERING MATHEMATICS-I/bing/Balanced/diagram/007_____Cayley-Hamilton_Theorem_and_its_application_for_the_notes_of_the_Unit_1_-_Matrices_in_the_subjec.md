### Cayley-Hamilton Theorem and its application

- The Cayley-Hamilton theorem is a fundamental result in linear algebra that establishes a relationship between a square matrix and its own characteristic polynomial .
- The characteristic polynomial of a square matrix A is defined as p_A(x) = det(A - xI), where det is the determinant, x is a scalar variable, and I is the identity matrix of the same size as A .
- The Cayley-Hamilton theorem states that every square matrix A satisfies its own characteristic equation, that is, p_A(A) = 0 .
- The theorem is named after the mathematicians Arthur Cayley and William Rowan Hamilton, who independently discovered it in the 19th century .
- The theorem has many important applications in mathematics, physics, and engineering, including solving systems of linear differential equations, diagonalizing matrices, finding inverse and higher powers of matrices, and computing matrix functions  .

#### Example

- Consider the matrix A = [[1, 2], [3, 4]].
- The characteristic polynomial of A is p_A(x) = det(A - xI) = (1 - x)(4 - x) - 6 = x^2 - 5x - 2.
- The Cayley-Hamilton theorem implies that p_A(A) = 0, that is, A^2 - 5A - 2I = 0.
- This can be verified by direct computation:

A^2 = [[1, 2], [3, 4]] * [[1, 2], [3, 4]] = [[7, 10], [15, 22]]

5A = 5 * [[1, 2], [3, 4]] = [[5, 10], [15, 20]]

2I = 2 * [[1, 0], [0, 1]] = [[2, 0], [0, 2]]

A^2 - 5A - 2I = [[7, 10], [15, 22]] - [[5, 10], [15, 20]] - [[2, 0], [0, 2]] = [[0, 0], [0, 0]] = 0

#### Application: Finding inverse of a matrix

- One application of the Cayley-Hamilton theorem is to find the inverse of a matrix, if it exists.
- Suppose A is an invertible n x n matrix, and p_A(x) = x^n + a_(n-1)x^(n-1) + ... + a_1x + a_0 is its characteristic polynomial, where a_0 is nonzero.
- Then, by the Cayley-Hamilton theorem, p_A(A) = 0, that is, A^n + a_(n-1)A^(n-1) + ... + a_1A + a_0I = 0.
- Multiplying both sides by A^(-1), we get A^(n-1) + a_(n-1)A^(n-2) + ... + a_1I + a_0A^(-1) = 0.
- Rearranging the terms, we get A^(-1) = (-1/a_0)(A^(n-1) + a_(n-1)A^(n-2) + ... + a_1I).
- This gives an explicit formula for the inverse of A in terms of its characteristic polynomial coefficients and its powers.

#### Example

- Consider the matrix A = [[1, 2], [3, 4]] as before.
- The characteristic polynomial of A is p_A(x) = x^2 - 5x - 2, as we have seen.
- The inverse of A is A^(-1) = (-1/-2)(A + 5I) = (1/2)([[1, 2], [3, 4]] + 5[[1, 0], [0, 1]]) = (1/2)([[6, 2], [3, 9]]) = [[3, 1], [3/2, 9/2]].
- This can be verified by direct computation:

A * A^(-1) = [[1,