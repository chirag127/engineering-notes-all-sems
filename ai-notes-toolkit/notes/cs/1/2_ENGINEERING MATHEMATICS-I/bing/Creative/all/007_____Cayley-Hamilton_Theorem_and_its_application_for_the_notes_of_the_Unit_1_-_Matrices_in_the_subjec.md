# Cayley-Hamilton Theorem and its application

- The Cayley-Hamilton theorem is a result in linear algebra that states that every square matrix satisfies its own characteristic equation.
- The characteristic equation of a square matrix A is obtained by equating the determinant of A - xI to zero, where x is a scalar variable and I is the identity matrix of the same size as A.
- The characteristic equation is a polynomial in x, called the characteristic polynomial of A, and has the same degree as the size of A.
- The Cayley-Hamilton theorem says that if we substitute A for x in the characteristic polynomial, we get the zero matrix.
- For example, if A is a 2 x 2 matrix with entries a, b, c, and d, then its characteristic polynomial is p(x) = x^2 - (a + d)x + (ad - bc), and the Cayley-Hamilton theorem says that p(A) = A^2 - (a + d)A + (ad - bc)I = 0.
- The Cayley-Hamilton theorem can be used to find the inverse of a matrix, if it exists, by expressing A^-1 as a linear combination of powers of A using the characteristic polynomial.
- For example, if A is a 2 x 2 matrix with entries a, b, c, and d, and ad - bc is not zero, then its inverse is A^-1 = (1/(ad - bc))(dI - bA + cA^2).
- The Cayley-Hamilton theorem can also be used to find the minimal polynomial of a matrix, which is the monic polynomial of the smallest degree that annihilates the matrix.
- The minimal polynomial of a matrix always divides its characteristic polynomial, and they are equal if and only if the matrix has distinct eigenvalues.
- The Cayley-Hamilton theorem has applications in various fields of mathematics, such as control theory, commutative algebra, and algebraic number theory.