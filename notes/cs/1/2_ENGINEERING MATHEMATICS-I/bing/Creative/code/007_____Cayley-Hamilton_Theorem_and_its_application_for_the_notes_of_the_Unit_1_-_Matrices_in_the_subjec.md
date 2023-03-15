### Cayley-Hamilton Theorem and its application

- The Cayley-Hamilton theorem is a result in linear algebra that states that every square matrix satisfies its own characteristic equation.
- The characteristic equation of a square matrix A is given by `p_A(x) = det(A - xI)`, where `det` denotes the determinant, `x` is a scalar variable, and `I` is the identity matrix of the same size as A.
- The Cayley-Hamilton theorem says that `p_A(A) = 0`, where `0` is the zero matrix. That is, if we substitute the matrix A for the variable x in the characteristic polynomial, we get a matrix of all zeros.
- The theorem was first proved by William Rowan Hamilton in 1853 for the case of quaternions, a non-commutative ring, and later generalized by Arthur Cayley for the case of matrices over a commutative ring.
- The Cayley-Hamilton theorem has many applications in mathematics and engineering, such as:
  - Computing the inverse of a matrix, if it exists, by using the adjugate matrix and the characteristic polynomial.
  - Finding the minimal polynomial of a matrix, which is the monic polynomial of smallest degree that annihilates the matrix. The minimal polynomial divides the characteristic polynomial, and they are equal if and only if the matrix is diagonalizable .
  - Solving linear recurrence relations, such as the Fibonacci sequence, by using matrix exponentiation and the Cayley-Hamilton theorem.
  - Analyzing the controllability and stability of linear systems, by using the Cayley-Hamilton theorem to find the eigenvalues and eigenvectors of the system matrix.
  - Proving important results in commutative algebra, such as Nakayama's lemma and the Jacobson theorem, by using a generalization of the Cayley-Hamilton theorem to modules over a ring.