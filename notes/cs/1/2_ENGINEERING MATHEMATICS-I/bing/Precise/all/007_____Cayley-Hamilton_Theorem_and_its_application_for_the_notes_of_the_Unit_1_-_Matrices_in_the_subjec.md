# Cayley-Hamilton Theorem and its application

The Cayley-Hamilton Theorem is a fundamental result in matrix algebra. It states that every square matrix satisfies its own characteristic equation. In other words, if A is an n x n matrix, and p(λ) is its characteristic polynomial, then p(A) = 0.

## Proof of the Cayley-Hamilton Theorem

The proof of the Cayley-Hamilton Theorem is based on the concept of matrix similarity. Two matrices A and B are said to be similar if there exists an invertible matrix P such that B = P^(-1)AP.

Let A be an n x n matrix, and let p(λ) be its characteristic polynomial. Then, by definition, p(λ) = det(A - λI). Let B = P^(-1)AP be a matrix similar to A. Then, the characteristic polynomial of B is given by p_B(λ) = det(B - λI) = det(P^(-1)AP - λI) = det(P^(-1)(A - λI)P) = det(P^(-1))det(A - λI)det(P) = det(A - λI) = p(λ).

Since B is similar to A, it follows that p(B) = p(P^(-1)AP) = 0. But then, p(A) = p(PP^(-1)A(PP^(-1})) = p(PB(P^(-1))) = Pp(B)(P^(-1)) = P0(P^(-1)) = 0.

## Application of the Cayley-Hamilton Theorem

The Cayley-Hamilton Theorem has many applications in matrix algebra. One of its most important applications is in the computation of matrix powers. Let A be an n x n matrix, and let p(λ) be its characteristic polynomial. Then, by the Cayley-Hamilton Theorem, p(A) = 0. This means that A^n can be expressed as a linear combination of lower powers of A.

For example, if A is a 2 x 2 matrix, then its characteristic polynomial is given by p(λ) = λ^2 - tr(A)λ + det(A), where tr(A) is the trace of A and det(A) is its determinant. By the Cayley-Hamilton Theorem, it follows that A^2 - tr(A)A + det(A)I = 0. This means that A^2 can be expressed as a linear combination of A and I.

In general, if A is an n x n matrix, then its characteristic polynomial is of degree n, and A^n can be expressed as a linear combination of A^(n-1), A^(n-2), ..., A, and I. This can be used to compute high powers of A efficiently.

Another important application of the Cayley-Hamilton Theorem is in the computation of the matrix exponential. The matrix exponential of a square matrix A is defined as e^A = I + A + A^2/2! + A^3/3! + ... . Using the Cayley-Hamilton Theorem, it is possible to express e^A as a finite sum of lower powers of A.

In summary, the Cayley-Hamilton Theorem is a powerful tool in matrix algebra that has many important applications. It allows us to express high powers of a matrix as a linear combination of lower powers, and it can be used to compute the matrix exponential efficiently. It is an essential result for anyone studying matrix algebra or its applications.