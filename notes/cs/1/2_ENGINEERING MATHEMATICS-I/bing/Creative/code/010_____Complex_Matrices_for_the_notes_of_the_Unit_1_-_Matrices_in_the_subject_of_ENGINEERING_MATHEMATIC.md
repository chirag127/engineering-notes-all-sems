# Complex Matrices

- A complex matrix is a matrix that has some complex number among its elements .
- A complex number is a number made up of a real part and an imaginary part, which is indicated by the letter i.
- For example, the matrix

$$
A = \begin{bmatrix}
1 + 2i & -3i \\
4 - i & 2 + 5i
\end{bmatrix}
$$

is a complex matrix.

- The set of all m × n complex matrices is denoted as $\mathbb{C}^{m \times n}$, or complex$^{m \times n}$.
- Complex matrices have similar properties and operations as real matrices, such as addition, subtraction, multiplication, transpose, inverse, determinant, rank, etc.
- However, some operations require a modification when dealing with complex matrices, such as the dot product, the conjugate, the adjoint, the norm, the eigenvalues, and the eigenvectors.
- The dot product of two complex vectors is defined as

$$
\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i \overline{v_i}
$$

where $\overline{v_i}$ is the complex conjugate of $v_i$.
- The complex conjugate of a complex number is obtained by changing the sign of the imaginary part. For example, the complex conjugate of $2 + 3i$ is $2 - 3i$.
- The complex conjugate of a complex matrix is a matrix whose entries are the complex conjugate of the entries of the original matrix. For example, the complex conjugate of the matrix A above is

$$
\overline{A} = \begin{bmatrix}
1 - 2i & 3i \\
4 + i & 2 - 5i
\end{bmatrix}
$$

- The adjoint of a complex matrix is the transpose of its complex conjugate. It is denoted by $A^*$ or $A^\dagger$. For example, the adjoint of the matrix A above is

$$
A^* = \begin{bmatrix}
1 - 2i & 4 + i \\
3i & 2 - 5i
\end{bmatrix}
$$

- A complex matrix is called Hermitian if it is equal to its adjoint. For example, the matrix

$$
B = \begin{bmatrix}
2 & 3 - i \\
3 + i & 4
\end{bmatrix}
$$

is Hermitian because $B = B^*$.
- A complex matrix is called unitary if its inverse is equal to its adjoint. For example, the matrix

$$
C = \frac{1}{\sqrt{2}} \begin{bmatrix}
1 & i \\
i & 1
\end{bmatrix}
$$

is unitary because $C^{-1} = C^*$.
- The norm of a complex vector is defined as the square root of the dot product of the vector with itself. For example, the norm of the vector

$$
\mathbf{u} = \begin{bmatrix}
2 + i \\
-1 - 3i
\end{bmatrix}
$$

is

$$
\|\mathbf{u}\| = \sqrt{\mathbf{u} \cdot \mathbf{u}} = \sqrt{(2 + i)(2 - i) + (-1 - 3i)(-1 + 3i)} = \sqrt{10}
$$

- The norm of a complex matrix is defined as the maximum of the norms of its columns. For example, the norm of the matrix A above is

$$
\|A\| = \max \{\|\mathbf{a}_1\|, \|\mathbf{a}_2\|\} = \max \{\sqrt{17}, \sqrt{34}\} = \sqrt{34}
$$

where $\mathbf{a}_1$ and $\mathbf{a}_2$ are the columns of A.
- The eigenvalues and eigenvectors of a complex matrix are the complex numbers and vectors that satisfy the equation

$$
A\mathbf{x} = \lambda \mathbf