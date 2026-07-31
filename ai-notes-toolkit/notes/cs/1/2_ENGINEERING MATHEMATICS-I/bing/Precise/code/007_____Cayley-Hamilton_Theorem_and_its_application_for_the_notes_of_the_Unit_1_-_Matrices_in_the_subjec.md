### Cayley-Hamilton Theorem and its application

The Cayley-Hamilton Theorem states that every square matrix satisfies its own characteristic equation. In other words, if A is an n x n matrix and p(λ) is its characteristic polynomial, then p(A) = 0.

The characteristic polynomial of a matrix A is defined as p(λ) = det(λI - A), where I is the identity matrix of the same size as A and det denotes the determinant.

The Cayley-Hamilton Theorem can be used to find the inverse of a matrix, if it exists. If A is invertible, then its characteristic polynomial can be written in the form p(λ) = λ^n + c_(n-1)λ^(n-1) + ... + c_1λ + c_0, where c_0 = det(A) ≠ 0. By the Cayley-Hamilton Theorem, we have p(A) = A^n + c_(n-1)A^(n-1) + ... + c_1A + c_0I = 0. Solving for A^(-1), we get A^(-1) = (-1/c_0)(A^(n-1) + c_(n-1)A^(n-2) + ... + c_1I).

The Cayley-Hamilton Theorem can also be used to find powers of a matrix. If p(A) = 0, then A^n can be expressed as a linear combination of lower powers of A. This can be useful when computing high powers of a matrix, as it can reduce the number of matrix multiplications required.

In summary, the Cayley-Hamilton Theorem is a powerful tool in matrix algebra with applications in finding the inverse and powers of a matrix. It is an important concept in the study of matrices in the subject of ENGINEERING MATHEMATICS-I.