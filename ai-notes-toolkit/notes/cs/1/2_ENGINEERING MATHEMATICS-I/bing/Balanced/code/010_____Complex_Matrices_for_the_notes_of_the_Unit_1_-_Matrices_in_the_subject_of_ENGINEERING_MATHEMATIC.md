# Complex Matrices

- A complex matrix is a matrix that has some complex number among its elements .
- A complex number is a number made up of a real part and an imaginary part, which is indicated by the letter i.
- For example, the matrix

$$
\begin{bmatrix}
1 + 2i & 3 - i \\
-4 + i & 2 + 5i
\end{bmatrix}
$$

is a complex matrix.

- The set of all m × n complex matrices is denoted as $\mathbb{C}^{m \times n}$ or complex$^{m \times n}$.
- Complex matrices can be added, subtracted, multiplied, and transposed, just like real matrices, with some modifications   .
- The addition and subtraction of complex matrices are done elementwise, by adding or subtracting the corresponding complex numbers in each position.
- The multiplication of complex matrices is done by multiplying the rows of the first matrix with the columns of the second matrix, and adding the products. However, the order of multiplication matters, as complex matrices are not commutative in general.
- The transpose of a complex matrix is obtained by swapping the rows and columns of the matrix, and changing the sign of the imaginary part of each element. This is also called the conjugate transpose or the Hermitian transpose of the matrix, and is denoted by $A^H$ or $A^*$.
- The dot or inner product of two complex vectors is defined as the sum of the products of the corresponding elements, where the first vector is conjugated. That is, if $\mathbf{x}$ and $\mathbf{y}$ are complex vectors, then

$$
\mathbf{x} \cdot \mathbf{y} = \sum_{i=1}^n \overline{x_i} y_i
$$

where $\overline{x_i}$ is the complex conjugate of $x_i$.

- The norm or length of a complex vector is defined as the square root of the dot product of the vector with itself. That is, if $\mathbf{x}$ is a complex vector, then

$$
\|\mathbf{x}\| = \sqrt{\mathbf{x} \cdot \mathbf{x}} = \sqrt{\sum_{i=1}^n |x_i|^2}
$$

where $|x_i|$ is the modulus or absolute value of $x_i$.

- The determinant of a complex matrix is defined as the sum of the products of the elements in any row or column with their corresponding cofactors. The cofactor of an element is the determinant of the submatrix obtained by deleting the row and column containing that element, multiplied by $(-1)^{i+j}$, where $i$ and $j$ are the row and column indices of the element. The determinant of a complex matrix can be a complex number as well.
- The inverse of a complex matrix is defined as the matrix that satisfies the equation $AA^{-1} = A^{-1}A = I$, where $I$ is the identity matrix. The inverse of a complex matrix can be found by dividing the adjoint matrix by the determinant of the matrix, if the determinant is nonzero. The adjoint matrix is the transpose of the matrix of cofactors.