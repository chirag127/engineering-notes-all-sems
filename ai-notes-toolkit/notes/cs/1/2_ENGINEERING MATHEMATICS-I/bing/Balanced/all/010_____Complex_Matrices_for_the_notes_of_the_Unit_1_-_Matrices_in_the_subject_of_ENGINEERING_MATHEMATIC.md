# Complex Matrices

- A complex matrix is a matrix that has some complex number among its elements.
- A complex number is a number made up of a real part and an imaginary part, which is indicated by the letter i.
- For example, the matrix

$$
A = \begin{bmatrix}
1 + 2i & 3 - i \\
-4 + i & 2 + 5i
\end{bmatrix}
$$

is a complex matrix.

- The set of all m × n complex matrices is denoted as $\mathbb{C}^{m \times n}$.
- Addition and scalar multiplication of complex matrices are defined entrywise in the usual manner, and the properties in Theorem 1.12 also hold for complex matrices.
- Theorem 1.12 states that for any matrices A, B, and C of the same size, and any scalars c and d, the following properties hold:

  - A + B = B + A (commutativity of addition)
  - (A + B) + C = A + (B + C) (associativity of addition)
  - A + 0 = A (additive identity)
  - A + (-A) = 0 (additive inverse)
  - c(A + B) = cA + cB (distributivity of scalar multiplication over matrix addition)
  - (c + d)A = cA + dA (distributivity of scalar addition over matrix multiplication)
  - c(dA) = (cd)A (associativity of scalar multiplication)
  - 1A = A (multiplicative identity of scalar multiplication)

- The conjugate of a complex matrix A is the matrix A obtained from A by conjugating every entry.
- The conjugate of a complex number z = x + yi is z = x - yi.
- For example, the conjugate of the matrix A above is

$$
A = \begin{bmatrix}
1 - 2i & 3 + i \\
-4 - i & 2 - 5i
\end{bmatrix}
$$

- The transpose of a complex matrix A is the matrix A^T obtained from A by interchanging the rows and columns.
- For example, the transpose of the matrix A above is

$$
A^T = \begin{bmatrix}
1 + 2i & -4 + i \\
3 - i & 2 + 5i
\end{bmatrix}
$$

- The conjugate transpose of a complex matrix A is the matrix A^H obtained from A by conjugating and transposing every entry.
- It is also called the Hermitian transpose or the adjoint of A.
- For example, the conjugate transpose of the matrix A above is

$$
A^H = \begin{bmatrix}
1 - 2i & -4 - i \\
3 + i & 2 - 5i
\end{bmatrix}
$$

- A complex matrix A is called Hermitian if A^H = A.
- A complex matrix A is called unitary if A^H A = AA^H = I, where I is the identity matrix.
- A complex matrix A is called normal if A^H A = AA^H.
- A complex matrix A is called skew-Hermitian if A^H = -A.