### Skew-Hermitian Matrix

- A square matrix A is called **skew-Hermitian** (or antihermitian) if it satisfies the condition A<sup>∗</sup> = −A, where A<sup>∗</sup> is the conjugate transpose of A .
- The conjugate transpose of a matrix is obtained by taking the complex conjugate of each element and then transposing the matrix.
- The complex conjugate of a complex number z = a + bi is z<sup>∗</sup> = a − bi, where a and b are real numbers and i is the imaginary unit.
- The transpose of a matrix is obtained by swapping the rows and columns of the matrix.
- A skew-Hermitian matrix has the following properties     :
  - The diagonal elements of a skew-Hermitian matrix are either zero or purely imaginary, i.e., they have no real part.
  - The eigenvalues of a skew-Hermitian matrix are either zero or purely imaginary, i.e., they have no real part.
  - A skew-Hermitian matrix is normal, i.e., it commutes with its conjugate transpose, i.e., AA<sup>∗</sup> = A<sup>∗</sup>A.
  - A skew-Hermitian matrix is diagonalizable, i.e., it can be written as A = UDU<sup>∗</sup>, where U is a unitary matrix and D is a diagonal matrix with the eigenvalues of A on the diagonal.
  - The eigenvectors of a skew-Hermitian matrix corresponding to distinct eigenvalues are orthogonal, i.e., they have zero inner product.
- Some examples of skew-Hermitian matrices are :
  - A 2 × 2 skew-Hermitian matrix: A = \begin{bmatrix} 0 & i \\ -i & 0 \end{bmatrix}
  - A 3 × 3 skew-Hermitian matrix: A = \begin{bmatrix} 0 & 1 + i & 2 - 3i \\ -1 - i & 0 & 4 + i \\ -2 + 3i & -4 - i & 0 \end{bmatrix}