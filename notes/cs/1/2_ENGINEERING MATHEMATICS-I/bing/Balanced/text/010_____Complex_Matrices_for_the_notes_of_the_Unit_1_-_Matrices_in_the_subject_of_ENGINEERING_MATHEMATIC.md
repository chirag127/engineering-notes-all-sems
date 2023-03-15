### Complex Matrices

- A complex matrix is a matrix that has some complex number among its elements.
- A complex number is a number made up of a real part and an imaginary part, which is indicated by the letter i.
- For example, the matrix

$$
\begin{bmatrix}
1 + 2i & -3i \\
4 - i & 2 + 5i
\end{bmatrix}
$$

is a complex matrix.

- The set of all m × n complex matrices is denoted as $\mathbb{C}^{m \times n}$.
- Addition and scalar multiplication of complex matrices are defined entrywise in the usual manner, and the properties in Theorem 1.12 also hold for complex matrices.
- The conjugate of a complex matrix A is the matrix A obtained from A by conjugating every entry.
- For example, the conjugate of the matrix

$$
\begin{bmatrix}
1 + 2i & -3i \\
4 - i & 2 + 5i
\end{bmatrix}
$$

is

$$
\begin{bmatrix}
1 - 2i & 3i \\
4 + i & 2 - 5i
\end{bmatrix}
$$

- The transpose of a complex matrix A is the matrix A^T obtained from A by interchanging the rows and columns.
- For example, the transpose of the matrix

$$
\begin{bmatrix}
1 + 2i & -3i \\
4 - i & 2 + 5i
\end{bmatrix}
$$

is

$$
\begin{bmatrix}
1 + 2i & 4 - i \\
-3i & 2 + 5i
\end{bmatrix}
$$

- The conjugate transpose of a complex matrix A is the matrix A^* obtained from A by conjugating every entry and then taking the transpose.
- For example, the conjugate transpose of the matrix

$$
\begin{bmatrix}
1 + 2i & -3i \\
4 - i & 2 + 5i
\end{bmatrix}
$$

is

$$
\begin{bmatrix}
1 - 2i & 4 + i \\
3i & 2 - 5i
\end{bmatrix}
$$

- A complex matrix A is called Hermitian if A^* = A.
- A complex matrix A is called unitary if A^*A = AA^* = I, where I is the identity matrix.
- A complex matrix A is called normal if A^*A = AA^*.
- A complex matrix A is called skew-Hermitian if A^* = -A.
- A complex matrix A is called orthogonal if A^TA = AA^T = I, where I is the identity matrix.
- A complex matrix A is called symmetric if A^T = A.
- A complex matrix A is called skew-symmetric if A^T = -A.