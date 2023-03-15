### Skew-Hermitian Matrix

- A square matrix A is called **skew-Hermitian** or **antihermitian** if its conjugate transpose A* is equal to -A, that is, A* = -A .
- The conjugate transpose of a matrix A is obtained by taking the complex conjugate of each element and then transposing the matrix, that is, A* = (A')* .
- The diagonal elements of a skew-Hermitian matrix are either zeros or pure imaginary numbers .
- A skew-Hermitian matrix is an example of a **normal matrix**, which means that it commutes with its conjugate transpose, that is, AA* = A*A .
- A normal matrix is **diagonalizable**, which means that it can be written as A = PDP*, where P is a unitary matrix and D is a diagonal matrix .
- The eigenvalues of a skew-Hermitian matrix are either purely imaginary or zeros . The eigenvectors for distinct eigenvalues are orthogonal .

#### Examples

- The matrix A = [[0, i], [-i, 0]] is skew-Hermitian, since A* = [[0, -i], [i, 0]] = -A. Its eigenvalues are i and -i, and its eigenvectors are [1, i] and [1, -i].
- The matrix B = [[i, 1 + i], [2 - 3i, -i]] is not skew-Hermitian, since B* = [[-i, 2 + 3i], [1 - i, i]] is not equal to -B.