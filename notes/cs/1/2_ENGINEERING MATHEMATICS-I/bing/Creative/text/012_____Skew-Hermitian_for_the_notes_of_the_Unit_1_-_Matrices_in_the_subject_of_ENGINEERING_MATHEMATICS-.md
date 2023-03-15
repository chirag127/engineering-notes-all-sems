### Skew-Hermitian Matrix

- A square matrix A is called **skew-Hermitian** or **anti-Hermitian** if it satisfies the condition A<sup>∗</sup> = -A, where A<sup>∗</sup> is the **conjugate transpose** of A. That is, A<sup>∗</sup> is obtained by taking the complex conjugate of each element of A and then transposing the matrix.
- The conjugate transpose of a matrix A is denoted by A<sup>∗</sup>, A<sup>H</sup>, or A<sup>†</sup>.
- The complex conjugate of a complex number z = a + bi is z<sup>∗</sup> = a - bi, where a and b are real numbers and i is the imaginary unit.
- A skew-Hermitian matrix has the following properties:
  - The diagonal elements of a skew-Hermitian matrix are either zero or purely imaginary. That is, a<sub>ii</sub> = -a<sub>ii</sub><sup>∗</sup> for all i.
  - The off-diagonal elements of a skew-Hermitian matrix are the negative complex conjugates of the corresponding elements in the upper or lower triangular part of the matrix. That is, a<sub>ij</sub> = -a<sub>ji</sub><sup>∗</sup> for all i ≠ j.
  - A skew-Hermitian matrix is a normal matrix, meaning that it commutes with its conjugate transpose. That is, AA<sup>∗</sup> = A<sup>∗</sup>A.
  - A skew-Hermitian matrix is diagonalizable, meaning that it can be written as A = PDP<sup>-1</sup>, where P is a unitary matrix and D is a diagonal matrix.
  - The eigenvalues of a skew-Hermitian matrix are either zero or purely imaginary. The eigenvectors corresponding to distinct eigenvalues are orthogonal.
- Examples of skew-Hermitian matrices are:
  - A = [0 1 + i -1 - i 0]
  - B = [i 2 - 3i -2 + 3i -i]
  - C = [0 1 0 -1 0 0 0 0 0]